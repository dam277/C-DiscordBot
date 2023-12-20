import discord
import os

from ....models.Server import Server
from ....models.File import File
from ..Command import Command


class GetFile(Command):
    def __init__(self, name):
        self.name = name

        super().__init__()

    async def execute(self, interaction: discord.Interaction):
        """ Execute the command /get_file
        $param interaction: discord.Interaction -> Interaction with the user
        Return message: str -> Send message on discord channel with the file as a reply"""
        # Get the file from the database
        file = await File.get_file_by_name(self.name)
        if file is None:
            await interaction.response.send_message(f"The file **'{self.name}'** does not exists in database !")
            return

        # Check if the path exists and if it don't exists, send error message
        if not os.path.exists(file.path):
            await interaction.response.send_message(f"The file **'{self.name}'** was not found in the folder !")
            return
        
        # Check if the file isn't too big to send it
        if os.stat(file.path).st_size > self.settings["resources"]["max_file_size"]:
            await interaction.response.send_message(f"Sorry, **'{file.name}'** is to big to send it to the server !")
            return

        # Get the file in the folder and send it to the channel
        with open(file.path, 'rb') as f:
            await interaction.response.send_message(content=f"Here is the file you asked : **{file.name}**", file=discord.File(f))
