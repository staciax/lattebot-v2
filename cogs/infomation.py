# Standard 
import discord
import random
import time
import re
import os
import typing
import unicodedata
import asyncio
import contextlib
from discord.ext import commands
from datetime import datetime, timedelta, timezone

# Third party
import typing
from typing import Union
from PIL import Image , ImageColor
from io import BytesIO

# Local
import utils
from config import *
#from utils.ButtonRef import roleinfo_view
from utils.view_converter import roleinfo_view, channel_info_view

emoji_s = utils.emoji_converter

class Infomation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def our_custom_check():
        async def predicate(ctx):
            return ctx.guild is not None \
                and ctx.author.guild_permissions.manage_channels \
                and ctx.me.guild_permissions.manage_channels
        return commands.check(predicate) #@our_custom_check()

    def is_it_me(ctx):
        return ctx.author.id == 385049730222129152 #@commands.check(is_it_me)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.command(description="Show server infomation", aliases=["si", "serverinformation", "serverinformations" , "guildinfo" , "gi"])
    @commands.guild_only()
    async def serverinfo(self, ctx):

        #afk_channel_check and timeout
        afk_channels = utils.afk_channel_check(ctx)      
        afk_timeouts = utils.afk_channel_timeout(ctx)

        #member_status and emoji_member_status
        statuses = utils.member_status(ctx)
        
        #emoji_count
        emoji_total = len(ctx.guild.emojis)
        emoji_regular = len([emoji for emoji in ctx.guild.emojis if not emoji.animated])
        emoji_animated = len([emoji for emoji in ctx.guild.emojis if emoji.animated])

        boost = utils.check_boost(ctx)

        embed = discord.Embed(title=f"Server info - {ctx.guild.name}",color=0xffffff)
        fields = [("Server name",ctx.guild.name, True),
				("Server Owner",f"{ctx.guild.owner.mention}", True),
                ("Server Region",str(ctx.guild.region).title(), True),
                ("Server Member",len([member for member in ctx.guild.members if not member.bot]), True),
                ("Server Bots",len([Member for Member in ctx.guild.members if Member.bot]), True),
                ("Server Roles",len(ctx.guild.roles), True),
                ("Text Channels",len(ctx.guild.text_channels), True),
                ("Voice Channels",len(ctx.guild.voice_channels), True),
                ("Stage Chennels",len(ctx.guild.stage_channels), True),
                ("Category size",len(ctx.guild.categories), True),
                ("AFK Chennels",afk_channels, True),
                ("AFK Timer",afk_timeouts,True),
                ("Rules Channel",utils.rules_channel(ctx),True),
                ("System Channel",utils.system_channel(ctx),True),
                ("Verification Level",utils.guild_verification_level(ctx),True),
                ("Activity",f"{emoji_s('member')} **Total:** {str(ctx.guild.member_count)}\n{emoji_s('online')} **Online:** {statuses[0]} \n{emoji_s('idle')} **Idle:** {statuses[1]} \n{emoji_s('dnd')} **Dnd:** {statuses[2]} \n{emoji_s('offline')} **Offline:** {statuses[3]}",True),
                ("Boosts",boost,True),
                ("Emoji",f"**Total:** {emoji_total}\n**Regular:** {emoji_regular}\n**Animated:** {emoji_animated}",True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        embed.set_thumbnail(url=ctx.guild.icon.url)
    
        await ctx.send(embed=embed)
    
    @commands.command(description="Show server icon", aliases=["servericon","guildicon" ,"sic"])
    @commands.guild_only()
    async def server_icon(self, ctx , *, guild_id: int = None):
        if guild_id is None:
            guild = ctx.guild
        else:
            guild = self.bot.get_guild(guild_id)
        
        try:
            embed = discord.Embed(title = f"{guild.name}'s Icon:", color=0xffffff).set_image(url = guild.icon.url)
            #start_view_button
            view = discord.ui.View()
            style = discord.ButtonStyle.gray
            item = discord.ui.Button(style=style, label="Server icon URL", url=guild.icon.url)
            view.add_item(item=item)
            await ctx.send(embed = embed , view=view)
        except:
            embed = discord.Embed(description="guild not found" , color=WHITE)
            await ctx.send(embed=embed)
    
    @commands.command(description="Show server banner",aliases=["serverbanner","sb","guildbanner"])
    @commands.guild_only()
    async def server_banner(self, ctx , *, guild_id: int = None):
        if guild_id is None:
            guild = ctx.guild
        else:
            guild = self.bot.get_guild(guild_id)
        
        try:
            embed = discord.Embed(title = f"{guild.name}'s Banner:", color=0xffffff).set_image(url = guild.banner.url)
            #start_view_button
            view = discord.ui.View()
            style = discord.ButtonStyle.gray
            item = discord.ui.Button(style=style, label="Server banner URL", url=guild.banner.url)
            view.add_item(item=item)
            await ctx.send(embed = embed, view=view)
        except:
            embed = discord.Embed(description="Not found" , color=WHITE)
            await ctx.send(embed=embed)
    
    @commands.command(description="Show server splash", aliases=["splash","serversplash","ssp","invitebanner"])
    @commands.guild_only()
    async def server_splash(self, ctx , *, guild_id: int = None):
        if guild_id is None:
            guild = ctx.guild
        else:
            guild = self.bot.get_guild(guild_id)
        
        try:
            embed = discord.Embed(title = f"{guild.name}'s Invite banner:", color=0xffffff).set_image(url = guild.splash.url)
            #start_view_button
            view = discord.ui.View()
            style = discord.ButtonStyle.gray
            item = discord.ui.Button(style=style, label="Splash URL", url=guild.splash.url)
            view.add_item(item=item)
            await ctx.send(embed=embed , view=view)
        except:
            embed = discord.Embed(description="Not found" , color=WHITE)
            await ctx.send(embed=embed)
        

    @commands.command(description="Userinfomation", usage=f"[member]" , aliases=["ui", "userinformation","memberinfo"])
    @commands.guild_only()
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author  

        #member_status
        mobiles = utils.mobile_status(member)
        desktop = utils.desktop_status(member)
        Web = utils.web_status(member)

        #member_badge
        flags = member.public_flags.all()
        badges ="\u0020".join(utils.profile_converter(f.name) for f in flags)
        if member.bot: badges = f"{badges} {utils.profile_converter('bot')}"
        if member.premium_since: badges = f"{badges} {utils.profile_converter('guildboost')}"

        #member_info
        member_joined = utils.format_dt(member.joined_at)
        member_created = utils.format_dt(member.created_at)
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        member_activity = f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "** **"
        roles = [role for role in member.roles]
        role_str = []
        if len(member.roles) > 1:
            role_string = ' '.join(reversed([r.mention for r in member.roles][1:]))
        else:
            role_string = "this user don't have a role"
        #fetch_banner
        fetch_member = await self.bot.fetch_user(member.id)
        #if fetchedMember.banner.is_animated() == True:

        #member_color
        if member.colour:
            M_color = member.colour
        else:
            M_color = 0xffffff

        #start_view
        view = discord.ui.View()
        style = discord.ButtonStyle.gray 

        embed = discord.Embed(title=f"{member}'s Infomation",colour=M_color)  #timestamp=ctx.message.created_at
        fields = [("Nickname",f"{member.display_name}", True),
                ("Is bot?","Yes" if member.bot else "No", True),
                ("Activity",member_activity, True),
                ("Join position",f"{str(members.index(member)+1)}/{ctx.guild.member_count}", True),
                ("Joined",f"{member_joined}", True),
                ("Registered",f"{member_created}", True),
                ("Status",f"{desktop}\n{mobiles}\n{Web}", True),
                ("Badge",f"{badges}** **", True),
                ("Top Role",member.top_role.mention, False),
                ("Roles ({})\n".format(len(member.roles)-1), role_string , False)]

        for name , value , inline in fields:
            embed.add_field(name=name , value=value , inline=inline)
        Member_URL = ""
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
            item = discord.ui.Button(style=style, label="Avatar URL", url=member.avatar.url)
            view.add_item(item=item)
        if fetch_member.banner:
            embed.set_image(url=fetch_member.banner.url)
            item2 = discord.ui.Button(style=style, label="Banner URL", url=fetch_member.banner.url) 
            view.add_item(item=item2)
        elif fetch_member.accent_color:
            embed.add_field(name=f"Banner color" , value=f"{fetch_member.accent_color} (HEX)", inline=False)
            embed.set_footer(text=f"ID: {member.id}")

        await ctx.send(embed=embed , view=view)
    
    @commands.group(invoke_without_command=True,description="Show avatar", usage=f"[member]" , aliases=["av"])
    @commands.guild_only()
    async def avatar(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title = f"{member.name}'s Avatar:", color=0xffffff)
        if member.avatar:
            embed.set_image(url = member.avatar.url)
            #start_view_button
            view = discord.ui.View()
            style = discord.ButtonStyle.gray
            item = discord.ui.Button(style=style, label="Avatar URL", url=member.avatar.url)
            view.add_item(item=item)
            await ctx.send(embed = embed , view=view)
        else:
            embed.description = f"this user must have a avatar."
            await ctx.send(embed = embed)
    
    @avatar.command(name="server",description="Show server avatar", usage=f"[member]" , aliases=["sav"])
    @commands.guild_only()
    async def display_avatar(self, ctx, member:discord.Member=None):
        member = member or ctx.author
        embed = discord.Embed(title = f"{member.name}'s Server avatar:", color=0xffffff)
        if member.avatar != member.display_avatar:
            embed.set_image(url = member.display_avatar.url)
            #start_view_button
            view = discord.ui.View()
            style = discord.ButtonStyle.gray
            item = discord.ui.Button(style=style, label="Server avatar URL", url=member.display_avatar.url)
            view.add_item(item=item)
            await ctx.send(embed = embed , view=view)
        else:
            embed.description = f"this user must have a server avatar."
            await ctx.send(embed = embed)

    
    @commands.command(description="Show banner", usage=f"[member]" , aliases=["bn"])
    @commands.guild_only()
    async def banner(self, ctx, *,member: discord.Member=None):
        member = member or ctx.author
        fetch_member = await self.bot.fetch_user(member.id)

        embed = discord.Embed(title=f"{member.name}'s Banner:",color=0xffffff)

        if fetch_member.banner:
            embed.set_image(url=fetch_member.banner.url)
            #start_view_button
            view = discord.ui.View()
            style = discord.ButtonStyle.gray
            item = discord.ui.Button(style=style, label="Banner URL", url=fetch_member.banner.url)
            view.add_item(item=item)
            await ctx.send(embed=embed , view=view)
        elif fetch_member.accent_color:
        #print(fetch_member.accent_color)
            #pillow_generate
            img = Image.new("RGB", (256, 144), ImageColor.getrgb(f"{fetch_member.accent_color}"))
            buffer = BytesIO()
            img.save(buffer, 'png')
            buffer.seek(0)
            f = discord.File(buffer, filename='banner.png')

            embed.set_image(url="attachment://banner.png")
            embed.add_field(name=f"this user don't have banner\n\nAccent color:" , value=f"{fetch_member.accent_color} (HEX)", inline=False)
            await ctx.send(file=f, embed=embed)
        else:
            embed.description = f"this user must have a banner."
            await ctx.send(embed=embed, delete_after=10)

    @commands.command(name="emojiinfo", aliases=["ei"], usage=f"<emoji>")
    @commands.guild_only()
    async def emoji_info(self, ctx, emoji: discord.Emoji = None):
        if not emoji:
            embed_help = discord.Embed(color = 0xffffff)
            if ctx.author.avatar.url is not None:
                embed_help.set_author(name=ctx.author.name , icon_url = ctx.author.avatar.url)
            else:
                embed_help.set_author(name=ctx.author.name)
            embed_help.add_field(name="Emoji Infomation" , value=f"```yaml\n{ctx.clean_prefix}emojiinfo [emoji] | {ctx.clean_prefix}ei [emoji]```", inline = True)
            return await ctx.send(embed=embed_help , delete_after=15)
        #            return await ctx.invoke(self.bot.get_command("help") , category="info")
                    

        try:
            emoji = await emoji.guild.fetch_emoji(emoji.id)
        except discord.NotFound:
            return await ctx.send("I could not find this emoji in the given guild.")

        is_managed = "Yes" if emoji.managed else "No"
        is_animated = "Yes" if emoji.animated else "No"
        requires_colons = "Yes" if emoji.require_colons else "No"
        creation_time = utils.format_dt(emoji.created_at)
        can_use_emoji = (
            "Everyone"
            if not emoji.roles
            else " ".join(role.name for role in emoji.roles)
        )

        description = f"""
        **Name:** {emoji.name}
        **Id:** {emoji.id}
        **URL:** [Link To Emoji]({emoji.url})
        **Author:** {emoji.user.mention}
        **Time Created:** {creation_time}
        **Guild Name:** {emoji.guild.name}
        **Guild Id:** {emoji.guild.id}
        """
        #        **Other:**
        #           **- Usable by:** {can_use_emoji}
        #        **- Animated:** {is_animated}
        #        **- Managed:** {is_managed}
        #        **- Requires Colons:** {requires_colons}
        #        **- Guild Name:** {emoji.guild.name}
        #        **- Guild Id:** {emoji.guild.id}
        #        """

        embed = discord.Embed(
            title=f"**Emoji Information for:** `{emoji.name}`",
            description=description,
            colour=0xADD8E6,
        )
        embed.set_thumbnail(url=emoji.url)
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["ri"], usage="<role>")
    async def roleinfo(self, ctx, role: discord.Role=None):
        if role is None:
            embed_error = discord.Embed(description="Please specify role",color=0xffffff)
            await ctx.send(embed=embed_error)
        embed_role = discord.Embed(color=role.color)
        role_perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in role.permissions if p[1]])
        info = f"""
        **Mention**: {role.mention}
        **ID**: {role.id}
        **Name**: {role.name}
        **Color**: {role.color}
        **Create**: {utils.format_dt(role.created_at)}
        **Positon**: {role.position}
        **Members**: {len(role.members)}
        **Permission**: {role_perm_string}
        """
        embed_role.description = f"{info}"

        role_member_list = []

        for x in role.members:
            member_role = f"{x} | `{x.id}`"
            role_member_list.append(member_role)

        view = roleinfo_view(ctx=ctx, embed=embed_role, entries=role_member_list, role=role)
        await view.start()

    @commands.command(description = "gives info on emoji_id and emoji image.", usage="<emoji>")
    @commands.guild_only()
    async def emoji_id(self, ctx, *, emoji : typing.Optional [typing.Union[discord.PartialEmoji, discord.Message, utils.EmojiBasic]] = None):

        if isinstance(emoji, discord.Message):
            emoji_message = emoji.content
            emoji = None
      
            with contextlib.suppress(commands.CommandError, commands.BadArgument):
                emoji = await utils.EmojiBasic.convert(ctx, emoji_message) or await commands.PartialEmojiConverter().convert(ctx, emoji_message)

        if emoji:
            embed = discord.Embed(description=f"Emoji ID: {emoji.id}",color=random.randint(0, 16777215))
            embed.set_image(url=emoji.url)
            await ctx.send(embed=embed)

        else:
            await ctx.send("Not a valid emoji id.")

    @commands.command(help="channel infomation", aliases=["ci"])
    @commands.guild_only()
    async def channel_info(self, ctx, channel: typing.Union[discord.TextChannel, discord.VoiceChannel]=None):
        if channel is None:
            embed_error = discord.Embed(description="Please specify channel",color=0xffffff)
            await ctx.send(embed=embed_error)
        embed = discord.Embed(color=0xffffff)
        embed.title = f"{channel.name}'s Info"
        if str(channel.type) == "voice": embed.add_field(
            name="infomation:",
            value=f"**Type:** voice channel\n**Birate:** {int(channel.bitrate / 1000)}kbps\n**Region:** {channel.rtc_region}\n**Connected:** {len(channel.members)} connected",
            inline=False
        )
        if str(channel.type) == "text": embed.add_field(
            name="infomation:", 
            value=f"**Type:** text channel\n**Topic** : {channel.topic}\n**NSFW** : {channel.nsfw}",
            inline=False
        )
        
        role_list = []
        member_list = []
        for role in channel.changed_roles:
            role_msg = f"{role.mention} | `{role.id}`"
            role_list.append(role_msg)
        for member in channel.members:
            member_msg = f"{member.name} | `{member.id}`"
            member_list.append(member_msg)
              
        embed.add_field(name="Category:" , value=f"{channel.category}" , inline=False)
        embed.add_field(name="Create date:" , value=f"{utils.format_dt(channel.created_at)}" , inline=False)
        embed.set_thumbnail(url=channel.guild.icon.url)
        embed.set_footer(text=f"ID : {channel.id}")

        if str(channel.type) == 'text':
            view = channel_info_view(ctx=ctx, embed=embed, channel=channel, role_list=role_list, member_list=member_list)
            await view.start_text()
        if str(channel.type) == 'voice':
            view = channel_info_view(ctx=ctx, embed=embed, channel=channel, role_list=role_list, member_list=member_list)
            await view.start_voice()

def setup(bot):
    bot.add_cog(Infomation(bot))