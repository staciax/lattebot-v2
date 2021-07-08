import discord
import json
import os
from discord.ext import commands, tasks
import random
import datetime
import asyncio
import re
from config import *
from datetime import datetime, timedelta

intents = discord.Intents()
intents.all()
intents.members = True 
intents = discord.Intents(messages=True, guilds=True)

client = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=discord.Intents.all(), owner_id=385049730222129152)

@client.remove_command("help") #remove help 

@client.event
async def on_ready():
    print(f"{client.user} in online")
    print(f"\ncommands list")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)