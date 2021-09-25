# Standard 
import discord , asyncio , re #import json #import os
from datetime import datetime, timedelta, timezone
from discord.ext import commands #, menus

# Third party

# Local
import utils
from config import *

emojis = utils.emoji_converter

class Help_selection(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Anime', description='Anime gif and picture', emoji=f"{emojis('miraishocked')}"),
            discord.SelectOption(label='Image', description='Image commands', emoji=f"{emojis('image')}"),
            discord.SelectOption(label='Utility', description='Some useful commands', emoji='⚙️'),
            discord.SelectOption(label='Infomation', description='All informative commands', emoji=f'{emojis("ShinoSmirk")}'),
            discord.SelectOption(label='Fun', description='Fun commands', emoji='🥳'),
            discord.SelectOption(label='Misc', description='Miscellaneous commands', emoji=f'{emojis("Ani1")}'),
            discord.SelectOption(label='Reaction roles', description='Self assignable roles', emoji=f'{emojis("chocolawow")}'),
            discord.SelectOption(label='Leveling', description='Leveling system', emoji=f'{emojis("ClevelandDeal")}'),
            discord.SelectOption(label='NSFW', description='NSFW commands', emoji=F'{emojis("Aoba")}'),
            discord.SelectOption(label='Tag', description='Tag commands', emoji=F'{emojis("amelia")}')
        ]

        super().__init__(placeholder='Select a category...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Anime": return await interaction.response.edit_message(embed=utils.Anime())
        elif self.values[0] == "Image": return await interaction.response.edit_message(embed=utils.Help_image())
        elif self.values[0] == "Utility": return await interaction.response.edit_message(embed=utils.Utility())
        elif self.values[0] == "Infomation": return await interaction.response.edit_message(embed=utils.Infomation())
        elif self.values[0] == "Fun": return await interaction.response.edit_message(embed=utils.Fun())
        elif self.values[0] == "Misc": return await interaction.response.edit_message(embed=utils.Meta())
        elif self.values[0] == "Reaction roles": return await interaction.response.edit_message(embed=utils.Reaction())
        elif self.values[0] == "Leveling": return await interaction.response.edit_message(embed=utils.Leveling())
        elif self.values[0] == "NSFW": return await interaction.response.edit_message(embed=utils.NSFW())
        elif self.values[0] == "Tag": return await interaction.response.edit_message(embed=utils.Help_tag())

class Admin_selection(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Giveaway', description='Create giveaway', emoji='🎉'),
            discord.SelectOption(label='Moderation', description='Moderation commands', emoji=f'{emojis("moderation")}')
        ]

        super().__init__(placeholder='Admin selection.', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Giveaway": return await interaction.response.edit_message(embed=utils.Giveaway())
        elif self.values[0] == "Moderation": return await interaction.response.edit_message(embed=utils.Moderation())

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command(name="help" , aliases=["latte"] , brief=f"{PREFIX}help", usage=f"{PREFIX}help")
    @commands.guild_only()
    async def custom_help(self, ctx, command=None):
        embedhelp = discord.Embed(title="✧ LATTE Help", description=f"Use **Selection** for more informations about a category.\n",color=0xffffff)
        
        embedhelp.add_field(name='** **', value=f"•{emojis('miraishocked')} Anime\n•{emojis('ShinoSmirk')} Infomation\n•{emojis('chocolawow')} Reaction Roles\n•{emojis('amelia')} Tag command")
        embedhelp.add_field(name='** **', value=f"•<:image:889841860183461918> Image\n•🥳 Fun\n•{emojis('ClevelandDeal')} Leveling")
        embedhelp.add_field(name='** **', value=f"•⚙️ Utility\n•{emojis('Ani1')} Misc\n•{emojis('Aoba')} NSFW")

        #if ctx.author.guild_permissions.administrator:
        if ctx.channel.id == LATTE_TEST_BOT:
            embedhelp.add_field(name='** **', value=f"•🎉 Giveaway\n•{emojis('moderation')} Moderation")
        #    embedhelp.add_field(name=f"•🎉 **Giveaway**", value=f"`{PREFIX}help gw`", inline=True)
        #    embedhelp.add_field(name=f"•{emojis('moderation')} **Moderation**", value=f"`{PREFIX}help mod`", inline=True)

        lastup = datetime(UYEAR, UMONTH, UDATE)
        dt = lastup.strftime("%d %B %Y") #%A,
        embedhelp.set_footer(text=f"{BOTVERSION} Recently updated • {dt}", icon_url=self.bot.user.avatar.url)
        embedhelp.set_image(url="https://i.imgur.com/3jz8m3V.png")

        #start_selection_view
        view = discord.ui.View(timeout=300)
        view.add_item(Help_selection())

        #button_view
        #style = discord.ButtonStyle.gray
        #source_button = discord.ui.Button(style=style, label="Source code", url="https://github.com/staciax/Latte-bot-v2-dpy-v2.0.0a" , emoji="<:github:889792131852546088>")
        #view.add_item(item=source_button)

        #for_admin
        if ctx.channel.id == LATTE_TEST_BOT:
            view.add_item(Admin_selection())
        
        if command is None:
            await ctx.send(embed=embedhelp, view=view)
        elif command == "anime":
            await ctx.send(embed=utils.Anime(), view=view)
        elif command == "image":
            await ctx.send(embed=utils.Help_image(), view=view)
        elif command in ["util","utils","utility"]:
            await ctx.send(embed=utils.Utility(), view=view)
        elif command in ["info","infomation","infomations"]:
            await ctx.send(embed=utils.Infomation(), view=view)
        elif command in ["mod","moderation"]:
            if ctx.author.guild_permissions.administrator:
                await ctx.send(embed=utils.Moderation(), view=view)
        elif command in ["gw","giveaway"]:
            if ctx.author.guild_permissions.administrator:
                await ctx.send(embed=utils.Giveaway(), view=view)
        elif command == "fun":
            await ctx.send(embed=utils.Fun(), view=view)
        elif command == "misc":
            await ctx.send(embed=utils.Meta(), view=view)
        elif command == ["rr","reaction","reaction role","reaction roles"]:
            await ctx.send(embed=utils.Reaction(), view=view)
        elif command == "level":
            await ctx.send(embed=utils.Leveling(), view=view)
        elif command == "nsfw":
            await ctx.send(embed=utils.NSFW(), view=view)
        elif command == "tag":
            await ctx.send(embed=utils.Help_tag(), view=view)
        else:
            helpEmbed = discord.Embed (
                color = 0xffffff
            )
        
            command = self.bot.get_command(name = command)
            
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

    #backup

    """
    class Test_selection(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.select(custom_id="squad_play_status", placeholder="Select a category.",
                        min_values=1, max_values=1,
                        options=[discord.SelectOption(label='Anime', value="Anime1",  description='Anime gif and picture', emoji='🟥'),
                                discord.SelectOption(label='Image', value="Image",description='Image commands', emoji='<:image:889841860183461918>'),
                                discord.SelectOption(label='Utility', value="Utility",description='Some useful commands', emoji='⚙️'),
                                discord.SelectOption(label='Infomation', value="Infomation",description='Display infomation', emoji='🟦'),
                                discord.SelectOption(label='Fun', value="Fun",description='Fun commands', emoji='🟦'),
                                discord.SelectOption(label='Misc', value="Misc",description='Setup , config and various other command', emoji='🟦'),
                                discord.SelectOption(label='Reaction roles', value="Reaction",description='Reaction Roles', emoji='🟦'),
                                discord.SelectOption(label='Leveling', value="Leveling",description='Leveling system', emoji='🟦'),
                                discord.SelectOption(label='NSFW', value="NSFW",description='NSFW gif and picture', emoji='🟦')])
        async def signup_callback(self, select: discord.ui.select, interaction: discord.Interaction):
            print(self.values[0])
    """
    #fields = [(f"•{emojis('miraishocked')} **Anime**", f"`{PREFIX}help anime`" , True),
            #        (f"•📷 **Image**", f"`{PREFIX}help image`" , True),
            #        (f"•{emojis('shidapout')} **Utility**", f"`{PREFIX}help util`" , True),
            #        (f"•{emojis('ShinoSmirk')} **Infomation**", f"`{PREFIX}help info`", True),
    #                   (f"•{emojis('lutoaraka')} **Moderation**", "`lt help mod`", True),
    #                   (f"•{emojis('winkai')} **Giveaway**", "`lt help gw`", True),
            #        (f"•{emojis('wowanime')} **Fun**", f"`{PREFIX}help fun`", True),
            #        (f"•{emojis('Ani1')} **Meta**", f"`{PREFIX}help meta`", True),
            #        (f"•{emojis('chocolawow')} **Reaction Roles**", f"`{PREFIX}help rr`", True),
            #        (f"•{emojis('ClevelandDeal')} **Leveling**", f"`{PREFIX}help level`", True),
            #        (f"•{emojis('tohka')} **NSFW**", f"`{PREFIX}help nsfw`", True)]
    #for name, value, inline in fields:
                #embedhelp.add_field(name=name, value=value, inline=inline)

    #elif command == "mod":
    #            if ctx.author.guild_permissions.administrator:
    #                await ctx.send(embed=utils.Moderation(ctx))
    #        elif command == "gw":
    #            if ctx.author.guild_permissions.administrator:
    #                await ctx.send(embed=utils.Giveaway(ctx))
            
def setup(bot):
    bot.add_cog(Help(bot))