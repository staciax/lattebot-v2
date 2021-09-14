# Standard 
import discord , asyncio
from discord import Asset , Member , User
from discord.ext import commands
from datetime import datetime, timezone
import utils

import requests
import typing
from typing import Union

# Third party
#from discord_components import *

#import humanize
from utils import Pag
from discord.ext import menus

# Local

class Testing(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        #DiscordComponents(self.bot)
        print(f"-{self.__class__.__name__}")
     
    @commands.command(name="testembed")
    async def test_embed(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://i.imgur.com/JOsg4RL.gif")

        await ctx.send(embed=embed)
    
    @commands.command()
    async def test_time2(self, ctx):
        await ctx.send(f"{utils.format_relative(ctx.author.created_at)}")
    
    @commands.command()
    async def test_time(self,ctx):
        format_relative = lambda dt: discord.utils.format_dt(dt, 'R')
        a = f'{time.format_relative(discord.utils.utcnow())}\n{format_relative(datetime.utcnow())}'
        await ctx.send(a)

    async def get_or_fetch_member(self, guild, member_id):

        member = guild.get_member(member_id)
        if member is not None:
            return member

        shard = self.get_shard(guild.shard_id)
        if shard.is_ws_ratelimited():
            try:
                member = await guild.fetch_member(member_id)
            except discord.HTTPException:
                return None
            else:
                return member

        members = await guild.query_members(limit=1, user_ids=[member_id], cache=True)
        if not members:
            return None
        return members[0]
    
    async def say_permissions(self, ctx, member, channel):
        permissions = channel.permissions_for(member)
        e = discord.Embed(colour=member.colour)
        avatar = member.avatar.with_static_format('png')
        e.set_author(name=str(member), url=avatar)
        allowed, denied = [], []
        for name, value in permissions:
            name = name.replace('_', ' ').replace('guild', 'server').title()
            if value:
                allowed.append(name)
            else:
                denied.append(name)

        e.add_field(name='Allowed', value='\n'.join(allowed))
        e.add_field(name='Denied', value='\n'.join(denied))
        await ctx.send(embed=e)
    
    @commands.command()
    @commands.guild_only()
    async def permissions(self, ctx, member: discord.Member = None, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author

        await self.say_permissions(ctx, member, channel)
    
    @commands.command()
    @commands.guild_only()
    async def botpermissions(self, ctx, *, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        member = ctx.guild.me
        await self.say_permissions(ctx, member, channel)

    @commands.command()
    async def debugpermissions(self, ctx, guild_id: int, channel_id: int, author_id: int = None):

        guild = self.bot.get_guild(guild_id)
        if guild is None:
            return await ctx.send('Guild not found?')

        channel = guild.get_channel(channel_id)
        if channel is None:
            return await ctx.send('Channel not found?')

        if author_id is None:
            member = guild.me
        else:
            member = await self.get_or_fetch_member(guild, author_id)

        if member is None:
            return await ctx.send('Member not found?')

        await self.say_permissions(ctx, member, channel)

    @commands.command()
    async def select(self, ctx):
        embed = discord.Embed(description="TEST (v2.0.0a)")
        await ctx.send(
           "test",
            components=[
                Select(
                    placeholder="Test",
                    options=[
                        SelectOption(label="TEST1", value="1.1"),
                    ],            
                ),
            ],
        )
        while True:
            interaction = await self.bot.wait_for("select_option")
            await interaction.respond(
                content=f"{','.join(map(lambda x: x.label, interaction.component))} selected!"
            )

    @commands.command()
    async def numtest(self,ctx , num:int):
        if num > 300:
            print("300+")
        else:
            print("no")
            
def setup(bot):
    bot.add_cog(Testing(bot))