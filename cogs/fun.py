# Standard 
import discord , datetime , time
from discord.ext import commands
from datetime import datetime, timezone

# Third party
# Local
from config import *
from utils import text_to_owo , notify_user

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="Any message to owo")
    @commands.is_owner()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))
    
    @commands.command()
    @commands.is_owner()
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")

def setup(client):
    client.add_cog(Fun(client))