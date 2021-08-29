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
    
    @commands.command(name="pastel" , description="pastel color")
    async def pastel(self, ctx):
        await ctx.send("https://colorhunt.co/palettes/pastel")
    
    @commands.command(name="color", description="color hex")
    async def color(self, ctx):
        await ctx.send("https://www.color-hex.com/")

    @commands.command(brief="Any message to owo")
    @commands.guild_only()
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))
    
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")
    
    @commands.command(brief="Random picture of a meow")
    @commands.guild_only()
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow" , color=0xffffff)
                    embed.set_image(url=data['file'])

                    await ctx.send(embed=embed)
    
    @commands.command(brief="Random picture of a floofy")
    @commands.guild_only()
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Fox", color=0xffffff)
                    embed.set_image(url=data['image'])

                    await ctx.send(embed=embed)

    @commands.command(aliases=['ani', 'anigif'])
    @commands.guild_only()
    async def anime_img(self, ctx , category=None):
            embed = discord.Embed(color=0xffffff)
            try:
                if category == None:
                    img_list = ['hug', 'kiss', 'cuddle', 'pat', 'kill', 'slap', 'wink']
                    img_random = random.choice(img_list)
                    img_link = anime.get_sfw(f"{img_random}")
                    embed.set_image(url=img_link)
                    await ctx.send(embed=embed)
                elif category == "list":
                    embed.description = "**Caterogy** : hug, kiss, cuddle, pat, kill, slap, wink , hentai\n**Example** : `lt ani hug` , `lt ani kiss`"
                    await ctx.send(embed=embed)
                elif category == "hentai":
                    if ctx.channel.is_nsfw():
                        img_list = ['hentai', 'boobs']
                        nsfw_random = random.choice(img_list)
                        nsfw_url = anime.get_nsfw(f"{nsfw_random}")
                        embed.set_image(url=nsfw_url)
                        await ctx.send(embed=embed)
                    else:
                        embed.description = "This is not a NSFW channel, **NSFW** is alollowed in <#850507964938715196>"
                        await ctx.send(embed=embed, delete_after=15)        
                else:
                    img_link = anime.get_sfw(f"{category}")
                    embed.set_image(url=img_link)
                    await ctx.send(embed=embed)
            except:
                return

    @commands.command(aliases=['hentai', 'nsfw'])
    @commands.guild_only()
    async def anime_img_nsfw(self, ctx):
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
    
    @commands.command(aliases=['gif'])
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
    
    @commands.command(name="rn", brief="takes smallest and largest numbers then does a random number between.")
    @commands.guild_only()
    async def random_number(self , ctx , *numbers: typing.Union[int,str]):
        numbers=sorted(list(filter(lambda x: isinstance(x, int), numbers)))
        if len(numbers) < 2:
            await ctx.send("Not enough numbers")

        else:
            embed = discord.Embed(title=f"Random Number: {random.randint(numbers[0],numbers[-1])} ",color=random.randint(0, 16777215))
            embed.add_field(name="Lowest Number:",value=f"{numbers[0]}")
            embed.add_field(name="Highest Number:",value=f"{numbers[-1]}")
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.guild_only()
    async def poll(self, ctx,*,message):
        embed = discord.Embed(title="POLL", description=f"{message}",color=0xffffff)
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction(f'{utils.emoji_converter("check")}')
        await msg.add_reaction(f'{utils.emoji_converter("xmark")}')
        await ctx.message.delete()
            
    @commands.command()
    async def sleep_temp(self, ctx, time,*, member : discord.Member=None):
        if not time:
            return
        if member is None:
            member = ctx.author

        timewait = utils.FutureTime_converter(time)
        futuredate = datetime.now(timezone.utc) + timedelta(seconds=timewait)
        futuredate2 = futuredate + timedelta(seconds=25200)
        futuredate_ = futuredate.strftime("%d, %m ,%Y, %H, %M")
        futuredate_2 = futuredate.strftime("%d-%B-%Y-%H-%M")

        self.sleeping[member.id] = {"time": futuredate_}

        embed = discord.Embed(color=YELLOW)
        embed.description = f"```Member: {member.name}\nDate : {futuredate2.strftime('%d %B %Y')}\nTime : {futuredate2.strftime('%H:%M')}```"

        m = await ctx.send(embed=embed)

        await m.add_reaction("<:greentick:881500884725547021>")
        await m.add_reaction("<:redtick:881500898273144852>")

        try:
            reaction , member = await self.bot.wait_for(
                "reaction_add",
                timeout=30,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )

        except asyncio.TimeoutError:
            await ctx.send("Confirmation Failure. Please try again.")
            return

        if str(reaction.emoji) not in ["<:greentick:881500884725547021>", "<:redtick:881500898273144852>"] or str(reaction.emoji) == "<:redtick:881500898273144852>":
            await ctx.send("cancelling sleep time!")
            return

        await m.clear_reactions()
        
        embed_edit = discord.Embed(color=PTGREEN , timestamp=futuredate)
        embed_edit.description = f"time to sleep <a:b_hitopotatosleep:864921119538937968>"
        embed_edit.set_footer(text=f"{member.name}" , icon_url=member.avatar.url)
        
        await m.edit(embed=embed_edit)

        self.sleeping[member.id] = {"time": str(futuredate_)}
    
    @commands.group(invoke_without_command=True , aliases=["sl" , "slp"])
    async def sleep(self, ctx, time,*, member : discord.Member=None):
        if not time:
            return         
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
            await ctx.send(embed=embed_t, delete_after=10)
            return

        if str(reaction.emoji) not in ["<:greentick:881500884725547021>", "<:redtick:881500898273144852>"] or str(reaction.emoji) == "<:redtick:881500898273144852>":
            embed_c = discord.Embed(description="Cancelling sleep time!" , color=0xffffff)
            await ctx.send(embed=embed_c , delete_after=10)
            await m.delete()
            await ctx.message.delete()
            return

        await m.clear_reactions()
        
        embed_edit = discord.Embed(color=PTGREEN , timestamp=futuredate)
        embed_edit.description = f"**time to sleep** <a:b_hitopotatosleep:864921119538937968>\n{utils.format_relative(futuredate)}"
        embed_edit.set_footer(text=f"{member.name}" , icon_url=member.avatar.url)
        if ctx.author != member:
            embed_edit.description += f"\n||Req by : {ctx.author.mention}||"
        
        await m.edit(embed=embed_edit)

        self.sleeping_db[str(member.id)] = {"time": futuredate_}
        with open("bot_config/sleeping.json", "w") as fp:
            json.dump(self.sleeping_db, fp , indent=4)
    

    @sleep.command(invoke_without_command=True , aliases=["del", "delete" , "off" , "stop"])
    async def sleep_delete(self, ctx, *, member: discord.Member=None):
        if member is None:
            member = ctx.author

        data = utils.read_json("sleeping")
        data[str(member.id)]["time"] = None

        try:
            utils.json_loader.write_json(data, "sleeping")
            embed = discord.Embed(description=f"{member.mention} : sleep timer deleted" , color=WHITE)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(description="Error timer deleted" , color=BRIGHTRINK)
            await ctx.send(embed=embed)
            return
    
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
        
    @commands.command(aliases=["fake"])
    @commands.guild_only()
    @commands.has_role(842304286737956876)
    async def saybot(self , ctx , msg):
        await ctx.message.delete()
        webhook = await ctx.channel.create_webhook(name=ctx.author.name)
        await webhook.send(msg, username=ctx.author.name, avatar_url=ctx.author.avatar.url)
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
    
    @commands.command(aliases=["fakem"])
    @commands.guild_only()
    @commands.has_role(842304286737956876)
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
    async def t(self , ctx ,*, member: discord.Member=None):
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
    
def setup(client):
    client.add_cog(Fun(client))