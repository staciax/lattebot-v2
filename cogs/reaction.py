# Standard 
import discord
from discord.ext import commands

# Third party
# Local
from config import *
import utils

class Reaction(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        ColourID = COLOR
        VerifyID = VERIFY
        MatchaID = VERIFYMATCHA

        member = payload.member
        guild = member.guild
        emoji = str(payload.emoji.id)

        if ColourID == payload.message_id:

            if emoji == '861130565804621835':
                role = discord.utils.get(guild.roles, name="⠀ latte ੭")
            if emoji == '861128977828806686':
                role = discord.utils.get(guild.roles, name="⠀ coco ੭")
            if emoji == '861128979418447942':
                role = discord.utils.get(guild.roles, name="⠀ lemon ੭")
            if emoji == '861128977410293761':
                role = discord.utils.get(guild.roles, name="⠀ peach ੭")
            if emoji == '861128978902024192':
                role = discord.utils.get(guild.roles, name="⠀ bubblegum ੭")
            if emoji == '861128979309133844':
                role = discord.utils.get(guild.roles, name="⠀ lavender ੭")
            if emoji == '861128977603231765':
                role = discord.utils.get(guild.roles, name="⠀ blue sky ੭")
            if emoji == '861128979313328128':
                role = discord.utils.get(guild.roles, name="⠀ mint ੭")
        
            await member.add_roles(role)

        if VerifyID == payload.message_id:

            if emoji == '861800747293212672':
                role = discord.utils.get(guild.roles, name="Vanilla・・ ✦")
                role2 = discord.utils.get(guild.roles, name="・┈・┈・┈・Level!・┈・┈・┈・⠀⠀")

            await member.add_roles(role , role2)

        """ MATCHA SERVER """

        if MatchaID == payload.message_id:
            if emoji == '873028548724670555':
                role = discord.utils.get(guild.roles, name="♡ ~ 𝙈𝘼𝙄𝘿𝙀𝙉 ~♡")
            if emoji == '873029782592446464':
                role = discord.utils.get(guild.roles, name="✭ : 𝘽𝙐𝙏𝙇𝙀𝙍 : ✭")
            
            await member.add_roles(role)
            

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        ColourID = COLOR
        VerifyID = VERIFY
        MatchaID = VERIFYMATCHA

        guild = await(self.client.fetch_guild(payload.guild_id))
        emoji = str(payload.emoji.id)
        member = await(guild.fetch_member(payload.user_id))

        if ColourID == payload.message_id:

            if emoji == '861130565804621835':
                role = discord.utils.get(guild.roles, name="⠀ latte ੭")
            if emoji == '861128977828806686':
                role = discord.utils.get(guild.roles, name="⠀ coco ੭")
            if emoji == '861128979418447942':
                role = discord.utils.get(guild.roles, name="⠀ lemon ੭")
            if emoji == '861128977410293761':
                role = discord.utils.get(guild.roles, name="⠀ peach ੭")
            if emoji == '861128978902024192':
                role = discord.utils.get(guild.roles, name="⠀ bubblegum ੭")
            if emoji == '861128979309133844':
                role = discord.utils.get(guild.roles, name="⠀ lavender ੭")
            if emoji == '861128977603231765':
                role = discord.utils.get(guild.roles, name="⠀ blue sky ੭")
            if emoji == '861128979313328128':
                role = discord.utils.get(guild.roles, name="⠀ mint ੭") 

            if member is not None:
                await member.remove_roles(role)
            else:
                print("Member Not Fount")
    
        if VerifyID == payload.message_id:
            guild = await(self.client.fetch_guild(payload.guild_id))
            emoji = str(payload.emoji.id)

            if emoji == '861800747293212672':
                role = discord.utils.get(guild.roles, name="Vanilla・・ ✦")
                role2 = discord.utils.get(guild.roles, name="・┈・┈・┈・Level!・┈・┈・┈・⠀⠀")
                
            if member is not None:
                await member.remove_roles(role , role2)
            else:
                print("Member Not Fount")
        
        """ MATCHA SERVER """

        if MatchaID == payload.message_id:
            if emoji == '873028548724670555':
                role = discord.utils.get(guild.roles, name="♡ ~ 𝙈𝘼𝙄𝘿𝙀𝙉 ~♡")
            if emoji == '873029782592446464':
                role = discord.utils.get(guild.roles, name="✭ : 𝘽𝙐𝙏𝙇𝙀𝙍 : ✭")
            
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Member Not Fount")

    @commands.command(description='add emoji in message')
    async def ar(self, ctx, msg_id: int = None, channel: discord.TextChannel = None, emote=None):
        if not msg_id:
            channel = self.client.get_channel(f'{channel}') 
        elif not channel:
            channel = ctx.channel
        msg = await channel.fetch_message(msg_id)
        await ctx.message.delete()
        await msg.add_reaction(emote)

    @ar.error
    async def ar_error(self, ctx, error):
        await ctx.send("pls try again! | `ar` `msg_id` `ch_id` `emoji` ")
        await ctx.message.delete()
        
def setup(client):
    client.add_cog(Reaction(client))