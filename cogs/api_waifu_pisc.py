# Standard 
import discord , asyncio
from discord import Embed
import datetime
from discord.ext import commands
from datetime import datetime, timezone , timedelta

# Third party
import aiohttp

# Local
from utils.waifu_pisc_api import *


class api_waifu2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        
    @commands.command()
    @commands.guild_only()
    async def waifu(self, ctx):
        title = "Waifu"
        if ctx.channel.is_nsfw():
            url = "https://api.waifu.pics/nsfw/waifu"
            view = base_pisc_api(ctx, url, title)
            await view.api_start()
        else:
            url = "https://api.waifu.pics/sfw/waifu"
            view = base_pisc_api(ctx, url, title)
            await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def neko(self, ctx):
        title = "Neko"
        if ctx.channel.is_nsfw():
            url = "https://api.waifu.pics/nsfw/neko"
            view = base_pisc_api(ctx, url, title)
            await view.api_start()
        else:
            url = "https://api.waifu.pics/sfw/neko"
            view = base_pisc_api(ctx, url, title)
            await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def shinobu(self, ctx):
        url = "https://api.waifu.pics/sfw/shinobu"
        title = "Shinobu"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def megumin(self, ctx):
        url = "https://api.waifu.pics/sfw/megumin"
        title = "Megumin"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def bully(self, ctx):
        url = "https://api.waifu.pics/sfw/bully"
        title = "Bully"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx):
        url = "https://api.waifu.pics/sfw/cuddle"
        title = "Cuddle"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def cry(self, ctx):
        url = "https://api.waifu.pics/sfw/cry"
        title = "Cry"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx):
        url = "https://api.waifu.pics/sfw/hug"
        title = "Hug"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def awoo(self, ctx):
        url = "https://api.waifu.pics/sfw/awoo"
        title = "Awoo"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def kiss(self, ctx):
        url = "https://api.waifu.pics/sfw/kiss"
        title = "Kiss"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx):
        url = "https://api.waifu.pics/sfw/lick"
        title = "Lick"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def pat(self, ctx):
        url = "https://api.waifu.pics/sfw/pat"
        title = "Pat"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def smug(self, ctx):
        url = "https://api.waifu.pics/sfw/smug"
        title = "Smug"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def bonk(self, ctx):
        url = "https://api.waifu.pics/sfw/bonk"
        title = "Bonk"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def yeet(self, ctx):
        url = "https://api.waifu.pics/sfw/yeet"
        title = "Yeet"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def blush(self, ctx):
        url = "https://api.waifu.pics/sfw/blush"
        title = "Blush"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def smile(self, ctx):
        url = "https://api.waifu.pics/sfw/smile"
        title = "Smile"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def wave(self, ctx):
        url = "https://api.waifu.pics/sfw/wave"
        title = "Wave"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def highfive(self, ctx):
        url = "https://api.waifu.pics/sfw/highfive"
        title = "Highfive"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def handhold(self, ctx):
        url = "https://api.waifu.pics/sfw/handhold"
        title = "Handhold"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def nom(self, ctx):
        url = "https://api.waifu.pics/sfw/nom"
        title = "Nom"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def bite(self, ctx):
        url = "https://api.waifu.pics/sfw/bite"
        title = "Bite"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def glomp(self, ctx):
        url = "https://api.waifu.pics/sfw/glomp"
        title = "Glomp"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx):
        url = "https://api.waifu.pics/sfw/slap"
        title = "Slap"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def kill(self, ctx):
        url = "https://api.waifu.pics/sfw/kill"
        title = "Kill"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def kicks(self, ctx):
        url = "https://api.waifu.pics/sfw/kick"
        title = "Kick"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def happy(self, ctx):
        url = "https://api.waifu.pics/sfw/happy"
        title = "Happy"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def wink(self, ctx):
        url = "https://api.waifu.pics/sfw/wink"
        title = "Wink"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def pokes(self, ctx):
        url = "https://api.waifu.pics/sfw/poke"
        title = "Poke"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def dance(self, ctx):
        url = "https://api.waifu.pics/sfw/dance"
        title = "Dance"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def cringe(self, ctx):
        url = "https://api.waifu.pics/sfw/cringe"
        title = "Cringe"
        view = base_pisc_api(ctx, url, title)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def trap(self, ctx):
        if ctx.channel.is_nsfw():
            url = "https://api.waifu.pics/nsfw/trap"
            title = "Trap"
            view = base_pisc_api(ctx, url, title)
            await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def blowjob(self, ctx):
        if ctx.channel.is_nsfw():
            url = "https://api.waifu.pics/nsfw/blowjob"
            title = ""
            view = base_pisc_api(ctx, url, title)
            await view.api_start()

def setup(bot):
    bot.add_cog(api_waifu2(bot))