import discord
from discord.ext import commands

import logging
from colorama import Fore

class BotBase:
    INTENTS = discord.Intents.all()
        
    def __init__(self, configs):
        logging.info(f"{Fore.CYAN} Initializing bot {Fore.RESET}")
        """ Init the bot instance """
        #Set the intents
        self.INTENTS.message_content = True
        self.INTENTS.guilds = True

        #Set the configs
        self.configs = configs
        print(self.configs)

        #Set the bot instance
        self.bot_instance = commands.Bot(command_prefix="+", intents=self.INTENTS)
        self.setup_events()

    def setup_events(self):
        """ Setup the bot base events """
        @self.bot_instance.event
        async def on_ready():
            """ Execute when the bot is ready """
            logging.info(f"{Fore.GREEN}Logged on as {self.bot_instance.user}")
            try:
                # Get the commands to sync
                synced = await self.bot_instance.tree.sync(guild=discord.Object(id=1024725027691712572))
                print(f"Synced {len(synced)} commands")
            except Exception as e:
                logging.error(f"{Fore.RED} {e}")
    
    def run(self):
        """ Run the bot """
        self.bot_instance.run(self.configs["discord_token"])