import discord
from discord import app_commands
from discord.ext import commands

from colorama import Fore

from .BotBase import BotBase

from ..commands.help.Commands import Commands

class PyBot(BotBase): 
    def __init__(self, configs): 
        super().__init__(configs)

    def setup(self):
        """ Setup the bot commands and events """

        @self.bot_instance.command()
        async def users(ctx: commands.context.Context):
            # await ctx.send(ctx.command.name)
            c = Commands(ctx)
            await c.execute()
            txt = await c.getText()
            print(txt)
            
        @self.bot_instance.event()
        async def on_message(message: discord.Message):
            """ Execute when a message is sended
            $param -> message : Message sended
            """
            if message.content.startswith(self.bot_instance.command_prefix):
                await self.bot_instance.process_commands(message)
            else:
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
        
        @self.bot_instance.tree.command(guild=discord.Object(id=1024725027691712572), name="gtn", description="guess number")
        async def gtn(interaction: discord.Interaction):
            """A Slash Command to play a Guess-the-Number game."""

            await interaction.response.send_message('Guess a number between 1 and 10.')

            found = False
            while not found:
                guess = await self.bot_instance.wait_for('message', check=lambda message: message.author == interaction.user)

                try:
                    if int(guess.content) == 5:
                        await guess.reply('You guessed it!')
                        found = True
                    else:
                        await guess.reply('Nope, try again.')
                except ValueError as ve:
                    print(ve)

        @self.bot_instance.tree.command(guild=discord.Object(id=1024725027691712572), name="embed", description="embed")
        async def hello(interaction: discord.Interaction):
            embed = discord.Embed(
                title="My Amazing Embed",
                description="Embeds are super easy, barely an inconvenience.",
                color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
            )
            embed.add_field(name="A Normal Field", value="A really nice field with some information. **The description as well as the fields support markdown!**")

            embed.add_field(name="Inline Field 1", value="Inline Field 1", inline=True)
            embed.add_field(name="Inline Field 2", value="Inline Field 2", inline=True)
            embed.add_field(name="Inline Field 3", value="Inline Field 3", inline=True)
        
            embed.set_footer(text="Footer! No markdown here.") # footers can have icons too
            embed.set_author(name="Pycord Team", icon_url="https://guide.pycord.dev/img/logo.png")
            embed.set_thumbnail(url="https://guide.pycord.dev/img/logo.png")
            embed.set_image(url="https://guide.pycord.dev/img/banner-v3.png")
        
            await interaction.response.send_message("Hello! Here's a cool embed.", embed=embed) # Send the embed with some text

        @self.bot_instance.tree.command(guild=discord.Object(id=1024725027691712572), name="account_creation_date", description="acc creation date")  # create a user command for the supplied guilds
        async def account_creation_date(interaction: discord.Interaction, member: discord.Member):  # user commands return the member
            await interaction.response.send_message(f"{member.name}'s account was created on {member.created_at}")



