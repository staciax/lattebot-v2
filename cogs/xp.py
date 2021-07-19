# Standard 
import discord 
import asyncio
from discord.ext import commands 

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



mango_url = MONGOURL
bot_channel = 861874852050894868
chat_channels = 840396784299147315

level = ["Mystic","Vanilla","Matcha"]
levelnum = [5,10,15]

cluster = MongoClient(mango_url)

levelling = cluster["discord"]["levelling"]


class xp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.Cog.listener()
    async def on_message(self, message):
         if (message.channel.id == 861883647070437386):
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
                        await message.channel.send(f"well done {message.author.mention}! You leveled up to **level: {lvl}**!")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(description=f"{message.author.mention} You have gotten role **{level[i]}**!!!")
                                embed.set_thumbnail(url=message.author.avatar.url)
                                await message.channel.send(embed=embed)
    
    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.id == bot_channel:
            stats = levelling.find_one({"id": ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="You haven't sent any messages, no rank!!!")
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

    @commands.command()
    async def leaderboard(self, ctx):
        if (ctx.channel.id == bot_channel):
            rankings = levelling.find().sort("xp",-1)
            i = 1
            embed = discord.Embed(title="Rankings:")
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            
            await ctx.channel.send(embed=embed)

    @commands.command(aliases=['lv', 'lvl'])
    async def rank2(self, ctx):
       
                stats = levelling.find_one({"id": ctx.author.id})
                if stats is None:
                    embed = discord.Embed(description="You haven't sent any messages, no rank!!!")
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
                    whitecc =  Image.new("RGB", (320, 320), (255, 255, 255))
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

                    background.paste(whitecc, (30, 20), mask=whitecc)

                    background.paste(logo, (40, 30), mask=logo)

                    # # Black Circle
                    draw = ImageDraw.Draw(background)
                    # draw.ellipse((160, 160, 208, 208), fill="#000")

                    big_font = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 90)
                    big2_font = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 120)
                    medium_font = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 70)
                    small_font = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 50)

                    textrank = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 120)
                    ranksize = ImageFont.FreeTypeFont("data/fonts/Daisy.ttf", 70)
                   
                    text_size = draw.textsize(str(lvl), font=big2_font)
                    offset_x = 510
                    offset_y = 195
                    draw.text((offset_x, offset_y), str(lvl), font=big2_font, fill="#77dd77")

                    text_size = draw.textsize("LEVEL", font=big_font)
                    offset_x -= text_size[0] + 5
                    levelx = 360
                    levely = 195
                    draw.text((levelx , levely + 27), "LEVEL", font=big_font, fill="#fff")

                    #rank

                    text_size = draw.textsize(f"#{rank}", font=textrank)
                    rank_x = 1250 - 15 - text_size[0]
                    rank_y = -10
                    draw.text((rank_x, rank_y), f"#{rank}", font=textrank, fill="#77dd77")

                    text_size = draw.textsize("RANK", font=ranksize)
                    rank_x -= text_size[0] + 5
                    draw.text((rank_x, rank_y + 41), "RANK", font=medium_font, fill="#fff")

                    bar_offset_x = 370
                    bar_offset_y = 320
                    bar_offset_x_1 = 1250
                    bar_offset_y_1 = 360
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

                    offset_x = 1250 - text_size[0]
                    offset_y = bar_offset_y - text_size[1] - 10

                    draw.text((offset_x, offset_y), f"/ {int(200*((1/2)*lvl))} XP", font=medium_font, fill="#ffffff")

                    #exp
                    text_size = draw.textsize(f"{xp}", font=medium_font)
                    offset_x -= text_size[0] + 8
                    draw.text((offset_x, offset_y), f"{xp}", font=medium_font, fill="#fff")


                    # Blitting Name
                    text_size = draw.textsize(ctx.author.name, font=medium_font)

                    offset_x = bar_offset_x
                    offset_y = bar_offset_y - text_size[1] - 5
                    draw.text((offset_x , offset_y -240 ), ctx.author.name, font=medium_font, fill="#fff")

                    # Discriminator
                    offset_x += text_size[0] + 5
                    offset_y += 15

                    draw.text((offset_x , offset_y -240 ), f"#{ctx.author.discriminator}", font=small_font, fill="#77dd77")

                    buffer = BytesIO()
                    background.save(buffer, 'png')
                    buffer.seek(0)
                    await ctx.channel.send(file=discord.File(fp=buffer, filename='latte-level.png'))
    
def setup(client):
    client.add_cog(xp(client))