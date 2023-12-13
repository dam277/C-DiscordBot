import discord
from discord.ext import commands

from ..bot_commands.setup.Setup import Setup

import os
import json

def setup_slash_commands(bot_instance: commands.Bot):
    """ Setup the bot slash commands events """
    s = open("src/resources/configs/settings.json")
    settings = json.load(s)
    
    @bot_instance.tree.command(guild=discord.Object(id=1024725027691712572), name="setup", description="Setup the server into the database")
    async def setup(interaction: discord.Interaction):
        """ Get the commands of the bot """
        command = Setup(interaction.guild.id, interaction.guild.name)
        await command.execute(interaction)

    @bot_instance.tree.command(guild=discord.Object(id=1024725027691712572), name="add_file", description="Add a file to the database")
    async def add_file(interaction: discord.Interaction, file: discord.Attachment):
        """ Add the file to the database """
        # Set the paths for the files
        dir_path = f"{settings["resources"]["filesPath"]}/{interaction.guild.id}"
        file_path = f"{dir_path}/{file.filename}"

        # Check if the path exists and create the folder if not
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            
        # Save the file
        await file.save(file_path)

        # Send the file to the server
        #await interaction.response.send_message(content="File sent:", file=discord.File(file_path))