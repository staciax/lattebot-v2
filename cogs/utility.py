# Standard 
import discord
import asyncio
import random
import datetime
import json
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party
import humanize
from googletrans import Translator
import typing , unicodedata
from typing import Union

# Local
import utils
from config import *
from utils.custom_menu import NewSimpage
from utils.converters import FutureTime_converter
from utils.json_loader import read_json , write_json
from utils.ButtonRef import Confirm
from utils.formats import format_dt
from utils.time import format_relative

class Utility_(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.channel_sleep = {}
        self.channel_sleeped.start()
    
    def cog_unload(self):
        self.channel_sleeped.cancel()
    
    @tasks.loop(minutes=1)
    async def channel_sleeped(self):
        guild = self.bot.get_guild(MYGUILD)
        data = read_json("channel_sleep")
        if not data:
            return
        for key in data.keys():
            dt = datetime.now(timezone.utc).strftime("%d%m%Y%H%M")
            if data[key]["time"] is None:
                return
            elif int(data[key]["time"]) == int(dt):
                channel = guild.get_channel(int(key))
                member_list = channel.members
                if member_list is not None:
                    try:
                        for x in member_list:
                            await x.move_to(channel=None)
                        data[key]["time"] = None
                        write_json(data, "channel_sleep")
                    except:
                        return print("error sleep")
    
    @channel_sleeped.before_loop
    async def before_channel_sleeped(self):
        await self.bot.wait_until_ready()
        
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

    @commands.command(description="Converter text to binary", help=f"i like you", usage=f"<message>")
    @commands.guild_only()
    async def binary(self, ctx, *, args=None):
        if args is None:
            return await ctx.send("missing argument converter to the **binary**")

        res = ' '.join(format(i, '08b') for i in bytearray(args, encoding ='utf-8'))

        await ctx.send(str(res))
    
    @commands.command(description="reverse message" , help=f"like this", usage=f"<message>")
    @commands.guild_only()
    async def reverse(self, ctx, *, args=None):
        res = ''.join(reversed(args))

        await ctx.send(str(res))
    
    @commands.command(name="rn", description="takes smallest and largest numbers then does a random number between.", help=f"20 300", usage=f"<Lowest number> <Highest number>")
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
    
    @commands.command(name="random", aliases=["r"], description="random", help="asuna alice silica")
    @commands.guild_only()
    async def random_(self, ctx ,*,msg=None):
        if msg is None:
            await ctx.send("Please enter a split message" , delete_after=15)
        #split message
        #message_response = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author) #message_response.content
        
        #convert_to_split
        input_value = msg 
        list_input = list(input_value.split())

        if len(list_input) == 1:
            await ctx.send("There must be at least 2 split messages." , delete_after=15)
            return
        

        #try_random
        try:
            await ctx.send(random.choice(list_input))
        except ValueError:
            await ctx.send("Invalid Range")

    @commands.command(name="random_invoice", aliases=["rnv"] ,description="random member in current voice channel")
    @commands.guild_only()
    async def random_voice_member(self, ctx, channel:discord.VoiceChannel=None):
        
        #check
        if channel is None:
            channel = ctx.author.voice.channel
            in_channel = ctx.author.voice.channel.members
        else:
            in_channel = channel.members

        embed = discord.Embed(title=f"Members - {channel.name}",color=WHITE)
        
        #get_member_in_voice
        member_list = []

        for members in in_channel:
            member_voice = members
            member_list.append(member_voice)
        
        p = NewSimpage(entries=member_list, ctx=ctx, member_list=member_list)
        p.embed.title = f"Members - {channel.name}"
        p.embed.color = WHITE
        await p.start()
                    
    @commands.command(aliases=["trans"] , description="Translate your message" , help="trans th こんにちは", usage="<output_language> <message>")
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

    @commands.command(description="Reminder" , help="10h working time", usege="<duration> [message]")
    @commands.guild_only()
    async def remind(self, ctx , time=None, *, msg=None):
        if time is None:
            embed_time = discord.Embed(description="**Please specify duration** : `(s|m|h|d)`\n```yaml\nExample : .sleep 5m , .sleep 2h```",color=WHITE)
            return await ctx.send(embed=embed_time , delete_after=15)
        if msg is None:
            msg = "..."
        elif len(msg) > 2000:
            return await ctx.send('remind message is a maximum of 2000 characters.', delete_after=15)

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
    
    @commands.command(description="Reminder in chat" , help="10h working time", usege="<duration> [message]")
    @utils.is_latte_guild()
    async def remind_chat(self, ctx , time=None, *, msg=None):
        if time is None:
            embed_time = discord.Embed(description="**Please specify duration**",color=WHITE)
            return await ctx.send(embed=embed_time , delete_after=15)
        if msg is None:
            msg = "..."
        elif len(msg) > 2000:
            return await ctx.send('remind message is a maximum of 2000 characters.', delete_after=15)

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
        
    @commands.command(description="Crete poll" , help="i pretty?", usege="<message>")
    @commands.guild_only()
    async def poll(self, ctx, *, message):
        if len(message) > 2000:
            return await ctx.send('remind message is a maximum of 2000 characters.', delete_after=15)
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
    
    @commands.command(name="platform", aliases=["pt"] , usege="<member>")
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
        if member.avatar.url is not None:
            embed.set_author(name=member , icon_url=member.avatar.url)
        else:
            embed.set_author(name=member)
        embed.description = f"{desktop}\n{mobiles}\n{Web}"

        await ctx.send(embed=embed)
        
    @commands.command(description="converter roman to number", aliases=["rtn"],help="XII", usage="<roman>")
    @commands.guild_only()
    async def roman_to_number(self, ctx, args:str=None):
        try:
            number = utils.roman_to_int(input=args)
            await ctx.send(number)
        except:
            return await ctx.send("Bad valid")

    @commands.command(description="converter number to roman",aliases=["ntr"],help="200", usage="<number>")
    @commands.guild_only()
    async def number_to_roman(self, ctx, args:int=None):
        try:
            number = utils.int_to_roman(input=args)
            await ctx.send(number)
        except:
            return await ctx.send("Bad valid")

    @commands.command(aliases=["gsmap","hoyomap","map","gmap"])
    @commands.guild_only()
    async def genshinmap(self, ctx):
        embed = discord.Embed(color=0x2484d7)
        embed.set_author(name='Genshin impact Map' , icon_url="https://cdn.discordapp.com/emojis/892114299793842266.png")
        #start_view_button
        view = discord.ui.View()
        Off = discord.ui.Button(style=discord.ButtonStyle.gray, label="Official", url="https://webstatic-sea.mihoyo.com/")
        Un = discord.ui.Button(style=discord.ButtonStyle.gray, label="Unofficial", url="https://genshin-impact-map.appsample.com/#/")
        view.add_item(item=Off)
        view.add_item(item=Un)
        await ctx.send(embed=embed, view=view)
    
    @commands.group(invoke_without_command=True, aliases=["boom",'slch','svc','sleep_vc'], usage="<time> [channel id]")
    @utils.is_latte_guild()
    async def sleep_channel(self, ctx, time=None, channel:discord.VoiceChannel=None):

        embed = discord.Embed()
        embed.color = BRIGHTRINK

        if time is None:
            embed.description = "Please specify duration"
            return await ctx.send(embed=embed , delete_after=15)

        if channel is None:
            try:
                channel = ctx.author.voice.channel
                in_channel = ctx.author.voice.channel.members
            except:
                embed.description = 'You must join a voice channel first.'
                return await ctx.send(embed=embed , delete_after=15)
        else:
            in_channel = channel.members
        
        if channel and len(in_channel) == 0:
            embed.description = f'No members found in `{channel}`'
            return await ctx.send(embed=embed , delete_after=15)

        timewait = FutureTime_converter(time)
        futuredate = datetime.now(timezone.utc) + timedelta(seconds=timewait) 
        futuredate_ = futuredate.strftime("%d%m%Y%H%M")

        #fixed_utc+7
        fix_date = futuredate + timedelta(seconds=25200)
        fix_date = fix_date.strftime("%H:%M %d/%m/%Y")

        cooldown = humanize.naturaldelta(timedelta(seconds=timewait))
        
        embed.color = YELLOW
        embed.add_field(name=f"**SLEEP TIMER** <a:b_hitopotatosleep:864921119538937968>" , value=f"** **\n**CHANNEL** : {channel.mention}\n\n`{fix_date}({cooldown})\n\nnow members: {len(in_channel)}`" , inline=False)

        view = Confirm(ctx)
        m = await ctx.reply(embed=embed, view=view , mention_author=False)
        await view.wait()
        if view.value is None:
            return
        elif view.value:
            view.clear_items()
            embed_edit = discord.Embed(color=ctx.author.colour)
            embed_edit.description = f"**SLEEP TIMER** <a:b_hitopotatosleep:864921119538937968>\n\n**CHANNEL**: {channel.mention}\n\n`{fix_date}`\n{format_relative(futuredate)}"
            if ctx.author.avatar is not None:
                embed_edit.set_footer(text='Sleep timer by %s' % (ctx.author) , icon_url=ctx.author.avatar.url)
            else:
                embed_edit.set_footer(text='Sleep timer by %s' % (ctx.author))

            #chat_send
            chat_channel = ctx.guild.get_channel(861883647070437386)
            chat_embed = discord.Embed(color=WHITE)
            # chat_embed.title = f"**SLEEP TIMER** <a:b_hitopotatosleep:864921119538937968>"
            chat_embed.description = f"**CHANNEL** : {channel.mention}\n\n`{fix_date}`\n{format_relative(futuredate)}"
            if ctx.author.avatar is not None:
                chat_embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)
            else:
                chat_embed.set_footer(text=f'Requested by {ctx.author}')
            
            await chat_channel.send(embed=chat_embed)

            if timewait > 600:
                self.channel_sleep[str(channel.id)] = {"time": futuredate_}
                with open("bot_config/channel_sleep.json", "w") as fp:
                    json.dump(self.channel_sleep, fp , indent=4)
                await m.edit(embed=embed_edit, view=view)

            else:
                await m.edit(embed=embed_edit, view=view)
                await asyncio.sleep(timewait)
                for member in in_channel:
                    await member.move_to(channel=None)
        else:
            embed_c = discord.Embed(description="*Cancelling!*" , color=WHITE)
            await ctx.send(embed=embed_c , delete_after=10)
            await m.delete()
            # await ctx.message.delete()
    
    @sleep_channel.command(invoke_without_command=True , aliases=["del", "delete" , "off" , "stop"], help="stop", usage="[channel id]")
    async def sleep_channel_stop(self, ctx, *, channel:discord.VoiceChannel=None):
        if channel is None:
            channel = ctx.author.voice.channel

        data = read_json("channel_sleep")
        check_data = data[str(channel.id)]["time"]

        if check_data is not None:
            try:
                data[str(channel.id)]["time"] = None
                write_json(data, "channel_sleep")
                embed = discord.Embed(description=f"{channel.mention} : sleep timer stoped" , color=WHITE)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(description="Error stop timer" , color=BRIGHTRINK)
                await ctx.send(embed=embed)
                return
        else:
            em_error = discord.Embed(description=f"{channel.mention} : sleep timer not found", color=BRIGHTRINK)
            await ctx.send(embed=em_error)
        

        

def setup(bot):
    bot.add_cog(Utility_(bot))
