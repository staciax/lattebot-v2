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

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command(name="help" , aliases=["latte"] , brief=f"{PREFIX}help", usage=f"{PREFIX}help")
    @commands.guild_only()
    async def custom_help(self, ctx, command=None):
        embedhelp = discord.Embed(title="✧ LATTE Help", description=f"Use {PREFIX}help <category> for more informations about a category.\n",color=0xffffff)
        fields = [(f"•{emojis('miraishocked')} **Anime**", f"`{PREFIX}help anime`" , True),
                (f"•📷 **Image**", f"`{PREFIX}help image`" , True),
                (f"•{emojis('shidapout')} **Utility**", f"`{PREFIX}help util`" , True),
                (f"•{emojis('ShinoSmirk')} **Infomation**", f"`{PREFIX}help info`", True),
#                   (f"•{emojis('lutoaraka')} **Moderation**", "`lt help mod`", True),
#                   (f"•{emojis('winkai')} **Giveaway**", "`lt help gw`", True),
                (f"•{emojis('wowanime')} **Fun**", f"`{PREFIX}help fun`", True),
                (f"•{emojis('Ani1')} **Meta**", f"`{PREFIX}help meta`", True),
                (f"•{emojis('chocolawow')} **Reaction Roles**", f"`{PREFIX}help rr`", True),
                (f"•{emojis('ClevelandDeal')} **Leveling**", f"`{PREFIX}help level`", True),
                (f"•{emojis('tohka')} **NSFW**", f"`{PREFIX}help nsfw`", True)]
           
        for name, value, inline in fields:
            embedhelp.add_field(name=name, value=value, inline=inline)

        if ctx.author.guild_permissions.administrator: #if ctx.channel.id == 844462710526836756:
            embedhelp.add_field(name=f"•{emojis('winkai')} **Giveaway**", value=f"`{PREFIX}help gw`", inline=True)
            embedhelp.add_field(name=f"•{emojis('lutoaraka')} **Moderation**", value=f"`{PREFIX}help mod`", inline=True)
        else:
            embedhelp.add_field(name="⠀", value="⠀", inline=True)
            embedhelp.add_field(name="⠀", value="⠀", inline=True)

        lastup = datetime(UYEAR, UMONTH, UDATE)
        dt = lastup.strftime("%d %B %Y") #%A,
        embedhelp.set_footer(text=f"Recently Updated • {dt}")
        embedhelp.set_image(url="https://i.imgur.com/3jz8m3V.png")

        if command is None:
            await ctx.send(embed=embedhelp)
        elif command == "anime":
            await ctx.send(embed=utils.Anime(ctx))
        elif command == "image":
            await ctx.send(embed=utils.Help_image(ctx))
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
#            print(f'Command: {command.name}\nBrief: {command.brief}')
            
            helpEmbed.title = command.name
            helpEmbed.description = command.description
            helpEmbed.description = f"{command.description}"
            
            helpEmbed.add_field (
                name = "Usage",
                value = f"```{command.usage}```",
                inline=False
                
            )

            if command.brief:
                helpEmbed.add_field (
                    name = "Example",
                    value = f"```{command.brief}```",
                    inline=False
                )

            if command.aliases:
                str_ali = ", ".join(command.aliases)
                helpEmbed.add_field (
                name = "Aliases",
                value = f"```{str_ali}```",
                inline=False
            )

            helpEmbed.set_footer(
                text="<> Required argument | [] Optional argument", 
                icon_url=self.bot.user.avatar.url
            )

            await ctx.send(embed = helpEmbed)
            
def setup(bot):
    bot.add_cog(Help_support(bot))