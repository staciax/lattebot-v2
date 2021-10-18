# Standard 
import discord
import json
import os
import datetime
import random
import asyncio
import re
import io
import sys
from discord.ext import commands, tasks
from datetime import datetime, timedelta, timezone

# Third party 
import motor.motor_asyncio
from pathlib import Path

# Local
from config import *
import utils.json_loader
from utils.mongo import Document

#cwd
cwd = Path(__file__).parents[0]
cwd = str(cwd)
# print(f"{cwd}\n-----")

#json_secret_file
secrets = utils.json_loader.read_json("secrets")
owner = secrets["owner"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(f'{PREFIX}'), case_insensitive=True, intents=intents, owner_id=owner , help_command=None)

bot.tester = ''

@bot.event
async def on_ready():
    bot_activity = "with my friends ♡ ₊˚"
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name=bot_activity)
    )
    print(f"\nName : {bot.user}\nActivity : {bot_activity}\nServer : {len(bot.guilds)}\nMembers : {len(set(bot.get_all_members()))}\nPrefix : {PREFIX}")
    print(f"\nCogs list\n-----")
    
@bot.event
async def on_disconnect():
    print("bot disconnected")

#json_loader
bot.config_token = secrets["token"]
bot.connection_url = secrets["mongo"]
bot.giphy_api_ = secrets["giphy"]

#jishaku
bot.load_extension('jishaku')

#latte_bot
bot.prefixes = {PREFIX}
bot.latte_version = BOTVERSION
bot.latte_source = LATTESOURCE
bot.invite_url = f'https://discord.com/api/oauth2/authorize?client_id=861179952576856065&permissions=8&scope=applications.commands%20bot'
bot.github = "https://github.com/staciax"
bot.top_gg = "-"
bot.bots_gg = "-"
bot.blacklist = {}
bot.latte_server_id = 840379510704046151
bot.latte_latte = "jhK46N6QWU"

#latte_private_voice
bot.underworldx = [873677543453126676, 873679362082369546]
bot.moonlightx = [875037193196945409, 875038018736644166]
bot.deathx = [883025077610876958, 883059509810040884]
bot.angelx = [873696566165250099, 883027485455941712]

# a = [100,200]
# print(a[0])
#cogs_and_mongodb
if __name__ == "__main__":

    if not bot.tester or len(bot.tester) == 0:
        bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(bot.connection_url))

        #db_main
        bot.db = bot.mongo["latteonly"]
        bot.sleepdb = Document(bot.db, "sleeping")
        bot.tagdb = Document(bot.db, "tags")

        #db_testing
        bot.db2 = bot.mongo["lattebot"]
        bot.latency_bot = Document(bot.db2, "latency")

        #db_leveling
        bot.db_level = bot.mongo["discord"]
        bot.latte_level = Document(bot.db_level, "levelling")

    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(bot.config_token)