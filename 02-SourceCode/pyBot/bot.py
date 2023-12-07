import discord
from discord.ext import commands

INTENTS = discord.Intents.all()
INTENTS.message_content = True

client = commands.Bot(command_prefix="$", intents=INTENTS)

@client.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands")
    embed.add_field(name="$info", value="Shows info about the bot", inline=False)
    embed.add_field(name="$users", value="Shows how many members the server has", inline=False)
    await ctx.send(content=None, embed=embed)

@client.command()
async def info(ctx):
    await ctx.send("Made by Ra'Ed#2931")

@client.command()
async def users(ctx):
    await ctx.send(f"""This server has {len(client.get_guild(1024725027691712572).members)} members""")

@client.tree.command(guild=discord.Object(id=1024725027691712572), name="test", description="Test command")
async def test_command(interaction: discord.Interaction):
    """ Execute when the command /test is sended
    $param -> interaction(discord.Interaction) : interaction of the user with the command
    """
    await interaction.response.send_message("test")

client.run("MTE4MTA3NzMzNDE4NzU5MzgxOA.GMBLlV.kzHtULxiS4d6XRJVDZpMHQ2VGUXBvvvZJZmbEg")
