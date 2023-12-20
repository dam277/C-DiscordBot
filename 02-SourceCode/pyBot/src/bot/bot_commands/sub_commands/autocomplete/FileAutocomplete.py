import discord
import os

from .....models.Server import Server
from .....models.File import File
from ...Command import Command


class FileAutocomplete(Command):
    def __init__(self, current, guild_id):
        self.current = current
        self.guild_id = guild_id

        super().__init__()

    async def execute(self):
        """ """
        # Get the server id
        server_id = await Server.get_server_id_by_guild_id(self.guild_id)

        # Get all the files of the server
        return await File.get_files_by_server_id(server_id)
