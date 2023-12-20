import discord
import os

from ....models.Server import Server
from ....models.File import File
from ..Command import Command


class AddFile(Command):
    def __init__(self, guild_id, file: discord.Attachment):
        self.guild_id = guild_id
        self.file = file

        super().__init__()

    async def execute(self, interaction: discord.Interaction):
        """ Execute the command /add_file
        $param interaction: discord.Interaction -> Interaction with the user
        Return message: str -> message sent on discord channel as a reply"""

        # Check if the file isn't too big to send it
        if self.file.size > self.settings["resources"]["max_file_size"]:
            await interaction.response.send_message(f"Sorry, **'{self.file.filename}'** is to big, a file must be less than 25mb !")
            return

        # Set the paths for the file
        dir_path = f"{self.settings["resources"]["filesPath"]}/{self.guild_id}"
        file_path = f"{dir_path}/{self.file.filename}"

        # Check if the path exists and create the folder if not
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            
        # Save the file
        await self.file.save(file_path)

        # Get the server by guild_id
        server = await Server.get_server_by_guild_id(self.guild_id)
        if server is None:
            await interaction.response.send_message("The server does not exists in database... Make a /setup first")
            return

        # Save the file to the database
        message = await File.add_file(name=self.file.filename, path=file_path, fk_server=server.id)
        await interaction.response.send_message(message)
