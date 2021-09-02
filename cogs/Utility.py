# Standard 
import discord , asyncio
import datetime
from discord.ext import commands
from datetime import datetime, timezone , timedelta

# Third party
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
        result =  translator.translate(f'{args}' , dest=f'{to_lang}')
        a = translator.detect(str(args))
        b = translator.detect(str(result.text))

        embed = discord.Embed(color=0xffffff)
        embed.set_author(name="Translator" , icon_url="https://upload.wikimedia.org/wikipedia/commons/d/db/Google_Translate_Icon.png")
        embed.add_field(name=f"Original ({str(a.lang)})", value=f"```{args}```", inline=False)
        embed.add_field(name=f"Translated ({str(b.lang)})", value=f"```{result.text}```", inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == TRANSLATE_CHANNEL:

            if message.author == self.client.user:
                return

            translator = Translator()
            result =  translator.translate(f'{message.clean_content}' , dest='th')

            await message.channel.send(result.text)

        
def setup(client):
    client.add_cog(Utility_(client))