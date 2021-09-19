# Standard 
import discord , asyncio
from discord.ext import commands
from datetime import datetime, timezone

# Third party

# Local
import utils
from config import *

intents = discord.Intents.all()

class DM_Message(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.direct = self.bot.get_channel(DM_CHANNEL)
        print(f"-{self.__class__.__name__}")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        #DM_to_DM
        stacia = self.bot.get_user(240059262297047041)
        pond = self.bot.get_user(371230466319187969)
        latte = self.bot.get_user(834834946832203776)

        if isinstance(message.channel, discord.DMChannel):
            if message.content:
                if message.author.id == 240059262297047041: #stacia > pond
                    await pond.send(f"{message.clean_content}", delete_after=1800)
                if message.author.id == 371230466319187969: #pond > stacia
                    await stacia.send(f"{message.clean_content}" , delete_after=1800)
                if message.author.id == 834834946832203776: #latte > stacia
                    await stacia.send(f"{message.clean_content}" , delete_after=1800)

            if message.attachments:
                image = message.attachments[0].proxy_url
                if message.author.id == 240059262297047041: #stacia > pond
                    await pond.send(image, delete_after=1800)
                if message.author.id == 371230466319187969: #pond > stacia
                    await stacia.send(image, delete_after=1800)
                if message.author.id == 834834946832203776: #latte > stacia
                    await stacia.send(image, delete_after=1800)
                        
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

def setup(bot):
    bot.add_cog(DM_Message(bot))