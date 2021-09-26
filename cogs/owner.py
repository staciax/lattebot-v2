# Standard 
import discord , asyncio , os
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party

# Local
import utils

class Owner_(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    #bot_config_read
    @commands.command(name="botconfig", aliases=["bconfig"])
    @commands.is_owner()
    async def config_py(self, ctx):
        with open('./config.py' , encoding='utf-8') as f:
            lines = f.read()
            embed = discord.Embed(description=f"```nim\n{lines}```",color=0xffffff)
            await ctx.send(embed=embed)
    
    #cogs
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        embed = discord.Embed()
        try:
            self.bot.load_extension(f'cogs.{extension}')
        except Exception as e:
            embed.set_author(name=f"Could not reload : `{extension}`")
            embed.color = 0xFF7878
            return

        embed.description = f"{utils.emoji_converter('greentick')} Load : `{extension}`"
        embed.color = 0x8be28b
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        embed = discord.Embed()
        try:
            self.bot.unload_extension(f'cogs.{extension}')
        except Exception as e:
            embed.set_author(name=f"Could not reload : `{extension}`")
            embed.color = 0xFF7878
            return
    
        embed.description = f"{utils.emoji_converter('greentick')} Unload : `{extension}`"
        embed.color = 0x8be28b
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        embed = discord.Embed()
        try:
            self.bot.unload_extension(f'cogs.{extension}')
            self.bot.load_extension(f'cogs.{extension}')
        except Exception as e:
            embed.set_author(name=f"Could not reload : `{extension}`")
            embed.color = 0xFF7878
            await ctx.send(embed=embed)
            return

        embed.description = f"{utils.emoji_converter('greentick')} Reload : `{extension}`"
        embed.color = 0x8be28b
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def reloadall(self, ctx):
        embed = discord.Embed()
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                if not filename == "owner.py":
                    try:
                        self.bot.reload_extension(f"cogs.{filename[:-3]}")
                    except Exception as e:
                        self.bot.load_extension(f"cogs.{filename[:-3]}")
                        return await ctx.send(f"{e}")
        
        embed.description = f"{utils.emoji_converter('greentick')} Reloaded all"
        embed.color = 0x8be28b
        await ctx.send(embed=embed)
    
    
def setup(bot):
    bot.add_cog(Owner_(bot))