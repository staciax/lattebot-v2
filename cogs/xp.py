# Standard 
import discord , random , asyncio
from discord.ext import commands 
from datetime import datetime, timedelta, timezone

intents = discord.Intents.default()
intents.members = True

# Third party
import pymongo 
from pymongo import MongoClient
from PIL import Image, ImageDraw , ImageFont , ImageEnhance , ImageFilter
from io import BytesIO
import numpy
import requests

# Local
import utils
from config import * 

#xpchannel
bot_channel = BOT_CH
chat_channel = CHAT_CH

#mongodb
mango_url = MONGOURL
level = LVLROLE #level role
levelnum = LVLNUM #level number
colorlvl = LVLROLECOLOR #level role color
cluster = MongoClient(mango_url)
levelling = cluster[MGDATABASE][MGDOCUMENT]

class xp(commands.Cog):

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
                else:
                    xp = stats["xp"] + 5
                    levelling.update_one({"id":message.author.id}, {"$set":{"xp":xp}})
                    lvl = 0 
                    while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        emlvup = discord.Embed(title="LEVEL UP!", description=f"Congratulations, {message.author.mention} you leveled up to **level {lvl}.**!",color=0xFF8C00)
                        await message.channel.send(embed=emlvup)
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(title="ROLE UPDATE!",description=f"{message.author.mention} **LEVEL UP!** you have gotten role **{level[i]}**!!!",color=0xffffff)
                                embed.set_thumbnail(url=message.author.avatar.url)
                                await message.channel.send(embed=embed)
                 
    @commands.command()
    async def testlevel(self, ctx):
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
                embed = discord.Embed(title="{}'s level stats".format(ctx.author.name))
                embed.add_field(name="Name" , value=ctx.author.mention , inline=True)
                embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                embed.add_field(name="XP", value=str(lvl), inline=True)
                embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                embed.add_field(name="Progress bar [lvl]", value=boxes * "<a:Aqua_panic:864932442191560735>" + (20-boxes) * ":white_large_square:", inline=False)
                await ctx.channel.send(embed=embed)

    @commands.command(aliases=['rank', 'ranking'])
    async def leaderboard(self, ctx): #only one ch use '==' , more use 'in'
#        if (ctx.channel.id in bot_channel):
            rankings = levelling.find().sort("xp",-1)
            i = 1
            embed = discord.Embed(color=0x77dd77 , timestamp=datetime.now(timezone.utc))
            embed.set_footer(text = f'{ctx.guild.name}', icon_url=ctx.guild.icon.url)
            embed.set_author(name=f"{self.client.user.name} Rankings", url=self.client.user.avatar.url) #, icon_url=ctx.guild.icon.url
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
#            embedbot = discord.Embed(title="BOT COMMAND ERROR",description=f"please use bot command in <#861874852050894868> !",color=0xffffff)
#            await ctx.message.delete()
#            await ctx.channel.send(embed=embedbot , delete_after=10)

    @commands.command(aliases=['lv', 'lvl' , 'xp' , 'exp'])
    async def level(self, ctx):
#        if ctx.channel.id in bot_channel:       
                stats = levelling.find({"id": ctx.author.id} , {"guild_id" : ctx.guild.id})
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

                    background = Image.open('data/images/level.png')
                    url = ctx.author.avatar.url
                    response = requests.get(url)
                    logo = Image.open(BytesIO(response.content)).resize((300, 300))
                    whitecc =  Image.new("RGB", (310, 310), (119, 221, 119))
                    bigsize = (logo.size[0] * 3, logo.size[1] * 3)
                    mask = Image.new("L", bigsize, 0)

                    draw = ImageDraw.Draw(mask)
                    draw.ellipse((0, 0) + bigsize, 255)

                    #draw.ellipse((140 * 3, 140 * 3, 189 * 3, 189 * 3), 0)

                    mask = mask.resize(logo.size, Image.ANTIALIAS )
                    logo.putalpha(mask)

                    bigsize = (whitecc.size[0] * 3, whitecc.size[1] * 3)
                    draw.ellipse((0, 0) + bigsize, 255)

                    mask = mask.resize(whitecc.size, Image.ANTIALIAS )
                    whitecc.putalpha(mask)

                    background.paste(whitecc, (35, 45), mask=whitecc)

                    background.paste(logo, (40, 50), mask=logo)

                    # # Black Circle
                    draw = ImageDraw.Draw(background)
                    # draw.ellipse((160, 160, 208, 208), fill="#000")

                    big_font = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 90)
                    big2_font = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 120)
                    medium_font = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 70)
                    small_font = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 50)

                    textrank = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 130)
                    ranksize = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 70)
                   
                    text_size = draw.textsize(str(lvl), font=big2_font)
                    offset_x = 510
                    offset_y = 220
                    draw.text((offset_x, offset_y), str(lvl), font=big2_font, fill="#77dd77")

                    text_size = draw.textsize("LEVEL", font=big_font)
                    offset_x -= text_size[0] + 5
                    levelx = 355
                    levely = 220
                    draw.text((levelx , levely + 27), "LEVEL", font=big_font, fill="#fff")

                    #rank

                    text_size = draw.textsize(f"#{rank}", font=textrank)
                    rank_x = 1250 - 15 - text_size[0]
                    rank_y = -10
                    draw.text((rank_x, rank_y), f"#{rank}", font=textrank, fill="#77dd77")

                    text_size = draw.textsize("RANK", font=big_font)
                    rank_x -= text_size[0] + 5
                    draw.text((rank_x, rank_y + 35), "RANK", font=big_font, fill="#fff")

                    bar_offset_x = 370
                    bar_offset_y = 340
                    bar_offset_x_1 = 1250
                    bar_offset_y_1 = 380
                    circle_size = bar_offset_y_1 - bar_offset_y  # Diameter

                    # Progress Bar
                    draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill="#727175")

                    # Left Circle
                    draw.ellipse(
                        (bar_offset_x - circle_size // 2, bar_offset_y, bar_offset_x + circle_size // 2, bar_offset_y_1), fill="#727175")                    

                    # Right Circle
                    draw.ellipse(
                        (bar_offset_x_1 - circle_size // 2, bar_offset_y, bar_offset_x_1 + circle_size // 2, bar_offset_y_1), fill="#727175")
                    
                    bar_length = bar_offset_x_1 - bar_offset_x
                    progress = (final_xp - xp) * 100 / final_xp
                    progress = 100 - progress
                    progress_bar_length = round(bar_length * progress / 100)
                    bar_offset_x_1 = bar_offset_x + progress_bar_length

                    # Progress Bar
                    draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill="#77dd77")

                    # Left Circle
                    draw.ellipse(
                        (bar_offset_x - circle_size // 2, bar_offset_y, bar_offset_x + circle_size // 2, bar_offset_y_1), fill="#77dd77")                    

                    # Right Circle
                    draw.ellipse(
                        (bar_offset_x_1 - circle_size // 2, bar_offset_y, bar_offset_x_1 + circle_size // 2, bar_offset_y_1), fill="#77dd77"
                    )

                    #final_exp 

                    text_size = draw.textsize(f"/ {int(200*((1/2)*lvl))} XP", font=medium_font)

                    offset_x = 1270 - text_size[0]
                    offset_y = bar_offset_y - text_size[1] - 10

                    draw.text((offset_x, offset_y), f"/ {int(200*((1/2)*lvl))} XP", font=medium_font, fill="#ffffff")

                    #exp
                    text_size = draw.textsize(f"{xp}", font=medium_font)
                    offset_x -= text_size[0] + 8
                    draw.text((offset_x, offset_y), f"{xp}", font=medium_font, fill="#fff")


                    # Blitting Name
                    #text_size = draw.textsize(ctx.author.name, font=big_font)

                    #offset_x = bar_offset_x
                    #offset_y = bar_offset_y - text_size[1] - 5
                    #draw.text((offset_x , offset_y -240 ), ctx.author.name, font=big_font, fill="#fff")

                    # Discriminator
                    #offset_x += text_size[0] + 5
                    #offset_y += 15

                    #draw.text((offset_x , offset_y -240 ), f"#{ctx.author.discriminator}", font=medium_font, fill="#77dd77")

                    buffer = BytesIO()
                    background.save(buffer, 'png')
                    buffer.seek(0)
                    file=discord.File(fp=buffer, filename='latte-level.png')

                    embedlv = discord.Embed(title="{}'s level stats".format(ctx.author.name),color=0x77dd77)
                    embedlv.set_image(url="attachment://latte-level.png")

                    await ctx.channel.send(file=file, embed=embedlv)

#        else:
#            embedbot = discord.Embed(title="BOT COMMAND ERROR",description=f"please use bot command in <#861874852050894868> !",color=0xffffff)
#            await ctx.message.delete()
#            await ctx.channel.send(embed=embedbot , delete_after=10)
  
    @commands.command()
    async def xprole(self, ctx):
        embed = discord.Embed(description="", color=PTYELLOW)
        embed.title = "XP ROLE!"
        lvlbar = "・┈・┈・┈・Level!・┈・┈・┈・⠀⠀"
        lvlbar2 = discord.utils.get(ctx.author.guild.roles, name=lvlbar)
        if not lvlbar2:
            await ctx.guild.create_role(name=lvlbar , colour=0x18191c)
        embed.description += f"{lvlbar2.mention}\n"
        
        for x, y in zip(reversed(level), reversed(colorlvl)):
            checkrole = discord.utils.get(ctx.author.guild.roles, name=level)
            if not checkrole:
                await ctx.guild.create_role(name=x , colour=y)
            else:
                return

        for i in reversed(range(len(level))):
            roles = discord.utils.get(ctx.author.guild.roles, name=level[i])
            if roles:
                embed.description += f"{roles.mention}\n"

        await ctx.channel.send(embed=embed)

    

    
def setup(client):

    client.add_cog(xp(client))