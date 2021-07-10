import discord
import platform
from config import *
from discord.ext import commands
from time import time
from datetime import datetime, timedelta, timezone

intents = discord.Intents.default()
intents.members = True

class Latte(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def status(self, ctx, statusType: str, *, statusText):

    # Setting `Playing ` status
        if statusType.lower() == "playing":
            await self.client.change_presence(activity=discord.Game(name=statusText))

    # Setting `Streaming ` status
        if statusType.lower() == "streaming":
            await self.client.change_presence(activity=discord.Streaming(name=statusText, url=""))

    # Setting `Listening ` status
        if statusType.lower() == "listening":
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=statusText))

    # Setting `Watching ` status
        if statusType.lower() == "watching":
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=statusText))

        await ctx.send("**✅ Status Changed!**")

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title=f"**invite bot**",description=f"**✧ LATTE Bot**\n♡ ꒷ now is online **{len(self.client.guilds)}** servers︰𓂃 ꒱\n\n⸝⸝﹒[`click to invite bot`](https://discord.com/api/oauth2/authorize?client_id=854134402954821643&permissions=8&scope=bot%20applications.commands) ꒱",color=0xFFFFFF,timestamp=datetime.now(timezone.utc))
        embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_image(url=ctx.guild.banner.url)
        embed.set_footer(text = f'Req by {ctx.author}', icon_url = ctx.author.avatar.url)
        
        await ctx.send(embed=embed)
    
    @commands.command(description="check latency bot")
    async def ping(self, ctx):
        start = time()
        embed = discord.Embed(description=(f'` latency: {round(self.client.latency * 1000)} ms`'),color=0xc4cfcf)
        message = await ctx.send(embed = embed)
        end = time()
        embedres = discord.Embed(description=(f'` latency: {round(self.client.latency * 1000)} ms | Response time: {(end-start)*1000:,.0f} ms.`'),color=0xc4cfcf)

        await message.edit(embed=embedres)

    @commands.command(name="stats")
    async def stats(self, ctx):

        BotVersion = BOTVERSION
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.client.guilds)
        memberCount = len(set(self.client.get_all_members()))

        embed = discord.Embed(description='\uFEFF', colour=0xffffff, timestamp=datetime.now(timezone.utc)) #title=f'{self.client.user.name} Stats',

        embed.add_field(name='Bot version:', value=BotVersion)
        embed.add_field(name='Python version:', value=pythonVersion)
        embed.add_field(name='Discord.py version:', value=dpyVersion)
        embed.add_field(name='Total servers:', value=serverCount)
        embed.add_field(name='Total users:', value=memberCount)
        embed.add_field(name='Bot developers:', value="<@385049730222129152>")

        embed.set_footer(text=f"Req by {ctx.author}" , icon_url = ctx.author.avatar.url) # (text=f"Req by {ctx.author} | {self.client.user.name}"
        embed.set_author(name=f"{self.client.user.name} Stats", icon_url=self.client.user.avatar.url)
#        embed.set_thumbnail(url=self.client.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['botdis', 'lattelg'])
    @commands.is_owner()
    async def logout(self, ctx):
        embed = discord.Embed(description="`Latte bot is disconnect`",color=0xffffff,timestamp=datetime.now(timezone.utc))
        embed.set_footer(text=f"Logout by {ctx.author}" , icon_url = ctx.author.avatar_url)
        embed.set_author(name=f"{self.client.user.name} Logout", icon_url=self.client.user.avatar.url)
        embed.set_thumbnail(url=self.client.user.avatar.url)

        await ctx.send(embed=embed) 
        await self.client.logout()
    
    @commands.command(name='bs')
    async def givebotsent(self, ctx, *, message=None):

        message = message or "Please specify what message the bot send."
        await ctx.message.delete()
        await ctx.send(message)

    @logout.error
    async def logout_error(self, ctx, error):
        await ctx.send("You do not own this bot.")
        await ctx.message.delete()
    
    @givebotsent.error
    async def givebotsent_error(self, ctx, error):
        await ctx.send('pls try again! | `bs` `msg` ')
        await ctx.message.delete()

def setup(client):
    client.add_cog(Latte(client))