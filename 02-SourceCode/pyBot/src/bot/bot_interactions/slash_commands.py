import discord
from discord.ext import commands

from ..bot_commands.setup.Setup import Setup
from ..bot_commands.files.AddFile import AddFile
from ..bot_commands.files.GetFile import GetFile
from ..bot_commands.sub_commands.autocomplete.FileAutocomplete import FileAutocomplete

def setup_slash_commands(bot_instance: commands.Bot):
    """ Setup the bot slash commands events """
    
    # ---- Setup command ------------------------
    @bot_instance.tree.command(name="setup", description="Setup the server into the database")
    async def setup(interaction: discord.Interaction):
        """ Get the commands of the bot """
        # Create object of the command with the datas
        command = Setup(interaction.guild.id, interaction.guild.name)
        await command.execute(interaction)

    # ---- use methods command ------------------------
    @bot_instance.tree.command(name="use_methods", description="Check methods of the bot object")
    async def use_methods(interaction: discord.Interaction):
        """ Get the file from the database and send it to the channel """
        for emoji in bot_instance.emojis:
            print(emoji)

    @bot_instance.tree.command(name="create_guild", description="Create a discord server with the specified name and image")
    async def create_guild(interaction: discord.Interaction, guild_name: str, guild_icon: discord.Attachment):
        g_icon = await guild_icon.read()
        guild = await bot_instance.create_guild(name=guild_name, icon=g_icon)
        await interaction.response.send_message(f"The server {guild.name} has been created")

    @bot_instance.tree.command(name="get_guild", description="Get a guild by his name where the bot is in it")
    async def get_guild(interaction: discord.Interaction, guild_name: str):
        for guild in bot_instance.guilds:
            print(guild.name)
            if guild.name == guild_name:
                channel = await guild.create_text_channel(name="general")
                link = await discord.abc.GuildChannel.create_invite(channel, max_age='300')
                await interaction.response.send_message(f"Here is an invite for the server {guild.name} : {link}")

    @bot_instance.tree.command(name="delete_guild", description="Delete a guild by his name, if name isn't specified, delete the server where you did this command.")
    async def delete_guild(interaction: discord.Interaction, guild_name: str|None):
        if guild_name is None: guild_name = interaction.guild.name
        for guild in bot_instance.guilds:
            print(guild.name)
            if guild.name == guild_name:
                await guild.delete()
                await interaction.response.send_message(f"The server {guild.name} has been deleted")

    # ---- File commands ------------------------
    # FILE AUTOCOMPLETE
    async def file_autocomplete(interaction: discord.Interaction, current: str) -> list[discord.app_commands.Choice[str]]:
        file_autocomplete = FileAutocomplete(current, interaction.guild.id)
        files = await file_autocomplete.execute()

        return [
            discord.app_commands.Choice(name=file.name, value=file.name)
            for file in files if current.lower() in file.name.lower()
        ]

    # ---- add file command ------------------------
    @bot_instance.tree.command(name="add_file", description="Add a file to the database")
    async def add_file(interaction: discord.Interaction, file: discord.Attachment):
        """ Add the file to the database """
        command = AddFile(interaction.guild.id, file)
        await command.execute(interaction)

    # ---- get file command ------------------------
    @bot_instance.tree.command(name="get_file", description="Get a file from the database and send it to the channel")
    @discord.app_commands.autocomplete(file_name=file_autocomplete)
    async def get_file(interaction: discord.Interaction, file_name: str):
        """ Get the file from the database and send it to the channel """
        command = GetFile(file_name)
        await command.execute(interaction)