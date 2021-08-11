# Standard 
import discord , datetime , time
from discord.ext import commands
from datetime import datetime, timezone

import io
import aiohttp
import random
import anime_images_api
import hmtai
import requests
import json

anime = anime_images_api.Anime_Images()

# Third party
# Local
from config import *
from utils import text_to_owo , notify_user

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="Any message to owo")
    @commands.is_owner()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))
    
    @commands.command()
    @commands.is_owner()
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")
    
    @commands.command(brief="Random picture of a meow")
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow" , color=0xffffff)
                    embed.set_image(url=data['file'])

                    await ctx.send(embed=embed)
    
    @commands.command(brief="Random picture of a floofy")
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Floof", color=0xffffff)
                    embed.set_image(url=data['image'])

                    await ctx.send(embed=embed)

    @commands.command(aliases=['ani', 'anigif'])
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
                    embed.description = "**List** : hug, kiss, cuddle, pat, kill, slap, wink , hentai"
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
    async def anime_img_nsfw(self, ctx):
            embed = discord.Embed(color=0xffffff)
            try:
                if ctx.channel.is_nsfw():
                    img_list = ['hentai', 'boobs']
                    nsfw_random = random.choice(img_list)
                    nsfw_url = anime.get_nsfw(f"{nsfw_random}")
                    embed.set_image(url=nsfw_url)
                    await ctx.send(embed=embed)
                else:
                    embed.description = "This is not a NSFW channel, **NSFW** is alollowed in <#850507964938715196>"
                    await ctx.send(embed=embed)          
            except:
                return
    
    @commands.command(aliases=['gif'])
    async def giphy(self, ctx, *, search=None):
        embed = discord.Embed(colour=0xffffff)
        session = aiohttp.ClientSession()

        if search == None:
            response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=8DkQhUOR3dPIMPAzJCgonC7ZW5pnjU3V')
            data = json.loads(await response.text())
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=8DkQhUOR3dPIMPAzJCgonC7ZW5pnjU3V&limit=10')
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

        await session.close()

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))