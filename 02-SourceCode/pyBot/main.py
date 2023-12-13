import logging

import src.models.Server as srv
import os
from dotenv import load_dotenv

from src.bot.PyBot import PyBot
from src.utils.logger import Logger as lg

def main():
    lg.Logger().get_instance().setup()

    load_dotenv()
    discord_token = os.getenv("BOT_TOKEN")
    bot = PyBot({"discord_token": discord_token})
    bot.run()

if __name__ == "__main__":
    main()