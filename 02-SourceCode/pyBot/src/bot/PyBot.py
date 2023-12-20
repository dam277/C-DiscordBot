import discord
from discord.ext import commands

from .bot_interactions import slash_commands
from .bot_interactions import events
from ..utils.logger import Logger as lg

class PyBot:
    INTENTS = discord.Intents.all()

    def __init__(self, configs):
        """ Init the bot instance """
        lg.Logger().get_instance().log(lg.LogDefinitions.INFO, f"Initializing {self.__class__.__name__}")

        self.configs = configs          # Set the configs

        # Set the bot instance
        self.bot_instance = commands.Bot(command_prefix="$", intents=self.INTENTS)

        # Setup the bot
        self.setup_intents()
        self.setup_events()
        slash_commands.setup_slash_commands(self.bot_instance)
        events.setup_events(self.bot_instance)

    def setup_intents(self):
        self.INTENTS.message_content = True
        self.INTENTS.guilds = True

    def setup_events(self):
        """ Setup the bot base events """
        @self.bot_instance.event
        async def on_ready():
            """ Execute when the bot is ready """
            lg.Logger().get_instance().log(lg.LogDefinitions.INFO, f"Logged on as {self.bot_instance.user}")
            try:
                # Get the commands to sync
                synced = await self.bot_instance.tree.sync()
                lg.Logger().get_instance().log(lg.LogDefinitions.SUCCESS, f"synced {len(synced)} commands")
            except Exception as e:
                lg.Logger().get_instance().log(lg.LogDefinitions.ERROR, e)

        @self.bot_instance.event
        async def on_connect():
            """ Execute when the bot is connected """
            lg.Logger().get_instance().log(lg.LogDefinitions.INFO, f"Connected as {self.bot_instance.user}")

        @self.bot_instance.event
        async def on_shard_connect(shard_id):
            print(shard_id)

        @self.bot_instance.event
        async def on_disconnect():
            """ Execute when the bot is connected """
            lg.Logger().get_instance().log(lg.LogDefinitions.WARNING, f"Disconnected as {self.bot_instance.user}")

    def run(self):
        """ Run the bot """
        self.bot_instance.run(self.configs["discord_token"])