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

intents = discord.Intents.all()

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
    
    @slash_command(name='xp' , description='show my exp' , guild_ids=[840379510704046151])
    async def xp_(self, inter):
        member = inter.author
        member_id = member.id 
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

    @slash_command(
        name="avatar",
        description="show my avatar",
        guild_ids=[840379510704046151],
        options=[
            Option("user", "recieving user", Type.USER, required=False),
        ],
    )
    async def avatar_slash(self, inter , user=None):
        if user is None:
            user = inter.author
        embed = discord.Embed(color=0xffffff)
        embed.title = f"{user.name}'s Avatar"
        embed.set_image(url=user.avatar.url)

        await inter.respond(embed=embed)
    
    @slash_command(
        name="embed",
        description="create embed",
        guild_ids=[840379510704046151],
        options=[
            Option("title", "recieving title", Type.STRING, required=False),
            Option("author", "recieving Author", Type.STRING, required=False),
            Option("author_url", "recieving Author url", Type.STRING, required=False),
            Option("description", "recieving description", Type.STRING, required=False),
            Option("color", "recieving color (HEX)", Type.STRING, required=False),
            Option("image", "recieving image link", Type.STRING, required=False),
            Option("thumnail", "recieving thumnail link", Type.STRING, required=False),
            Option("footer", "recieving footer", Type.STRING, required=False),
            Option("footer_url", "recieving footer icon url ", Type.STRING, required=False),
        ],
    )
    async def embed_slash(self, inter , title=None, author=None, author_url=None, description=None, color=None, image=None, thumnail=None, footer=None, footer_url=None):
        embed = discord.Embed()

        #title
        if title:
            embed.title = f"{title}"
        elif title is None:
            pass

        #author
        if author and author_url:
            embed.set_author(name=f"{author}" , icon_url=f"{author_url}")
        elif author:
            embed.set_author(name=f"{author}")
        else:
            pass
        
        #description
        if description:
            embed.description = f"{description}"
        elif description is None:
            pass
        
        #color
        if color:
            color_hex = int(f"{color}", 16)
            embed.color = color_hex
        elif color is None:
            pass

        #thumnail
        if thumnail:
            embed.set_thumbnail(url=f"{thumnail}")
        elif thumnail is None:
            pass

        #image
        if image:
            embed.set_image(url=f"{image}")
        elif image is None:
           pass

        #footer
        if footer and footer_url:
            embed.set_footer(text=f"{footer}" , icon_url=f"{footer_url}")
        elif footer:
            embed.set_footer(text=f"{footer}")
        else:
            pass

        await inter.channel.send(embed=embed)

def setup(client):

    client.add_cog(XP_user(client))