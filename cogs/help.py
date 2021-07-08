import discord
import json
from discord.ext import commands
from discord_components import DiscordComponents, Button, Select, SelectOption

class Helptest(commands.Cog): #@commands.Cog.listener()  

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help')

    @commands.command()
    async def select(self, ctx):
        
        embed = discord.Embed(title="title")
        embednew = discord.Embed(title="title")

        msg = await ctx.send(embed=embed , components = [
                        Select(placeholder="select something!", options=[SelectOption(label="Page 1", value="A"), SelectOption(label="Page 2", value="B")])
                    ])

        interaction = await self.client.wait_for("select_option", check = lambda i: i.component[0].value == "A")

        await interaction.respond(interaction.component[0].label)

def setup(client):
    client.add_cog(Helptest(client))