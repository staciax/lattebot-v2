# Standard 
import discord
from discord.ext import commands
from datetime import datetime, timezone

# Third party
# Local
import utils

class Message(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.command()
    async def latte(self, ctx):
        await ctx.send('เราชอบกินลาเต้นะ')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.content.startswith('latte'):
            await message.delete()
            await message.channel.send('เอะ! เรียกเราหรอ?  <:S_CuteGWave3:859660565160001537>')
        
#        if message.content.startswith('latte'):
#            await message.delete()
#            await message.channel.send('`You can type `lt help` for more info`')

        if message.content.startswith('it'):
#            await message.delete()
            await message.channel.send('no no prefix bot is **LT ** > `lt help`', delete_after=10)

        if self.client.user.mentioned_in(message):
            await message.channel.send("You can type `lt help` for more info")
    
    @commands.command(name='bdm')
    @commands.has_permissions(administrator = True)
    async def botdm(self, ctx, member: discord.Member, reason=None):
        embedrr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify a message! |`prefix` `bdm [member] [message]`",color=0xffffff)    
        if reason == None:
#            await message.delete()
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

    @botdm.error
    async def botdm_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify a member! |`prefix` `bdm [member] [message]`",color=0xffffff)  
#           await ctx.message.delete()
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Message(client))