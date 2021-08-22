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
            
        await ctx.send(f"set welcome channel : {channel.mention}")
    
    @welcome.command(name="delete")
    async def delete_welcome(self ,ctx):
        self.welcome[str(ctx.guild.id)] = None

        with open("bot_config/welcome.json", "w") as welcome_: #encoding='UTF8'
            json.dump(self.welcome, welcome_, indent=4)
        
        await ctx.send(f"channel is deleted")
    
    #set_leave_channel
    @set.group(invoke_without_command=True)
    async def leave(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            await ctx.send('You havent defined text channel!')
            return
        self.leave[str(ctx.guild.id)] = channel.id
        with open("bot_config/leave.json", "w") as welcome_change: #encoding='UTF8'
            json.dump(self.leave, welcome_change, indent=4)

        await ctx.send(f"set leave channel : {channel.mention}")
    
    @leave.command(name="delete")
    async def delete_leave(self, ctx):
        self.leave[str(ctx.guild.id)] = None
        with open("bot_config/leave.json", "w") as welcome_change: #encoding='UTF8'
            json.dump(self.leave, welcome_change, indent=4)
        
        await ctx.send(f"set leave channel : {self.leave[str(ctx.guild.id)]}")

    #start_set_log_channel
    @commands.group(invoke_without_command=True)
    async def log(self, ctx):
        await ctx.send("server , message , voice , role")

    #server_log      
    @log.group(invoke_without_command=True)
    async def server(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["server-log"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f'set server-log log channel : {data["server-log"]}')
        except:
            print("error")

    @server.command(name="delete")
    async def delete_server(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["server-log"] = None
        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f"server-log channel is deleted")
        except:
            print("error")

    #message_log
    @log.group(invoke_without_command=True)
    async def message(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["message-log"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f'set message-log log channel : {data["message-log"]}')
        except:
            print("error")

    @message.command(name="delete")
    async def delete_message(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["message-log"] = None

        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f"message-log channel is deleted")
        except:
            print("error")
    
    #voice_log
    @log.group(invoke_without_command=True)
    async def voice(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        data = utils.json_loader.read_json("latte")
        data["voice-log"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f'set voice log channel : {data["voice-log"]}')
        except:
            print("error")

    @voice.command(name="delete")
    async def delete_voice(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["voice-log"] = None

        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f"voice channel is deleted")
        except:
            print("error")
    
    #role_log
    @log.group(invoke_without_command=True)
    async def role(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["role-log"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f'set role log channel : {data["role-log"]}')
        except:
            print("error")

    @role.command(name="delete")
    async def delete_role(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["role-log"] = None
        
        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f"role channel is deleted")
        except:
            print("error")

    #start_only
    @commands.group(invoke_without_command=True)
    async def only(self, ctx):
        await ctx.send("server , message , voice , role")

    #only_image     
    @only.group(invoke_without_command=True)
    async def image(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            channel = ctx.channel
        
        data = utils.json_loader.read_json("latte")

        data["only-image"] = channel.id
        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f'set server-log log channel : {data["only-image"]}')
        except:
            print("error")

    @image.command(name="delete")
    async def delete_image(self ,ctx):
        data = utils.json_loader.read_json("latte")
        data["only-image"] = None
        try:
            utils.json_loader.write_json(data, "latte")
            await ctx.send(f"server-log channel is deleted")
        except:
            print("error")
    
    #log_channel_ignor
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
            await ctx.send(f'set log_channel log channel : {data["log-channel"]}')
        except:
            print("error")

    #view_config
    @commands.command(aliases=["lconfig"])
    @utils.owner_bot()
    async def latte_config(self, ctx, *, json_config = None):
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