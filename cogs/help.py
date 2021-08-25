# Standard 
import discord , asyncio , re #import json #import os
from datetime import datetime, timedelta, timezone
from discord.ext import commands
from discord import Embed

# Third party
#from discord_components import *

# Local
import utils
from config import *

emojis = utils.emoji_converter

class Help(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        #DiscordComponents(self.client)
        print(f"-{self.__class__.__name__}")
    
    @commands.command()
    @commands.guild_only()
    async def help2(self, ctx):

        embedhelp = discord.Embed(title="✧ LATTE Help", description="Prefix of this bot `lt ` or `l ` and `.` \nUse `selection` below for more info on an command. \n",color=0xffffff)
        embedhelp.add_field(name='** **', value=f"•{emojis('shidapout')} **Utility**\n•{emojis('winkai')} **Giveaway**\n•{emojis('chocolawow')} **Reaction Roles**")
        embedhelp.add_field(name='** **', value=f"•{emojis('ShinoSmirk')} **Infomation**\n•{emojis('wowanime')} **Fun**\n•{emojis('ClevelandDeal')} **Leveling**")
        embedhelp.add_field(name='** **', value=f"•{emojis('lutoaraka')} **Moderation**\n•{emojis('Ani1')} **Meta**\n•{emojis('tohka')} **NSFW**")

#        fields = [(f"•{emojis('shidapout')} **Utility**", "`-some useful commands`" , True),
#                (f"•{emojis('ShinoSmirk')} **Infomation**", "`-infomation commands`", True),
#                (f"•{emojis('lutoaraka')} **Moderation**", "`-keep your server safe`", True),
#                (f"•{emojis('winkai')} **Giveaway**", "`-giveaway for you server`", True),
#                (f"•{emojis('wowanime')} **Fun**", "`-have a good laugh with member `", True),
#                (f"•{emojis('Ani1')} **Meta**", "`-bot infomation`", True),
#                (f"•{emojis('chocolawow')} **Reaction Roles**", "`-let member pick roles`", True),
#                (f"•{emojis('ClevelandDeal')} **Leveling**", "`-reward members for talking`", True),
#                (f"•{emojis('tohka')} **NSFW**", "`-test`", True)]
                
#        for name, value, inline in fields:
#            embedhelp.add_field(name=name, value=value, inline=inline)
        embedhelp.add_field(name='** **', value=f"**Support**\n {INVITELINK} | {SUPPORT_SERVER} | {GITHUB_DEV}", inline=False)
        lastup = datetime(UYEAR, UMONTH, UDATE)
        dt = lastup.strftime("%d %B %Y") #%A,
        embedhelp.set_footer(text=f"Recently Updated • {dt}")
#        embedhelp.set_thumbnail(url=self.client.user.avatar.url)
        embedhelp.set_image(url="https://i.imgur.com/3jz8m3V.png")
      
        msg = await ctx.send(embed=embedhelp,
        components=[
                Select(placeholder="Select a catogory",
                            options=[
                                SelectOption(
                                    label="Utility",
                                    value="test1.2",
                                    description="Utility Commands",
                                    emoji=self.client.get_emoji(867683219733348363)
                                ),
                                SelectOption(
                                    label="Infomation",
                                    value="test2.2",
                                    description="Infomation commands",
                                    emoji=self.client.get_emoji(867686091501994004)
                                ),
                                SelectOption(
                                    label="Moderation",
                                    value="test3.2",
                                    description="Moderation commands",
                                    emoji=self.client.get_emoji(867683214298054696)
                                ),
                                SelectOption(
                                    label="Giveaway",
                                    value="test4.2",
                                    description="Giveaway commands",
                                    emoji=self.client.get_emoji(867701465983615006)
                                ),
                                SelectOption(
                                    label="Fun",
                                    value="test5.2",
                                    description="Fun commands",
                                    emoji=self.client.get_emoji(867701428998635522) #""
                                ),
                                SelectOption(
                                    label="Meta",
                                    value="test6.2",
                                    description="Game commands",
                                    emoji=self.client.get_emoji(867705949933666324)
                                ),
                                SelectOption(
                                    label="Reaction",
                                    value="test7.2",
                                    description="Reaction roles",
                                    emoji=self.client.get_emoji(867704973865254922)
                                ),
                                SelectOption(
                                    label="Leveling",
                                    value="test8.2",
                                    description="Leveling",
                                    emoji=self.client.get_emoji(867693328560947200)
                                ),
                                SelectOption(
                                    label="NSFW",
                                    value="test9.2",
                                    description="NSFW",
                                    emoji=self.client.get_emoji(867707490379628564)
                                ),
                                SelectOption(
                                    label="Help",
                                    value="test10.2",
                                    description="back to main page",
                                    emoji=self.client.get_emoji(864921120226279504)
                                ),
                            ])]
                            )
                           
        embed1 = discord.Embed(title="Utility commands",description="Utility Commands\n\n`coming soon..`",color=0xffffff)
        embed1.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

        embed2 = discord.Embed(title="Infomation Commands",description="Infomation Commands\n\n`userinfo , ui [targer] :` show userinfo infomation\n\n`serverinfo , sv :` show server infomation\n\n`avatar , av [targer] :` show user avatar profile",color=0xffffff)
        embed2.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

        embed3 = discord.Embed(title="Moderation Commands",description="Moderation Commands\n\n`clear [number] or all :` clear message\n\n`muterole :` create muterole\n\n`mute [target] :` mute member\n\n`unmute [target] :` unmute member\n\n`kick [target]:` kick member\n\n`ban [target]:` ban member\n\n`unban [target]:`unban member\n\n`lockdown :`disable text channel\n\n`changenick [member]:` change nickname member\n\n`slowmode [seconds]:` set slowmode in channel",color=0xffffff)
        embed2.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

        embed4 = discord.Embed(title="Giveaway Commands",description="Giveaway Commands\n\n`giveaway , g :` The group command for managing giveaways\n\n`reroll :` reroll giveaway",color=0xffffff)
        embed4.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

        embed5 = discord.Embed(title="Fun Commands",description="Fun Commands\n\n`bm [message]:` Let the bot send the message\n\n`poll [message]:` poll in your server",color=0xffffff)
        embed5.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

        embed6 = discord.Embed(title="Meta Commands",description="Meta Commands\n\n`ping :` check latency bot\n\n`stats :` show stats bot\n\n`invite :` invite the bot!!\n\n`feedback` : send message to bot developer\n\n`support :` Get the invite link for the support server!\n\n`vote :`  Get the voting link for the bot",color=0xffffff)
        embed6.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
        
        embed7 = discord.Embed(title="Reaction",description="Reaction Roles\n\nGive color role: <#840380566862823425>",color=0xffffff)
        embed7.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

        embed8 = discord.Embed(title="Leveling",description="Leveling Commands\nways you can get experience\ntalk in <#861883647070437386> <#840398821544296480> <#859960606761549835> \n\n`xp [target]:` check my level\n\n`rank :` show ranking level all member",color=0xffffff)
        embed8.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

        embed9 = discord.Embed(title="NSFW",description="NSFW Commands\n\n`coming soon..`",color=0xffffff)
        embed9.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)

        while True:
            try:
                event = await self.client.wait_for("select_option")
                label = event.component[0].label

                if label == "Utility":
                    await event.respond(
                        type=7,
                        embed=embed1
                    )

                elif label == "Infomation":
                    await event.respond(
                        type=7,
                        embed=embed2                    
                    )
          
                elif label == "Moderation":
                    await event.respond(                        
                        type=7,
                        embed=embed3
                    )
                
                elif label == "Giveaway":
                    await event.respond(                        
                        type=7,
                        embed=embed4
                    )
                
                elif label == "Fun":
                    await event.respond(                        
                        type=7,
                        embed=embed5
                    )

                elif label == "Meta":
                    await event.respond(                        
                        type=7,
                        embed=embed6
                    )

                elif label == "Reaction":
                    await event.respond(                        
                        type=7,
                        embed=embed7
                    )
                
                elif label == "Leveling":
                    await event.respond(                        
                        type=7,
                        embed=embed8
                    )
                elif label == "NSFW":
                    await event.respond(                        
                        type=7,
                        embed=embed9
                    )

                elif label == "Help":
                    await event.respond(                        
                        type=7,
                        embed=embedhelp
                    )

            except discord.NotFound:
                print("error.")  

def setup(client):
    client.add_cog(Help(client))