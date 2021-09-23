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
        if ctx.channel.is_nsfw():
            view = nsfw_waifu(ctx)
            await view.api_start()
        else:
            view = sfw_waifu(ctx)
            await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def neko(self, ctx):
        if ctx.channel.is_nsfw():
            view = nsfw_neko(ctx)
            await view.api_start()
        else:
            view = sfw_neko(ctx)
            await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def shinobu(self, ctx):
        view = sfw_shinobu(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def megumin(self, ctx):
        view = sfw_megumin(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def bully(self, ctx):
        view = sfw_bully(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def cuddle(self, ctx):
        view = sfw_cuddle(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def cry(self, ctx):
        view = sfw_cry(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx):
        view = sfw_hug(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def awoo(self, ctx):
        view = sfw_awoo(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def kiss(self, ctx):
        view = sfw_kiss(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def lick(self, ctx):
        view = sfw_lick(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def pat(self, ctx):
        view = sfw_pat(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def hug(self, ctx):
        view = sfw_hug(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def smug(self, ctx):
        view = sfw_smug(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def bonk(self, ctx):
        view = sfw_bonk(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def yeet(self, ctx):
        view = sfw_yeet(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def blush(self, ctx):
        view = sfw_blush(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def smile(self, ctx):
        view = sfw_smile(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def wave(self, ctx):
        view = sfw_wave(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def highfive(self, ctx):
        view = sfw_highfive(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def handhold(self, ctx):
        view = sfw_handhold(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def nom(self, ctx):
        view = sfw_nom(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def bite(self, ctx):
        view = sfw_bite(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def glomp(self, ctx):
        view = sfw_glomp(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def slap(self, ctx):
        view = sfw_slap(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def kill(self, ctx):
        view = sfw_kill(ctx)
        await view.api_start()
    
    @commands.command()
    @commands.guild_only()
    async def kicks(self, ctx):
        view = sfw_kick(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def happy(self, ctx):
        view = sfw_happy(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def wink(self, ctx):
        view = sfw_wink(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def pokes(self, ctx):
        view = sfw_poke(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def dance(self, ctx):
        view = sfw_dance(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def cringe(self, ctx):
        view = sfw_cringe(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def trap(self, ctx):
        view = nsfw_trap(ctx)
        await view.api_start()

    @commands.command()
    @commands.guild_only()
    async def blowjob(self, ctx):
        view = nsfw_blowjob(ctx)
        await view.api_start()

def setup(bot):
    bot.add_cog(api_waifu2(bot))