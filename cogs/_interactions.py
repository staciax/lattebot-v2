from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name="testslash", guild_ids=[840379510704046151])
    async def testslash(self, ctx: SlashContext):
        embed = Embed(title="Embed Test")
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(Slash(client))