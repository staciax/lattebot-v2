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
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        self.welcome = {}
        self.leave = {}

    #set_welcome_channel
    @commands.group(invoke_without_command=True)
    async def set(self, ctx):
        await ctx.send(embed=utils.set_channel_embed(ctx))
            
    @set.group(invoke_without_command=True)
    async def welcome(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            await ctx.send(embed=utils.welcome_help(ctx))
            return

        self.welcome[ctx.guild.id] = channel.id
        with open("bot_config/set_welcome.json", "w") as welcome_: #encoding='UTF8'
            json.dump(self.welcome, welcome_ , indent=4)
            
        await ctx.send(f"set welcome channel : {channel.mention}")
    
    @welcome.command(name="delete")
    async def delete_(self ,ctx):
        self.welcome[ctx.guild.id] = None

        with open("bot_config/set_welcome.json", "w") as welcome_: #encoding='UTF8'
            json.dump(self.welcome, welcome_, indent=4)
        
        await ctx.send(f"channel is deleted")
    
    #set_leave_channel
    @set.group(invoke_without_command=True)
    async def leave(self, ctx , channel: discord.TextChannel=None): 
        if channel is None:
            await ctx.send('You havent defined text channel!')
            return
        self.leave[ctx.guild.id] = channel.id
        with open("bot_config/set_leave.json", "w") as welcome_change: #encoding='UTF8'
            json.dump(self.leave, welcome_change, indent=4)

        await ctx.send(f"set leave channel : {channel.mention}")
    
    @leave.command(name="delete")
    async def delete__(self, ctx):
        self.leave[ctx.guild.id] = None
        with open("bot_config/set_leave.json", "w") as welcome_change: #encoding='UTF8'
            json.dump(self.leave, welcome_change, indent=4)
        
        await ctx.send(f"set leave channel : {self.leave[ctx.guild.id]}")
    
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

#    @commands.command()
#    async def test_wel(self, ctx):
#        data = utils.json_loader.read_json("welcome")
#        channel = data[f"{ctx.guild.id}"]
#
#        await ctx.send(channel)
        
def setup(client):
    client.add_cog(Latte_config(client))