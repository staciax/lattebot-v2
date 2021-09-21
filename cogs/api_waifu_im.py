import discord
import datetime
import aiohttp
from discord.ext import commands, menus

class api_waifu_im(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['sfw_waifu', 'waifu_sfw'])
    async def waifu2(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/sfw/waifu/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Waifu", url=json['url'], color=dominant_color) #timestamp=discord.utils.utcnow(),
        embed.set_image(url=json['url'])
#        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command(aliases=['sfw_maid', 'maid_sfw'])
    async def maid(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/sfw/maid/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Maid", url=json['url'], color=dominant_color) #timestamp=discord.utils.utcnow(),
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['nsfw_ass', 'ass_nsfw'])
    @commands.is_nsfw()
    async def ass(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/ass/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Ass", url=json['url'], color=dominant_color) #timestamp=discord.utils.utcnow(),
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)
        
    @commands.command(aliases=['nsfw_ecchi', 'ecchi_nsfw'])
    @commands.is_nsfw()
    async def ecchi(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/ecchi/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Ecchi", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)
        
    @commands.command(aliases=['nsfw_ero', 'ero_nsfw'])
    @commands.is_nsfw()
    async def ero(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/ero/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Ero", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)
        
    @commands.command(aliases=['nsfw_hentai', 'hentai_nsfw'])
    @commands.is_nsfw()
    async def hentai(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/hentai/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Hentai", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)
        
    @commands.command(aliases=['maidh', 'nsfw_maid', 'maid_nsfw'])
    @commands.is_nsfw()
    async def hmaid(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/maid/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Maid", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['nsfw_milf', 'milf_nsfw'])
    @commands.is_nsfw()
    async def milf(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/milf/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Milf", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['nsfw_oppai', 'oppai_nsfw'])
    @commands.is_nsfw()
    async def oppai(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/oppai/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Oppai", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['nsfw_oral', 'oral_nsfw'])
    @commands.is_nsfw()
    async def oral(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/oral/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Oral", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['nsfw_paizuri', 'paizuri_nsfw'])
    @commands.is_nsfw()
    async def paizuri(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/paizuri/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Paizuri", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)
        
    @commands.command(aliases=['nsfw_selfies', 'selfies_nsfw', 'selfie', 'nsfw_selfie', 'selfie_nsfw'])
    @commands.is_nsfw()
    async def selfies(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/selfies/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Selfie", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])
 #       embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed, mention_author=False)
        
    @commands.command(aliases=['nsfw_uniform', 'uniform_nsfw'])
    @commands.is_nsfw()
    async def uniform(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://api.waifu.im/nsfw/uniform/')
            json = await request.json()
            
        dominant_color1 = str(json['dominant_color']).replace('#', '')
        dominant_color = int(dominant_color1, 16)

        embed = discord.Embed(title="Uniform", url=json['url'], color=dominant_color)
        embed.set_image(url=json['url'])

        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(api_waifu_im(bot))