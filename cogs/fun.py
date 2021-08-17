# Standard 
import discord , datetime , time
from discord.ext import commands
from datetime import datetime, timezone

# Third party
import json
import io
import aiohttp , random , anime_images_api , requests , json
anime = anime_images_api.Anime_Images()

import typing , unicodedata
from typing import Union

# Local
from config import *
from utils import text_to_owo , notify_user

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="Any message to owo")
    @commands.guild_only()
    @commands.is_owner()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))
    
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")
    
    @commands.command(brief="Random picture of a meow")
    @commands.guild_only()
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow" , color=0xffffff)
                    embed.set_image(url=data['file'])

                    await ctx.send(embed=embed)
    
    @commands.command(brief="Random picture of a floofy")
    @commands.guild_only()
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Fox", color=0xffffff)
                    embed.set_image(url=data['image'])

                    await ctx.send(embed=embed)

    @commands.command(aliases=['ani', 'anigif'])
    @commands.guild_only()
    async def anime_img(self, ctx , category=None):
            embed = discord.Embed(color=0xffffff)
            try:
                if category == None:
                    img_list = ['hug', 'kiss', 'cuddle', 'pat', 'kill', 'slap', 'wink']
                    img_random = random.choice(img_list)
                    img_link = anime.get_sfw(f"{img_random}")
                    embed.set_image(url=img_link)
                    await ctx.send(embed=embed)
                elif category == "list":
                    embed.description = "**Caterogy** : hug, kiss, cuddle, pat, kill, slap, wink , hentai\n**Example** : `lt ani hug` , `lt ani kiss`"
                    await ctx.send(embed=embed)
                elif category == "hentai":
                    if ctx.channel.is_nsfw():
                        img_list = ['hentai', 'boobs']
                        nsfw_random = random.choice(img_list)
                        nsfw_url = anime.get_nsfw(f"{nsfw_random}")
                        embed.set_image(url=nsfw_url)
                        await ctx.send(embed=embed)
                    else:
                        embed.description = "This is not a NSFW channel, **NSFW** is alollowed in <#850507964938715196>"
                        await ctx.send(embed=embed)          
                else:
                    img_link = anime.get_sfw(f"{category}")
                    embed.set_image(url=img_link)
                    await ctx.send(embed=embed)
            except:
                return

    @commands.command(aliases=['hentai', 'nsfw'])
    @commands.guild_only()
    async def anime_img_nsfw(self, ctx):
            try:
                if ctx.channel.is_nsfw():
                    embed = discord.Embed(color=0xffffff)
                    img_list = ['hentai', 'boobs']
                    nsfw_random = random.choice(img_list)
                    nsfw_url = anime.get_nsfw(f"{nsfw_random}")
                    embed.set_image(url=nsfw_url)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(color=0xffffff)
                    embed.description = "This is not a NSFW channel, **NSFW** is alollowed in <#850507964938715196>"
                    await ctx.send(embed=embed)          
            except:
                return
    
    @commands.command(aliases=['gif'])
    @commands.guild_only()
    async def giphy(self, ctx, *, search=None):
        gipht_apis = self.client.giphy_api_
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
    
    @commands.command(name="rn", brief="takes smallest and largest numbers then does a random number between.")
    @commands.guild_only()
    async def random_number(self , ctx , *numbers: typing.Union[int,str]):
        numbers=sorted(list(filter(lambda x: isinstance(x, int), numbers)))
        if len(numbers) < 2:
            await ctx.send("Not enough numbers")

        else:
            embed = discord.Embed(title=f"Random Number: {random.randint(numbers[0],numbers[-1])} ",color=random.randint(0, 16777215))
            embed.add_field(name="Lowest Number:",value=f"{numbers[0]}")
            embed.add_field(name="Highest Number:",value=f"{numbers[-1]}")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))