# Standard 
import discord , asyncio
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party

# Local
import utils

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command()
    async def bypass(self, ctx):
        await ctx.message.delete()
        await ctx.send("https://discord.gg/jhK46N6QWU this link will not keep history", delete_after=15)
    
def setup(bot):
    bot.add_cog(Misc(bot))