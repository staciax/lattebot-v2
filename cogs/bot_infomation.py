# Standard 
import discord , asyncio , re , os, platform 
from datetime import datetime, timedelta, timezone
from discord.ext import commands

# Third party
import json
import requests

# Local
import utils
import utils.json_loader
from config import *

class Bot_infomations(commands.Cog): 

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command(aliases=["botinfo", "about"])
    async def latte_info_(self, ctx):
        stacia = self.client.get_user(385049730222129152) or await self.client.fetch_user(385049730222129152)
        embed = discord.Embed(
            title=f"Info about {self.client.user.name}",
            color=0xffffff
        )
        
        fields = [
            ("Prefix" , " ``l `` | ``lt ``" , False),
            ("Language" , "Python" , False),
            ("Library" , f"Discord.py {discord.__version__}" , False),
            ("DataBase" , "MongoDB" , False),
            ("Developer" , f"{str(self.client.get_user(self.client.owner_id))}" , False),
            ("Open Source", "Yes... but not now...", False),
            ("Bot created", f"{utils.format_relative(self.client.user.created_at)}", False),
            ("Platform", f"{platform.system()} {platform.release()}", False)

        ]

        for name , value , inline in fields:
            embed.add_field(name=name , value=value , inline=inline)

        embed.set_thumbnail(url=self.client.user.avatar.url)
        
        await ctx.send(embed=embed, mention_author=False)
    
    @commands.command(aliases=["owner" , "dev"])
    async def stacia(self, ctx):
        embed = discord.Embed(
            title="STACIA PROFILE",
            color=0xffffff
        )

        fields = [
            ("Facebook" , "[**Art Nathanan**](https://www.facebook.com/nathanan.xx/)" , False),
            ("Github" , "[**STACIA**](https://github.com/staciax)" , False),
            ("My girlfriend ", "[**^*&@^&**](https://c.tenor.com/BBtu3YU-z80AAAAC/kawaii-anime.gif) ", False)
        ]

        for name , value , inline in fields:
            embed.add_field(name=name , value=value , inline=inline)

        user = self.client.get_user(385049730222129152) or await self.client.fetch_user(385049730222129152)
        embed.set_thumbnail(url=user.avatar.url)
        
        await ctx.send(embed=embed)


    
def setup(client):
    client.add_cog(Bot_infomations(client))