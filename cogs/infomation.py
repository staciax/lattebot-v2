# Standard 
import discord , random , time , re , os , typing , unicodedata , asyncio
from discord.ext import commands
from datetime import datetime, timedelta, timezone


# Third party
import giphy_client 
import typing
from typing import Union
from giphy_client.rest import ApiException

from utils import Pag

# Local
import utils
from config import *

intents = discord.Intents.all()

emoji_s = utils.emoji_converter

class Infomation(commands.Cog):

    def __init__(self, client):
        self.client = client

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

    @commands.command(aliases=["si", "serverinformation", "serverinformations" , "guildinfo" , "gi"])
    @commands.guild_only()
    async def serverinfo(self, ctx):

        #afk_channel_check and timeout
        sec = utils.afk_channel_timeout(ctx)

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
                ("AFK Chennels",ctx.guild.afk_channel, True),
                ("AFK Timer",sec,True),
                ("Rules Channel",utils.rules_channel(ctx),True),
                ("System Channel",utils.system_channel(ctx),True),
                ("Verification Level",ctx.guild.verification_level,True),
                ("Activity",f"{emoji_s('member')} **Total:** {str(ctx.guild.member_count)}\n{emoji_s('online')} **Online:** {statuses[0]} \n{emoji_s('idle')} **Idle:** {statuses[1]} \n{emoji_s('dnd')} **Dnd:** {statuses[2]} \n{emoji_s('offline')} **Offline:** {statuses[3]}",True),
                ("Boosts",boost,True),
                ("Emoji",f"**Total:** {emoji_total}\n**Regular:** {emoji_regular}\n**Animated:** {emoji_animated}",True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        embed.set_thumbnail(url=ctx.guild.icon.url)
    
        await ctx.send(embed=embed , mention_author=False)
    
    @commands.command(aliases=["servericon","guildicon" ,"sic"])
    @commands.guild_only()
    async def server_icon(self, ctx , *, guild_id: int = None):
        if guild_id is None:
            guild = ctx.guild
        else:
            guild = self.client.get_guild(guild_id)
        
        try:
            embed = discord.Embed(title = f"{guild.name}'s Icon:", color=0xffffff).set_image(url = guild.icon.url)
            await ctx.send(embed = embed)
        except:
            embed = discord.Embed(description="guild not found" , color=WHITE)
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["serverbanner","sb","guildbanner"])
    @commands.guild_only()
    async def server_banner(self, ctx , *, guild_id: int = None):
        if guild_id is None:
            guild = ctx.guild
        else:
            guild = self.client.get_guild(guild_id)
        
        try:
            embed = discord.Embed(title = f"{guild.name}'s Banner:", color=0xffffff).set_image(url = guild.banner.url)
            await ctx.send(embed = embed)
        except:
            embed = discord.Embed(description="guild not found" , color=WHITE)
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["serversplash","ss","guildsplash","splash","invitebanner"])
    @commands.guild_only()
    async def server_invite_splash(self, ctx , *, guild_id: int = None):
        if guild_id is None:
            guild = ctx.guild
        else:
            guild = self.client.get_guild(guild_id)
        
        try:
            embed = discord.Embed(title = f"{guild.name}'s Invite banner:", color=0xffffff).set_image(url = guild.splash.url)
            await ctx.send(embed = embed)
        except:
            embed = discord.Embed(description="guild not found" , color=WHITE)
            await ctx.send(embed=embed)
        

    @commands.command(aliases=["ui", "userinformation", "userinformations" , "memberinfo" ,"mi"])
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

        embed = discord.Embed(colour=0xffffff)  #timestamp=ctx.message.created_at, #title=f"User Info - {member}")        embed.set_author(name=f"User info - {member}", icon_url=member.avatar.url)
        fields = [("Nickname",f"{member.display_name}", True),
                ("Is bot?","Yes" if member.bot else "No", True),
                ("Activity",member_activity, True),
                ("Join position",f"{str(members.index(member)+1)}/{ctx.guild.member_count}", True),
                ("Joined",f"{member_joined}", True),
                ("Registered",f"{member_created}", True),
                ("Status",f"{desktop}\n{mobiles}\n{Web}", True),
                ("Badge :",f"{badges}** **", True),
                ("Top Role",member.top_role.mention, False),
                ("Roles ({})\n".format(len(member.roles)-1), role_string , False)]

        for name , value , inline in fields:
            embed.add_field(name=name , value=value , inline=inline)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"ID: {member.id}")

        await ctx.send(embed=embed)

    @commands.command(aliases=['av'])
    @commands.guild_only()
    async def avatar(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title = f"{member.name}'s Avatar:", color=0xffffff).set_image(url = member.avatar.url)
        await ctx.send(embed = embed)

    @commands.command(name="emojiinfo", aliases=["ei"])
    @commands.guild_only()
    async def emoji_info(self, ctx, emoji: discord.Emoji = None):
        if not emoji:
            embed_help = discord.Embed(color = 0xffffff)
            embed_help.set_author(name=f"{ctx.author.name}" , icon_url = ctx.author.avatar.url)
            embed_help.add_field(name="Emoji Infomation" , value="```yaml\n.emojiinfo [emoji] | .ei [emoji]```", inline = True)
            return await ctx.send(embed=embed_help , delete_after=15)
#            return await ctx.invoke(self.client.get_command("help") , category="info")
                    

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
    
    @commands.command(aliases=["ri"])
    async def roleinfo(self, ctx, role: discord.Role=None):
        if role is None:
            print("role is None")
        embed = discord.Embed(color=role.color)
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
        embed.description = f"{info}"

        msg = await ctx.send(embed=embed)

        await msg.add_reaction("<:greentick:881500884725547021>")

        try:
            reaction , user = await self.client.wait_for(
                "reaction_add",
                timeout=30,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )

        except asyncio.TimeoutError:
            await msg.delete()
            return

        await msg.delete()

        pages = []
        member_per_page = 10
        a = 0
        for i in range(0, len(role.members), member_per_page):
            message = ""
            next_commands = role.members[i: i + member_per_page]
            
            for x in next_commands:
                a += 1
                message += f"**{a}**. {x} | `{x.id}`\n"

            pages.append(message)

        await Pag(title=f"List member in role {role.name}",color=role.color, entries=pages, length=1).start(ctx)

    @commands.command(brief = "gives info on emoji_id and emoji image.")
    @commands.guild_only()
    async def emoji_id(self, ctx, *, emoji : typing.Optional [typing.Union[discord.PartialEmoji, discord.Message, utils.EmojiBasic]] = None):

        if isinstance(emoji, discord.Message):
            emoji_message = emoji.content
            emoji = None
      
            with contextlib.suppress(commands.CommandError, commands.BadArgument):
                emoji = await utils.EmojiBasic.convert(ctx, emoji_message) or await commands.PartialEmojiConverter().convert(ctx, emoji_message)

        if emoji:
            embed = discord.Embed(description=f" Emoji ID: {emoji.id}",color=random.randint(0, 16777215))
            embed.set_image(url=emoji.url)
            await ctx.send(embed=embed)

        else:
            await ctx.send("Not a valid emoji id.")

#error

#    @emoji_info.error
#    async def emoji_info_error(self , ctx , error):
#        embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Emoji not found",color=0xffffff)
#        await ctx.send(embed=embedar , delete_after=15)

#    @poll.error
#    async def poll_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify message to poll | `poll` `[message]`",color=0xffffff)
#            await ctx.message.delete()
#            await ctx.send(embed=embedar , delete_after=15)


def setup(client):
    client.add_cog(Infomation(client))