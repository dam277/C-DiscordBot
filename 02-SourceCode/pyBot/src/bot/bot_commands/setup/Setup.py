import discord

from ....models.Server import Server
from ..Command import Command


class Setup(Command):
    def __init__(self, guild_id, name):
        self.guild_id = guild_id
        self.name = name

    async def execute(self, interaction: discord.Interaction):
        message = await Server.create_server(guild_id=self.guild_id, name=self.name)
        await interaction.response.send_message(message, ephemeral=True)
