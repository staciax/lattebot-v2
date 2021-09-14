# Standard 
import discord , asyncio
import datetime
from discord.ext import commands
from datetime import datetime, timezone , timedelta

# Third party
import aiohttp

# Local
import utils

class api_waifu(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command()
    @commands.guild_only()
    async def bully(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/bully") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Bully", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return

    @commands.command()
    @commands.guild_only()
    async def cry(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/cry") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Cry", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)           
                else:
                    error=api["error"]

    @commands.command()
    @commands.guild_only()
    async def bonk(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/bonk") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Bonk", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)          
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def kiss(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/kiss") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Kiss", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/lick") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Lick", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def pat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/pat") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Pat", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def smug(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/smug") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Smug", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def blush(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/blush") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Blush", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def smile(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/smile") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Smile", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def nom(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/nom") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Nom", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def bite(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/bite") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Bite", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/slap") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Slap", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def kicks(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/kick") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Kick", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def happy(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/happy") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Happy", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def wink(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/sfw/wink") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Wink", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def waifu2(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/nsfw/waifu") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Waifu", color=0xffffff)
                        embed.set_image(url=image_url)

                        await ctx.send(embed=embed)
                    else:
                        return
        else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/sfw/waifu") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Waifu", color=0xffffff)
                        embed.set_image(url=image_url)

                        await ctx.send(embed=embed)
                    else:
                        return
    
    @commands.command()
    @commands.guild_only()
    async def neko(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/nsfw/neko") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Neko", color=0xffffff)
                        embed.set_image(url=image_url)

                        await ctx.send(embed=embed)
                    else:
                        return
        else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/sfw/neko") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Neko", color=0xffffff)
                        embed.set_image(url=image_url)

                        await ctx.send(embed=embed)
                    else:
                        return

    #nsfw
    @commands.command()
    @commands.is_nsfw()
    async def trap(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/nsfw/trap") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Trap", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return
    
    @commands.command()
    @commands.is_nsfw()
    async def blowjob(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.waifu.pics/nsfw/blowjob") as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Blowjob", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
                else:
                    return

def setup(client):
    client.add_cog(api_waifu(client))