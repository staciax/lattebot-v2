# Standard 
import discord, asyncio, json, random
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party
import aiohttp

# Local
import utils
from config import *

class Images_(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command(description="Random picture of a meow",brief=f"{PREFIX}cat", usage=f"{PREFIX}cat")
    @commands.guild_only()
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow" , color=0xffffff)
                    embed.set_image(url=data['file'])

                    await ctx.send(embed=embed)
    
    @commands.command(description="Random picture of a floofy" , brief=f"{PREFIX}fox", usage=f"{PREFIX}fox")
    @commands.guild_only()
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Fox", color=0xffffff)
                    embed.set_image(url=data['image'])

                    await ctx.send(embed=embed)

    @commands.command(aliases=['gif'], brief=f"{PREFIX}giphy aqua", usage=f"{PREFIX}giphy [search]")
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