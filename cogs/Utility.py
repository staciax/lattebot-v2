# Standard 
import discord , asyncio
import datetime
from discord.ext import commands
from datetime import datetime, timezone , timedelta

# Third party
import humanize
from googletrans import Translator

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

    @commands.command()
    async def binary(self, ctx, *, args=None):
        if args is None:
            return await ctx.send("missing argument converter to the **binary**")

        res = ' '.join(format(i, '08b') for i in bytearray(args, encoding ='utf-8'))

        await ctx.send(str(res))
    
    @commands.command()
    async def reverse(self, ctx, *, args=None):
        res = ''.join(reversed(args))

        await ctx.send(str(res))

    @commands.command(aliases=["trans"])
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
        

        
def setup(client):
    client.add_cog(Utility_(client))