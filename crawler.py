import requests
from bs4 import BeautifulSoup


def writeLine(menuType, price, menuItem):
    return '{0:>}\t{1:<}\t{2:>}\n'.format(menuType.strip(), price.strip(), menuItem.strip())


def writeHeader(head):
    return f"**{head}**\n"


def subHeader(head):
    return f"*{head}*\n"


def codeBlock(msg):
    return "```" + msg + "```\n"


def getFiitFood():

    url = "http://www.freefood.sk/menu/#fiit-food"
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    response = requests.get(url,  headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    weeklyMenu = soup.findAll(
        "ul", {"class": "daily-offer"})[0].findAll("ul", {"class": "day-offer"})[3]

    msg = writeHeader("FIIT FOOD")
    menuString = ""
    for menu in weeklyMenu:
        spans = menu.findAll("span")
        menuType = spans[0].text
        price = spans[1].text
        menuItem = menu.text.replace(menuType, "").replace(price, "")
        menuType = "Polievka" if spans[0].text.strip(
        ) == "P." else "Menu " + spans[0].text.strip()

        menuString += writeLine(menuType, price, menuItem)

    msg += codeBlock(menuString)
    return msg


def getKoliba():
    url = "https://mlynskakoliba.sk/#done"
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    response = requests.get(url,  headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    weeklyMenu = soup.findAll(
        "section", {"id": "done-section"})[0].findAll("div", {"class": "inner"})[3]
    priceRange = soup.find("p", {"id": "text11"}
                           ).text.strip().replace(" ", "\t")

    msg = writeHeader("MLYNSKÁ KOLIBA")
    msg += priceRange + "\n"
    menuString = ""

    for menu in weeklyMenu:
        spans = menu.findAll("span")
        for i, span in enumerate(spans):
            if "menu".upper() in span.text.upper() or "polievka".upper() in span.text.upper():
                menuString += span.text + "\t"
            else:
                if len(spans) > i+1 and "menu".upper() not in spans[i+1].text.upper():
                    menuString += span.text + " "
                else:
                    menuString += span.text + "\n"

    msg += codeBlock(menuString)
    return msg


def getEat():
    url = "http://eatandmeet.sk/tyzdenne-menu"
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    response = requests.get(url,  headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    weeklyMenu = soup.findAll(
        "div", {"id": "day-3"})[0].findAll("div", {"class": "menu-details"})

    msg = writeHeader("EAT&MEET")
    msg += subHeader("Denné Menu")
    menuString = ""
    for menu in weeklyMenu:
        menuType = menu.findAll("h4")[0].text.strip()
        price = menu.findAll("span", {"class": "price"})[0].text.strip()
        name = menu.findAll("p", {"class": "desc"})[0].text.strip()

        menuString += writeLine(menuType, price, name)
    msg += codeBlock(menuString)

    weeklyMenu = soup.findAll("section", {"class": "page-section-pt mb-20 weak-menu our-menu"})[
        0].findAll("div", {"class": "menu-details"})
    msg += subHeader("Grill menu")
    menuString = ""
    for menu in weeklyMenu:
        menuType = menu.findAll("h5")[0].text.strip()
        price = menu.findAll("span", {"class": "price"})[0].text.strip()
        name = menu.findAll("p", {"class": "desc"})[0].text.strip()

        menuString += writeLine(price, menuType, name)
    msg += codeBlock(menuString)

    weeklyMenu = soup.findAll("section", {"class": "page-section-pt mb-20 weak-menu our-menu"})[
        1].findAll("div", {"class": "menu-details"})
    msg += subHeader("Live menu")
    menuString = ""
    for menu in weeklyMenu:
        menuType = menu.findAll("h5")[0].text.strip()
        price = menu.findAll("span", {"class": "price"})[0].text.strip()
        name = menu.findAll("p", {"class": "desc"})[0].text.strip()

        menuString += writeLine(price, menuType, name)
    msg += codeBlock(menuString)

    return msg
