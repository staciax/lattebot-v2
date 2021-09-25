# Standard 
import discord , asyncio
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party

# Local
import utils
from config import *

class Latte_user(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command()
    @commands.guild_only()
    async def takeru(self, ctx):
        embed = discord.Embed(title="Who is that Pokemon?", color=PTYELLOW)
        embed.set_image(url="https://c.tenor.com/2E9qKpHMWFUAAAAd/psylexx-crl.gif")
        
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Latte_user(bot))