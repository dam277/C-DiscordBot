import logging

import os
from dotenv import load_dotenv

from src.bot.PyBot import PyBot

def main():
    logging.basicConfig(level=logging.INFO)

    load_dotenv()
    discord_token = os.getenv("BOT_TOKEN")
    bot = PyBot({"discord_token": discord_token})
    bot.setup()
    bot.run()

if __name__ == "__main__":
    main()