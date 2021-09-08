# Standard 
import discord , asyncio
import datetime
from discord.ext import commands
from datetime import datetime, timezone , timedelta

# Third party
import aiohttp

#button
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

# Local
import utils

# hori_api_token
token="eyJpZCI6MjQwMDU5MjYyMjk3MDQ3MDQxLCJzZWNyZXQiOiI1YzZmdjJXZVlyc1VIdyJ9.TCHvudlvbahx4OaEJY8_8Hx503Y"

headers = {'Stacia':f'aiohttp/{aiohttp.__version__}; Lattebot','Authorization':f"Bearer {token}"}

class hori_api(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.bot = client
        slash = InteractionClient(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command()
    @commands.guild_only()
    async def waifu(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/sfw/waifu/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Waifu", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def ecchi(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/ecchi/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Ecchi", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def ero(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/ero/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Ero", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/hentai/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Hentai", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def maid(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/maid/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Maid", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def milf(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/milf/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Milf", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
                    return
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def oppai(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/oppai/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Oppai", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def oral(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/oral/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Oral", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def paizuri(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/paizuri/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Paizuri", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def selfies(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/selfies/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Selfies", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]
    
    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def uniform(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.hori.ovh/nsfw/uniform/",headers=headers) as rep:
                api = await rep.json()
                if rep.status == 200:
                    image_url=api["url"]
                    embed = discord.Embed(title="Uniform", color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.send(embed=embed)
            
                else:
                    error=api["error"]

#    @commands.command()
#    async def button_test(self, ctx):
#        buttons = ActionRow(
#        Button(
#            style=ButtonStyle.green,
#            label="->",
#            custom_id="next"
#            )
#        )
#
#        async with aiohttp.ClientSession() as cs:
#            async with cs.get(f"https://api.hori.ovh/sfw/waifu/",headers=headers) as rep:
#                api = await rep.json()
#                if rep.status == 200:
#                    image_url=api["url"]
#                    embed = discord.Embed(title="Waifu", color=0xffffff)
#                    embed.set_image(url=image_url)
#            
#                else:
#                    error=api["error"]
#
#        msg = await ctx.send(embed=embed,
#            components=[buttons]
#        )
#
#        on_click = msg.create_click_listener(timeout=60)
#        
#        def check(inter):
#            return inter.message.id == msg.id
#        inter = await ctx.wait_for_button_click(check)
#        
#        @on_click.matching_id("next")
#        async def on_next(inter):
#            async with aiohttp.ClientSession() as cs:
#                async with cs.get(f"https://api.hori.ovh/sfw/waifu/",headers=headers) as rep:
#                    api = await rep.json()
#                    if rep.status == 200:
#                        image_url=api["url"]
#                        embed = discord.Embed(title="Waifu", color=0xffffff)
#                        embed.set_image(url=image_url)
#                
#                    else:
#                        error=api["error"]
#            await inter.reply(embed=embed)

#        @on_click.timeout
#        async def on_timeout():
#            await msg.edit(components=[])
    

def setup(client):
    client.add_cog(hori_api(client))