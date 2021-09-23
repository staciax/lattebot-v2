# Standard 
import discord , asyncio
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta
from discord import Embed

# Third party
import aiohttp

# Local
from utils.waifu_pisc_api import *

class Button_test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.command()
    async def test_view(self, ctx):
        view = sfw_megumin(ctx)
        await view.api_start()
        #view.stop()
        
def setup(bot):
    bot.add_cog(Button_test(bot))