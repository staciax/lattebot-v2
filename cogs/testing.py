# Standard 
import discord , asyncio
from discord.ext import commands
from datetime import datetime, timezone

# Third party
#from discord_components import *
import utils

# Local

class Testing(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        #DiscordComponents(self.client)
        print(f"-{self.__class__.__name__}")

    @commands.command()
    async def embed(self, ctx):
        member = ctx.author
        utils.level_gif(member)
    
    @commands.command()
    async def select(self, ctx):
        embed = discord.Embed(description="TEST (v2.0.0a)")
        await ctx.send(
           "test",
            components=[
                Select(
                    placeholder="Test",
                    options=[
                        SelectOption(label="TEST1", value="1.1"),
                    ],            
                ),
            ],
        )
        while True:
            interaction = await self.client.wait_for("select_option")
            await interaction.respond(
                content=f"{','.join(map(lambda x: x.label, interaction.component))} selected!"
            )

def setup(client):
    client.add_cog(Testing(client))