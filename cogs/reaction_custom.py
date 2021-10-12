# Standard 
import discord
from discord.ext import commands

# Third party
import aiofiles

# Local
from config import *
import utils

class Reaction_custom(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.reaction_roles = []

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        async with aiofiles.open("bot_config/reaction_roles.txt", mode="a") as temp:
            pass
        
        async with aiofiles.open("bot_config/reaction_roles.txt", mode="r") as file:
            lines = await file.readlines()
            for line in lines:
                data = line.split(" ")
                self.reaction_roles.append((int(data[0]), int(data[1]), data[2].strip("\n")))

    @commands.command(name="rc")
    @commands.has_permissions(administrator=True)
    async def set_reaction(self, ctx, role: discord.Role=None, msg: discord.Message=None, emoji=None):
        if role != None and msg != None and emoji != None:
            await msg.add_reaction(emoji)
            self.reaction_roles.append((role.id, msg.id, str(emoji.encode("utf-8"))))
        
            async with aiofiles.open("bot_config/reaction_roles.txt", mode="a") as file:
                emoji_utf = emoji.encode("utf-8")
                await file.write(f"{role.id} {msg.id} {emoji_utf}\n")

            await ctx.channel.send("Reaction has been set.")
        
        else:
            await ctx.send("Invalid arguments.")
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        for role_id, msg_id, emoji in self.reaction_roles:
            if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
                await payload.member.add_roles(self.bot.get_guild(payload.guild_id).get_role(role_id))
                return

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        for role_id, msg_id, emoji in self.reaction_roles:
            if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
                guild = self.bot.get_guild(payload.guild_id)
                await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))
                return
    
def setup(bot):
    bot.add_cog(Reaction_custom(bot))