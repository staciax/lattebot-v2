import discord
from discord.ext import commands
from discord import Embed


def set_channel_embed(ctx):
    embed = Embed(title="Set channel", color=0xffffff)

    embed.add_field(name="\u200b" , value="**WELCOME**" , inline=False)
    embed.add_field(name="welcome channel" , value="```lt welcome set [channel]```" , inline=False)
    embed.add_field(name="Delete welcome channel" , value="```lt welcome delete```" , inline=False)

    embed.add_field(name="\u200b" , value="\u200b**LEAVE**" , inline=False)
    embed.add_field(name="leave channel" , value="```lt leave set [channel]```" , inline=False)
    embed.add_field(name="Delete leave channel" , value="```lt leave delete```" , inline=False)
    
    return embed