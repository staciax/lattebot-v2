# Standard 
import discord #import json #import os
import asyncio
import re
from discord.ext import commands

# Third party
from discord_components import *

# Local


class Help(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.client)
        print(f"-{self.__class__.__name__}")

    @commands.command()
    async def help(self, ctx):

        embedhelp = discord.Embed(title="✧ LATTE Help", description="Prefix of this bot `lt `\nUse `selection` below for more info on an command. \n",color=0xffffff)
#        embedhelp.add_field(name='** **', value="•**Utility**\n•**Fun**\n•**reaction**")
#        embedhelp.add_field(name='** **', value="•**Infomation**\n•**Game**")
#        embedhelp.add_field(name='** **', value="•**Moderation**\n•**Meta**")

        fields = [("'Utility", "`-`" , True),
                ("Infomation", "`-`", True),
                ("Moderation", "`-`", True),
                ("Fun", "`-`", True),
                ("Game", "`-`", True),
                ("Meta", "`-`", True),
                ("Reaction", "`-`", True),
                ("Leveling", "`-`", True)]
                
        for name, value, inline in fields:
            embedhelp.add_field(name=name, value=value, inline=inline)
        embedhelp.add_field(name='** **', value="**Support**\n[Invite Bot](https://discord.com/api/oauth2/authorize?client_id=861179952576856065&permissions=8&scope=bot%20applications.commands) | [Support Server](https://discord.gg/eNK44ngRvn) | [Github](https://github.com/staciax)", inline=False)
        embedhelp.set_thumbnail(url=self.client.user.avatar.url)
      
        msg = await ctx.send(embed=embedhelp,
        components=
        [Select(placeholder="Select a catogory",
                            options=[
                                SelectOption(
                                    label="Utility",
                                    value="test1.2",
                                    description="Utility Commands",
                                    emoji=self.client.get_emoji(864930911869992980)
                                ),
                                SelectOption(
                                    label="Infomation",
                                    value="test2.2",
                                    description="Infomation commands",
                                    emoji=self.client.get_emoji(864921120468369438)
                                ),
                                SelectOption(
                                    label="Moderation",
                                    value="test3.2",
                                    description="Moderation commands",
                                    emoji=self.client.get_emoji(864921119873695774)
                                ),
                                SelectOption(
                                    label="Fun",
                                    value="test4.2",
                                    description="Fun commands",
                                    emoji=self.client.get_emoji(864921119072059463)
                                ),
                                SelectOption(
                                    label="Game",
                                    value="test5.2",
                                    description="Game commands",
                                    emoji=self.client.get_emoji(864921121319944212) #""
                                ),
                                SelectOption(
                                    label="Meta",
                                    value="test6.2",
                                    description="Game commands",
                                    emoji=self.client.get_emoji(864921118296506418)
                                ),
                                SelectOption(
                                    label="Reaction",
                                    value="test7.2",
                                    description="Reaction roles",
                                    emoji=self.client.get_emoji(864921120226279504)
                                ),
                                SelectOption(
                                    label="Leveling",
                                    value="test7.3",
                                    description="Leveling",
                                    emoji=self.client.get_emoji(864921120226279504)
                                ),
                                SelectOption(
                                    label="Help",
                                    value="test8.3",
                                    description="Help",
                                    emoji=self.client.get_emoji(864921120226279504)
                                ),

                            ])]
                            )
                           
        embed1 = discord.Embed(title="Utility commands",description="Utility Commands\n\n`coming soon..`",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name} Stats", icon_url=ctx.author.avatar.url)

        embed2 = discord.Embed(title="Infomation Commands",description="Infomation Commands\n\n`userinfo [targer] :` show userinfo infomation\n\n`serverinfo :` show server infomation\n\n`avatar [targer]:` show user avatar profile",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name} Stats", icon_url=ctx.author.avatar.url)

        embed3 = discord.Embed(title="Moderation Commands",description="Moderation Commands\n\n`clear [number]:` clear message\n\n`mute [target] :` mute member\n\n`unmute [target] :` unmute member\n\n`kick [target]:` kick member\n\n`ban [target]:` ban member\n\n`unban [target]:`unban member",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name} Stats", icon_url=ctx.author.avatar.url)

        embed4 = discord.Embed(title="Fun Commands",description="Fun Commands\n\n`coming soon..`",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name} Stats", icon_url=ctx.author.avatar.url)

        embed5 = discord.Embed(title="Game Commands",description="Game Commands\n\n`coming soon..`",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name} Stats", icon_url=ctx.author.avatar.url)

        embed6 = discord.Embed(title="Meta Commands",description="Meta Commands\n\n`ping : check ping , respondtime of bot`\n\n`invite :` invite the bot!!\n\n`support :` Get the invite link for the support server!\n\n`vote :`  Get the voting link for the bot",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name} Stats", icon_url=ctx.author.avatar.url)
        
        embed7 = discord.Embed(title="Reaction",description="Reaction Roles\n\n`coming soon..`",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name} Stats", icon_url=ctx.author.avatar.url)

        embed8 = discord.Embed(title="Leveling",description="Leveling Commands\n\n`coming soon..`",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name} Stats", icon_url=ctx.author.avatar.url)

        while True:
            try:

                event = await self.client.wait_for("select_option", check=None)

                label = event.component[0].label

                if label == "Utility":
                    await msg.edit(embed=embed1)
                    await event.respond(
                        type=7
                    )

                elif label == "Infomation":
                    await msg.edit(embed=embed2)
                    await event.respond(
                        type=7                        
                    )
          
                elif label == "Moderation":
                    await msg.edit(embed=embed3)
                    await event.respond(                        
                        type=7
                    )
                
                elif label == "Fun":
                    await msg.edit(embed=embed4)
                    await event.respond(                        
                        type=7
                    )
                
                elif label == "Game":
                    await msg.edit(embed=embed5)
                    await event.respond(                        
                        type=7
                    )

                elif label == "Meta":
                    await msg.edit(embed=embed6)
                    await event.respond(                        
                        type=7
                    )

                elif label == "Reaction":
                    await msg.edit(embed=embed7)
                    await event.respond(                        
                        type=7
                    )
                
                elif label == "Leveling":
                    await msg.edit(embed=embed8)
                    await event.respond(                        
                        type=7
                    )

                elif label == "Help":
                    await msg.edit(embed=embedhelp)
                    await event.respond(                        
                        type=7
                    )

            except discord.NotFound:
                print("error.") 

def setup(client):
    client.add_cog(Help(client))