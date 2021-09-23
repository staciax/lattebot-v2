# Standard 
import discord
import datetime
import aiohttp
from discord.ext import commands, menus

# Third party
import aiohttp

# Local
from utils.waifu_im_api import *

class api_waifu_im(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    #embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

    @commands.command(aliases=['sfw_all', 'all_sfw'])
    @commands.guild_only()
    async def all_waifu(self, ctx):
        view = sfw_all_view(ctx)
        await view.api_start()

    @commands.command(aliases=['sfw_waifu', 'waifu_sfw'])
    @commands.guild_only()
    async def waifu2(self, ctx):
        view = sfw_waifu_view(ctx)
        await view.api_start()
    
    @commands.command(aliases=['sfw_maid', 'maid_sfw'])
    @commands.guild_only()
    async def maid(self, ctx):
        view = sfw_maid_view(ctx)
        await view.api_start()

    @commands.command(aliases=['nsfw_ass', 'ass_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def ass(self, ctx):
        view = nsfw_ass_view(ctx)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_ecchi', 'ecchi_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def ecchi(self, ctx):
        view = nsfw_ecchi_view(ctx)
        await view.api_start()        

    @commands.command(aliases=['nsfw_ero', 'ero_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def ero(self, ctx):
        view = nsfw_ero_view(ctx)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_hentai', 'hentai_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        view = nsfw_hentai_view(ctx)
        await view.api_start()
        
    @commands.command(aliases=['maidh', 'nsfw_maid', 'maid_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def hmaid(self, ctx):
        view = nsfw_maid_view(ctx)
        await view.api_start()

    @commands.command(aliases=['nsfw_milf', 'milf_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def milf(self, ctx):
        view = nsfw_milf_view(ctx)
        await view.api_start()

    @commands.command(aliases=['nsfw_oppai', 'oppai_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def oppai(self, ctx):
        view = nsfw_oppai_view(ctx)
        await view.api_start()

    @commands.command(aliases=['nsfw_oral', 'oral_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def oral(self, ctx):
        view = nsfw_oral_view(ctx)
        await view.api_start()

    @commands.command(aliases=['nsfw_paizuri', 'paizuri_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def paizuri(self, ctx):
        view = nsfw_paizuri_view(ctx)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_selfies', 'selfies_nsfw', 'selfie', 'nsfw_selfie', 'selfie_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def selfies(self, ctx):
        view = nsfw_selfies_view(ctx)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_uniform', 'uniform_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def uniform(self, ctx):
        view = nsfw_uniform_view(ctx)
        await view.api_start()

def setup(bot):
    bot.add_cog(api_waifu_im(bot))