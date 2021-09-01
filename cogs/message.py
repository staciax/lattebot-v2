# Standard 
import discord , json , re , asyncio
from discord.ext import commands
from datetime import datetime, timezone
from re import search

# Third party
import io
import aiohttp

# Local
import utils
import utils.json_loader
from utils import create_voice_channel , get_channel_by_name , get_category_by_name
from config import *

class Message(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        self.links_allowed = ()

    @commands.Cog.listener()
    async def on_ready(self):
        self.afk = {}
        self.sniped_message = {}
        self.sniped_text = {}
        self.sniped_img = {}
        print(f"-{self.__class__.__name__}")

    @commands.command() 
    @commands.guild_only()
    async def afk(self, ctx, *, reason=None):
        if reason is None:
            reason = "personal problems"
        self.afk[ctx.author.id] = reason #storing at self.afk as {657846039914479617: "reason"}
        embed = discord.Embed(description=f"I have set your afk: {reason}" , color=WHITE)
        m = await ctx.send(embed=embed)#, delete_after=10)
        if ctx.channel.id == 861883647070437386:
            await asyncio.sleep(10)
            await m.delete()
            await ctx.message.delete()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        #only_image_channel
        data = utils.json_loader.read_json("latte")
        only_image = data["only-image"]
        if message.channel.id == only_image:
            if message.content:
                if message.content and message.attachments:
                    return
                elif message.content:
                    await message.delete()
        
        #only_link_channel
        data = utils.json_loader.read_json("latte")
        only_link = data["only-link"]
        if message.channel.id == only_link:
            if search(self.url_regex, message.content):
                return
            else:
                await message.delete()

        #afk
        if message.content.startswith("lt afk"):
            return
        if message.content.startswith("l afk"):
            return
        if message.content.startswith(".afk"):
            return
        for id in self.afk.keys():
            if message.author.id == id:
                del self.afk[id]
                return await message.channel.send(f"{message.author.mention}, welcome back onii-chan!" , delete_after=10)
            
            member = message.guild.get_member(id)
            if member.mentioned_in(message):
                embed = discord.Embed(description=f'**{member.display_name}** is afk for: {self.afk[id]}' , color=WHITE)
#                embed.set_image(url="https://media.giphy.com/media/LPETDRbj82wbrYm7q6/source.gif")
                await message.channel.send(embed=embed , delete_after=10)

        #message
        if message.content.startswith('latte'):
            await message.delete()
            await message.channel.send('เอะ! เรียกเราหรอ?  <:S_CuteGWave3:859660565160001537>')
        
        if message.content.startswith('invite'):
            await message.delete()
            await message.channel.send('https://discord.gg/bvwpZ2B4rj' , delete_after=15)
        
        if message.content.startswith('tempinvite'):
            await message.delete()
            await message.channel.send('https://discord.gg/f6adY5B8k2' , delete_after=15)

        if message.content.startswith('it'):
            await message.channel.send(f"This is my prefix `.` or `lt ` or `l `\nexample : `lt help` or `l help` or `.help`", delete_after=10)
        
        #temp_channel
        if message.content.startswith('uw'):
            if message.author.voice:
                chname = "ᵁᴺᴰᴱᴿᵂᴼᴿᴸᴰ"
                checkvoice = get_channel_by_name(message.channel.guild, channel_name=chname)
                if checkvoice is None:
                    channel = await create_voice_channel(message.channel.guild, f'{chname}'.lower() , category_name="୨ ♡ ─ 「 Private 」♡")
                    
                    if channel is not None:
                        await message.author.move_to(channel)
                        await message.delete()
                    
                else:
                    await message.author.move_to(checkvoice)
                    await message.delete()
            else:
                await message.delete()

        #when_mention_bot
        if self.client.user.mentioned_in(message):
            await message.channel.send(f"This is my prefix `.` \nExample: .help", delete_after=15)

        #temp_channel
        if message.channel.id == TEMP_CH:
            await asyncio.sleep(60)
            await message.delete()
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.embeds:
            return
        #snipe_message
        if message.guild.id == MYGUILD:
            #.
            if message.content.startswith('.sni'):
                return
            if message.content.startswith('.snipe'):
                return
            if message.content.startswith('.blackmail'):
                return

            #l
            if message.content.startswith('l sni'):
                return
            if message.content.startswith('l snipe'):
                return
            if message.content.startswith('l blackmail'):
                return

            #lt
            if message.content.startswith('lt sni'):
                return
            if message.content.startswith('lt snipe'):
                return
            if message.content.startswith('lt blackmail'):
                return
            
            if message.author == self.client.user:
                return
            if message.content:
                self.sniped_text[message.guild.id] = (message.content, message.author, message.channel.mention, message.created_at)

            if message.attachments:
                image = message.attachments[0].proxy_url
                self.sniped_img[message.guild.id] = (image , message.author, message.channel.mention, message.created_at)
            else:
                image = "none"

            self.sniped_message[message.guild.id] = (image , message.content, message.author, message.channel.mention, message.created_at)

            #message.channel.id or message.guild.id

            #snipe_time_delete
            data = utils.json_loader.read_json("latte")
            snipe_time = data["snipe-time"]
            if snipe_time:
                await asyncio.sleep(snipe_time)
                self.sniped_text[message.guild.id] = None
                self.sniped_img[message.guild.id] = None
                self.sniped_message[message.guild.id] = None
                print("deleted")
        else:
            return
            
    @commands.command(name="snipe", aliases=["sni", "blackmail"] ,description="snipe message and image")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def snipe(self , ctx , choice=None):
        embed = discord.Embed(description= "" ,color=0xffffff)
        text_aliases = ["t", "text"]
        images_aliases = ["i", "image" , "images"]

        data = utils.json_loader.read_json("latte")
        sniped_time = data["sniped"]
        if choice == None:
            if self.sniped_message:
                try:
                    image , content , author , channel_name, time = self.sniped_message[ctx.guild.id]
                except:
                    await ctx.channel.send("Couldn't find a message to snipe!")
                    return
                if image == "none":
                    embed.description += f"**Deleted in:** {channel_name}\n**Content:** {content}"
                    embed.timestamp = time
                    embed.set_author(name=f"{author.name}#{author.discriminator}" , icon_url=author.avatar.url)
                    embed.set_footer(text=f"Message delete")
                    if sniped_time:
                        await ctx.channel.send(embed=embed , delete_after=sniped_time)
                    else:
                        await ctx.channel.send(embed=embed)
                else:
                    if content:
                        content_check = f"\n**Content:** ```{content}```"
                    else:
                        content_check = ""
                    embed.description += f"**Deleted in:** {channel_name}{content_check}\n**Attachments :** [**URL**]({image})"
                    embed.timestamp = time
                    try:
                        embed.set_image(url=image)
                    except:
                        pass
                    embed.set_author(name=f"{author.name}#{author.discriminator}" , icon_url=author.avatar.url)
                    embed.set_footer(text=f"Message delete")

                    if sniped_time:
                        await ctx.channel.send(embed=embed , delete_after=sniped_time)
                    else:
                        await ctx.channel.send(embed=embed)
            else:
                await ctx.channel.send("Couldn't find a message to snipe!" , delete_after=15)
                return

        elif choice in images_aliases: #snipe image
            try:
                image , author , channel_name, time = self.sniped_img[ctx.guild.id]
            except:
                await ctx.channel.send("Couldn't find a message to snipe!", delete_after=15)
                return

            embed = discord.Embed(description=f"**Deleted in:** {channel_name}\n**Attachments :** [**URL**]({image})",color=0xffffff , timestamp=time)
            try:
                embed.set_image(url=image)
            except:
                pass
            embed.set_author(name=f"{author.name}#{author.discriminator}" , icon_url=author.avatar.url)
            embed.set_footer(text=f"Message delete")
            if sniped_time:
                await ctx.channel.send(embed=embed , delete_after=sniped_time)
            else:
                await ctx.channel.send(embed=embed)
  
        elif choice in text_aliases: #snipe text
            try:
                content , author , channel_name, time = self.sniped_text[ctx.guild.id]
            except:
                await ctx.channel.send("Couldn't find a message to snipe!", delete_after=15)
                return
                
            embed = discord.Embed(description=f"**Deleted in:** {channel_name}\n**Content:** ```{content}```" , color=0xffffff , timestamp=time)
            embed.set_author(name=f"{author.name}#{author.discriminator}" , icon_url=author.avatar.url)
            embed.set_footer(text=f"Message delete")
            if sniped_time:
                await ctx.channel.send(embed=embed , delete_after=sniped_time)
            else:
                await ctx.channel.send(embed=embed)

    @commands.command(name='dm' , description="direct message user")
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def botdm(self, ctx, user: discord.Member=None,* , args=None):       
        if user != None and args != None:
            try:
                embed = discord.Embed(title="",description=f"** **\nMessage : `{args}`\n\n** **",color=0xFFFFFF,timestamp=datetime.now(timezone.utc))
                embed.set_footer(text=f"{self.client.user.name}" , icon_url = self.client.user.avatar.url)
                embed.set_author(name=f"{ctx.guild.name} | Direct Message", icon_url= ctx.guild.icon.url)

                embedsc = discord.Embed(title=f"{self.client.user.name} | Direct Message",description=f"Bot has been sent message to `{user.name}#{user.discriminator}`\n\nMessage : `{args}`\n\n",color=0xFFFFFF,timestamp=datetime.now(timezone.utc))
                embedsc.set_footer(text=f"Req by {ctx.guild.name} " , icon_url = ctx.guild.icon.url)
                await user.send(embed=embed)
                await ctx.channel.send(embed=embedsc)

            except:
                embed = discord.Embed(description="Couldn't dm the given user.", color=0xffffff)
                await ctx.channel.send(embed)
        
        else:
            embed = discord.Embed(description="You didn't provide a user's id and/or a message.", color=0xffffff)
            await ctx.channel.send(embed=embed)
        
def setup(client):
    client.add_cog(Message(client))