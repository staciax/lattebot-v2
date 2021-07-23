# Standard 
import discord
import platform
import os
import asyncio
from discord.ext import commands
from datetime import datetime, timedelta, timezone
from time import time

# Third party
# Local
import utils
from config import *

intents = discord.Intents.default()
intents.members = True

class Data(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.launch_time = datetime.utcnow()
    
#    async def process_commands(self, message):
#        ctx = await self.get_context(message, cls=Context)

#        if ctx.command is not None and ctx.guild is not None:            
#            if not self.ready:
#                await ctx.send("I'm not ready to receive commands. Please wait a few seconds.")
            
#            else:
#                await self.invoke(ctx)

    @commands.Cog.listener()
    async def on_ready(self):
        self.log_channel = self.client.get_channel(REPORTBUG)
        self.bug_channel = self.client.get_channel(865609918945820692)
        print(f"-{self.__class__.__name__}")


    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, statusType: str, *, statusText):

        if statusType.lower() == "playing":  # Setting `Playing ` status
            await self.client.change_presence(activity=discord.Game(name=statusText))

        if statusType.lower() == "streaming": # Setting `Streaming ` status
            await self.client.change_presence(activity=discord.Streaming(name=statusText, url=""))

        if statusType.lower() == "listening": # Setting `Listening ` status
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=statusText))

        if statusType.lower() == "watching": # Setting `Watching ` status
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=statusText))

        embed = discord.Embed(description=f"{utils.emoji_converter('check')} **Status Changed!**\n\n`{statusText}`",color=0xffffff)
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title=f"**invite bot**",description=f"**✧ LATTE Bot**\n♡ ꒷ now is online **{len(self.client.guilds)}** servers︰𓂃 ꒱\n\n⸝⸝﹒[`click to invite bot`](https://discord.com/api/oauth2/authorize?client_id=861179952576856065&permissions=8&scope=bot%20applications.commands) ꒱",color=0xFFFFFF,timestamp=datetime.now(timezone.utc))
        embed.set_thumbnail(url=self.client.user.avatar.url)
#       embed.set_image(url='https://i.imgur.com/rzGqQwn.png')
#         embed.set_footer(text = f'Req by {ctx.author}', icon_url = ctx.author.avatar.url)
        
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
        totalcogs = len(self.client.cogs)
        totalcommands = len(self.client.commands)
        
        delta_uptime = datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if days == 0:
            days = ""
        else:
            days = f"{days}d "

        if hours == 0:
            hours = ""
        else:
            hours = f"{hours}h "
               
        if minutes == 0:
            minutes = ""
        else:
            minutes = f"{minutes}m "

        embed = discord.Embed(description='\uFEFF', colour=0xffffff, timestamp=datetime.now(timezone.utc)) #title=f'{self.client.user.name} Stats',
        
        fields = [("Bot version:",f"```{BotVersion}```", True),
                    ("Python version:",f"```{pythonVersion}```", True),
                    ("Discord.py version:",f"```{dpyVersion}```", True),
                    ("Total servers:",f"```{serverCount}```", True),
                    ("Total users:",f"```{memberCount}```", True),
                    ("Uptime:",f"```{days}{hours}{minutes}{seconds}s```", True),
                    ("Total Cogs:",f"```{totalcogs}```", True),
					("Total Commands:",f"```{totalcommands}```", True),
                    ("Bot developers:","```ꜱᴛᴀᴄɪᴀ.#0001 (385049730222129152)```", False)]
            
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_footer(text=f"Req by {ctx.author}" , icon_url = ctx.author.avatar.url) # (text=f"Req by {ctx.author} | {self.client.user.name}"
        embed.set_author(name=f"{self.client.user.name} Stats", icon_url=self.client.user.avatar.url)
#        embed.set_image(url=ctx.guild.banner.url)
#        embed.set_thumbnail(url=self.client.user.avatar.url)
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
    
    @commands.command(name="bm")
    async def bm(self, ctx, *, message=None):
        embed = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify what message bot send the message | `prefix` `bm [message]`",color=0xffffff)
        if message == None:
            message = await ctx.send(embed=embed)
        else:
            await ctx.send(f'{message}')
            await ctx.message.delete()
    
    @commands.command(aliases=['report','bug','fb'])
    async def feedback(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        embedwait = discord.Embed(title="FEED BACK",description=f"Please write a feedback.\n\n`note: within 1 minute`",color=0xffffff)
        embedfail = discord.Embed(title="FEED BACK",description=f"{utils.emoji_converter('xmark')} You took to long, please try again.",color=0xffffff)
        await ctx.send(embed=embedwait)
        try:
            msg1 = await self.client.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send(embed=embedfail)

        reportembed = discord.Embed(title="FEED BACK",
                                 description=f"{msg1.content}",
                                 color=0xffffff)
        reportembed.set_thumbnail(url=ctx.author.avatar.url)

        embedsc = discord.Embed(title="FEED BACK",description=f"{ctx.author.mention} Thank you for feedback {utils.emoji_converter('whiteheart')} !",color=0xffffff)

        await self.log_channel.send(embed=reportembed)
        await ctx.send(embed=embedsc)

# dm message to my text channel   
#    @commands.Cog.listener()
#    async def on_message(self, message):
#        if not message.author.bot:
#            if isinstance(message.channel, discord.DMChannel):
#                if len(message.content) < 20:
#                    await message.channel.send("<a:b_hitopotatowhat:864921118296506418>")
#
#               else:
#                    embed = discord.Embed(title="DM Report",
#                                            color=0xffffff,
#                                            timestamp=datetime.now(timezone.utc)
#                    )
#                    embed.set_thumbnail(url=message.author.avatar.url)
#
#                    fields = [("Member", message.author.display_name, False),
#                                ("Message",message.content, False)
#                    
#                    ]
#                    for name, value, inline in fields:
#                        embed.add_field(name=name, value=value , inline=inline)
#
#                    await self.bug_channel.send(embed=embed)
#                    await message.channel.send("message relayed to bot developer")            
#            else:
#                await self.process_commands(message)

# error commands

    @logout.error
    async def logout_error(self, ctx, error):
        embed = discord.Embed(description=f"{utils.emoji_converter('xmark')} You do not own this bot.",color=0xffffff)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @status.error
    async def status_error(self, ctx, error):
        embedra = discord.Embed(description=f"{utils.emoji_converter('xmark')} `prefix status` `[statustype]` `[statustext]`\n\n `Status Type` : `playing` | `Streaming` | `Listening` | `Watching`",color=0xffffff)
        embedow = discord.Embed(description=f"{utils.emoji_converter('xmark')}You do not own this bot.",color=0xffffff)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embedra)
        else:
            await ctx.send(embed=embedow)
            await ctx.message.delete()


def setup(client):
    client.add_cog(Data(client))