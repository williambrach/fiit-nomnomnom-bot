from commands.base_command  import BaseCommand
from utils                  import get_emoji
from random                 import randint
import requests
from bs4 import BeautifulSoup
import crawler
import datetime
# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Test(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Testing"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        weekDay = datetime.datetime.today().weekday()
        skDay = {
            0 : "Pondelok",
            1 : "Utorok",
            2 : "Streda",
            3 : "Štvrtok",
            4 : "Piatok",
            5 : "Sobota",
            6 : "Nedeľa",
        }

        msg =  str(skDay[weekDay]) + "\t" + str(datetime.date.today()) + "\n"
        try:
            msg += crawler.getFiitFood(weekDay-1)
        except:
            if weekDay == 5 or weekDay == 6:
                msg += "**FIITFOOD**\n"
                msg += "FiitFood je počaš víkendu bohužial zatvorený.\n"
            else:
                msg += "**FIITFOOD**\n"
                msg += "Pri spracovaní FIITFOOD nastala chyba, Ospravedlňujem sa za problém admin už rieši.\n"
                msg += "Menu môžeš nájsť na linku - http://www.freefood.sk/menu/#fiit-food \n"
        try:
            msg += crawler.getKoliba(weekDay-1)
        except:
            if weekDay == 5 or weekDay == 6:
                msg += "**MLYNSKÁ KOLIBA**\n"
                msg += "Mlynská koliba počaš víkendu nevarí obedové menu.\n"
            else:
                msg += "**MLYNSKÁ KOLIBA**\n"
                msg += "Pri spracovaní Mlynskej koliby nastala chyba, Ospravedlňujem sa za problém admin už rieši.\n"
                msg += "Menu môžeš nájsť na linku - https://mlynskakoliba.sk/#done \n"
                
        try:
            msg += crawler.getEat(weekDay)
        except:
            msg += "**EAT&MEET**\n"
            msg += "Pri spracovaní EAT&MEET nastala chyba, Ospravedlňujem sa za problém admin už rieši.\n"
            msg += "Menu môžeš nájsť na linku - http://eatandmeet.sk/tyzdenne-menu \n"        

        await message.channel.send(msg)
