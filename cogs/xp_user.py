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
from dislash import *

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

class XP_user(commands.Cog):

    def __init__(self, client):
        self.client = client
        InterClient = InteractionClient(self.client)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @user_command(name='XP' , guild_ids=[840379510704046151])
    async def level(self, inter):
        member = inter.user
        member_id = inter.user.id 
        stats = levelling.find_one({"id": member_id})
        if stats is None:
            embed = discord.Embed(description="You haven't sent any messages, **no xp**!!",color=0xffffff)
            await inter.respond(embed=embed)
        else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                    if xp < ((50*(lvl**2))+(50*lvl)):
                        break
                    lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                rankings = levelling.find().sort("xp",-1)
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                final_xp = (200*((1/2)*lvl))
                
                embedlv = discord.Embed(title=f"{member.name}'s level stats | {inter.guild.name}",color=0x77dd77)
                embedlv.set_image(url="attachment://latte-level.png")

                await inter.channel.send(file=utils.level_images(member, final_xp, lvl, rank, xp) , embed=embedlv)


    
def setup(client):

    client.add_cog(XP_user(client))