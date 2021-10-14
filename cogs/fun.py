# Standard
import discord
import datetime
import time
import asyncio
import re
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party
import json
from json import JSONEncoder
import io
import aiohttp , random , requests
import typing , unicodedata
from typing import Union
import humanize

# Local
from config import *
import utils
from utils import text_to_owo , notify_user

intents = discord.Intents.all()

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.sleeping = {}
        self.sleep_sec = {}
        self.sleeping_db = {}
        self.sleeped.start()
    #        self.sleeped_delete.start()
    
    def cog_unload(self):
        self.sleeped.cancel()
    #        self.sleeped_delete.cancel()

    #    @tasks.loop(minutes=2)
    #    async def sleeped_delete(self):
    #        for key in self.sleeping.keys():
    #            if self.sleeping[key]["time"] is None:
    #                self.sleeping = {}
    #                print(f"deleted {self.sleeping}")
    
    #    @sleeped_delete.before_loop
    #    async def before_sleeped_delete(self):
    #        await self.bot.wait_until_ready()
        
    @tasks.loop(minutes=1)
    async def sleeped(self):
        guild = self.bot.get_guild(MYGUILD)
    #        for key in self.sleeping.keys():
    #            dt = datetime.now(timezone.utc).strftime("%d, %m ,%Y, %H, %M")
    #            print(self.sleeping[key]["time"] , dt)
    #            if self.sleeping[key]["time"] is None:
    #                return print("time != dt")
    #            if self.sleeping[key]["time"] < dt:
    #                member_sleep = guild.get_member(key)
    #                if member_sleep is None:
    #                    return
    #                self.sleeping[key]["time"] = None
    #                await member_sleep.move_to(channel=None)

        data = utils.json_loader.read_json("sleeping")
        if not data:
            return #print("data = None")
        for key in data.keys():
            dt = datetime.now(timezone.utc).strftime("%d%m%Y%H%M")
            if data[key]["time"] is None:
                return #print(f"time = None {data}")
            elif int(data[key]["time"]) == int(dt):
                print(data[key]['time'])
                member_sleep = guild.get_member(int(key))
                if member_sleep:
                    try:
                        await member_sleep.move_to(channel=None)
                        data[key]["time"] = None
                        utils.json_loader.write_json(data, "sleeping")
                    except:
                        return print("error sleep")
            
    #        delete_dt = datetime.now(timezone.utc).strftime("%M")
    #        if delete_dt == "00":
    #            self.sleeping_db = {}
    #            print("deleted")

    #        delete_dt = datetime.now(timezone.utc).strftime("%M")
    #        if delete_dt == "00":
    #            if self.sleeping[key]["time"] is None:
    #                self.sleeping = {}
    #                print(f"deleted {self.sleeping}")
    #            else:
    #                print("sleep is have data")
                      
    @sleeped.before_loop
    async def before_sleeped(self):
        await self.bot.wait_until_ready()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
    
    @commands.command(name="pastel" , description="pastel color")
    async def pastel(self, ctx):
        await ctx.send("https://colorhunt.co/palettes/pastel")
    
    @commands.command(name="color", description="color hex")
    async def color(self, ctx):
        await ctx.send("https://www.color-hex.com/")

    @commands.command(description="Any message to owo",help="drink latte" , usage="<message>")
    @commands.guild_only()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))
    
    @commands.command(description="Poke", help="@latte" , usage="<member>")
    @commands.guild_only()
    @commands.is_owner()
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")
        
    #custom_cooldown
    def custom_cooldown(message):
        if discord.utils.get(message.author.roles, name="Mystic・・ ♡"):
            return commands.Cooldown(5, 60)  # 5 per minute
        return commands.Cooldown(2, 60)  # 2
                
    @commands.group(invoke_without_command=True , aliases=["sl" , "slp"], help="25min", usage="<duration> [member]")
    @commands.dynamic_cooldown(custom_cooldown, commands.BucketType.user)
    async def sleep(self, ctx, time=None,*, member : discord.Member=None):
        if time is None:
            embed_time = discord.Embed(description=f"**Please specify duration** : `(s|m|h|d)`\n```yaml\nExample : {PREFIX}sleep 5m , {PREFIX}sleep 2h\nDelete : {PREFIX}sleep stop [member]```",color=WHITE)
            return await ctx.send(embed=embed_time , delete_after=15)      
        if member is None:
            member = ctx.author

        timewait = utils.FutureTime_converter(time)
        futuredate = datetime.now(timezone.utc) + timedelta(seconds=timewait) 
        futuredate2 = futuredate + timedelta(seconds=25200)
        futuredate_ = futuredate.strftime("%d%m%Y%H%M")

        embed = discord.Embed(color=YELLOW)
        embed.add_field(name="Datetime sleep:", value=f"{utils.format_dt(futuredate)}" , inline=False)
        if member.avatar.url is not None:
            embed.set_footer(text=member , icon_url=member.avatar.url)
        else:
            embed.set_footer(text=member)

        m = await ctx.send(embed=embed)

        await m.add_reaction("<:greentick:881500884725547021>")
        await m.add_reaction("<:redtick:881500898273144852>")

        try:
            reaction , user = await self.bot.wait_for(
                "reaction_add",
                timeout=30,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )

        except asyncio.TimeoutError:
            embed_t = discord.Embed(description="Confirmation Failure. Please try again." , color=0xffffff)
            await ctx.send(embed=embed_t, delete_after=15)
            await m.delete()
            return

        if str(reaction.emoji) not in ["<:greentick:881500884725547021>", "<:redtick:881500898273144852>"] or str(reaction.emoji) == "<:redtick:881500898273144852>":
            embed_c = discord.Embed(description="Cancelling sleep time!" , color=0xffffff)
            await ctx.send(embed=embed_c , delete_after=10)
            await m.delete()
            await ctx.message.delete()
            return

        await m.clear_reactions()
        
        embed_edit = discord.Embed(color=member.colour , timestamp=futuredate)
        embed_edit.description = f"**TIME TO SLEEP** <a:b_hitopotatosleep:864921119538937968>\n{utils.format_relative(futuredate)}"
        if member.avatar.url is not None:
            embed_edit.set_footer(text=member , icon_url=member.avatar.url)
        else:
            embed_edit.set_footer(text=member)
        
        if timewait > 600:
            if member == ctx.author:
                embed_edit.description += f"\n||**Stoped timer** : {PREFIX}sleep stop||"
            if ctx.author != member:
                embed_edit.description += f"\n||**Stoped timer** : {PREFIX}sleep stop @{member.display_name}||"
            await m.edit(embed=embed_edit)
            self.sleeping_db[str(member.id)] = {"time": futuredate_}
            with open("bot_config/sleeping.json", "w") as fp:
                json.dump(self.sleeping_db, fp , indent=4)
        else:
            embed_edit.description += f"\n__||Timer can't be stopped.||__"
            await m.edit(embed=embed_edit)
            await asyncio.sleep(timewait)
            await member.move_to(channel=None)
    

    @sleep.command(invoke_without_command=True , aliases=["del", "delete" , "off" , "stop"], help="stop", usage="[member]")
    async def sleep_stop(self, ctx, *, member: discord.Member=None):
        if member is None:
            member = ctx.author

        data = utils.read_json("sleeping")
        check_data = data[str(member.id)]["time"]

        if check_data is not None:
            try:
                data[str(member.id)]["time"] = None
                utils.json_loader.write_json(data, "sleeping")
                embed = discord.Embed(description=f"{member.mention} : sleep timer stoped" , color=WHITE)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(description="Error stop timer" , color=BRIGHTRINK)
                await ctx.send(embed=embed)
                return
        else:
            em_error = discord.Embed(description=f"**{member}** : sleep timer not found", color=WHITE)
            await ctx.send(embed=em_error)
    
    # @commands.command(name="sldb")
    # async def sleep_db(self, ctx, time,*, member : discord.Member=None):
    #     if not time:
    #         return         
    #     if member is None:
    #         member = ctx.author
        
    #     #time
    #     timewait = utils.FutureTime_converter(time)
    #     futuredate = datetime.now(timezone.utc) + timedelta(seconds=timewait)
    #     futuredate_utc7 = futuredate + timedelta(seconds=25200)
    #     futuredate_ = futuredate.strftime("%d%m%Y%H%M")
        
    #     data = await self.bot.sleepdb.find_by_custom({"member_id": member.id})
    #     if data is None:
    #         data = {
    #             "member_id": member.id,
    #             "timer": futuredate_
    #         }
    #     data["timer"] = futuredate_
    #     await self.bot.sleepdb.update_by_custom(
    #         {"member_id": member.id}, data
    #     )

    #     embed_edit = discord.Embed(color=PTGREEN , timestamp=futuredate)
    #     embed_edit.description = f"**time to sleep** <a:b_hitopotatosleep:864921119538937968>\n{utils.format_dt(futuredate_utc7)}"
    #     embed_edit.set_footer(text=f"{member.name}" , icon_url=member.avatar.url)
    #     if ctx.author != member:
    #         embed_edit.description += f"\n||Req by : {ctx.author.mention}||"
    #     await ctx.send("sleep db")
        
    @commands.command(aliases=["fake"] , help="holamyfrient", usage="<message>")
    @commands.guild_only()
    async def saybot(self , ctx , *, msg):
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=ctx.author.display_name)
        if ctx.author.avatar.url is not None:
            await webhook.send(msg, username=ctx.author.name, avatar_url=ctx.author.avatar.url)
        else:
            await webhook.send(msg, username=ctx.author.name)
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
    
    @commands.command(aliases=["fakem","saybotm"] , help="@Latte iloveyou", usage="<member> <message>")
    @commands.guild_only()
    async def saybot_member(self , ctx , member:discord.Member=None,*, msg):
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=member.display_name)
        if member.avatar.url is not None:
            await webhook.send(msg, username=member.display_name, avatar_url=member.avatar.url)
        else:
            await webhook.send(msg, username=member.display_name)
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
    
    # @commands.command()
    # async def test_webwook(self, ctx ,*, msg):
    #     async with aiohttp.ClientSession() as session:
    #         webhook = discord.Webhook.partial(881116610453180437,"Ljuzp58fs8zH9MSThtwOko5XGSAqPWg9Qt9OzYjAEMYJ0mp_5SbpgoQdOXaqw2sCZk1Y",session=session)
    #         await webhook.send(msg, username=ctx.message.author.name , avatar_url=ctx.message.author.avatar.url)
    
    @commands.command(aliases=["temprole","tr"])
    @commands.guild_only()
    async def t_role(self , ctx ,*, member: discord.Member=None):
        if ctx.guild.id == MYGUILD:
            if not member:
                member = ctx.author
            role = discord.utils.get(ctx.guild.roles, id = 879258879987449867)
            member_role = discord.utils.get(member.roles, id = 879258879987449867)
            if member_role:
                embed_role = discord.Embed(description=f"{member.name} is already a temp role!", color=WHITE)
                return await ctx.send(embed=embed_role , delete_after=10)
            await member.add_roles(role)
            embed = discord.Embed(description="temp is ready" , color=WHITE)
            await ctx.send(embed=embed , delete_after=10)
            await asyncio.sleep(43200)
            await member.remove_roles(role)

    @commands.command(name="apex")
    @commands.guild_only()
    async def apex_weapon(self, ctx, category=None):
        
        #converter_from_utils.game_converter
        await ctx.send(embed=utils.apex_random_weapon(category))
    
    @commands.group(invoke_without_command=True, name="valorant" , aliases=["vlr"] , usage="<type : agent , weapon >")
    @commands.guild_only()
    async def valorant(self, ctx):
        embed = discord.Embed(
            title="Valorant random",
            color=0xffffff
        )
        embed.add_field(name="Agent", value=f"```yaml\nUsage: {PREFIX}vlr agent [type]\nType: Duelist, Controller, Initiator, Sentinel```",inline=False)
        embed.add_field(name="Weapon", value=f"```yaml\nUsage: {PREFIX}vlr weapon [type]\nType: sidearm, smg, shotgun, rifle, sniper, machine gun ```",inline=False)

        await ctx.send(embed=embed)

    @valorant.command(invoke_without_command=True, name="agent", aliases=["a"])
    @commands.guild_only()
    async def agent(self, ctx, category=None):

        #converter_from_utils.game_converter
        await ctx.send(embed=utils.valorant_random_agent(category))

    @valorant.command(name="weapon" , aliases=["gun","w"])
    @commands.guild_only()
    async def weapon(self, ctx, *,category=None):
        
        #converter_from_utils.game_converter
        await ctx.send(embed=utils.valorant_random_weapon(category))
    
def setup(bot):
    bot.add_cog(Fun(bot))