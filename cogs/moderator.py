import discord
import datetime
import utils
from config import *
from discord.ext import commands
from datetime import datetime, timedelta, timezone

intents = discord.Intents()
intents.all()
intents.members = True 
intents = discord.Intents(messages=True, guilds=True)

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderator')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name=WELCOME)
        if channel:
            embed=discord.Embed(
        description=f"ʚ˚̩̥̩ɞ ◟‧Welcome‧ *to* **{member.guild}!** <a:ab__purplestar:854958903656710144>\n　。\nෆ ₊˚don’t forget to check out . . .\n\n‧˚₊ ପ <:a_pink_dot:860493678723072000>︰<#861774918290636800> ଓ ♡ ˖˚˳\n♡ ꒷ get latte roles~︰𓂃 ꒱\n\n⸝⸝﹒{member.mention} ꒱ <a:S_wtfemoji:860490611048054845>", #⊹₊˚**‧Welcome‧**˚₊⊹ 
        timestamp=datetime.now(timezone.utc),
        color=0xc4cfcf
    
        )
        embed.set_author(name=f"{member}", icon_url=member.avatar.url), 
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"You're our {member.guild.member_count} members ෆ"),

        await channel.send(embed=embed) #(content=f"||{member.mention}||", embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name=LEAVE)
        if channel:
            embed = discord.Embed(
                description=f"**Leave Server\n`{member}`**",
                color=0xdbd7d2)
            embed.set_footer(text="—・see ya good bye")
            embed.timestamp = datetime.now(timezone.utc)

        await channel.send(embed = embed)  #await channel.send(f"{member} has left the server")

    @commands.command(description="ban member")
    @commands.has_permissions(administrator = True)
#    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        embed = discord.Embed(title="Banned Member", description=f'{member.name}#{member.discriminator} has been banned from server\nReason: {reason}',timestamp=datetime.now(timezone.utc),color=0xffffff)
        embed.set_footer(text=f"Banned by {ctx.author}" , icon_url = ctx.author.avatar.url)

        embedprm = discord.Embed(title="Ban Error\n", description="`Bot doesn't have enough permission to ban someone.`",color=0xffffff)
       
        try:
            await member.ban(reason=reason)
            await ctx.message.delete()
            await ctx.channel.send(embed=embed)
        except Exception:
            await ctx.channel.send(embed=embedprm)

    @commands.command()
    @commands.has_permissions(ban_members=True) 
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            embedub = discord.Embed(title="Unbanned Member\n", description=f"You has been unbanned : {user.mention} !",color=0xffffff)

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(embed=embedub)

    @commands.command(name="kick", description="kick member", pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        embedkick = discord.Embed(title="Kicked Member", description=f'Member {member.mention} has been Kicked\nReason : {reason}',color=0xffffff)

        await member.kick(reason=reason)
        await ctx.send(embed=embedkick)
    
    @commands.command(description="clear message")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: str):
        if amount == 'all':
             await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=(int(amount) + 1))

    @commands.command(description="mute member")
    @commands.has_permissions(administrator = True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        if not mutedRole:
            mutedRole = await guild.create_role(name=MUTEROLE , colour=discord.Colour(COLORMUTE))
            embedcreate = discord.Embed(title="BOT SETTING UP",description=f"`your server don't have` **`Muted Role`**\n**ROLE** : `creating role...`\n**Permissions** : `setting up...`\n\n**Role permission Syncing**\n`text channel :`\n`voice channel :`\n`category :`",color=0xffffff)
            msg = await ctx.send(embed=embedcreate)

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        embed = discord.Embed(description=f"**MUTED MEMBER**\n\n`You has been mute :` `{member.display_name}#{member.discriminator}`",color=0xffffff)
        embed.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)

        embedmute = discord.Embed(description=f"**SERVER MUTED**\n\n`You are muted on the server : {ctx.guild.name}\nReason : {reason} `\n\n",color=0xfdfd96, timestamp=datetime.now(timezone.utc))
        embedmute.set_footer(text=f"{self.client.user.name}",icon_url=self.client.user.avatar.url)

        embedfinish = discord.Embed(title="BOT SETTING SUCCESS",description=f"**ROLE** : {mutedRole.mention}\n**Permissions**\n`speak : false`\n`send message : false`\n\n**Role permission sync**\n`text channel : sync`\n`voice channel : sync`\n`category : sync`\n\n `please move` **`Muted Role`** `above other role.`",color=0xffffff)
        await ctx.send(embed = embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(embed=embedmute)
        await msg.edit(embed = embedfinish)

    @commands.command(description="unmute member")
    @commands.has_permissions(administrator = True)
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        embed = discord.Embed(description=f"**UNMUTED MEMBER**\n\n`You has been unmute :` `{member.display_name}#{member.discriminator}`",color=0xfdfd96)
        embed.set_footer(text=f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar.url)

        await member.remove_roles(mutedRole)
        await ctx.send(embed=embed)

    @commands.command(description="join voice channel")
    async def join(self, ctx):
        channel = ctx.author.voice.channel
#        await ctx.message.delete()
        await channel.connect()

    @commands.command(description="leave voice channel")
    async def leave(self, ctx):
#        await ctx.message.delete()
        await ctx.voice_client.disconnect()

## error commands

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **ban!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Only **administrators** can use this command!",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr) #("`You doesn't have enough permission to ban someone.`")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **unban****",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} Only **administrators** can use this command.",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)
   
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **kick!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to mute!",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)
    
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **member** to **unmute!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embedar = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify **numbers** of messages to **delete..**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedar)
        if isinstance(error, commands.MissingPermissions):
            embedpr = discord.Embed(description=f"{utils.emoji_converter('xmark')} You doesn't have enough **permission!**",color=0xffffff)
            await ctx.message.delete()
            await ctx.send(embed=embedpr)

def setup(client):
    client.add_cog(Admin(client))

#auto riole event
##@client.event  // auto role
##async def on_member_join(member):
##  role = get(member.guild.roles, id=role_id)
##  await member.add_roles(role)