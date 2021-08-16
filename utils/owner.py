import discord

from discord.ext import commands

def owner_bot():
    def pred(ctx):
        owner_ids = [385049730222129152, 240059262297047041]
        if ctx.author.id in owner_ids:
            return True
        return False
    return commands.check(pred)