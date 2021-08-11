import discord, re, random
from discord.ext import commands
#from discord.http import Route
from datetime import datetime, timedelta, timezone
import time

from discord.ext.buttons import Paginator

class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass

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

class TimeConverter(commands.Converter):
    
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