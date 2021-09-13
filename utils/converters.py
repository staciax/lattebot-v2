import discord, re, random
from discord import Member , User
from discord.ext import commands
#from discord.http import Route
from datetime import datetime, timedelta, timezone
import time
from time import perf_counter

from discord.ext.buttons import Paginator

import typing
from typing import Union

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass

def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content

class MemberConverter(commands.Converter):
    async def convert(self, ctx, argument):
        """
        This will raise MemberNotFound if the member is not found.
        """
        try:
            return await commands.MemberConverter().convert(ctx, argument)
        except commands.MemberNotFound:
            # Let's try a utils.find:
            def check(member):
                return (
                    member.name.lower() == argument.lower() or
                    member.display_name.lower() == argument.lower() or
                    str(member).lower() == argument.lower() or
                    str(member.id) == argument
                )
            if found := discord.utils.find(check, ctx.guild.members):
                return found
            raise commands.MemberNotFound(argument)
        
        
class UserConverter(commands.Converter):
    async def convert(self, ctx, argument):
        """
        This will take into account members if a guild exists.
        Raises UserNotFound if the user is not found.
        """
        if ctx.guild:
            try:
                return await MemberConverter().convert(ctx, argument)
            except commands.MemberNotFound:
                pass

        try:
            return await commands.UserConverter().convert(ctx, argument)
        except commands.UserNotFound:
            def check(user):
                return (
                    user.name.lower() == argument.lower() or
                    str(user).lower() == argument.lower() or
                    str(user.id) == argument
                )
            if found := discord.utils.find(check, ctx.bot.users):
                return found
            raise commands.UserNotFound(argument)

class DurationConverter(commands.Converter):
  async def convert(self, ctx, argument):
    amount = argument[:-1]
    unit = argument[-1]

    if amount.isdigit() and unit in ['s', 'm', 'h', 'd', 'w' 'y']:
      return (int(amount), unit)
    
    raise commands.BadArgument(message='Not a valid duration')

class TimeConverter2(commands.Converter):
    
    async def convert(self, ctx, *, time: str):
        arser = _parse_time(time) # returns datetime.timedelta object
        human_time = _human_time(parser)
        return parser, human_time

def mods_or_owner():
    """
    Check that the user has the correct role to execute a command
    """
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(MODERATOR_ROLE_NAME))
    return commands.check(predicate)

async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)


def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format(
                'Y' if v.isupper() else 'y', v))

    return text

class Timer:
    def __init__(self):
        self._start = None
        self._end = None

    def start(self):
        self._start = time.perf_counter()

    def stop(self):
        self._end = time.perf_counter()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def __int__(self):
        return round(self.time)

    def __float__(self):
        return self.time

    def __str__(self):
        return str(self.time)

    def __repr__(self):
        return f"<Timer time={self.time}>"

    @property
    def time(self):
        if self._end is None:
            raise ValueError("Timer has not been ended.")
        return self._end - self._start
"""
with Timer() as timer:
  # do stuff that takes time here
  print("hello")
print(f"That took {timer} seconds to do") 
"""

time_regex = re.compile(r"(\d{1,5}(?:[.,]?\d{1,5})?)([smhd])")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        matches = time_regex.findall(argument.lower())
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
            except ValueError:
                raise commands.BadArgument("{} is not a number!".format(v))
        return time

def FutureTime_converter(time):
    since = time
    seconds = ("s", "sec", "secs", 'second', "seconds")
    minutes = ("m", "min", "mins", "minute", "minutes")
    hours = ("h", "hour", "hours")
    days = ("d", "day", "days")
    weeks = ("w", "week", "weeks")
    rawsince = since

    try:
        temp = re.compile("([0-9]+)([a-zA-Z]+)")
        res = temp.match(since).groups()
        time = int(res[0])
        since = res[1]

    except ValueError:
        return
        
    if since.lower() in seconds:
        timewait = time
    elif since.lower() in minutes:
        timewait = time * 60
    elif since.lower() in hours:
        timewait = time * 3600
    elif since.lower() in days:
        timewait = time * 86400
    elif since.lower() in weeks:
        timewait = time * 604800

    return timewait

class Banner(discord.Asset): # This is our banner class. The only reason for this to add a `.color` and a `.url`.
    def __init__(self, state, url, banner_color):
        super().__init__(state, url)
        self.color = banner_color

    @property
    def url(self):
        if self._url is None:
            return None
            
        return self.BASE + self._url

async def fetch_banner(self, user: typing.Union[Member, User], *, format: str = None, size: int = 512):
    user_id: int = user.id
    usr: dict = await self.http.get_user(user_id) # Call the API to get banner hash.
    state = user._state # The sole reason for this is only for the Asset.
    
    banner_hash: typing.Union[str, None] = usr.get('banner') # Tries to get banner hash
    banner_color: typing.Union[int, None] = usr.get('accent_color') # Tries to get banner colour

    url = None
    if banner_hash:
        def get_format(): # Tries to get the banner format
            if banner_hash.startswith('a_'): # Check if the banner is animated
                return 'gif' # Returns the format as gif.
                
            return (format or 'png') # Returns format arg or png.

        fmt = get_format() # Get the format

        url = f'/banners/{user_id}/{banner_hash}.{fmt}?size={size}' # Generate the URL.

    return Banner(state, url, banner_color) # Return our custom Banner class.

"""
```You can use it like: ```py
>>> banner = await fetch_banner(Member/User)
>>> banner.color
<Banner Color>/None
>>> banner.url
<Banner URL>/None
```
"""