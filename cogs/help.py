import discord
import json
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

        embedhelp = discord.Embed(title="✧ LATTE Help",description="Prefix of this bot `lt `\nUse `lt help [category]` for more info on an command or a category.")
        
        embedhelp.add_field(name='** **', value="•Moderation\n•Game")
        embedhelp.add_field(name='** **', value="•Infomation\n•Botinfo")
        embedhelp.add_field(name='** **', value="•Fun\n•Utility")
        embedhelp.add_field(name='** **', value="**Support**\n[**Invite Bot**](https://discord.com/api/oauth2/authorize?client_id=854134402954821643&permissions=8&scope=bot%20applications.commands) | [Support Server](https://discord.gg/eNK44ngRvn) | [Developer](https://www.facebook.com/nathanan.xx/)", inline=False)

        
        msg = await ctx.send(embed=embedhelp,
        components=
        [Select(placeholder="Select help catogory",
                            options=[
                                SelectOption(
                                    label="test1",
                                    value="test1.2",
                                    description="test1.3",
                                    emoji=self.client.get_emoji(859399025841537064)
                                ),
                                SelectOption(
                                    label="test2",
                                    value="test2.2",
                                    description="test2.3",
                                    emoji="😘"
                                ),
                                SelectOption(
                                    label="test3",
                                    value="test3.2",
                                    description="test3.3",
                                    emoji="😚"
                                ),

                            ])]
                            )
                           
        embed1 = discord.Embed(title="✧ LATTE Help",description="test1")
        embed2 = discord.Embed(title="test2",description="test2")
        embed3 = discord.Embed(title="test3",description="test3")

        while True:
            try:
                event = await self.client.wait_for("select_option", check=None)

                label = event.component[0].label

                if label == "test1":
                    await event.respond(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=True,
                        embed=embed1
                    )

                elif label == "test2":
                    await event.respond(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=True,
                        embed=embed2
                    )
          
                elif label == "test3":
                    await event.respond(
                        type=InteractionType.ChannelMessageWithSource,
                        ephemeral=True,
                        embed=embed3
                    )

            except discord.NotFound:
                print("error.")


def setup(client):
    client.add_cog(Help(client))