# Standard 
import discord 
import asyncio
from discord.ext import commands 

# Third party
import pymongo 
from pymongo import MongoClient

# Local
import utils
from config import * 

mango_url = MONGOURL

class Exp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.guild:
            cluster = MongoClient(mango_url)
            db = cluster["database"]
            collection = db["new"]
            author_id = ctx.author.id
            guild_id = ctx.guild.id 
        
            author = ctx.author
        
            user_id = {"_id": author_id}
        
            if ctx.author == self.client.user:
                return
            if ctx.author.bot:
                return
            
            if(collection.count_documents({}) == 0):
                user_info = {"_id": author_id, "GuildID": guild_id, "Level": 1, "XP": 0}
                collection.insert_one(user_info)

            if(collection.count_documents(user_id) == 0):
                user_info = {"_id": author_id, "GuildID": guild_id, "Level": 1, "XP": 0}
                collection.insert_one(user_info)
            
            exp = collection.find(user_id)
            for xp in exp:
                cur_xp = xp["XP"]
           
                new_xp = cur_xp + 1 
        
            collection.update_one({"_id": author_id}, {"$set":{"XP":new_xp}}, upsert=True)

	        #await ctx.channel.send("1 xp up") 
        
            lvl = collection.find(user_id)
            for levl in lvl:
                lvl_start = levl["Level"]
                new_level = lvl_start + 1

            if cur_xp >= round(5 * (lvl_start ** 4 / 5)):
                collection.update_one({"_id": author_id}, {"$set":{"Level":new_level}}, upsert=True)
                await ctx.channel.send(f"{author.name} has leveled up to {new_level}!")
            
            if new_level >= 100:
                new_level = ("LEVEL MAX")
                lv15 = discord.utils.get(ctx.guild.roles, name ="-          Level : 15           -")     
                await author.add_roles(lv15)
        else:
            pass

    @commands.command(aliases=['lv', 'lvl'])
    async def level(self, ctx, *, member: discord.Member = None):
        if ctx.guild:
            if not member:
                member = ctx.message.author
            
            if member == self.client.user:
                return
            if member.bot:
                await ctx.channel.send("this is a bot")
                return
            
            cluster = MongoClient(mango_url)
            db = cluster["database"]
            collection = db["new"]
            author_id = member.id
            guild_id = ctx.guild.id 

            author = ctx.message.author
        
            user_id = {"_id": author_id}

            if(collection.count_documents({}) == 0):
                user_info = {"_id": author_id, "GuildID": guild_id, "Level": 1, "XP": 0}

            exp = collection.find(user_id)
            for xp in exp:
                cur_xp = xp["XP"]

            lvl = collection.find(user_id)
            for levl in lvl:
                lvl_start = levl["Level"]

            else:
                lastxp = round(5 * (lvl_start ** 4 / 5))
        
            if lvl_start > 100:
                lvl_start = ("LEVEL MAX")
      
            await ctx.channel.send(f"{member.name} Exp: {cur_xp}/{lastxp} \nLevel : {lvl_start}!" , delete_after=10)
            await asyncio.sleep(10)
            await ctx.message.delete()
        
        else:
            pass
#            await ctx.channel.send("test")



def setup(client):
    client.add_cog(Exp(client))