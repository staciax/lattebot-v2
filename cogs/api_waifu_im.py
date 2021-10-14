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
    
    @commands.command(aliases=['sfw_all', 'all_sfw'])
    @commands.guild_only()
    async def waifuall(self, ctx):
        url = "https://api.waifu.im/sfw/all/"
        view = sfw_all_view(ctx, url)
        await view.api_start()

    @commands.command(aliases=['sfw_waifu', 'waifu_sfw'])
    @commands.guild_only()
    async def waifu2(self, ctx):
        url = "https://api.waifu.im/sfw/waifu/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()
    
    @commands.command(aliases=['sfw_maid', 'maid_sfw', 'hmaid'])
    @commands.guild_only()
    async def maid(self, ctx):
        if ctx.channel.is_nsfw():
            url = "https://api.waifu.im/nsfw/maid/"
            view = base_waifu_im_api(ctx, url)
            await view.api_start()
        else:
            url = "https://api.waifu.im/sfw/maid/"
            view = base_waifu_im_api(ctx, url)
            await view.api_start()

    @commands.command(aliases=['nsfw_ass', 'ass_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def ass(self, ctx):
        url = "https://api.waifu.im/nsfw/ass/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_ecchi', 'ecchi_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def ecchi(self, ctx):
        url = "https://api.waifu.im/nsfw/ecchi/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()       

    @commands.command(aliases=['nsfw_ero', 'ero_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def ero(self, ctx):
        url = "https://api.waifu.im/nsfw/ero/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_hentai', 'hentai_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        url = "https://api.waifu.im/nsfw/hentai/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_milf', 'milf_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def milf(self, ctx):
        url = "https://api.waifu.im/nsfw/milf/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()

    @commands.command(aliases=['nsfw_oppai', 'oppai_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def oppai(self, ctx):
        url = "https://api.waifu.im/nsfw/oppai/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()

    @commands.command(aliases=['nsfw_oral', 'oral_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def oral(self, ctx):
        url = "https://api.waifu.im/nsfw/oral/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()

    @commands.command(aliases=['nsfw_paizuri', 'paizuri_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def paizuri(self, ctx):
        url = "https://api.waifu.im/nsfw/paizuri/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_selfies', 'selfies_nsfw', 'selfie', 'nsfw_selfie', 'selfie_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def selfies(self, ctx):
        url = "https://api.waifu.im/nsfw/selfies/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()
        
    @commands.command(aliases=['nsfw_uniform', 'uniform_nsfw'])
    @commands.guild_only()
    @commands.is_nsfw()
    async def uniform(self, ctx):
        url = "https://api.waifu.im/nsfw/uniform/"
        view = base_waifu_im_api(ctx, url)
        await view.api_start()

def setup(bot):
    bot.add_cog(api_waifu_im(bot))