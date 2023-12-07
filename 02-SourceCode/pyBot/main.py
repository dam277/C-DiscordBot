import logging

import os
from dotenv import load_dotenv

from src.bots.PyBot import PyBot
from src.utils.logger import Logger as lg

def main():
    lg.Logger().get_instance().setup()
    logging.warning('This message will get logged on to a file')

    load_dotenv()
    discord_token = os.getenv("BOT_TOKEN")
    bot = PyBot({"discord_token": discord_token})
    bot.setup()
    bot.run()

if __name__ == "__main__":
    main()