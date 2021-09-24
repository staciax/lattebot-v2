# Standard 
import discord , asyncio , random
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

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.latte_chat = self.bot.get_channel(LATTE_CHAT)
        print(f"-{self.__class__.__name__}")

    @commands.Cog.listener()
    async def on_message(self, message):

        #google_translator
        if message.channel.id == TRANSLATE_CHANNEL:
            if message.author == self.bot.user:
                return
            translator = Translator()
            try:
                result =  translator.translate(f'{message.clean_content}' , dest='th')
            except:
                return await ctx.send("เกิดข้อผิดพลาดในการแปลภาษา" , delete_after=10)

            await message.channel.send(result.text)

    @commands.command(description="Converter text to binary", brief=f"{PREFIX}binary i like you", usage=f"{PREFIX}binary <message>")
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
    
    @commands.command(name="rn", description="takes smallest and largest numbers then does a random number between.", brief=f"{PREFIX}rn 20 300", usage=f"{PREFIX}rn <Lowest number> <Highest number>")
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
    
    @commands.command(name="random", aliases=["r"], description="random", brief=f"{PREFIX}random", usage=f"{PREFIX}random")
    @commands.guild_only()
    async def random_(self, ctx ,*,msg) :
        #        await ctx.send("Please Enter a Range:")

        #split message
        #        message_response = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        input_value = msg#message_response.content
        list_input = list(input_value.split())

        #try_random
        try:
            await ctx.send(random.choice(list_input))
        except ValueError:
            await ctx.send("Invalid Range")

    @commands.command(name="random_invoice", aliases=["rnv"] ,description="random member in voice channel", brief=f"{PREFIX}rnv @latte 840381453779206166", usage=f"{PREFIX} <member> <voice>")
    @commands.guild_only()
    async def random_voice_member(self, ctx, member:discord.Member=None, channel:discord.VoiceChannel=None):
        
        #check
        if member is None and channel is None:
            channel = ctx.author.voice.channel
            in_channel = ctx.author.voice.channel.members
        else:
            in_channel = member.voice.channel.members

        #get_member_in_voice
        member_list = []
        for members in in_channel:
            member_voice = members.id
            member_list.append(int(member_voice))

        #random
        random_member = random.choice(member_list)
        rn_member = ctx.guild.get_member(random_member)

        #send_member
        embed = discord.Embed(title=f"{rn_member.display_name}",color=rn_member.colour)
        embed.set_thumbnail(url=rn_member.avatar.url)
        embed.set_footer(text=f"Random in: {channel}")
        await ctx.send(embed=embed)
        
            
    @commands.command(aliases=["trans"] , description="Translate your message" , brief=f"{PREFIX}trans th こんにちは\n{PREFIX}trans en สวัสดีค่ะ", usage=f"{PREFIX}trans <output_language> <message>")
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

    @commands.command(description="Reminder" , brief=f"{PREFIX}remind 10h working time\n{PREFIX}remind 10m i will go sleep ", usage=f"{PREFIX}remind <when> [message]")
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
    
    @commands.command(description="Reminder in chat" , brief=f"{PREFIX}remind_chat 10h working time\n{PREFIX}remind_chat 10m i will go sleep ", usage=f"{PREFIX}remind_chat <when> [message]")
    @commands.guild_only()
    async def remind_chat(self, ctx , time=None, *, msg=None):
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

        await ctx.send(f'Alright {ctx.author.mention}, {future_data}: {msg}\nchannel : {self.latte_chat.mention}')
        await discord.utils.sleep_until(remind_time)
        await self.latte_chat.send(f"{ctx.author.mention}, {utils.format_relative(remind_time)}: {msg}")
        
    @commands.command(description="Crete poll" , brief=f"{PREFIX}poll i pretty?", usage=f"{PREFIX}poll <message>")
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
                reaction , user = await self.bot.wait_for(
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
    
    @commands.command(name="platform", aliases=["pt"] , usage=f"{PREFIX}usage <member>")
    @commands.guild_only()
    async def check_platform(self, ctx, member: discord.Member=None):

        #check_member
        if not member:
            member = ctx.author 
        
        #fetch_member_status
        mobiles = utils.mobile_status(member)
        desktop = utils.desktop_status(member)
        Web = utils.web_status(member)

        #embed
        embed = discord.Embed(color=member.colour)
        embed.set_author(name=member , icon_url=member.avatar.url)
        embed.description = f"{desktop}\n{mobiles}\n{Web}"

        await ctx.send(embed=embed)
    
    @commands.command(brief="Send a message with a button!") # Create a command inside a cog
    @commands.guild_only()
    async def some_button(self, ctx):
        view = discord.ui.View() # Establish an instance of the discord.ui.View class
        style = discord.ButtonStyle.gray  # The button will be gray in color
        item = discord.ui.Button(style=style, label="Read the docs!", url="https://discordpy.readthedocs.io/en/master")  # Create an item to pass into the view class.
        view.add_item(item=item)  # Add that item into the view class
        await ctx.send("This message has buttons!", view=view)

    @commands.command(aliases=["gmap","genshin map"])
    @commands.guild_only()
    async def genshinmap(self, ctx):
        await ctx.send("https://genshin-impact-map.appsample.com/#/")

        
def setup(bot):
    bot.add_cog(Utility_(bot))