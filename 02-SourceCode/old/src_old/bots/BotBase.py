import discord
from discord.ext import commands

from ..utils.logger import Logger as lg
from colorama import Fore

class BotBase:
    INTENTS = discord.Intents.all()
    instance = None
        
    def __init__(self, configs):
        lg.Logger().get_instance().log(lg.LogDefinitions.INFO, f"Initializing {self.__class__.__name__}")
        """ Init the bot instance """
        #Set the intents
        self.INTENTS.message_content = True
        self.INTENTS.guilds = True
        #Set the configs
        self.configs = configs

        #Set the bot instance
        self.bot_instance = commands.Bot(command_prefix="$", intents=self.INTENTS)
        self.setup_events()

    def setup_events(self):
        """ Setup the bot base events """
        @self.bot_instance.event
        async def on_ready():
            """ Execute when the bot is ready """
            lg.Logger().get_instance().log(lg.LogDefinitions.INFO, f"Logged on as {self.bot_instance.user}")
            try:
                # Get the commands to sync
                synced = await self.bot_instance.tree.sync(guild=discord.Object(id=1024725027691712572))
                lg.Logger().get_instance().log(lg.LogDefinitions.SUCCESS, f"synced {len(synced)} commands")
            except Exception as e:
                lg.Logger().get_instance().log(lg.LogDefinitions.ERROR, e)
    
    def run(self):
        """ Run the bot """
        self.bot_instance.run(self.configs["discord_token"])

