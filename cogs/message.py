# Standard 
import discord
from discord.ext import commands
from datetime import datetime, timezone
import asyncio

# Third party
import io
import aiohttp

# Local
import utils
from utils import create_voice_channel , get_channel_by_name , get_category_by_name
from config import *

class Message(commands.Cog):

    def __init__(self, client):
        self.client = client

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
        await ctx.send(embed=embed, delete_after=10) 
        await asyncio.sleep(10)
        await ctx.message.delete()

    @commands.command()
    async def latte(self, ctx):
        await ctx.send('เราชอบกินลาเต้นะ')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.startswith("lt afk"):
            return
        if message.content.startswith("l afk"):
            return
        for id in self.afk.keys():
            if message.author.id == id:
                del self.afk[id]

                return await message.channel.send(f"{message.author.mention}, Welcome back!" , delete_after=15)
            
            member = message.guild.get_member(id)
            if member.mentioned_in(message):
                embed = discord.Embed(description=f'**{member.display_name}** is afk for: {self.afk[id]}' , color=WHITE)
                embed.set_image(url="https://media.giphy.com/media/LPETDRbj82wbrYm7q6/source.gif")
                await message.channel.send(embed=embed , delete_after=10)

        if message.content.startswith('latte'):
            await message.delete()
            await message.channel.send('เอะ! เรียกเราหรอ?  <:S_CuteGWave3:859660565160001537>')
        
        if message.content.startswith('invite'):
            await message.delete()
            await message.channel.send('https://discord.gg/bvwpZ2B4rj' , delete_after=15)

        if message.content.startswith('it'):
            await message.channel.send(f"This is my prefix `lt ` or `l `\nexample : `lt help` or `l help`", delete_after=10)
        
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

        if self.client.user.mentioned_in(message):
            await message.channel.send(f"This is my prefix `lt ` or `l `\nexample : `lt help` or `l help`", delete_after=15)
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
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
        
    @commands.command(name="snipe", aliases=["sni", "blackmail"] ,description="snipe message and image")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def snipe(self , ctx , choice=None):
        embed = discord.Embed(description= "" ,color=0xffffff)
        text_aliases = ["t", "text"]
        images_aliases = ["i", "image" , "images"]
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

                    await ctx.channel.send(embed=embed)
            else:
                await ctx.channel.send("Couldn't find a message to snipe!")
                return

        elif choice in images_aliases: #snipe image
            try:
                image , author , channel_name, time = self.sniped_img[ctx.guild.id]
            except:
                await ctx.channel.send("Couldn't find a message to snipe!")
                return

            embed = discord.Embed(description=f"**Deleted in:** {channel_name}\n**Attachments :** [**URL**]({image})",color=0xffffff , timestamp=time)
            try:
                embed.set_image(url=image)
            except:
                pass
            embed.set_author(name=f"{author.name}#{author.discriminator}" , icon_url=author.avatar.url)
            embed.set_footer(text=f"Message delete")
            await ctx.channel.send(embed=embed)
  
        elif choice in text_aliases: #snipe text
            try:
                content , author , channel_name, time = self.sniped_text[ctx.guild.id]
            except:
                await ctx.channel.send("Couldn't find a message to snipe!")
                return
                
            embed = discord.Embed(description=f"**Deleted in:** {channel_name}\n**Content:** ```{content}```" , color=0xffffff , timestamp=time)
            embed.set_author(name=f"{author.name}#{author.discriminator}" , icon_url=author.avatar.url)
            embed.set_footer(text=f"Message delete")
            await ctx.channel.send(embed=embed)

    @commands.command(name='bdm')
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def botdm(self, ctx, member: discord.Member, reason=None):
        embedrr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify a message! |`prefix` `bdm [member] [message]`",color=0xffffff)    
        if reason == None:
            return await ctx.send(embed=embedrr)
        
        embed = discord.Embed(title="",description=f"** **\nMessage : `{reason}`\n\n** **",color=0xFFFFFF,timestamp=datetime.now(timezone.utc))
        embed.set_footer(text=f"{self.client.user.name}" , icon_url = self.client.user.avatar.url)
        embed.set_author(name=f"{ctx.guild.name} | Direct Message", icon_url= ctx.guild.icon.url)

        embedsc = discord.Embed(title=f"{self.client.user.name} | Direct Message",description=f"Bot has been sent message to `{member.name}#{member.discriminator}`\n\nMessage : `{reason}`\n\n",color=0xFFFFFF,timestamp=datetime.now(timezone.utc))
        embedsc.set_footer(text=f"Req by {ctx.guild.name} " , icon_url = ctx.guild.icon.url)
        await member.send(embed=embed)
        await ctx.send(embed=embedsc)
        await message.delete()
        
#error commands

#    @botdm.error
#    async def botdm_error(self, ctx, error):
#        if isinstance(error, commands.MissingRequiredArgument):
#            embed = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify a member! |`prefix` `bdm [member] [message]`",color=0xffffff)  
#           await ctx.message.delete()
#            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Message(client))