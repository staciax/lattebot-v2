# Standard 
import discord , asyncio , re #import json #import os
from datetime import datetime, timedelta, timezone
from discord.ext import commands #, menus

# Third party

# Local
import utils
from config import *

emojis = utils.emoji_converter

class Help_support(commands.Cog): 

    def __init__(self, client):
        self.client = client
        self.bot = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command(name="help" , aliases=["latte"])
    @commands.guild_only()
    async def custom_help(self, ctx, command=None):
        embedhelp = discord.Embed(title="✧ LATTE Help", description="Prefix of this bot `.` or `lt ` or `l `\nUse `commands` below for more info on an command. \n",color=0xffffff)
        fields = [(f"•{emojis('shidapout')} **Utility**", "`.help util`" , True),
                (f"•{emojis('ShinoSmirk')} **Infomation**", "`.help info`", True),
#                   (f"•{emojis('lutoaraka')} **Moderation**", "`lt help mod`", True),
#                   (f"•{emojis('winkai')} **Giveaway**", "`lt help gw`", True),
                (f"•{emojis('wowanime')} **Fun**", "`.help fun`", True),
                (f"•{emojis('Ani1')} **Meta**", "`.help meta`", True),
                (f"•{emojis('chocolawow')} **Reaction Roles**", "`.help rr`", True),
                (f"•{emojis('ClevelandDeal')} **Leveling**", "`.help level`", True),
                (f"•{emojis('tohka')} **NSFW**", "`.help nsfw`", True)]
        
            
        for name, value, inline in fields:
            embedhelp.add_field(name=name, value=value, inline=inline)

        if ctx.author.guild_permissions.administrator: #if ctx.channel.id == 844462710526836756:
            embedhelp.add_field(name=f"•{emojis('winkai')} **Giveaway**", value="`.help gw`", inline=True)
            embedhelp.add_field(name=f"•{emojis('lutoaraka')} **Moderation**", value="`.help mod`", inline=True)
        else:
            embedhelp.add_field(name="⠀", value="⠀", inline=True)
            embedhelp.add_field(name="⠀", value="⠀", inline=True)

        lastup = datetime(UYEAR, UMONTH, UDATE)
        dt = lastup.strftime("%d %B %Y") #%A,
        embedhelp.set_footer(text=f"Recently Updated • {dt}")
        embedhelp.set_image(url="https://i.imgur.com/3jz8m3V.png")

        if command is None:
            await ctx.send(embed=embedhelp)
        elif command == "util":
            await ctx.send(embed=utils.Utility(ctx))
        elif command == "info":
            await ctx.send(embed=utils.Infomation(ctx))
        elif command == "mod":
            if ctx.author.guild_permissions.administrator:
                await ctx.send(embed=utils.Moderation(ctx))
        elif command == "gw":
            if ctx.author.guild_permissions.administrator:
                await ctx.send(embed=utils.Giveaway(ctx))
        elif command == "fun":
            await ctx.send(embed=utils.Fun(ctx))
        elif command == "meta":
            await ctx.send(embed=utils.Meta(ctx))
        elif command == "rr":
            await ctx.send(embed=utils.Reaction(ctx))
        elif command == "level":
            await ctx.send(embed=utils.Leveling(ctx))
        elif command == "nsfw":
            await ctx.send(embed=utils.NSFW(ctx))#, delete_after=300)
        else:
            helpEmbed = discord.Embed (
                color = 0xffffff
            )
        
            command = self.bot.get_command(name = command)
            print(f'Command: {command.name}\nBrief: {command.brief}')
            print('Adding field')
            
            helpEmbed.title = command.name
            helpEmbed.description = command.description
            helpEmbed.description = f"{command.description}"
            helpEmbed.add_field (name = "Usage",
                value = f"```{command.usage}```"
            )
            helpEmbed.add_field (
                name = "Example",
                value = f"```{command.brief}```",
                inline=False
            )
            helpEmbed.set_footer(
                text="<> Required argument | [] Optional argument", 
                icon_url=self.bot.user.avatar.url
            )

            await ctx.send(embed = helpEmbed)
            
    """
    @commands.command(brief = 'test', description = 'test2')
    async def helphelp(self, ctx, command = None):
        await ctx.message.delete()
        #await ctx.send(self.bot.Cogs)
        
        if command is None:
            helpEmbed = discord.Embed (
                title = 'Help',
                color = 0xffffff,
            )

            for command_ in self.bot.commands:
                helpEmbed.add_field (
                name = command_,
                value = command_.brief,
                )
            
            await ctx.send(embed = helpEmbed)
        
        else:
            helpEmbed = discord.Embed (
                title = command,
                color = 0xffffff
            )
        
            command = self.bot.get_command(name = command)
            print(f'Command: {command.name}\nBrief: {command.brief}')
            print('Adding field')
            
            helpEmbed.add_field (
                name = command.name,
                value = command.description
            )
            
            await ctx.send(embed = helpEmbed)
        """


def setup(client):
    client.add_cog(Help_support(client))