import discord
from discord.ext import commands
import re
import os
from datetime import datetime, timedelta, timezone
from config import *

intents = discord.Intents.default()
intents.members = True

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs info : online')

    @commands.command(aliases=['sv'])
    async def serverinfo(self, Ctx):
        header = f"Server infomation - {Ctx.guild.name}\n\n"
        rows = {
            "Name"                  : Ctx.guild.name,
            "ID"                    : Ctx.guild.id,
            "Region"                : str(Ctx.guild.region).title(),
		    "Owner"                 : Ctx.guild.owner.display_name,
		    "Shard ID"              : Ctx.guild.shard_id,
		    "Created on"            : Ctx.guild.created_at.strftime("%d/%m/%y %H:%M:%S"),
		    "joined"                : max([Member.joined_at for Member in Ctx.guild.members]).strftime("%d/%m/%y %H:%M:%S"),
		    "Members with bots"     : Ctx.guild.member_count,
		    "Members"               : len([member for member in Ctx.guild.members if not member.bot]),
		    "Bots"                  : len([Member for Member in Ctx.guild.members if Member.bot]),   
		    "categories"            : len(Ctx.guild.categories),
		    "text channels"         : len(Ctx.guild.text_channels),
		    "voice channels"        : len(Ctx.guild.voice_channels),
		    "roles"                 : len(Ctx.guild.roles),
		    "Banned members"        : len(await Ctx.guild.bans()),
	        "Most recent member"    : [Member for Member in Ctx.guild.members if Member.joined_at is max([Member.joined_at for Member in Ctx.guild.members])][0].display_name,          
		    "invite link"           : len(await Ctx.guild.invites()),

        }
        table = header + "\n".join([f"{key}{' '*(max([len(key) for key in rows.keys()])+2-len(key))}{value}" for key, value in rows.items()])
        await Ctx.send(f"```{table}```")
        return

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