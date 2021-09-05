# Standard 
import discord , asyncio
import datetime
from discord.ext import commands
from datetime import datetime, timezone , timedelta

# Third party
import humanize
from googletrans import Translator
import typing , unicodedata
from typing import Union

# Local
import utils
from config import *

class Utility_(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.bot = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.Cog.listener()
    async def on_message(self, message):

        #google_translator
        if message.channel.id == TRANSLATE_CHANNEL:
            if message.author == self.client.user:
                return
            translator = Translator()
            try:
                result =  translator.translate(f'{message.clean_content}' , dest='th')
            except:
                return await ctx.send("เกิดข้อผิดพลาดในการแปลภาษา" , delete_after=10)

            await message.channel.send(result.text)

    @commands.command()
    @commands.guild_only()
    async def binary(self, ctx, *, args=None):
        if args is None:
            return await ctx.send("missing argument converter to the **binary**")

        res = ' '.join(format(i, '08b') for i in bytearray(args, encoding ='utf-8'))

        await ctx.send(str(res))
    
    @commands.command()
    @commands.guild_only()
    async def reverse(self, ctx, *, args=None):
        res = ''.join(reversed(args))

        await ctx.send(str(res))
    
    @commands.command(name="rn", brief="takes smallest and largest numbers then does a random number between.")
    @commands.guild_only()
    async def random_number(self , ctx , *numbers: typing.Union[int,str]):
        numbers=sorted(list(filter(lambda x: isinstance(x, int), numbers)))
        if len(numbers) < 2:
            await ctx.send("Not enough numbers")

        else:
            embed = discord.Embed(title=f"Random Number: {random.randint(numbers[0],numbers[-1])} ",color=WHITE)
            embed.add_field(name="Lowest Number:",value=f"{numbers[0]}")
            embed.add_field(name="Highest Number:",value=f"{numbers[-1]}")
            await ctx.send(embed=embed)

    @commands.command(aliases=["trans"])
    @commands.guild_only()
    async def translate(self, ctx, to_lang=None, *, args=None):
        if to_lang is None:
            embed_tl = discord.Embed(description="**Translater help**\n```yaml\nEx : .trans en こんにちは\n>> 'Hello'\nEx2 : .trans th こんにちは\n>> 'สวัสดี'```")
            return await ctx.send(embed=embed_tl)


        translator = Translator()
        try:
            a = translator.detect(str(args))
        except:
            return await ctx.send("ภาษานี้ไม่ได้อยู่ในระบบ" , delete_after=10)

        try:
            result =  translator.translate(f'{args}' , dest=f'{to_lang}')
            b = translator.detect(str(result.text))
        except:
            return await ctx.send("เกิดข้อผิดพลาดในการแปลภาษา" , delete_after=10)

        embed = discord.Embed(color=0xffffff)
        embed.set_author(name="Translate" , icon_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Google_Translate_Icon.png")
        embed.add_field(name=f"Original ({str(a.lang)})", value=f"```{args}```", inline=False)
        embed.add_field(name=f"Translated ({str(b.lang)})", value=f"```{result.text}```", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def remind(self, ctx , time=None, *, msg=None):
        if time is None:
            embed_time = discord.Embed(description="**Please specify duration** : `(s|m|h|d)`\n```yaml\nExample : .sleep 5m , .sleep 2h```",color=WHITE)
            return await ctx.send(embed=embed_time , delete_after=15)
        if msg is None:
            msg = "..."

        #try_converter
        try:
            #time_converter_to_seconds
            future = utils.FutureTime_converter(time)

            #time_converted
            remind_time = datetime.now(timezone.utc) + timedelta(seconds=future)
            future_data = humanize.naturaldelta(future, minimum_unit='milliseconds')
        except:
            embed_error = discord.Embed(description="Time is invalid", color=WHITE)
            return await ctx.send(embed=embed_error)

        await ctx.send(f'Alright {ctx.author.mention}, {future_data}: {msg}')
        await discord.utils.sleep_until(remind_time)
        await ctx.send(f"{ctx.author.mention}, {utils.format_relative(remind_time)}: {msg}\n\n{ctx.message.jump_url}")
        
    @commands.command()
    @commands.guild_only()
    async def poll(self, ctx,*,message):
        embed = discord.Embed(title="POLL", description=f"{message}",color=0xffffff)
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("<:greentick:881500884725547021>")
        await msg.add_reaction("<:redtick:881500898273144852>")

        if ctx.channel.id == LATTE_CHAT:
            await ctx.message.delete()
        else:
            await ctx.message.add_reaction(f"{utils.emoji_converter('trash')}")
            try:
                reaction , user = await self.client.wait_for(
                    "reaction_add",
                    timeout=30,
                    check=lambda reaction, user: user == ctx.author
                    and reaction.message.channel == ctx.channel
                )

            except asyncio.TimeoutError:
                await ctx.message.clear_reactions()
                return

            if str(reaction.emoji) == "<:trashcan:883641203051073557>":
                await ctx.message.delete()
        
def setup(client):
    client.add_cog(Utility_(client))