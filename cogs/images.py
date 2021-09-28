# Standard 
import discord
import asyncio
import json
import random
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party
import aiohttp

# Local
from config import *
from utils.images_converter import *

class Images_(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command(description="Random picture of a meow")
    @commands.guild_only()
    async def cat(self, ctx):
        view = cat_view(ctx)
        await view.api_start()
    
    @commands.command(description="Random picture of a floofy")
    @commands.guild_only()
    async def fox(self, ctx):
        view = fox_view(ctx)
        await view.api_start()

    @commands.command(aliases=['gif'], help=f"aqua", usage=f"[search]")
    @commands.guild_only()
    async def giphy(self, ctx, *, search=None):
        gipht_apis = self.bot.giphy_api_
        embed = discord.Embed(colour=0xffffff)
        session = aiohttp.ClientSession()
        if search == None:
            response = await session.get(f'https://api.giphy.com/v1/gifs/random?api_key={gipht_apis}')
            data = json.loads(await response.text())
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + f'&api_key={gipht_apis}&limit=10')
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

        await session.close()

        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Images_(bot))