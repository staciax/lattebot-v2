# Standard 
import discord , json , os , datetime , random , asyncio , re
from discord.ext import commands, tasks
from datetime import datetime, timedelta

# Third party 
import pymongo
from pymongo import MongoClient

# Local
from config import *

intents = discord.Intents()
intents.all()
client = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=discord.Intents.all(), owner_id=DEV_OWNER_ID)
    
@client.remove_command("help") #remove help 

@client.event
async def on_ready():
    print(f"{client.user} in online")
    print(f"\nCogs list\n-----")

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

client.load_extension('jishaku')

client.run(TOKEN)