import discord, re, random
from discord.ext import commands
from discord.http import Route
import humanize
import datetime
from datetime import datetime, timedelta, timezone
from typing import Union

from utils import emoji_converter

class BetterMemberConverter(commands.Converter):
  async def convert(self, ctx, argument):
    try:
      user = await commands.MemberConverter().convert(ctx, argument)
    except commands.MemberNotFound:
      user = None

    if user == None:
      tag = re.match(r"#?(\d{4})",argument)
      if tag:
        if ctx.guild:
          test=discord.utils.get(ctx.guild.members, discriminator = tag.group(1))
          user = test or ctx.author

        if ctx.guild is None:
          user = await BetterUserconverter().convert(ctx,argument)
          user = user or ctx.author
               
    return user

class BetterUserconverter(commands.Converter):
  async def convert(self, ctx, argument):
    try:
     user=await commands.UserConverter().convert(ctx,argument)
    except commands.UserNotFound:
      user = None
    if not user and ctx.guild:
      user=ctx.guild.get_member_named(argument)

    if user == None:
      role = None

      with contextlib.suppress(commands.RoleNotFound, commands.NoPrivateMessage):
        role = await commands.RoleConverter().convert(ctx, argument)
      
      if role:
        if role.is_bot_managed():
          user=role.tags.bot_id
          user = ctx.bot.get_user(user) or await ctx.bot.fetch_user(user)

    if user == None:
      tag = re.match(r"#?(\d{4})",argument)
      if tag:
        test=discord.utils.get(ctx.bot.users, discriminator = tag.group(1))
        user = test or ctx.author
    return user

class EmojiConverter(commands.Converter):
  async def convert(self, ctx: commands.Context, arg: str): 
    emojis = emoji.unicode_codes.EMOJI_UNICODE["en"].values()
    try:
      return await commands.PartialEmojiConverter().convert(ctx,arg)
    except commands.PartialEmojiConversionFailure: pass
    if arg.rstrip("\N{variation selector-16}") in emojis or arg in emojis:
      return discord.PartialEmoji(name=arg)
    else:
      raise commands.BadArgument(f"{arg} is not an emoji")

class EmojiBasic:
    def __init__(self, id: int, url: str):
        self.id = id
        self.url = url

    @classmethod
    async def convert(cls,ctx,argument):
        match=re.match(r'(?P<id>[0-9]{15,21})',argument)
        if match:
            emoji_id=(match.group(0))
            extentions = ["gif","png"]

        for x in extentions:
            response=await ctx.bot.session.get(f"https://cdn.discordapp.com/emojis/{emoji_id}.{x}")
            if response.ok:
                return cls(emoji_id,response.real_url)

        else:
            return None

""" Server info converter"""
emoji_s = emoji_converter
m_online = emoji_s('online')
m_offline = emoji_s('offline')
m_idle = emoji_s('idle')
m_dnd = emoji_s('dnd')
m_invisible = emoji_s('invisible')

def afk_channel_check(ctx):
    if ctx.guild.afk_channel: afk_channels = ctx.guild.afk_channel
    else: afk_channels = "⠀"
    return afk_channels

def afk_channel_timeout(ctx):
    if ctx.guild.afk_channel:
        if ctx.guild.afk_timeout: afk_time = f"{int(ctx.guild.afk_timeout / 60)} Minutes"
    else: afk_time = "⠀"
    return afk_time

def member_status(ctx):
    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]    
    return statuses

def rules_channel(ctx):
    if ctx.guild.rules_channel is None: rs = "⠀"
    else: rs = ctx.guild.rules_channel.mention   
    return rs

def system_channel(ctx):
    if ctx.guild.system_channel is None: sy = "⠀"
    else: sy = ctx.guild.system_channel.mention
    return sy

def guild_verification_level(ctx):
    if str(ctx.guild.verification_level) == "none": gvl = "⠀"
    else: gvl = ctx.guild.verification_level
    return gvl

def check_boost(ctx):
    format_relative = lambda dt: discord.utils.format_dt(dt, 'R')
    if ctx.guild.premium_tier != 0:
        boosts = f'**Level:** {ctx.guild.premium_tier}\n**Boosts:** {ctx.guild.premium_subscription_count}'
        last_boost = max(ctx.guild.members, key=lambda m: m.premium_since or ctx.guild.created_at)
        if last_boost.premium_since is not None:
            boosts = f'{boosts}\n**Last Boost:**\n{last_boost} ({format_relative(last_boost.premium_since)})'
    else:
        boosts_1 = f'**Level:** \n**Boosts:** '
        boosts = f'{boosts_1}\n**Last Boost:**\n'

    return boosts

""" member infomation converter"""

def mobile_status(member):
    mobile = str(member.mobile_status)
    if mobile == 'offline':
        mb = f"{m_offline} Mobile"
    elif mobile == 'dnd':
        mb = f"{m_dnd} Mobile"
    elif mobile == 'idle':
        mb = f"{m_idle} Mobile"
    elif mobile == 'online':
        mb = f"{m_online} Mobile"  
    else:
        mb = f"{m_invisible} Mobile"    
    return mb

def desktop_status(member):
    desktop = str(member.desktop_status)
    if desktop == 'offline':
        dt = f"{m_offline} Desktop"
    elif desktop == 'dnd':
        dt = f"{m_dnd} Desktop"
    elif desktop == 'idle':
        dt = f"{m_idle} Desktop"
    elif desktop == 'online':
        dt = f"{m_online} Desktop"       
    else:
        dt = f"{m_invisible} Desktop"
    return dt

def web_status(member):
    Web = str(member.web_status)
    if Web == 'offline':
        wb = f"{m_offline} Web"
    elif Web == 'dnd':
        wb =  f"{m_dnd} Web"
    elif Web == 'idle':
        wb = f"{m_idle} Web"
    elif Web == 'online':
        wb = f"{m_online} Web"
    else:
        wb = f"{m_invisible} Web"
    return wb

def is_me():
    def predicate(ctx):
        return ctx.message.author.id == 385049730222129152
    return commands.check(predicate)

def is_guild_owner(): #@commands.check(is_owner)
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

def data_time(seconds , minutes , hours, days):
    if days == 0:
            days = ""
    else:
        days = f"{days}d "

    if hours == 0:
        hours = ""
    else:
        hours = f"{hours}h "
            
    if minutes == 0:
        minutes = ""
    else:
        minutes = f"{minutes}m "

    time = f"{days}{hours}{minutes}{seconds}"

    return time

class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]

def custom_cooldown(message):
    if message.author.permissions.manage_messages:
        return None  # no cooldown
    elif utils.get(message.author.roles, name="Nitro Booster"):
        return commands.Cooldown(2, 60)  # 2 per minute
    return commands.Cooldown(1, 60)  # 1 per minute

def status_icon(current_status):
    status = str(current_status)
    if status == "online":
        output = "https://cdn.discordapp.com/emojis/864171414466592788.png"
    elif status == "idle":
        output = "https://cdn.discordapp.com/emojis/864185381833277501.png"
    elif status == "dnd":
        output = "https://cdn.discordapp.com/emojis/864173608321810452.png"
    elif status == "offline":
        output = "https://cdn.discordapp.com/emojis/864171414750625812.png"

    return output
    
#def guess_user_nitro_status(user: Union[discord.User, discord.Member]):
#    """Guess if an user or member has Discord Nitro"""

#    if isinstance(user, discord.Member):
#        # Check if they have a custom emote in their status
#        has_emote_status = any([a.emoji.is_custom_emoji() for a in user.activities if hasattr(a, 'emoji') and a.emoji])
#
#        return any([user.avatar.is_animated(), has_emote_status, user.premium_since])
#
#    return any([user.avatar.is_animated(), user.banner])

def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise TypeError
    if not 0 < input < 4000:
        raise ValueError
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

def roman_to_int(input):
    if not isinstance(input, type("")):
        raise TypeError
    input = input.upper(  )
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            # If the next place holds a larger number, this value is negative
            if i+1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else: sum += value
        except KeyError:
            raise ValueError
    # easiest test for validity...
    if int_to_roman(sum) == input:
        return sum
    else:
        raise ValueError