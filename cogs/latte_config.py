# Standard 
import discord , asyncio , re , os
from datetime import datetime, timedelta, timezone
from discord.ext import commands

# Third party
import json
import requests

# Local
import utils
import utils.json_loader
from config import *

class Latte_config(commands.Cog): 

    def __init__(self, client):
        self.bot = client
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        self.welcome = {}
        self.leave = {}
        self.log_config = self.bot.get_channel(844462710526836756)
    
    #set_welcome_channel
    @commands.group(invoke_without_command=True)
    async def set(self, ctx):
        await ctx.send(embed=utils.set_channel_embed(ctx))

    #set_welcome_channel      
    @set.group(invoke_without_command=True)
    async def welcome(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            await ctx.send(embed=utils.welcome_help(ctx))
            return

        self.welcome[str(ctx.guild.id)] = channel.id
        with open("bot_config/welcome.json", "w") as welcome_: #encoding='UTF8'
            json.dump(self.welcome, welcome_ , indent=4)

        em = discord.Embed(description=f"welcome is enable : {channel.mention}" , color=WHITE)
        await ctx.send(embed=em)
                
    @welcome.command(name="delete")
    async def delete_welcome(self ,ctx):
        self.welcome[str(ctx.guild.id)] = None

        with open("bot_config/welcome.json", "w") as welcome_: #encoding='UTF8'
            json.dump(self.welcome, welcome_, indent=4)
        
        em = discord.Embed(description="welcome is disable" , color=WHITE)
        await ctx.send(embed=em)
    
    #set_leave_channel
    @set.group(invoke_without_command=True)
    async def leave(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            await ctx.send('You havent defined text channel!')
            return
        self.leave[str(ctx.guild.id)] = channel.id
        with open("bot_config/leave.json", "w") as welcome_change: #encoding='UTF8'
            json.dump(self.leave, welcome_change, indent=4)

        em = discord.Embed(description=f"leave is enable : {channel.mention}" , color=WHITE)
        await ctx.send(embed=em)
    
    @leave.command(name="delete")
    async def delete_leave(self, ctx):
        self.leave[str(ctx.guild.id)] = None
        with open("bot_config/leave.json", "w") as welcome_change: #encoding='UTF8'
            json.dump(self.leave, welcome_change, indent=4)
        
        em = discord.Embed(description="leave is disable" , color=WHITE)
        await ctx.send(embed=em)

    #start_set_log_channel
    @commands.group(invoke_without_command=True)
    async def log(self, ctx):
        embed = discord.Embed(description="set log channel" , color=WHITE)
        await ctx.send(embed=embed)

    #server_log      
    @log.group(invoke_without_command=True)
    async def server(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["server-log"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'set server-log channel : {data["server-log"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')

    @server.command(name="delete")
    async def delete_server(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["server-log"] = None
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f"server-log channel is disable" , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')

    #message_log
    @log.group(invoke_without_command=True)
    async def message(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["message-log"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'set message-log log channel : {data["message-log"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')

    @message.command(name="delete")
    async def delete_message(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["message-log"] = None

        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'message-log channel is disable' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')
    
    #voice_log
    @log.group(invoke_without_command=True)
    async def voice(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        data = utils.json_loader.read_json("latte")
        data["voice-log"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'set voice-log channel : {data["voice-log"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')

    @voice.command(name="delete")
    async def delete_voice(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["voice-log"] = None

        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f"voice-log channel is disable" , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')
    
    #role_log
    @log.group(invoke_without_command=True)
    async def role(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["role-log"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'set role-log channel : {data["role-log"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')

    @role.command(name="delete")
    async def delete_role(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["role-log"] = None
        
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'role-log channel is disable : {data["role-log"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')

    #start_only
    @commands.group(invoke_without_command=True)
    async def only(self, ctx):
        embed = discord.Embed(description="set only channel\nimage\nlink" , color=WHITE)
        await ctx.send(embed=embed)

    #only_image     
    @only.group(invoke_without_command=True)
    async def image(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["only-image"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'set only-image channel : {data["only-image"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')

    @image.command(name="delete")
    async def delete_image(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["only-image"] = None
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f"only-image channel is disable" , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')
    
    @only.group(invoke_without_command=True)
    async def link(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["only-link"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'set only-link channel : {data["only-link"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')

    @link.command(name="delete")
    async def delete_link(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["only-link"] = None
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f"only-link channel is disable" , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')
    
    #log_channel_ignor #ยังไม่เปิดใช้งาน
    @commands.command(name="ignor-channel")
    async def log_channel(self, ctx): 
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        embedwait = discord.Embed(description=f"Edit channel log",color=0xffffff)
        embedfail = discord.Embed(description=f"You took to long, please try again.",color=0xffffff)
        await ctx.send(embed=embedwait)
        try:
            msg = await self.client.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send(embed=embedfail)

        data = utils.json_loader.read_json("latte")
        
        data["log-channel"] = [msg.clean_content]
        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f'set log_channel log channel : {data["log-channel"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            print("error")
            await ctx.send('error')
    
    @commands.command(name="snipetime")
    async def set_snipetime(self, ctx , time:int = None):
        data = utils.json_loader.read_json("latte")
        if time is None:
            time = None

        data["snipe-time"] = time

        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f' snipetime {data["snipe-time"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            await ctx.send('error')
    
    @commands.command(name="snipedtime")
    async def set_sniped(self, ctx , time = None):
        data = utils.json_loader.read_json("latte")
        if time is None:
            snipe_mode = None
        else:
            snipe_mode = int(time)

        data["sniped"] = snipe_mode

        try:
            utils.json_loader.write_json(data, "latte")
            em = discord.Embed(description=f' snipedtime {data["sniped"]}' , color=WHITE)
            await ctx.send(embed=em)
        except:
            await ctx.send('error')

    #view_config
    @commands.group(invoke_without_command=True , aliases=["lconfig", "config"])
    @utils.owner_bot()
    async def latte_config(self, ctx):
        await ctx.send("description")
    
    @latte_config.command(aliases=["file", "json"])
    @utils.owner_bot()
    async def latte_config_file(self, ctx, *, json_config = None):
        guild = self.bot.get_guild(840379510704046151)
        if json_config == "secrets":
            return
        elif json_config is None:
            i = 0
            embed = discord.Embed(description="" , color=0xffffff)
            embed.set_author(name=f"{guild.name}'s config file" , icon_url=guild.icon.url)
            for filename in os.listdir('./bot_config'):
                if filename.endswith('.json'):
                    if not filename == "secrets.json":
                        i += 1
                        embed.description += f"`{filename[:-5]}`\n"

            await ctx.send(embed=embed)
        else:
            try:
                data = utils.json_loader.read_json(str(json_config))
                embed = discord.Embed(description= f"{json_config}.json\n```json\n{json.dumps(data, indent = 1)}```" , color=0xffffff)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(description= "file not found!" , color=0xffffff)
                await ctx.send(embed=embed)

#    @commands.command(name="del-w-off")
#    async def del_welcome_(self, ctx):
#        with open('bot_config/welcome.json', 'w') as w:
#            with open('bot_config/welcome.json', 'r') as r:
#                for line in r:
#                    element = json.loads(line.strip())
#                    if f"{ctx.guild.id}" in element:
#                        del element[f"{ctx.guild.id}"]
#                    w.write(json.dumps(element))
#        
#       await ctx.send("test")
        
def setup(client):
    client.add_cog(Latte_config(client))