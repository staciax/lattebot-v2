# Standard 
import discord , platform , os , asyncio , re , platform 
from discord.ext import commands
from datetime import datetime, timedelta, timezone
import time
from time import perf_counter

# Third party
import psutil
import pymongo 
import json
from pymongo import MongoClient

# Local
import utils
from config import *

#open_json
with open('bot_config/secrets.json') as f:
    data = json.load(f)

#mongodb
mango_url = data["mongo"]
cluster = MongoClient(mango_url)
check_ping = cluster[MGDATABASE][LATTEDOCUMENT]

intents = discord.Intents.all()

class Data(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.launch_time = datetime.utcnow()
    
    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=Context)

        if ctx.command is not None and ctx.guild is not None:            
            if not self.ready:
                await ctx.send("I'm not ready to receive commands. Please wait a few seconds.")
            
            else:
                await self.invoke(ctx)

    @commands.Cog.listener()
    async def on_ready(self):
        self.log_channel = self.client.get_channel(REPORTBUG)
        self.request_message = self.client.get_channel(REQUEST_ME)
        self.bug_channel = self.client.get_channel(865609918945820692)
        print(f"-{self.__class__.__name__}")
    
    @commands.command(aliases=["botinfo", "about"])
    async def latte_info_(self, ctx):
        stacia = self.client.get_user(385049730222129152) or await self.client.fetch_user(385049730222129152)
        embed = discord.Embed(
            title=f"{self.client.user.name} Info about ",
            color=0xffffff
        )
        
        fields = [
            ("Prefix" , "``lt ``" , True),
            ("Language" , "`Python`" , True),
            ("Library" , f"`Discord.py {discord.__version__}`" , True),
            ("DataBase" , "`MongoDB`" , True),
            ("Platform", f"`{platform.system()} {platform.release()}`", True),
            ("Developer" , f"`{str(self.client.get_user(self.client.owner_id))}`" , True),
            ("Open Source", "`Yes. but not now.`", True),
            ("Bot created", f"{utils.format_relative(self.client.user.created_at)}", True)

        ]

        for name , value , inline in fields:
            embed.add_field(name=name , value=value , inline=inline)

        embed.set_thumbnail(url=self.client.user.avatar.url)
        
        await ctx.send(embed=embed, mention_author=False)

    @commands.command()
    @utils.owner_bot()
    async def status(self, ctx, statusType: str, *, statusText):

        if statusType.lower() == "playing":  # Setting `Playing ` status
            await self.client.change_presence(activity=discord.Game(name=statusText))
        if statusType.lower() == "streaming": # Setting `Streaming ` status
            await self.client.change_presence(activity=discord.Streaming(name=statusText, url=""))
        if statusType.lower() == "listening": # Setting `Listening ` statu
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=statusText))
        if statusType.lower() == "watching": # Setting `Watching ` status
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=statusText))

        embed = discord.Embed(description=f"{utils.emoji_converter('check')} **Status Changed!**\n\n`{statusText}`",color=0xffffff)
        await ctx.send(embed=embed)

    @commands.command(description="invite bot")
    async def invite(self, ctx):
        embed = discord.Embed(title=f"**invite bot**",description=f"**✧ LATTE Bot**\n♡ ꒷ now is online **{len(self.client.guilds)}** servers︰𓂃 ꒱\n\n⸝⸝﹒{INVITELINK} ꒱",color=0xFFFFFF,timestamp=datetime.now(timezone.utc))
        embed.set_thumbnail(url=self.client.user.avatar.url)    
        await ctx.send(embed=embed)
    
    @commands.command(description="check latency bot")
    @commands.guild_only()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)

        typings = time.monotonic()
        await ctx.trigger_typing()
        typinge = time.monotonic()
        typingms = round((typinge - typings) * 1000)

        dbstart = time.monotonic()
        check_ping
        dbend = time.monotonic()
       
        embed = discord.Embed(description="",color=0xc4cfcf)
        embed.add_field(name=f"{utils.emoji_converter('latteicon')} Latency", value=f"```nim\n{bot_latency} ms```", inline=True)
        embed.add_field(name=f"{utils.emoji_converter('typing')} Typing", value=f"```nim\n{typingms} ms```", inline=True)
        embed.add_field(name=f"{utils.emoji_converter('mongodb')} Database", value=f"```nim\n{(dbend-dbstart)*1000:,.2f} ms```", inline=True)
        await ctx.send(embed=embed)
    
    @commands.command(name="stats")
    @utils.owner_bot()
    async def stats(self, ctx):

        # bot / version data
        BotVersion = BOTVERSION
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.client.guilds)
        memberCount = len(set(self.client.get_all_members()))
        totalcogs = len(self.client.cogs)
        totalcommands = len(self.client.commands)

        # time
        delta_uptime = datetime.utcnow() - self.client.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        data_time = utils.data_time(seconds, minutes, hours, days)
        
        # psutil server data
        process = psutil.Process()
        CPU_Usage = round(psutil.cpu_percent(), 1)
        Aviable_CPU = round(100 - CPU_Usage, 1) 
        CPU_Cores = psutil.cpu_count(logical=False)
        CPU_Thread = psutil.cpu_count()
        used_MemoryGB = round(round(psutil.virtual_memory().used) / 102400000) / 10
        used_MemoryPC = round(psutil.virtual_memory().percent, 1)
        total_Ram = round(round(psutil.virtual_memory().total) / 102400000) / 10
        free_Memory = round(total_Ram - used_MemoryGB, 1)

        # psutil bot data
        bot_ramUsage = f"{process.memory_info().rss / 1048576:.01f}"
        bot_ramUsagePC = f"{process.memory_percent():.01f}"

        embed = discord.Embed(description='\uFEFF', colour=0xffffff) #title=f'{self.client.user.name} Stats',
        
        fields = [("Bot version:",f"```{BotVersion}```", True),
                    ("Python version:",f"```{pythonVersion}```", True),
                    ("Discord.py version:",f"```{dpyVersion}```", True),
                    ("Total servers:",f"```{serverCount}```", True),
                    ("Total users:",f"```{memberCount}```", True),
                    ("Uptime:",f"```{data_time}s```", True),
                    ("Total Cogs:",f"```{totalcogs}```", True),
					("Total Commands:",f"```{totalcommands}```", True),
                    ("Bot developers:","```ꜱᴛᴀᴄɪᴀ.#0001 (385049730222129152)```\n\n", False),
                    ("CPU usage:",f"```{CPU_Usage} %```", True),
                    ("CPU Cores / Threads:",f"```{CPU_Cores}/{CPU_Thread}```", True),
                    ("Total RAM:",f"```{total_Ram} GB```", True),
                    ("RAM Usage:",f"```{used_MemoryGB} GB ({used_MemoryPC} %)```", True),
                    ("Bot RAM usage:",f"```{bot_ramUsage} MB ({bot_ramUsagePC} %)```", True),
                ]
            
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        
        lastup = datetime(UYEAR, UMONTH, UDATE)
        dt = lastup.strftime("%d %B %Y") #%A,
        embed.set_footer(text=f"Recently Updated • {dt}")
        embed.set_author(name=f"{self.client.user.name} Stats", icon_url=self.client.user.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['botdis'])
    @commands.is_owner()
    async def logout(self, ctx): #ทำเหมือน giveaway version x
        embed = discord.Embed(color=0xffffff)
        embed.set_author(name=f"{self.client.user.name} Logout",icon_url=self.client.user.avatar.url)
        embed.description = f"are you sure? {utils.emoji_converter('what')}"

        m = await ctx.send("Are these all valid?", embed=embed , delete_after=60)
        await m.add_reaction("✅")
        await m.add_reaction("🇽")

        try:
            reaction, member = await self.client.wait_for(
                "reaction_add",
                timeout=60,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )
        except asyncio.TimeoutError:
            await ctx.send("Confirmation Failure. Please try again.")
            return
        
        if str(reaction.emoji) not in ["✅", "🇽"] or str(reaction.emoji) == "🇽":
            await ctx.message.delete()
            await ctx.send("logout cancelling", delete_after=10)
            await m.delete()
            return
        
        await m.delete()
        embed_lg = discord.Embed(color=0xffffff)
        embed_lg.set_footer(text=f"{self.client.user.name} is disconnect" , icon_url=self.client.user.avatar.url)

        await ctx.message.delete()
        await ctx.send(embed=embed_lg, delete_after=10)
        await self.client.logout()
    
    @commands.command()
    @commands.guild_only()
    async def echo(self, ctx, *, message=None):
        embed = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify what message bot send the message | `prefix` `bm [message]`",color=0xffffff)
        if message == None:
            message = await ctx.send(embed=embed)
        else:
            await ctx.send(f'{message}')
            await ctx.message.delete()
    
    @commands.command(aliases=['report','bug'])
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
    
    @commands.command(aliases=['req','Requests'])
    @utils.is_latte_guild()
    async def request(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("write what you want to requests?")
        try:
            msg1 = await self.client.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.send("You took to long, please try again.")

        embedq = discord.Embed(title="Request",
                                 description=f"{msg1.content}",
                                 color=0xffffff)

        embedf = discord.Embed(description="Thanks for your request!")

        await self.request_message.send(embed=embedq)
        await ctx.send(embed=embedf)
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(view_audit_log=True)
    async def audit(self,ctx, num: int=None):
        embed=discord.Embed(title='Audit Logs',description="", color=0xffffff)
        embed.set_footer(text=f"Requested by {ctx.author}")
        async for entry in ctx.guild.audit_logs(limit=num):
            embed.description += f'**User:** `{entry.user}` **Action:** `{entry.action}`  **Target:** `{entry.target}`  **Category:** `{entry.category}` **Time:** `{entry.created_at.strftime("%a, %#d %B %Y, %I:%M %p")}\n\n`'
        await ctx.reply(embed=embed, mention_author=False)
    
    @commands.command(aliases=['temp','tempinvite'])
    @commands.guild_only()
    async def temp_invite(self, ctx):
        if not ctx.guild.id == MYGUILD:
            return
        await ctx.message.delete()
        await ctx.channel.send('https://discord.gg/f6adY5B8k2' , delete_after=15)

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

def setup(client):
    client.add_cog(Data(client))