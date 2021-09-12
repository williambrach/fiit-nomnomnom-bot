from events.base_event import BaseEvent
from utils import get_channel
from datetime import datetime
import crawler
import datetime
# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class


class ExampleEvent(BaseEvent):

    def __init__(self):
        interval_minutes = 60  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        now = datetime.now()

        if now.hour == 8:
            weekDay = datetime.datetime.today().weekday()
            skDay = {
                0: "Pondelok",
                1: "Utorok",
                2: "Streda",
                3: "Štvrtok",
                4: "Piatok",
                5: "Sobota",
                6: "Nedeľa",
            }

            msg = str(skDay[weekDay]) + "\t" + str(datetime.date.today()) + "\n"
            try:
                msg += crawler.getFiitFood(weekDay)
            except:
                if weekDay == 5 or weekDay == 6:
                    msg += "**FIITFOOD**\n"
                    msg += "FiitFood je počaš víkendu bohužial zatvorený.\n"
                else:
                    msg += "**FIITFOOD**\n"
                    msg += "Pri spracovaní FIITFOOD nastala chyba, Ospravedlňujem sa za problém admin už rieši.\n"
                    msg += "Menu môžeš nájsť na linku - http://www.freefood.sk/menu/#fiit-food \n"
            try:
                msg += crawler.getKoliba(weekDay)
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

            channel = get_channel(client, "papanie")
            await channel.purge()
            await channel.send(msg)
