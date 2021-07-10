import datetime
import discord
from config import *
from discord.ext import commands
from datetime import datetime, timezone
import time


class Log(commands.Cog):

    def __init__(self, client):
        self.bot = client

    @commands.Cog.listener()
    async def on_ready(self):       
        self.log_channel = self.bot.get_channel(SERVER_LOG)
        print('log')

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        if before.name != after.name:
            embed = discord.Embed(title="Username change",colour=after.colour,timestamp=datetime.utcnow())

            fields = [("`Before`", before.name, False),
					  ("`After`", after.name, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
                embed.set_thumbnail(url=after.avatar.url)
                embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)
            
            await self.log_channel.send(embed=embed)
        
        if before.discriminator != after.discriminator:
            embed = discord.Embed(title="Discriminator change",
                                colour=after.colour,
                                timestamp=datetime.utcnow())

            fields = [("`Before`", before.discriminator, False),
					  ("`After`", after.discriminator, False)]
            
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
                embed.set_footer(text=f"{after.display_name}#{after.discriminator}", icon_url=after.avatar.url)
            
            await self.log_channel.send(embed=embed)
        
        if before.avatar.url != after.avatar.url:
            embed = discord.Embed(title="Avatar change",description="New image is below, old to the right.",
						  colour=self.log_channel.guild.get_member(after.id).colour,
						  timestamp=datetime.utcnow())
            embed.set_thumbnail(url=before.avatar.url)
            embed.set_image(url=after.avatar.url)
            embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)

            await self.log_channel.send(embed=embed)

    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.display_name != after.display_name:
            embed = discord.Embed(title="Nickname change",
                                colour=0xFFDF00, #colour=after.colour,
						        timestamp=datetime.utcnow())

            fields = [("`Before`", before.display_name, False),
					  ("`After`", after.display_name, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
                embed.set_thumbnail(url=after.avatar.url)
                embed.set_footer(text="", icon_url=after.avatar.url)

            await self.log_channel.send(embed=embed)
        

        elif before.roles != after.roles:
            embed = discord.Embed(title="Role updates",
                                colour=0xb19cd9, #colour=after.colour,
						        timestamp=datetime.utcnow())

            fields = [(" `Before`", ", ".join([r.mention for r in before.roles]), False),
					  ("`After`", ", ".join([r.mention for r in after.roles]), False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
                embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)

            await self.log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            if before.content != after.content:
                embed = discord.Embed(title="Message edit",
                            colour=0xFF8C00, #after.author.colour,
                            timestamp=datetime.utcnow())
                
                fields = [("`Before`", before.content , False),
						  ("`After`", after.content, False)]
                
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_footer(text=f"{after.author.display_name}", icon_url=after.author.avatar.url)
                
                await self.log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            embed = discord.Embed(title="Message deletion",
                                colour=0xDC143C, #message.author.colour
                                timestamp=datetime.utcnow())
            
            fields = [("`Content`", message.content, False)]
            
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
                embed.set_footer(text=f"{message.author.display_name}", icon_url=message.author.avatar.url)
            
            await self.log_channel.send(embed=embed)
    
#    @commands.Cog.listener() #activity = role
#    async def on_presence_update(self, before, after):
#        games = ["game1", "game2", "game3"]
#        if after.activity and after.activity.name.lower() in games:
#            role = discord.utils.get(after.guild.roles, name=after.activity)
#            await after.add_roles(role)
#        elif before.activity and before.activity.name.lower() in games and not after.activity:
#            role = discord.utils.get(after.guild.roles, name=after.activity)
#            if role in after.roles: 
#                await after.remove_roles(role)

#    @commands.Cog.listener() #online offlie = role
#    async def on_presence_update(self, before, after):
#        if str(before.status) == "online":
#            if str(after.status) == "offline":
#                guild = self.bot.get_guild(840379510704046151)
#                role = discord.utils.find(lambda r: r.name == '୨ offline role ୧', guild.roles)
#                await after.add_roles(role)
#                await before.remove_roles(role)


def setup(client):
    client.add_cog(Log(client))