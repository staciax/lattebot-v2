# Standard 
import discord , random , asyncio
from discord.ext import commands 
from datetime import datetime, timedelta, timezone

intents = discord.Intents.default()
intents.members = True

# Third party
import json
import pymongo 
from pymongo import MongoClient
from PIL import Image, ImageDraw , ImageFont , ImageEnhance , ImageFilter
from io import BytesIO
import requests

# Local
import json
import utils
from config import * 
from utils import Pag

#xpchannel
bot_channel = BOT_CH
chat_channel = CHAT_CH

#open_json
with open('bot_config/secrets.json') as f:
    data = json.load(f)

#mongodb
mango_url = data["mongo"]
level = LVLROLE #level role
levelnum = LVLNUM #level number
colorlvl = LVLROLECOLOR #level role color
cluster = MongoClient(mango_url)
levelling = cluster[MGDATABASE][MGDOCUMENT]

class XP(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in chat_channel: #only one ch use '==' , more use 'in'
            stats = levelling.find_one({"id" : message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id" : message.author.id, "xp" : 100}
                    levelling.insert_one(newuser)
                    guild = message.guild
                    lvl_bar = discord.utils.get(guild.roles, id = 854503041775566879)#・ ──────꒰ ・ levels ・ ꒱────── ・
                    await message.author.add_roles(lvl_bar)
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id":message.author.id}, {"$set":{"xp":xp}})
                    lvl = 0 
                    while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
#                    print(f'now level{lvl}')
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        emlvup = discord.Embed(description=f"**Congratulations**, {message.author.mention} you leveled up to **level {lvl}.**!",color=0xffffff)
                        msg = await message.channel.send(embed=emlvup)
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(description=f"**Congratulations**, {message.author.mention} you leveled up to **level {lvl}.**!\nyou have gotten role **{level[i]}**!!!",color=0xffffff)
#                                embed.set_thumbnail(url=message.author.avatar.url)
                                await msg.edit(embed=embed)
                 
    @commands.command(name="xp2")
    async def level_2(self, ctx):
        if ctx.channel.id in bot_channel: #only one ch use '==' , more use 'in'
            stats = levelling.find_one({"id": ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="You haven't sent any messages, **no xp**!!")
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < ((50*(lvl**2))+(50*lvl)):
                        break
                    lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                boxes = int((xp/(200*((1/2) * lvl)))*20)
                rankings = levelling.find().sort("xp",-1)
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                embed = discord.Embed(color=0xffffff)
#                embed.add_field(name="Name" , value=ctx.author.mention , inline=True)
                embed.set_author(name=f'{ctx.author.name}s level stats', icon_url=ctx.author.avatar.url)
                embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                embed.add_field(name="Level", value=str(lvl), inline=True)
                embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                embed.add_field(name="Progress bar [lvl]", value="<:start_full:876998828048416849>" + boxes * "<:mid_full:876998976774234183>" + (17-boxes) * "<:mid_empty:876998865734221865>" + "<:end_blank:876998841818292224>", inline=False)
                await ctx.channel.send(embed=embed)

    @commands.command(aliases=['rank', 'ranking'])
    @commands.guild_only()
    async def leaderboard(self, ctx): #only one ch use '==' , more use 'in'
#        if (ctx.channel.id in bot_channel):
            rankings = levelling.find().sort("xp",-1)
            i = 1
            embed = discord.Embed(color=0x77dd77 , timestamp=datetime.now(timezone.utc))
#           embed.set_author(name=f"{self.client.user.name} Rankings", url=self.client.user.avatar.url) #, icon_url=ctx.guild.icon.url            
            embed.set_author(name=f"{ctx.guild.name} Rankings", url=ctx.guild.icon.url , icon_url=ctx.guild.icon.url)
            embed.set_footer(text = f'{self.client.user.name}') # icon_url=self.client.user.avatar.url
#            for x in rankings:
#                try:
#                    temp = ctx.guild.get_member(x["id"])
#                    tempxp = x["xp"]       
#                    embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp} ", inline=False)
#                    i += 1
#                except:
#                    pass
#                if i == 11:
#                    break

            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]       
                    if i == 1:
                        embed.add_field(name=f"{i}: {temp.name} {utils.emoji_converter('1st')}", value=f"Total XP: {tempxp}", inline=False)
                    elif i == 2:
                        embed.add_field(name=f"{i}: {temp.name} {utils.emoji_converter('2nd')}", value=f"Total XP: {tempxp}", inline=False)
                    elif i == 3:
                        embed.add_field(name=f"{i}: {temp.name} {utils.emoji_converter('3rd')}", value=f"Total XP: {tempxp}", inline=False)
                    elif i == 4:
                        embed.add_field(name=f"{i}: {temp.name}  ", value=f"Total XP: {tempxp}", inline=False)
                    else:
                        embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
                except:
                    pass
                i += 1
                if i == 11:
                    break
       
            await ctx.channel.send(embed=embed)

#        else:
#            embedbot = discord.Embed(description=f"please use bot command in <#861874852050894868> !",color=0xffffff)
#            await ctx.message.delete()
#            await ctx.channel.send(embed=embedbot , delete_after=10)

    @commands.command(aliases=['lv', 'lvl' , 'xp' , 'exp'])
    @commands.guild_only()
    async def level(self, ctx, member: discord.Member = None): 
        async with ctx.typing():
                if not member:  # if member is no mentioned
                    member = ctx.message.author
                member_id = member.id
#        if ctx.channel.id in bot_channel:   
                stats = levelling.find_one({"id": member_id})
                if stats is None:
                    embed = discord.Embed(description="You haven't sent any messages, **no xp**!!",color=0xffffff)
                    await ctx.channel.send(embed=embed)
                else:
                    xp = stats["xp"]
                    lvl = 0
                    rank = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    boxes = int((xp/(200*((1/2) * lvl)))*20)
                    rankings = levelling.find().sort("xp",-1)
                    for x in rankings:
                        rank += 1
                        if stats["id"] == x["id"]:
                            break
                    final_xp = (200*((1/2)*lvl))

                    embedlv = discord.Embed(title=f"{member.name}'s level stats | {ctx.guild.name}",color=0x77dd77)
                    embedlv.set_image(url="attachment://latte-level.png")

                    await ctx.channel.send(file=utils.level_images(member, final_xp, lvl, rank, xp), embed=embedlv)
#        else:
#            embedbot = discord.Embed(title="BOT COMMAND ERROR",description=f"please use bot command in <#861874852050894868> !",color=0xffffff)
#            await ctx.message.delete()
#            await ctx.channel.send(embed=embedbot , delete_after=10)
  
    @commands.command()
    @commands.guild_only()
    async def xprole(self, ctx):
        embed = discord.Embed(description="", color=PTYELLOW)
        embed.title = "✧ LATTE XP ROLE!"
        lvlbar = "・┈・┈・┈・Level!・┈・┈・┈・⠀⠀"
        lvlbar2 = discord.utils.get(ctx.author.guild.roles, name=lvlbar)
        if not lvlbar2:
            await ctx.guild.create_role(name=lvlbar , colour=0x18191c)
            embed.description += f"{lvlbar.mention}\n"
            embed.description += f"{lvlbar2.mention}\n"
        
            for x, y in zip(reversed(level), reversed(colorlvl)):
                checkrole = discord.utils.get(ctx.author.guild.roles, name=level)
                if not checkrole:
                    await ctx.guild.create_role(name=x , colour=y)
                else:
                    return
        elif lvlbar2:
            for i in reversed(range(len(level))):
                roles = discord.utils.get(ctx.author.guild.roles, name=level[i])
                if roles:
                    embed.description += f"{roles.mention}\n"

            await ctx.channel.send(embed=embed)

    
def setup(client):

    client.add_cog(XP(client))