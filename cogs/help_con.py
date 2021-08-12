# Standard 
import discord , asyncio , re #import json #import os
from datetime import datetime, timedelta, timezone
from discord.ext import commands

# Third party
from discord_components import *

# Local
import utils
from config import *

emojis = utils.emoji_converter

class Help_con(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.client)
        print(f"-{self.__class__.__name__}")
    
    @commands.command()
    @commands.guild_only()
    async def help(self, ctx, *, category=None):

        if category == None:
            embedhelp = discord.Embed(title="✧ LATTE Help", description="Prefix of this bot `lt ` or `l `\nUse `commands` below for more info on an command. \n",color=0xffffff)
            fields = [(f"•{emojis('shidapout')} **Utility**", "`-lt help util`" , True),
                    (f"•{emojis('ShinoSmirk')} **Infomation**", "`-lt help info`", True),
                    (f"•{emojis('lutoaraka')} **Moderation**", "`-lt help mod`", True),
                    (f"•{emojis('winkai')} **Giveaway**", "`-lt help gw`", True),
                    (f"•{emojis('wowanime')} **Fun**", "`-lt help fun`", True),
                    (f"•{emojis('Ani1')} **Meta**", "`-lt help meta`", True),
                    (f"•{emojis('chocolawow')} **Reaction Roles**", "`-lt help rr`", True),
                    (f"•{emojis('ClevelandDeal')} **Leveling**", "`-lt help level`", True),
                    (f"•{emojis('tohka')} **NSFW**", "`-lt help nsfw`", True)]
                
            for name, value, inline in fields:
                embedhelp.add_field(name=name, value=value, inline=inline)
            embedhelp.add_field(name='** **', value=f"**Support**\n {INVITELINK} | {SUPPORT_SERVER} | {GITHUB_DEV}", inline=False)
            lastup = datetime(UYEAR, UMONTH, UDATE)
            dt = lastup.strftime("%d %B %Y") #%A,
            embedhelp.set_footer(text=f"Recently Updated • {dt}")
            embedhelp.set_image(url="https://i.imgur.com/3jz8m3V.png")

            await ctx.send(embed=embedhelp)
        elif category == "util":
            await ctx.send(embed=utils.Utility(ctx) , delete_after=100)
        elif category == "info":
            await ctx.send(embed=utils.Infomation(ctx), delete_after=100)
        elif category == "mod":
            await ctx.send(embed=utils.Moderation(ctx), delete_after=100)
        elif category == "gw":
            await ctx.send(embed=utils.Giveaway(ctx), delete_after=100)
        elif category == "fun":
            await ctx.send(embed=utils.Fun(ctx), delete_after=100)
        elif category == "meta":
            await ctx.send(embed=utils.Meta(ctx), delete_after=100)
        elif category == "rr":
            await ctx.send(embed=utils.Reaction(ctx), delete_after=100)
        elif category == "level":
            await ctx.send(embed=utils.Leveling(ctx), delete_after=100)
        elif category == "nsfw":
            await ctx.send(embed=utils.NSFW(ctx), delete_after=100)
      
def setup(client):
    client.add_cog(Help_con(client))