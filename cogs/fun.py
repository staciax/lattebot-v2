# Standard
import discord , datetime , time , asyncio , re 
from discord.ext import commands , tasks
import time
import datetime
from datetime import datetime, timezone , timedelta

# Third party
import json
from json import JSONEncoder
import io
import aiohttp , random , anime_images_api , requests
anime = anime_images_api.Anime_Images()
import typing , unicodedata
from typing import Union
import humanize

# Local
from config import *
import utils
from utils import text_to_owo , notify_user

intents = discord.Intents.all()

class Fun(commands.Cog):

    def __init__(self, client):
        self.bot = client
        self.client = client
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
        guild = self.client.get_guild(MYGUILD)
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
    
    @commands.command(name="pastel" , description="pastel color" , usage=f"{PREFIX}pastel" , brief=f"{PREFIX}pastel")
    async def pastel(self, ctx):
        await ctx.send("https://colorhunt.co/palettes/pastel")
    
    @commands.command(name="color", description="color hex", usage=f"{PREFIX}color", brief=f"{PREFIX}color")
    async def color(self, ctx):
        await ctx.send("https://www.color-hex.com/")

    @commands.command(description="Any message to owo",brief=f"{PREFIX}owo drink latte" , usage=f"{PREFIX}owo <message>")
    @commands.guild_only()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))
    
    @commands.command(description="Poke",brief=f"{PREFIX}poke @latte" , usage=f"{PREFIX}poke <member>")
    @commands.guild_only()
    @commands.is_owner()
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")
    
    @commands.command(description="Random picture of a meow",brief=f"{PREFIX}cat", usage=f"{PREFIX}cat")
    @commands.guild_only()
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow" , color=0xffffff)
                    embed.set_image(url=data['file'])

                    await ctx.send(embed=embed)
    
    @commands.command(description="Random picture of a floofy" , brief=f"{PREFIX}fox", usage=f"{PREFIX}fox")
    @commands.guild_only()
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Fox", color=0xffffff)
                    embed.set_image(url=data['image'])

                    await ctx.send(embed=embed)

    @commands.command(description="Random gif of anime", brief=f"{PREFIX}anime", usage=f"{PREFIX}anime")
    @commands.guild_only()
    async def ani(self, ctx):
        embed = discord.Embed(color=0xffffff)
        img_list = ['hug', 'kiss', 'cuddle', 'pat', 'kill', 'slap', 'wink']
        img_random = random.choice(img_list)
        try:
            img_link = anime.get_sfw(f"{img_random}")
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)
        except:
            return

    @commands.command(name="hug" , brief=f"{PREFIX}hug", usage=f"{PREFIX}hug")
    @commands.guild_only()
    async def anime_hug(self, ctx):
        embed = discord.Embed(color=0xffffff)
        try:     
            img_link = anime.get_sfw("hug")
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)
        except:
            return
    
    @commands.command(name="kiss", brief=f"{PREFIX}kiss", usage=f"{PREFIX}kiss")
    @commands.guild_only()
    async def anime_kiss(self, ctx):
        embed = discord.Embed(color=0xffffff)
        try:     
            img_link = anime.get_sfw("kiss")
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)
        except:
            return
    
    @commands.command(name="cuddle", brief=f"{PREFIX}cuddle", usage=f"{PREFIX}cuddle")
    @commands.guild_only()
    async def anime_cuddle(self, ctx):
        embed = discord.Embed(color=0xffffff)
        try:     
            img_link = anime.get_sfw("cuddle")
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)
        except:
            return
    
    @commands.command(name="pat", brief=f"{PREFIX}pat", usage=f"{PREFIX}pat")
    @commands.guild_only()
    async def anime_pat(self, ctx):
        embed = discord.Embed(color=0xffffff)
        try:     
            img_link = anime.get_sfw("pat")
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)
        except:
            return
    
    @commands.command(name="kill", brief=f"{PREFIX}kill", usage=f"{PREFIX}kill")
    @commands.guild_only()
    async def anime_kill(self, ctx):
        embed = discord.Embed(color=0xffffff)
        try:     
            img_link = anime.get_sfw("kill")
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)
        except:
            return
    
    @commands.command(name="slap", brief=f"{PREFIX}slap", usage=f"{PREFIX}slap")
    @commands.guild_only()
    async def anime_slap(self, ctx):
        embed = discord.Embed(color=0xffffff)
        try:     
            img_link = anime.get_sfw("slap")
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)
        except:
            return
    
    @commands.command(name="wink", brief=f"{PREFIX}.wink", usage=f"{PREFIX}wink")
    @commands.guild_only()
    async def anime_wink(self, ctx):
        embed = discord.Embed(color=0xffffff)
        try:     
            img_link = anime.get_sfw("wink")
            embed.set_image(url=img_link)
            await ctx.send(embed=embed)
        except:
            return
    
    @commands.command(aliases=['nsfw'], brief=f"{PREFIX}nsfw", usage=f"{PREFIX}nsfw")
    @commands.guild_only()
    async def anime_nsfw(self, ctx):
            try:
                if ctx.channel.is_nsfw():
                    embed = discord.Embed(color=0xffffff)
                    img_list = ['hentai', 'boobs']
                    nsfw_random = random.choice(img_list)
                    nsfw_url = anime.get_nsfw(f"{nsfw_random}")
                    embed.set_image(url=nsfw_url)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(color=0xffffff)
                    embed.description = "This is not a NSFW channel, **NSFW** is alollowed in <#850507964938715196>"
                    await ctx.send(embed=embed , delete_after=15)          
            except:
                return
    
    @commands.command(aliases=['gif'], brief=f"{PREFIX}hentai aqua", usage=f"{PREFIX}hentai [search]")
    @commands.guild_only()
    async def giphy(self, ctx, *, search=None):
        gipht_apis = self.client.giphy_api_
        embed = discord.Embed(colour=0xffffff)
        session = aiohttp.ClientSession()
        if search == None:
            response = await session.get(f'https://api.giphy.com/v1/gifs/random?api_key={gipht_apis}')
            data = json.loads(await response.text())
            embed.set_image(url=data['data']['images']['original']['url'])
        else:
            search.replace(' ', '+')
            response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + f'&api_key={gipht_apis}&limit=10')
            data = json.loads(await response.text())
            gif_choice = random.randint(0, 9)
            embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

        await session.close()

        await ctx.send(embed=embed)
    
    #custom_cooldown
    def custom_cooldown(message):
        if discord.utils.get(message.author.roles, name="Mystic・・ ♡"):
            return commands.Cooldown(5, 60)  # 5 per minute
        return commands.Cooldown(2, 60)  # 2
                
    @commands.group(invoke_without_command=True , aliases=["sl" , "slp"], brief=f"{PREFIX}sleep 25min\n{PREFIX}sleep 1h @latte", usage=f"{PREFIX}sleep <duration> [member]\n{PREFIX}sleep stop [member]")
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
        embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)

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
        embed_edit.set_footer(text=f"{member.name}" , icon_url=member.avatar.url)
        
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
    

    @sleep.command(invoke_without_command=True , aliases=["del", "delete" , "off" , "stop"], brief=f"{PREFIX}sleep stop\n{PREFIX}sleep stop @latte", usage=f"{PREFIX}sleep stop [member]")
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
    
    @commands.command(name="sldb")
    async def sleep_db(self, ctx, time,*, member : discord.Member=None):
        if not time:
            return         
        if member is None:
            member = ctx.author
        
        #time
        timewait = utils.FutureTime_converter(time)
        futuredate = datetime.now(timezone.utc) + timedelta(seconds=timewait)
        futuredate_utc7 = futuredate + timedelta(seconds=25200)
        futuredate_ = futuredate.strftime("%d%m%Y%H%M")
        
        data = await self.client.sleepdb.find_by_custom({"member_id": member.id})
        if data is None:
            data = {
                "member_id": member.id,
                "timer": futuredate_
            }
        data["timer"] = futuredate_
        await self.client.sleepdb.update_by_custom(
            {"member_id": member.id}, data
        )

        embed_edit = discord.Embed(color=PTGREEN , timestamp=futuredate)
        embed_edit.description = f"**time to sleep** <a:b_hitopotatosleep:864921119538937968>\n{utils.format_dt(futuredate_utc7)}"
        embed_edit.set_footer(text=f"{member.name}" , icon_url=member.avatar.url)
        if ctx.author != member:
            embed_edit.description += f"\n||Req by : {ctx.author.mention}||"
        await ctx.send("sleep db")
        
    @commands.command(aliases=["fake"] , brief=f"{PREFIX}saybot holamyfrient", usage=f"{PREFIX}saybot <message>")
    @commands.guild_only()
    @commands.has_role(mystic_role)
    async def saybot(self , ctx , *, msg):
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=ctx.author.display_name)
        await webhook.send(msg, username=ctx.author.name, avatar_url=ctx.author.avatar.url)
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
    
    @commands.command(aliases=["fakem","saybotm"] , brief=f"{PREFIX}saybotm <member> iloveyou", usage=f"{PREFIX}saybotm <member> [member]")
    @commands.guild_only()
    @commands.has_role(mystic_role)
    async def saybot_member(self , ctx , member:discord.Member=None,*, msg):
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=member.display_name)
        await webhook.send(msg, username=member.display_name, avatar_url=member.avatar.url)
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
    
    @commands.command()
    async def test_webwook(self, ctx ,*, msg):
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.partial(881116610453180437,"Ljuzp58fs8zH9MSThtwOko5XGSAqPWg9Qt9OzYjAEMYJ0mp_5SbpgoQdOXaqw2sCZk1Y",session=session)
            await webhook.send(msg, username=ctx.message.author.name , avatar_url=ctx.message.author.avatar.url)
    
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
    
    @commands.group(invoke_without_command=True, name="valorant" , aliases=["vlr"])
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
    
def setup(client):
    client.add_cog(Fun(client))