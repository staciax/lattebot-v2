import discord
from discord.ext import commands
import time
import re
import os
from datetime import datetime, timedelta, timezone
from config import *
from typing import Union
import time

intents = discord.Intents.default()
intents.members = True


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Info')

    @commands.command()
    async def info(self, ctx, *, user: Union[discord.Member, discord.User] = None):
        """Shows info about a user."""

        user = user or ctx.author
        e = discord.Embed()
        roles = [role.name.replace('@', '@\u200b') for role in getattr(user, 'roles', [])]
        e.set_author(name=str(user))

        voice = getattr(user, 'voice', None)
        if voice is not None:
            vc = voice.channel
            other_people = len(vc.members) - 1
            voice = f'{vc.name} with {other_people} others' if other_people else f'{vc.name} by themselves'
            e.add_field(name='Voice', value=voice, inline=False)

        if roles:
            e.add_field(name='Roles', value=', '.join(roles) if len(roles) < 10 else f'{len(roles)} roles', inline=False)

        colour = user.colour
        if colour.value:
            e.colour = colour

        if user.avatar:
            e.set_thumbnail(url=user.avatar.url)

        if isinstance(user, discord.User):
            e.set_footer(text='This member is not in this server.')

        await ctx.send(embed=e)

    @commands.command(aliases=['sv'])
    async def serverinfo(self, ctx):
        embed = discord.Embed(title=f"Server info - {ctx.guild.name}",color=0xffffff)
        embed.add_field(name="Server name", value=ctx.guild.name)
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner.display_name}#{ctx.guild.owner.discriminator}\n{ctx.guild.owner.mention}")
        embed.add_field(name="Server Member", value=len([member for member in ctx.guild.members if not member.bot]))
        embed.add_field(name="Server Region", value=str(ctx.guild.region).title())
        embed.add_field(name="Server Bots", value=len([Member for Member in ctx.guild.members if Member.bot]))
        embed.add_field(name="Server Roles", value=len(ctx.guild.roles))
        embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels))
        embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels))
        embed.add_field(name="Stage Chennels", value=len(ctx.guild.stage_channels))
        embed.add_field(name="Category size", value=len(ctx.guild.categories))
        embed.add_field(name="AFK Chennels", value=ctx.guild.afk_channel)
        conversion = timedelta(seconds=ctx.guild.afk_timeout)
        converted_time = str(conversion)
        embed.add_field(name="AFK Timer", value=converted_time)
        embed.add_field(name="Rules Channel", value=ctx.guild.rules_channel.mention)
        embed.add_field(name="System Channel", value=ctx.guild.system_channel.mention)
        embed.add_field(name="Verification Level", value=ctx.guild.verification_level)
        embed.set_thumbnail(url=self.client.user.avatar.url)
#        onlines = len(ctx.status.online)
#        offlines = len(ctx.status.offline)
#        idles = len(ctx.status.idle)
#        Dnds = len(ctx.status.do_not_disturb)
#        embed.add_field(name=f"Activity", value=f"Online : {onlines}\nOffline{offlines}\nIdle : {idles}\n Dnd: {Dnds}")

        if ctx.guild.premium_tier != 0:
            boosts = f'Level {ctx.guild.premium_tier}\n{ctx.guild.premium_subscription_count} boosts'
            last_boost = max(ctx.guild.members, key=lambda m: m.premium_since or ctx.guild.created_at)
            if last_boost.premium_since is not None:
                boosts = f'{boosts}\nLast Boost: {last_boost}'
            embed.add_field(name='Boosts', value=boosts, inline=False)
    
        await ctx.send(embed=embed)

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=0xffffff)  #timestamp=ctx.message.created_at, #title=f"User Info - {member}")
        embed.set_author(name=f"User info - {member}", icon_url=member.avatar.url)
        embed.set_thumbnail(url=member.avatar.url)
#        embed.add_field(name="Display Name", value=member.mention)   
        embed.add_field(name="Nickname", value=member.display_name)         
        embed.add_field(name="Current status", value=str(member.status).title())
#        embed.add_field(name=f"Boost status", value="Yes" if bool(member.premium_since) else "No", inline=True)
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name=f"Join position", value=str(members.index(member)+1), inline=True)
        embed.add_field(name="Current Activity", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None")
        embed.add_field(name="Is bot?", value="Yes" if member.bot else "No" , inline=True)     
        embed.add_field(name="Joined", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p") ,inline=False)
        embed.add_field(name="Registered", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p"), inline=False) 
        embed.add_field(name="Top Role", value=member.top_role.mention , inline=False)
        if len(member.roles) > 1:
            role_string = ' '.join([r.mention for r in member.roles][1:])
            embed.add_field(name="Roles ({})\n".format(len(member.roles)-1), value=role_string, inline=False) #delete @everyone role
#        embed.add_field(name="ID" ,value=member.id)
#        embed.add_field(name="mention member, value=member.mention, inline=False)
#        memberbot = "Yes" if member.bot else "No"
        embed.set_footer(text=f"ID: {member.id}" ) #, icon_url = ctx.author.avatar.url)        
#        print(member.top_role.mention)
        await ctx.send(embed=embed) #text=f"You're our {member.guild.member_count} members ෆ"

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        embed = discord.Embed(title = f"{member.name}'s avatar", color = 0xc4cfcf)
        embed.set_image(url =  member.avatar.url) # Shows the avatar
        embed.set_footer(text = f'Requested by {ctx.author}', icon_url = ctx.author.avatar.url)
        await ctx.send(embed = embed)
        
def setup(client):
    client.add_cog(Info(client))