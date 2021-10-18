# Standard 
import discord
import time
import datetime
from discord.ext import commands

# Third party
import aiohttp

# Local
import utils

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    # @commands.command()
    # async def testing_waifu_im(self, ctx, type : str=None):
    #     url = "https://api.waifu.im/nsfw/ass/"

    #     if str(type).lower() == "gif":
    #         url = "https://api.waifu.im/nsfw/ass/?gif=True"

    #     async with aiohttp.ClientSession() as session:
    #         request = await session.get(url)
    #         json = await request.json()

    #     dominant_color1 = str(json['tags'][0]['images'][0]['dominant_color']).replace('#', '')
    #     dominant_color = int(dominant_color1, 16)
    #     print(dominant_color)

    #     embed = discord.Embed(title="Ass", url=json['tags'][0]['images'][0]['url'], color=dominant_color)
    #     embed.set_image(url=json['tags'][0]['images'][0]['url'])

    #     await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Test(bot))