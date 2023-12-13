from discord.ext import commands
class Command:
    def __init__(self, ctx: commands.context.Context):
        print("ctx")
        self.ctx = ctx

    async def execute(self):
        print("Executing command")
        await self.ctx.send(self.ctx.command.name)

    async def getText(self):
        return "test"