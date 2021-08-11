# Standard 
import discord
from discord.ext import commands
from datetime import datetime, timezone
import asyncio

# Third party
# Local
import utils
from utils import create_voice_channel , get_channel_by_name , get_category_by_name

intents = discord.Intents()
intents.all()

my_discord = [240059262297047041 , 385049730222129152]

class Dm(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.direct = self.client.get_channel(874942964462391357)
        print(f"-{self.__class__.__name__}")

    @commands.Cog.listener()
    async def on_message(self, message):
        stacia = self.client.get_user(240059262297047041)
        pond = self.client.get_user(371230466319187969)
        if message.author == self.client.user:
            return
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id == 240059262297047041: #stacia > pond
                await pond.send(f"{message.clean_content}", delete_after=15)
                await asyncio.sleep(5)
                await message.delete()
            if message.author.id == 371230466319187969: #pond > stacia
                await stacia.send(f"{message.clean_content}" , delete_after=15)
                await asyncio.sleep(5)
                await message.delete()
                        
        if message.channel.id == 874942964462391357:
            if message.content:
                member = message.guild.get_member(240059262297047041)
                embed = discord.Embed(description=f"{message.clean_content}")
                embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
                await member.send(embed=embed)
                await message.delete()

def setup(client):
    client.add_cog(Dm(client))