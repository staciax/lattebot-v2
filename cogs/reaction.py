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
        MatchaColor = MATCHA_COLOR

        member = payload.member
        guild = member.guild
        emoji = str(payload.emoji.id)

        #latte_color
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

            role_lvl = discord.utils.get(guild.roles, id = 854506876674244608) #name="・ ──────꒰ ・ colors ・ ꒱────── ・")

            await member.add_roles(role)
        
        #latte_verify
        if VerifyID == payload.message_id:
            if emoji == '861800747293212672':    
                role = discord.utils.get(guild.roles, id = 842309176104976387) #name="Vanilla・・ ✦")
                role2 = discord.utils.get(guild.roles, id = 854503426977038338) #name="・ ───────꒰ ・ ♡ ・ ꒱─────── ・")
                role3 = discord.utils.get(guild.roles, id = 854503041775566879) #name="・ ──────꒰ ・ levels ・ ꒱────── ・")

            await member.add_roles(role , role2 , role3)

        """ MATCHA SERVER """
        if MatchaColor == payload.message_id:
            emoji = str(payload.emoji.name)
            if emoji == '🍓':
                role = discord.utils.get(guild.roles, id=837729400241520640)
            elif emoji == '🍊':
                role = discord.utils.get(guild.roles, id=837729404548284487)
            elif emoji == '🍌':
                role = discord.utils.get(guild.roles, id=837729407643811861)
            elif emoji == '🍏':
                role = discord.utils.get(guild.roles, id=837729411272540211)
            elif emoji == '🖤':
                role = discord.utils.get(guild.roles, id=837729413259984906)
            elif emoji == '🥶':
                role = discord.utils.get(guild.roles, id=837729413826347120)
            elif emoji == '🍇':
                role = discord.utils.get(guild.roles, id=837729414099894273)
            elif emoji == '☁️':
                role = discord.utils.get(guild.roles, id=837729506226864180)
            elif emoji == '🌺':
                role = discord.utils.get(guild.roles, id=837729508378935326)
            elif emoji == '🌸':
                role = discord.utils.get(guild.roles, id=854262148062511135)
            elif emoji == '🌊':
                role = discord.utils.get(guild.roles, id=854261956408246323)
            elif emoji == '🥤':
                role = discord.utils.get(guild.roles, id=854316816805527553) 

            await member.add_roles(role)

        if MatchaID == payload.message_id:
            if emoji == '873028548724670555':
                role = discord.utils.get(guild.roles, id = 735500646882607156) #name="♡ ~ 𝙈𝘼𝙄𝘿𝙀𝙉 ~♡")
            if emoji == '873029782592446464':
                role = discord.utils.get(guild.roles, id = 858186876494151716) # name="✭ : 𝘽𝙐𝙏𝙇𝙀𝙍 : ✭")
            
            await member.add_roles(role)
            

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        ColourID = COLOR
        VerifyID = VERIFY
        MatchaID = VERIFYMATCHA
        MatchaColor = MATCHA_COLOR

        guild = await(self.client.fetch_guild(payload.guild_id))
        emoji = str(payload.emoji.id)
        member = await(guild.fetch_member(payload.user_id))

        #latte_color
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

            role_lvl = discord.utils.get(guild.roles, id = 854506876674244608) #name="・ ──────꒰ ・ colors ・ ꒱────── ・")

            if member is not None:
                await member.remove_roles(role , role_lvl)
            else:
                print("Member Not Fount")

        #latte_verify
        if VerifyID == payload.message_id:
            if emoji == '861800747293212672':    
                role = discord.utils.get(guild.roles, id = 842309176104976387)#name="Vanilla・・ ✦")
                role2 = discord.utils.get(guild.roles, id = 854503426977038338) #name="・ ───────꒰ ・ ♡ ・ ꒱─────── ・")
                role3 = discord.utils.get(guild.roles, id = 854503041775566879) #name="・ ──────꒰ ・ levels ・ ꒱────── ・")
                
            if member is not None:
                await member.remove_roles(role , role2 , role3)
            else:
                print("Member Not Fount")
        
        """ MATCHA SERVER """
        
        if MatchaColor == payload.message_id:
            emoji = str(payload.emoji.name)
            if emoji == '🍓':
                role = discord.utils.get(guild.roles, id=837729400241520640)
            elif emoji == '🍊':
                role = discord.utils.get(guild.roles, id=837729404548284487)
            elif emoji == '🍌':
                role = discord.utils.get(guild.roles, id=837729407643811861)
            elif emoji == '🍏':
                role = discord.utils.get(guild.roles, id=837729411272540211)
            elif emoji == '🖤':
                role = discord.utils.get(guild.roles, id=837729413259984906)
            elif emoji == '🥶':
                role = discord.utils.get(guild.roles, id=837729413826347120)
            elif emoji == '🍇':
                role = discord.utils.get(guild.roles, id=837729414099894273)
            elif emoji == '☁️':
                role = discord.utils.get(guild.roles, id=837729506226864180)
            elif emoji == '🌺':
                role = discord.utils.get(guild.roles, id=837729508378935326)
            elif emoji == '🌸':
                role = discord.utils.get(guild.roles, id=854262148062511135)
            elif emoji == '🌊':
                role = discord.utils.get(guild.roles, id=854261956408246323)
            elif emoji == '🥤':
                role = discord.utils.get(guild.roles, id=854316816805527553) 

            if member is not None:
                await member.remove_roles(role)
            else:
                print("Member Not Fount")

        if MatchaID == payload.message_id:
            if emoji == '873028548724670555':
                role = discord.utils.get(guild.roles, id = 735500646882607156) #name="♡ ~ 𝙈𝘼𝙄𝘿𝙀𝙉 ~♡")
            if emoji == '873029782592446464':
                role = discord.utils.get(guild.roles, id = 858186876494151716) # name="✭ : 𝘽𝙐𝙏𝙇𝙀𝙍 : ✭")
            
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Member Not Fount")

    @commands.command(description='add emoji in message')
    @commands.guild_only()
    async def ar(self, ctx, msg_id: int = None, channel: discord.TextChannel = None, emote=None):
        if not msg_id:
            channel = self.client.get_channel(f'{channel}') 
        elif not channel:
            channel = ctx.channel
        msg = await channel.fetch_message(msg_id)
        await ctx.message.delete()
        await msg.add_reaction(emote)

#    @ar.error
#    async def ar_error(self, ctx, error):
#        await ctx.send("pls try again! | `ar` `msg_id` `ch_id` `emoji` ")
#        await ctx.message.delete()
        
def setup(client):
    client.add_cog(Reaction(client))