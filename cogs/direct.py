# Standard 
import discord , asyncio
from discord.ext import commands
from datetime import datetime, timezone

# Third party

# Local
import utils

intents = discord.Intents.all()

class DM_Message(commands.Cog):

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
        latte = self.client.get_user(834834946832203776)
        if message.author == self.client.user:
            return
            
        if isinstance(message.channel, discord.DMChannel):
            if message.content:
                if message.author.id == 240059262297047041: #stacia > pond
                    await pond.send(f"{message.clean_content}", delete_after=300)
                if message.author.id == 371230466319187969: #pond > stacia
                    await stacia.send(f"{message.clean_content}" , delete_after=300)
                if message.author.id == 834834946832203776: #latte > stacia
                    await stacia.send(f"{message.clean_content}" , delete_after=300)
            if message.attachments:
                image = message.attachments[0].proxy_url
                if message.author.id == 240059262297047041: #stacia > pond
                    await pond.send(image, delete_after=300)
                if message.author.id == 371230466319187969: #pond > stacia
                    await stacia.send(image, delete_after=300)
                if message.author.id == 834834946832203776: #latte > stacia
                    await stacia.send(image, delete_after=300)
                        
        if message.channel.id == 874942964462391357:
            if message.content:
                member = message.guild.get_member(240059262297047041)
                embed = discord.Embed(description=f"{message.clean_content}")
                embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
                await member.send(embed=embed)
                await message.delete()
            if message.attachments:
                image = message.attachments[0].proxy_url
                member = message.guild.get_member(240059262297047041)
                embed = discord.Embed(description=f"{message.clean_content}")
                embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
                embed.set_image(url=image)
                await member.send(embed=embed)
                await message.delete()

def setup(client):
    client.add_cog(DM_Message(client))