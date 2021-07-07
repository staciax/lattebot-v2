import discord
from discord.ext import commands
from datetime import datetime, timezone

class Message(commands.Cog):

    def __init__(self, client):
        self.client = client

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
        
        if message.content.startswith('ปอน'):
#            await message.delete()
            await message.channel.send('ไอ้หนุ่มน้ำอัดลม')

        if message.content.startswith('ไอ้ปอน'):
#            await message.delete()
            await message.channel.send('ผมเด็กแว๊นนะค้าบ ตี3ยังค้าบเนี้ย')
    
    @commands.command(name='bdm')
#    @commands.has_permissions(administrator = True)
    async def botdm(self, ctx, member: discord.Member, reason=None):    
        if reason == None:
            return await ctx.send('Please specify a message! | `bdm` `member` `message`')
        
        embed = discord.Embed(title="",description=f"`{reason}`",color=0xFFFFFF,timestamp=datetime.utcnow())
        embed.set_footer(text=f"DM by {ctx.author}" , icon_url = ctx.author.avatar.url)
        embed.set_author(name=f"{self.client.user.name} Direct Message", icon_url=self.client.user.avatar.url)
        await member.send(embed=embed)

    @botdm.error
    async def botdm_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            await ctx.send('Please specify member! | `bdm` `member` `message`')

def setup(client):
    client.add_cog(Message(client))