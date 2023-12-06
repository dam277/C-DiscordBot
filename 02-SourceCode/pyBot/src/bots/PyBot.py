import discord
from discord import app_commands
from discord.ext import commands

import logging
from colorama import Fore
import json

from .BotBase import BotBase

class PyBot(BotBase): 
    def __init__(self, configs): 
        super().__init__(configs)

    def setup(self):
        """ Setup the bot commands and events """
        @self.bot_instance.event
        async def on_message(message):
            """ Execute when a message is sended
            $param -> message : Message sended
            """
            print(f"{Fore.WHITE} -> {message.author}: {message.content}")
            
            # Check if the author is the bot himself
            if message.author == self.bot_instance.user:
                return
            
            # Check the command to send the message
            if message.content.startswith('$hello'):
                await message.reply(f'Hello {message.author.display_name}')

        @self.bot_instance.tree.command(guild=discord.Object(id=1024725027691712572), name="test", description="Test command")
        async def test_command(interaction: discord.Interaction):
            """ Execute when the command /test is sended
            $param -> interaction(discord.Interaction) : interaction of the user with the command
            """
            await interaction.response.send_message("test")