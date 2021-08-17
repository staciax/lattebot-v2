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
        with open("bot_config/latte.json", "r" , encoding='UTF8') as f:
            self.latte = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.command()
    async def welcome_(self, ctx , channel: discord.TextChannel=None):
        if channel is None:
            channel = ctx.channel  
        channel_name = channel.name

        self.latte["welcome"] = channel_name

        with open("bot_config/latte.json", "w" , encoding='UTF8') as welcome_change:
            json.dump(self.latte, welcome_change, indent=4)
        
        await ctx.send(f"set welcome channel : {self.latte['welcome']}")
        
    
    @commands.command()
    async def leave_(self, ctx , channel: discord.TextChannel=None):
        if channel is None:
            channel = ctx.channel
        channel_name = channel.name

        self.latte["leave"] = channel_name

        with open("bot_config/latte.json", "w" , encoding='UTF8') as welcome_change:
            json.dump(self.latte, welcome_change, indent=4)

#    @commands.command()
#    async def set_welcome(self, ctx):
#        file = open('bot_config/latte.json', 'w',encoding='UTF8')
#        data = {}
#        data["welcome"] = f"{ctx.channel.name}"
#        data
#        json.dump(data, file, ensure_ascii=False)
#        file.close()
        
def setup(client):
    client.add_cog(Latte_config(client))