import discord, re, random
from discord.ext import commands
from discord.http import Route

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
          user = ctx.client.get_user(user) or await ctx.bot.fetch_user(user)

    if user == None:
      tag = re.match(r"#?(\d{4})",argument)
      if tag:
        test=discord.utils.get(ctx.bot.users, discriminator = tag.group(1))
        user = test or ctx.author
    return user