import discord, re, random
from discord.ext import commands
#from discord.http import Route

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

    if amount.isdigit() and unit in ['s', 'm']:
      return (int(amount), unit)
    
    raise commands.BadArgument(message='Not a valid duration')