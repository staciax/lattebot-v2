# Standard 
import discord
import random
import time
import re
import os
from discord.ext import commands
from datetime import datetime, timedelta, timezone


# Third party
import giphy_client 
import typing
from typing import Union

# Local
import utils
from config import *
from giphy_client.rest import ApiException

intents = discord.Intents.default()
intents.members = True

#giphy

class Info(commands.Cog):

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

    @commands.command(aliases=['sv'])
    async def serverinfo(self, ctx):

        embed = discord.Embed(title=f"Server info - {ctx.guild.name}",color=0xffffff)
        embed.add_field(name="Server name", value=ctx.guild.name)
        embed.add_field(name="Server Owner ", value=f"{ctx.guild.owner.display_name}#{ctx.guild.owner.discriminator}\n{ctx.guild.owner.mention}")
        embed.add_field(name="Server Region", value=str(ctx.guild.region).title())
        embed.add_field(name="Server Member", value=len([member for member in ctx.guild.members if not member.bot]))
        embed.add_field(name="Server Bots", value=len([Member for Member in ctx.guild.members if Member.bot]))
        embed.add_field(name="Server Roles", value=len(ctx.guild.roles))
        embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels))
        embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels))
        embed.add_field(name="Stage Chennels", value=len(ctx.guild.stage_channels))
        embed.add_field(name="Category size", value=len(ctx.guild.categories))
        embed.add_field(name="AFK Chennels", value=ctx.guild.afk_channel)
#        conversion = timedelta(seconds=ctx.guild.afk_timeout)
#        sec = str(conversion)
        sec = ctx.guild.afk_timeout
        if ctx.guild.afk_channel == None:
            sec = "None"

        if sec == 3600:
            sec = "1 Hour"
        elif sec == 1800:
            sec = "30 Minutes"
        elif sec == 900:
            sec = "15 Minutes"
        elif sec == 300:
            sec = "5 Minutes"
        elif sec == 60:
            sec = "1 Minute"

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        eoffline = '<:offline:864171414750625812>'
        ednd = '<:dnd2:864173608321810452>'
        eidle = '<:idle:864185381833277501>'
        eonline = '<:Online:864171414466592788>'
        emember = '<:member:864219999954796615>'
        memberCount = str(ctx.guild.member_count)

        rs = ""
        rulesch = ctx.guild.rules_channel
        if rulesch == None:
            rs += ("none")
        else:
            rs = ctx.guild.rules_channel.mention

        sy = ""
        systemch = ctx.guild.system_channel
        if systemch == None:
            sy += ("none")
        else:
            sy = ctx.guild.system_channel.mention

        embed.add_field(name="AFK Timer", value=sec)
        embed.add_field(name="Rules Channel", value=rs)
        embed.add_field(name="System Channel", value=sy)
        embed.add_field(name="Verification Level", value=ctx.guild.verification_level)
        emojitotal = len(ctx.guild.emojis)
        emojiregular = len([emoji for emoji in ctx.guild.emojis if not emoji.animated])
        emojianimated = len([emoji for emoji in ctx.guild.emojis if emoji.animated])
        embed.add_field(name="Activity", value=f"{emember} **Total:** {memberCount}\n{eonline} **Online:** {statuses[0]} \n{eidle} **Idle:** {statuses[1]} \n{ednd} **Dnd:** {statuses[2]} \n{eoffline} **Offline:** {statuses[3]}")
        embed.set_thumbnail(url=self.client.user.avatar.url)

#        onlines = len(ctx.status.online)
#        offlines = len(ctx.status.offline)
#        idles = len(ctx.status.idle)
#        Dnds = len(ctx.status.do_not_disturb)
#        embed.add_field(name=f"Activity", value=f"Online : {onlines}\nOffline{offlines}\nIdle : {idles}\n Dnd: {Dnds}")

        if ctx.guild.premium_tier != 0:
            boosts = f'**Level:** {ctx.guild.premium_tier}\n**Boosts:** {ctx.guild.premium_subscription_count}'
            last_boost = max(ctx.guild.members, key=lambda m: m.premium_since or ctx.guild.created_at)
            if last_boost.premium_since is not None:
                boosts = f'{boosts}\n**Last Boost:**\n{last_boost}'
            embed.add_field(name='Boosts', value=boosts)
        embed.add_field(name="Emoji",value=f"**Total:** {emojitotal}\n**Regular:** {emojiregular}\n**Animated:** {emojianimated}")
    
        await ctx.send(embed=embed)

    @commands.command(aliases=['ui'] , pass_context=True)
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour=0xffffff)  #timestamp=ctx.message.created_at, #title=f"User Info - {member}")
        embed.set_author(name=f"User info - {member}", icon_url=member.avatar.url)
        embed.set_thumbnail(url=member.avatar.url)
#        embed.add_field(name="Display Name", value=member.mention)   
        embed.add_field(name="Nickname", value=f"`{member.display_name}`")         
#        embed.add_field(name=f"Boost status", value="Yes" if bool(member.premium_since) else "No", inline=True)

        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Is bot?", value="`Yes`" if member.bot else "`No`" , inline=True)
        embed.add_field(name="Activity", value=f"`{str(member.activity.type).title().split('.')[1]} {member.activity.name}`" if member.activity is not None else "** **")
        embed.add_field(name=f"Join position", value=f"`{str(members.index(member)+1)}/{ctx.guild.member_count}`", inline=True)
        eoffline = '<:offline:864171414750625812>'
        ednd = '<:dnd2:864173608321810452>'
        eidle = '<:idle:864185381833277501>'
        eonline = '<:Online:864171414466592788>'

        mobiles = str(member.mobile_status)
        if mobiles == 'offline':
            mobiles = f"{eoffline} Mobile"
        elif mobiles == 'dnd':
            mobiles = f"{ednd} Mobile"
        elif mobiles == 'idle':
            mobiles = f"{eidle} Mobile"
        elif mobiles == 'online':
            mobiles = f"{eonline} Mobile"  
        else:
            mobiles = f"{eonline} Mobile"
        
        desktop = str(member.desktop_status)
        if desktop == 'offline':
            desktop = f"{eoffline} Desktop"
        elif desktop == 'dnd':
            desktop = f"{ednd} Desktop"
        elif desktop == 'idle':
            desktop = f"{eidle} Desktop"
        elif desktop == 'online':
            desktop = f"{eonline} Desktop"       
        else:
            desktop = f"{eonline} Desktop"
        
        Web = str(member.web_status)
        if Web == 'offline':
            Web = f"{eoffline} Web"
        elif Web == 'dnd':
            Web =  f"{ednd} Web"
        elif Web == 'idle':
            Web = f"{eidle} Web"
        elif Web == 'online':
            Web = f"{eonline} Web"
        else:
            Web = f"{eonline} Web"
        
        embed.add_field(name="Joined", value=member.joined_at.strftime("`%d-%m-%Y, %H:%M`"))
        embed.add_field(name="Registered", value=member.created_at.strftime("`%d-%m-%Y, %H:%M`"))        
        embed.add_field(name=f"Status", value=F"{desktop}\n{mobiles}\n{Web}")   
        flags = member.public_flags.all()
        badges ="\u0020".join(utils.profile_converter(f.name) for f in flags)
        if member.bot: badges = f"{badges} {utils.profile_converter('bot')}"
        if member.premium_since: badges = f"{badges} {utils.profile_converter('guildboost')}"
        embed.add_field(name=f"Badge :", value=f"{badges}** **")
        embed.add_field(name="Top Role", value=member.top_role.mention , inline=False) 
#        embed.add_field(name="Current status", value=f"`{str(member.status).title()}`")
        
        if len(member.roles) > 1:
            role_string = ' '.join([r.mention for r in member.roles][1:])
            embed.add_field(name="Roles ({})\n".format(len(member.roles)-1), value=role_string, inline=False) #delete @everyone role
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

    @commands.command(name="emojiinfo", aliases=["ei"])
    async def emoji_info(self, ctx, emoji: discord.Emoji = None):
        if not emoji:
#            embed = discord.Embed()
            return await ctx.invoke(self.client.get_command("help"), entity="emojiinfo")

        try:
            emoji = await emoji.guild.fetch_emoji(emoji.id)
        except discord.NotFound:
            return await ctx.send("I could not find this emoji in the given guild.")

        is_managed = "Yes" if emoji.managed else "No"
        is_animated = "Yes" if emoji.animated else "No"
        requires_colons = "Yes" if emoji.require_colons else "No"
        creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
        can_use_emoji = (
            "Everyone"
            if not emoji.roles
            else " ".join(role.name for role in emoji.roles)
        )

        description = f"""
        **General:**
        **- Name:** {emoji.name}
        **- Id:** {emoji.id}
        **- URL:** [Link To Emoji]({emoji.url})
        **- Author:** {emoji.user.mention}
        **- Time Created:** {creation_time}
        **- Usable by:** {can_use_emoji}
        
        **Other:**
        **- Animated:** {is_animated}
        **- Managed:** {is_managed}
        **- Requires Colons:** {requires_colons}
        **- Guild Name:** {emoji.guild.name}
        **- Guild Id:** {emoji.guild.id}
        """

        embed = discord.Embed(
            title=f"**Emoji Information for:** `{emoji.name}`",
            description=description,
            colour=0xADD8E6,
        )
        embed.set_thumbnail(url=emoji.url)
        await ctx.send(embed=embed)

    @emoji_info.error
    async def emoji_info_error(self , ctx , error):
        await ctx.send("not found")

    @commands.command()
    async def poll(self, ctx,*,message):
        emb=discord.Embed(title=" POLL", description=f"{message}")
        msg=await ctx.channel.send(embed=emb)
        await msg.add_reaction(f'{utils.emoji_converter("xmark")}')
        await msg.add_reaction(f'{utils.emoji_converter("check")}')
        await ctx.message.delete()

    @commands.command()
    async def gif(self, ctx,*,q="random"):

        api_instance = giphy_client.DefaultApi()
        api_key = GIPHYAPI

        try: 
        
            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q,color=0xffffff)
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)



def setup(client):
    client.add_cog(Info(client))