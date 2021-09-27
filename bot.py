# Standard 
import discord , json , os , datetime , random , asyncio , re , io , contextlib , logging , sys , logging , asyncpg
from discord.ext import commands, tasks
from datetime import datetime, timedelta, timezone

# Third party 
import aiohttp
import textwrap
import motor.motor_asyncio
from traceback import format_exception
from pathlib import Path

# Local
from config import *
import utils.json_loader
from utils import clean_code , Pag
from utils.mongo import Document

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

#json_secret_file
secrets = utils.json_loader.read_json("secrets")
owner = secrets["owner"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(f'{PREFIX}'), case_insensitive=True, intents=intents, owner_id=owner , help_command=None)
bot.latte_version = BOTVERSION
bot.latte_source = LATTESOURCE

@bot.event
async def on_ready():
    bot_activity = "with my friends ♡ ₊˚"
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name=bot_activity)
    )
    print(f"\nName : {bot.user}\nActivity : {bot_activity}\nServer : {len(bot.guilds)}\nMembers : {len(set(bot.get_all_members()))}\nPrefix : {PREFIX}")
    print(f"\nCogs list\n-----")

#json_loader
bot.config_token = secrets["token"]
bot.connection_url = secrets["mongo"]
bot.giphy_api_ = secrets["giphy"]

#eval
@bot.command(name="eval", aliases=["exec"])
@commands.is_owner()
async def _eval(ctx, *, code):
#    await ctx.reply("Let me evaluate this code for you! Won't be a sec")
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": bot,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message,
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
        result = "".join(format_exception(e, e, e.__traceback__))

    pager = Pag(
        timeout=100,
        entries=[result[i : i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```",
    )

    await pager.start(ctx)

#jishaku
bot.load_extension('jishaku')

#cogs_and_mongodb
if __name__ == "__main__":
    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(bot.connection_url))
    bot.db = bot.mongo["latteonly"]
    bot.sleepdb = Document(bot.db, "sleeping")
    bot.tagdb = Document(bot.db, "tags")

    #db_2nd
    bot.db2 = bot.mongo["lattebot"]
    bot.latency_bot = Document(bot.db2, "latency")

    #db_leveling
    bot.db_level = bot.mongo["discord"]
    bot.latte_level = Document(bot.db_level, "levelling")

    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(bot.config_token)