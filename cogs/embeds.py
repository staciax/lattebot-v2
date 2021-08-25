# Standard 
import discord , datetime , time , asyncio
from discord.ext import commands
from datetime import datetime, timezone

# Third party
import json , requests , matplotlib
from tagformatter import Parser

# Local
import utils
from config import *

parser = Parser(case_insensitive=True)

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.bot = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    #create_embed
    @commands.group(invoke_without_command=True , aliases=["em"])
    async def embeds(self, ctx):
        data = utils.json_loader.read_json("embed")
        embed = discord.Embed(description= f"embed.json\n```nim\n{json.dumps(data, indent = 1)[1:-1]}```" , color=0xffffff)
        await ctx.send(embed=embed)
    
    @embeds.group(invoke_without_command=True , aliases=["cre"])
    async def create(self, ctx): 

        data = utils.json_loader.read_json("embed")
        em_title = data["title"]
        em_description = data["description"]
        em_color = data["colour"]
        em_author = data["author"]
        em_author_url = data["author-icon-url"]
        em_footer = data["footer"]
        em_footer_url = data["footer-icon-url"]

        try:
            embed = discord.Embed()
            if em_title:
                embed.title = em_title
            if em_description:
                embed.description = em_description
            if em_color:
                embed.color = em_color
            if em_author:
                if em_author_url:
                    embed.set_author(name=em_author , icon_url=em_author_url)
                else:
                    embed.set_author(name=em_author)
            if em_footer:
                if em_footer_url:
                    embed.set_footer(text=em_footer , icon_url=em_footer_url)
                else:
                    embed.set_footer(text=em_footer)

            await ctx.send(embed=embed)
        except:
            return await ctx.send("embed error")

    @embeds.group(invoke_without_command=True , aliases=["reset"])
    async def embeds_reset(self, ctx):
        data = utils.json_loader.read_json("embed")
        data["title"] = None
        data["description"] = None
        data["colour"] = None
        data["author"] = None
        data["author-icon-url"] = None
        data["footer"] = None
        data["footer-icon-url"] = None

        try:
            utils.json_loader.write_json(data, "embed")
            await ctx.send("reset embed")
        except:
            print("error")
        
    @embeds.group(invoke_without_command=True)
    async def title(self, ctx , *, title): 

        data = utils.json_loader.read_json("embed")

        data["title"] = title
        try:
            utils.json_loader.write_json(data, "embed")
            await ctx.send(f'set embed title : {data["title"]}')
        except:
            print("error")
    
    @embeds.group(invoke_without_command=True)
    async def description(self, ctx , *, description): 
        
        data = utils.json_loader.read_json("embed")

        data["description"] = description
        try:
            utils.json_loader.write_json(data, "embed")
            await ctx.send(f'set embed description : {data["description"]}')
        except:
            print("error")

    @embeds.group(invoke_without_command=True)
    async def color(self, ctx , color):
        
        try:
            embed_color = (matplotlib.colors.cnames[f"{color.lower()}"])
        except:
            await ctx.send("https://htmlcolorcodes.com/color-names/")

        data = utils.json_loader.read_json("embed")

        data["colour"] = int(embed_color[1:], 16)
        
        try:
            utils.json_loader.write_json(data, "embed")
            embed = discord.Embed(description="set embed color" , color=data["colour"])
            await ctx.send(embed=embed)
            print(hex(data["colour"]))
        except:
            print("error")
        
    @embeds.group(invoke_without_command=True)
    async def author(self, ctx , author):
        data = utils.json_loader.read_json("embed")

        data["author"] = author
        try:
            utils.json_loader.write_json(data, "embed")
            await ctx.send(f'set embed author : {data["author"]}')
        except:
            print("error")
    
    @author.command(name="url")
    async def author_icon_url(self, ctx , author_url):
        data = utils.json_loader.read_json("embed")

        data["author-icon-url"] = author_url
        try:
            utils.json_loader.write_json(data, "embed")
            await ctx.send(f'set embed author url : {data["author-icon-url"]}')
        except:
            print("error")
    
    @embeds.group(invoke_without_command=True)
    async def footer(self, ctx , footer):
        data = utils.json_loader.read_json("embed")
        data["footer"] = footer
        try:
            utils.json_loader.write_json(data, "embed")
            await ctx.send(f'set embed footer : {data["footer"]}')
        except:
            print("error")
    
    @footer.command(name="url")
    async def footer_icon_url(self, ctx , footer_url):
        data = utils.json_loader.read_json("embed")

        data["footer-icon-url"] = footer_url
        try:
            utils.json_loader.write_json(data, "embed")
            await ctx.send(f'set embed footer url : {data["footer-icon-url"]}')
        except:
            print("error")

    
def setup(client):
    client.add_cog(Utility(client))