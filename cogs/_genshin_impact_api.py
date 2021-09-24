# Standard 
import discord , asyncio , json
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party
import genshinstats as gs

# Local
from utils.json_loader_gs import *

class genshin_impact_api(commands.Cog):

    #token
    data = read_json('genshin_secrets')
    gs.set_cookie_auto()

    def __init__(self, bot):
        self.bot = bot
        self.stacia_uid = 800665932
        self.register_uid = {}

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command(aliases=["gsmap"])
    @commands.guild_only()
    async def genshinmap(self, ctx):
        await ctx.send("https://genshin-impact-map.appsample.com/#/")
    
    @commands.command(name="uid")
    @commands.guild_only()
    async def register_uid(self, ctx , uid:int , member:discord.Member=None):
        
        #write_json_uid
        self.register_uid[str(ctx.author.id)] = uid
        with open("data/genshin_uid.json", "w" , encoding='UTF8') as gs_uid:
            json.dump(self.register_uid, gs_uid , indent=4)

    @commands.command(name="gs_char")
    @commands.guild_only()
    async def gs_character_count(self, ctx , uid:int=None):
        data_char = gs.get_user_stats(uid)
        total_characters = len(data_char['characters'])
        await ctx.send(f'user uid {uid} has a total of, {total_characters}, characters')

        all_char = ""
        characters = gs.get_characters(uid)
        for char in characters:
            all_char += f"{char['rarity']}* {char['name']:10} | lvl {char['level']:2} C{char['constellation']}\n"
        await ctx.send(all_char)
    
    @commands.command(name="abyss")
    @commands.guild_only()
    async def abyss(self, ctx , uid:int=None):
        spiral_abyss = gs.get_spiral_abyss(uid, previous=True)
        stats = spiral_abyss['stats']
        for field, value in stats.items():
            await ctx.send(f"{field}: {value}")

    @commands.command(name="wish_character")
    @commands.guild_only()
    async def wish_character(self, ctx):
        message = ""
        for i in gs.get_wish_history(301):
            message += f" {i['name']} ({i['rarity']}* {i['type']})\n"
        
        embed = discord.Embed(color=0xffffff)
        embed.description = message
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(genshin_impact_api(bot))