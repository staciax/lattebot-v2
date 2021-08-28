# Standard 
import discord , json , os , datetime , random , asyncio , re , io , contextlib , logging
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

#owner
secrets = utils.json_loader.read_json("secrets")
owner = secrets["owner"]

intents = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=intents, owner_id=owner , help_command=None)

client.connection_url = secrets["mongo"]

#remove_default_help
#@client.remove_command("help")

@client.event
async def on_ready():
    bot_activity = "lt help"
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name=bot_activity)
    )
    print(f"\nName : {client.user}\nActivity : {bot_activity}\nServer : {len(client.guilds)}\nMembers : {len(set(client.get_all_members()))}")
    print(f"\nCogs list\n-----")

#json_secret_file
secret_file = utils.json_loader.read_json("secrets")
client.config_token = secret_file["token"]
client.connection_url = secret_file["mongo"]
client.giphy_api_ = secret_file["giphy"]

#prefix
@client.command()
async def prefix(ctx):
    await ctx.send("This is my prefix `lt ` or `l `")

#cogs
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send("Could not load cog")
        return
    await ctx.send(f"Cog loaded : {extension}")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send("Could not unload cog")
        return
    await ctx.send(f"Cog unloaded : {extension}")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
    except Exception as e:
        await ctx.send("Could not reload cog")
        return
    await ctx.send(f"Cog reloaded : {extension}")

#eval
@client.command(name="eval", aliases=["exec"])
@commands.is_owner()
async def _eval(ctx, *, code):
#    await ctx.reply("Let me evaluate this code for you! Won't be a sec")
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": client,
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

@client.command()
async def send_webhook(ctx , output):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('https://discord.com/api/webhooks/881095764519043073/b0x0UDuhLs79DJ64IQMD7AW7z1k7dDGL6uZ9LviaXkzvF5wgbRQpMo7Q8D2AYkQJXGoW', adapter=AsyncWebhookAdapter(session))
        await webhook.send(output, username=ctx.message.author.name)

#jishaku
client.load_extension('jishaku')

#bot_config_read
@client.command(name="botconfig", aliases=["bconfig"])
@utils.owner_bot()
async def bot_config_(ctx):
    with open('config.py' , encoding='utf-8') as f:
        lines = f.read()
        embed = discord.Embed(description=f"```nim\n{lines}```",color=0xffffff)
        await ctx.send(embed=embed)

if __name__ == "__main__":
    client.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(client.connection_url))
    client.db = client.mongo["latteonly"]
    client.sleepdb = Document(client.db, "sleeping")

    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            client.load_extension(f"cogs.{file[:-3]}")

    client.run(client.config_token)