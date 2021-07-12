from discord.ext import commands
import discord, random, os
import platform
from time import time
from datetime import datetime, timedelta, timezone

intents = discord.Intents.default()
intents.members = True


class addleave(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channels = [channel for channel in guild.channels]
        roles = roles= [role for role in guild.roles]
        embed = discord.Embed(title="Bot just joined: "+str(guild.name), color=random.randint(0,16777215))
        embed.set_thumbnail(url = guild.icon.url)
        embed.add_field(name='Server Name:',value=f'{guild.name}')
        embed.add_field(name='Server ID:',value=f'{guild.id}')
        embed.add_field(name='Server region:',value=f'{guild.region}')
        embed.add_field(name='Server Creation Date:',value=f'{guild.created_at.strftime(r"%d/%m/%Y %H:%M")}')
        embed.add_field(name='Server Owner:',value=f'{guild.owner}')
        embed.add_field(name='Server Owner ID:',value=f'{guild.owner_id}')
        embed.add_field(name='Member Count:',value=f'{guild.member_count}')
        embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
        embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
        await self.client.get_channel(863806084414439454).send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channels = [channel for channel in guild.channels]
        roles = roles= [role for role in guild.roles]
        embed = discord.Embed(title="Bot just left: "+str(guild.name), color=random.randint(0,16777215))
        embed.set_thumbnail(url = guild.icon.url)
        embed.add_field(name='Server Name:',value=f'{guild.name}')
        embed.add_field(name='Server ID:',value=f'{guild.id}')
        embed.add_field(name='Server region:',value=f'{guild.region}')
        embed.add_field(name='Server Creation Date:',value=f'{guild.created_at.strftime(r"%d/%m/%Y %H:%M")}')
        embed.add_field(name='Server Owner:',value=f'{guild.owner}')
        embed.add_field(name='Server Owner ID:',value=f'{guild.owner_id}')
        try:
            embed.add_field(name='Member Count:',value=f'{guild.member_count}')
        except:
            pass
        embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
        embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
        await self.client.get_channel(863811115238948864).send(embed=embed)

def setup(client):
    client.add_cog(addleave(client))