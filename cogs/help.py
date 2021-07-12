import discord
#import json
import asyncio
import re
#import os
from discord.ext import commands
from discord_components import *
#Embed = discord.Embed()

class Help(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.client)
        print('Help')

    @commands.command()
    async def help(self, ctx):

        embedhelp = discord.Embed(title="✧ LATTE Help",description="Prefix of this bot `lt `\nUse `selection` below for more info on an command. \n\u200b",color=0xdfa3ff)
        embedhelp.add_field(name='Utility', value="•")
        embedhelp.add_field(name='Infomation', value="•")
        embedhelp.add_field(name='Moderation', value="•")
        embedhelp.add_field(name='Fun', value="•")
        embedhelp.add_field(name='Game', value="•")
        embedhelp.add_field(name='Meta', value="•")
        embedhelp.add_field(name='Automation', value="•")
        embedhelp.add_field(name='** **', value="**Support**\n[Invite Bot](https://discord.com/api/oauth2/authorize?client_id=854134402954821643&permissions=8&scope=bot%20applications.commands) | [Support Server](https://discord.gg/eNK44ngRvn) | [Github](https://github.com/staciax)", inline=False)
      
        msg = await ctx.send(embed=embedhelp,
        components=
        [Select(placeholder="Select a catogory",
                            options=[
                                SelectOption(
                                    label="Utility",
                                    value="test1.2",
                                    description="Utility Commands",
                                    emoji=self.client.get_emoji(859399025841537064)
                                ),
                                SelectOption(
                                    label="Infomation",
                                    value="test2.2",
                                    description="Infomation commands",
                                    emoji="😘"
                                ),
                                SelectOption(
                                    label="Moderation",
                                    value="test3.2",
                                    description="Moderation commands",
                                    emoji="😚"
                                ),
                                SelectOption(
                                    label="Fun",
                                    value="test4.2",
                                    description="Fun commands",
                                    emoji="😚"
                                ),
                                SelectOption(
                                    label="Game",
                                    value="test5.2",
                                    description="Game commands",
                                    emoji="😚"
                                ),
                                SelectOption(
                                    label="Meta",
                                    value="test6.2",
                                    description="Game commands",
                                    emoji="😚"
                                ),
                                SelectOption(
                                    label="Automation",
                                    value="test7.2",
                                    description="Reaction roles",
                                    emoji="😚"
                                ),

                            ])]
                            )
                           
        embed1 = discord.Embed(title="Utility commands",description="Utility Commands\n\n`coming soon..`",color=0xdfa3ff)    

        embed2 = discord.Embed(title="Infomation Commands",description="Infomation Commands\n\n`userinfo [targer] :` show userinfo infomation\n\n`serverinfo :` show server infomation\n\n`avatar [targer]:` show user avatar profile",color=0xdfa3ff)
        
        embed3 = discord.Embed(title="Moderation Commands",description="Moderation Commands\n\n`clear [number]:` clear message\n\n`mute [target] :` mute member\n\n`unmute [target] :` unmute member\n\n`kick [target]:` kick member\n\n`ban [target]:` ban member\n\n`unban [target]:`unban member",color=0xdfa3ff)
        
        embed4 = discord.Embed(title="Fun Commands",description="Fun Commands\n\n`coming soon..`",color=0xdfa3ff)
        
        embed5 = discord.Embed(title="Game Commands",description="Game Commands\n\n`coming soon..`",color=0xdfa3ff)
        
        embed6 = discord.Embed(title="Meta Commands",description="Meta Commands\n\n`ping : check ping , respondtime of bot`\n\n`invite :` invite the bot!!\n\n`support :` Get the invite link for the support server!\n\n`vote :`  Get the voting link for the bot",color=0xdfa3ff)
        
        embed7 = discord.Embed(title="Automation",description="Reaction Roles\nฺ\n`coming soon..`",color=0xdfa3ff)


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

                elif label == "Automation":
                    await msg.edit(embed=embed7)
                    await event.respond(                        
                        type=7
                    )

            except discord.NotFound:
                print("error.") 

def setup(client):
    client.add_cog(Help(client))