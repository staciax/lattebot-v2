# Standard 
import discord , asyncio
from discord import Embed
import datetime
from discord.ext import commands
from datetime import datetime, timezone , timedelta

# Third party
import aiohttp

# Local
import utils

#button_view
class button(discord.ui.Button):
    async def callback(self, interaction):
        if self.label == "❤️":
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/sfw/waifu") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Waifu",url=api["url"], color=0xffffff)
                        embed.set_image(url=image_url)

        elif self.label == "💙":
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/nsfw/waifu") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Waifu",url=api["url"], color=0xffffff)
                        embed.set_image(url=image_url)
                    
        await interaction.response.edit_message(embed=embed, view=self.view)

class api_waifu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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
                    embed = discord.Embed(title="Bully",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Cry",url=api["url"] , color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)           
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
                    embed = discord.Embed(title="Bonk" , url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)          
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
                    embed = discord.Embed(title="Kiss",url=api["url"] , color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Lick",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Pat",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Smug",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Blush",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Smile",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Nom",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Bite",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Slap",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Kick",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Happy",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Wink",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
                else:
                    return
    
    @commands.command()
    @commands.guild_only()
    async def waifu(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/nsfw/waifu") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Waifu",url=api["url"], color=0xffffff)
                        embed.set_image(url=image_url)

                        #with_button
                        view = discord.ui.View(timeout=300)
                        view.add_item(button(label="💙"))
                        await ctx.send(embed=embed, view=view)
                    else:
                        return
        else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/sfw/waifu") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Waifu",url=api["url"], color=0xffffff)
                        embed.set_image(url=image_url)

                        #with_button
                        view = discord.ui.View(timeout=300)
                        view.add_item(button(label="❤️"))
                        await ctx.send(embed=embed, view=view)
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
                        embed = discord.Embed(title="Neko",url=api["url"], color=0xffffff)
                        embed.set_image(url=image_url)

                        await ctx.reply(embed=embed, mention_author=False)
                    else:
                        return
        else:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f"https://api.waifu.pics/sfw/neko") as rep:
                    api = await rep.json()
                    if rep.status == 200:
                        image_url=api["url"]
                        embed = discord.Embed(title="Neko",url=api["url"], color=0xffffff)
                        embed.set_image(url=image_url)

                        await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Trap",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
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
                    embed = discord.Embed(title="Blowjob",url=api["url"], color=0xffffff)
                    embed.set_image(url=image_url)

                    await ctx.reply(embed=embed, mention_author=False)
                else:
                    return

def setup(bot):
    bot.add_cog(api_waifu(bot))