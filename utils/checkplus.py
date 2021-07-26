import discord, re, random
from discord.ext import commands

def is_me():
    def predicate(ctx):
        return ctx.message.author.id == 385049730222129152
    return commands.check(predicate)

def is_guild_owner(): #@commands.check(is_owner)
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]