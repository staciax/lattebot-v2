# Standard 
import discord
import asyncio
import re
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party

# Local
import utils
from config import BYPASS_INVITE

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command()
    @commands.has_role(842309176104976387) 
    async def bypass(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"https://discord.gg/{BYPASS_INVITE} this link will not keep history", delete_after=15)
    
    @commands.command(help="Takes a screenshot of a website", aliases=["ss"])
    @commands.guild_only()
    async def screenshot(self, ctx, link):
        URL_REGEX = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
        
        if not re.fullmatch(URL_REGEX, link):
            return await ctx.send("Invalid URL! Make sure you put `https://` infront of it.")
        
        else:
            embed=discord.Embed(title=f"Screenshot : {link}", color=0xffffff)
            embed.set_image(url=f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{link}")
            await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Misc(bot))