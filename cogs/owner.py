# Standard 
import discord
import asyncio
import os
import io
import datetime
import contextlib
import textwrap
from traceback import format_exception
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party

# Local
import utils
from utils import clean_code , Pag

class Owner_(commands.Cog):

    def __init__(self, bot):
        self.hidden = True
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command()
    @commands.is_owner()
    async def enable(self, ctx, command : str):
        command = self.bot.get_command(command)
        if command.enabled:
            return await ctx.send(f"`{command}` is already enabled.")
        command.enabled = True
        await ctx.send(f"Successfully enabled the `{command.name}` command.")
        
    @commands.command()
    @commands.is_owner()
    async def disable(self, ctx, command : str):
        command = self.bot.get_command(command)
        if not command.enabled:
            return await ctx.send(f"`{command}` is already disabled.")
        command.enabled = False
        await ctx.send(f"Successfully disabled the `{command.name}` command.")
    
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
            embed.description = f"{utils.emoji_converter('greentick')} Load : `{extension}`"
            embed.color = 0x8be28b
        except Exception as e:
            embed.description(f"Could not reload : `{extension}`")
            embed.color = 0xFF7878

        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        embed = discord.Embed()
        try:
            self.bot.unload_extension(f'cogs.{extension}')
            embed.description = f"{utils.emoji_converter('greentick')} Unload : `{extension}`"
            embed.color = 0x8be28b
        except Exception as e:
            embed.description(f"Could not reload : `{extension}`")
            embed.color = 0xFF7878

        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        embed = discord.Embed()
        try:
            self.bot.unload_extension(f'cogs.{extension}')
            self.bot.load_extension(f'cogs.{extension}')
            embed.description = f"{utils.emoji_converter('greentick')} Reload : `{extension}`"
            embed.color = 0x8be28b
        except Exception as e:
            embed.description(f"Could not reload : `{extension}`")
            embed.color = 0xFF7878

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
    
    #eval
    @commands.command(name="eval", aliases=["exec"])
    @commands.is_owner()
    async def _eval(self, ctx, *, code):
    #    await ctx.reply("Let me evaluate this code for you! Won't be a sec")
        code = clean_code(code)

        local_variables = {
            "discord": discord,
            "commands": commands,
            "bot": self.bot,
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
    
def setup(bot):
    bot.add_cog(Owner_(bot))