from discord import Embed
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="testslash", guild_ids=[840379510704046151])
    async def testslash(self, ctx: SlashContext):
        embed = Embed(title="Embed Test")
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Slash(bot))