# Standard 
import discord, random, os , platform
from discord.ext import commands
from time import time
from datetime import datetime, timedelta, timezone

# Third party
# Local

intents = discord.Intents.default()
intents.members = True

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.command()
    async def test1(self, ctx):
        embed = discord.Embed(description=f"Congratulations, {ctx.author.mention} you leveled up to **level 2.**!",color=0xffffff)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Test(client))