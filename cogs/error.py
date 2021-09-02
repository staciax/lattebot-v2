# Standard 
import discord
from discord.ext import commands
from datetime import datetime, timezone
import asyncio

# Third party

# Local
import utils

class Error(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.direct = self.client.get_channel(874942964462391357)
        print(f"-{self.__class__.__name__}")
    
    @commands.Cog.listener()
    @commands.bot_has_permissions(send_messages=True)
    async def on_command_error(self , ctx, error):
        embed = discord.Embed(color=0xffffff)
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.CommandOnCooldown):
            cm_error = f"You are on cooldown, try again in {error.retry_after:.0f} seconds"
        elif isinstance(error, commands.MessageNotFound):
            cm_error = "I can't find that message!"
        elif isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound):
            cm_error = "I can't find that user!"
        elif isinstance(error, commands.ChannelNotFound):
            cm_error = "I can't find that channel!"
        elif isinstance(error, commands.ChannelNotReadable):
            cm_error = "I don't have acces to read anything in that channel!"
        elif isinstance(error, commands.RoleNotFound):
            cm_error = "I can't find that role!"
        elif isinstance(error, commands.EmojiNotFound):
            cm_error = "I can't find that emoji!"
        elif isinstance(error, commands.MissingPermissions):
            cm_error = f"You don't have **{str(error)[15:-35]}** **permission(s)** to run this command!"
        elif isinstance(error, commands.MissingRole):
            cm_error = f"You don't have **{error.missing_role}** role(s) to run this command!"
        elif isinstance(error, commands.MissingAnyRole):
            cm_error = f"You don't have **{error.missing_role}** role(s) to run this command!"
        elif isinstance(error, commands.MissingRequiredArgument):
            cm_error = "You didn't pass a required argument!"
        elif isinstance(error, commands.CheckFailure):
            print(f"check fail {ctx.author.name}")
        else:
#            print(error)
            cm_error = f"{error}"
        embed.add_field(name="Commands Error!", value=f"{cm_error}")
        await ctx.send(embed=embed, delete_after=15)
    
def setup(client):
    client.add_cog(Error(client))