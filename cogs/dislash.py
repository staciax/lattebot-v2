import discord
from discord.ext import commands

from dislash import *
from config import *
import utils

class Dislash(commands.Cog):

    def __init__(self, client):
        self.client = client
        InteractionClient(self.client)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @user_command(name='Avatar' , guild_ids=[840379510704046151])
    async def avatar_msg(self, inter):
        embed = discord.Embed(color=WHITE)
        embed.set_image(url=inter.user.avatar.url)
        await inter.respond(embed=embed)
           
#slash_commands
#user_commands
#message_commands


def setup(client):
    client.add_cog(Dislash(client))