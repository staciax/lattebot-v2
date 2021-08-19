# Standard 
import discord , json , os , datetime , random , asyncio , re , io , contextlib , logging
from discord.ext import commands, tasks
from datetime import datetime, timedelta, timezone

# Third party 
import textwrap
from traceback import format_exception

# Local
from config import *
import utils.json_loader
from utils import clean_code , Pag

intents = discord.Intents()
intents.all()
client = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=discord.Intents.all(), owner_id=DEV_OWNER_ID)
    
@client.remove_command("help") #remove help 

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

@client.command()
async def prefix(ctx):
    await ctx.send("This is my prefix `lt ` or `l `")

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
#    client.load_extension(f'cogs.{extension}')

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

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

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

client.load_extension('jishaku')

def owner_bot():
    def pred(ctx):
        owner_ids = [385049730222129152, 240059262297047041]
        if ctx.author.id in owner_ids:
            return True
        return False
    return commands.check(pred)

client.owner_bot = owner_bot()

client.run(client.config_token)