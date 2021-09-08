import requests
from bs4 import BeautifulSoup

def getFiitFood():
    url = "http://www.freefood.sk/menu/#fiit-food"
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    response = requests.get(url,  headers=headers)

    soup=BeautifulSoup(response.content, "html.parser")
    weeklyMenu = soup.findAll("ul", {"class" : "daily-offer"})[0].findAll("ul",{"class":"day-offer"})[3]
    msg = "**FIIT FOOD** \n"
    msg += "```"
    for menu in weeklyMenu:
            spans = menu.findAll("span")
            menuType = spans[0].text 
            price = spans[1].text
            menuItem = menu.text.replace(menuType,"").replace(price,"")
            menuType = "Polievka" if spans[0].text.strip() == "P." else "Menu " + spans[0].text.strip() 
            
            msg += f"{menuType} {price} {menuItem} \n"
    msg += "```\n"
    return msg


def getKoliba():
    url = "https://mlynskakoliba.sk/#done"
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    response = requests.get(url,  headers=headers)

    soup=BeautifulSoup(response.content, "html.parser")
    msg = "**MLYNSKA KOLIBA**\n"
    weeklyMenu = soup.findAll("section", {"id" : "done-section"})[0].findAll("div",{"class":"inner"})[3]
    priceRange = soup.find("p",{"id":"text11"}).text.strip()
    msg += priceRange + "\n"
    msg += "```"
    for menu in weeklyMenu:
        
        spans = menu.findAll("span")
        for span in spans:
            msg += span.text + "\n"
    msg += "```"
    
    return msg 


def getEat():
    url = "http://eatandmeet.sk/tyzdenne-menu"
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    response = requests.get(url,  headers=headers)

    soup=BeautifulSoup(response.content, "html.parser")

    weeklyMenu = soup.findAll("div", {"id" : "day-3"})[0].findAll("div", {"class" : "menu-details"})
    msg = "**EAT&MEET**\n"
    msg += "*Denné Menu* \n"
    msg += "```"
    for menu in weeklyMenu:
        menuType = menu.findAll("h4")[0].text.strip()
        price = menu.findAll("span", {"class": "price"})[0].text.strip()
        name = menu.findAll("p", {"class": "desc"})[0].text.strip()
        msg += f"{menuType}  {price} {name}\n"
    msg += "```"
    msg += "*Grill menu*\n"
    msg += "```"
    weeklyMenu = soup.findAll("section", {"class" : "page-section-pt mb-20 weak-menu our-menu"})[0].findAll("div", {"class" : "menu-details"})
    for menu in weeklyMenu:
        menuType = menu.findAll("h5")[0].text.strip()
        price = menu.findAll("span", {"class": "price"})[0].text.strip()
        name = menu.findAll("p", {"class": "desc"})[0].text.strip()
        msg += f"{menuType}  {price} {name}\n"
    msg += "```"
    msg += "*Live menu*\n"
    msg += "```"
    
    weeklyMenu = soup.findAll("section", {"class" : "page-section-pt mb-20 weak-menu our-menu"})[1].findAll("div", {"class" : "menu-details"})
    for menu in weeklyMenu:
        menuType = menu.findAll("h5")[0].text.strip()
        price = menu.findAll("span", {"class": "price"})[0].text.strip()
        name = menu.findAll("p", {"class": "desc"})[0].text.strip()
        msg += f"{menuType}  {price} {name}\n"
    msg += "```\n"
    return msg