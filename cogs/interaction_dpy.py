# Standard 
import discord , asyncio
import datetime
from discord.ext import commands , tasks
#from discord.integrations import Integration
#from discord.ui import button, View, Button
from datetime import datetime, timezone , timedelta

# Third party

# Local
import utils

class interaction_dpy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
def setup(bot):
    bot.add_cog(interaction_dpy(bot))