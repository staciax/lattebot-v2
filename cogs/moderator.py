# Standard 
import discord
import datetime
import asyncio
import os
import json
from discord.ext import commands
from datetime import datetime, timedelta, timezone

# Third party
import aiohttp
from re import search
from io import BytesIO

# Local
import utils
from config import *
from utils.paginator import SimplePages

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot        
        self.only_images = (ONLYIMG,)
        self.testing_only = (ONLYTESTING,)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        while True:
        #print("spam detct")
            await asyncio.sleep(10)
            with open("data/spam_detect.txt", "r+") as file:
                file.truncate(0)

    @commands.command(description="ban member from your server", help="@latte", usage="<member> [reason]")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
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
    
    @commands.command(help="Gets the current guild's list of bans")
    @commands.has_permissions(ban_members=True)
#    @commands.bot_has_permissions(send_messages=True, embed_links=True, ban_members=True)
    async def bans(self, ctx) -> discord.Message:
        bans = await ctx.guild.bans()
        if not bans:
            return await ctx.send(embed=discord.Embed(title="There are no banned users in this server",color=WHITE))
        ban_list = []
        for ban_entry in bans:
            ban_list.append(f"**{ban_entry.user}**")
        p = SimplePages(entries=ban_list, per_page=10, ctx=ctx)
        p.embed.title = "Bans list"
        p.embed.color = WHITE
        await p.start()


    @commands.command(description="unbanned member", help="@latte", usage="<member>")
    @commands.guild_only()
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
    
    @commands.command(name="kick", description="kick member", pass_context=True, help="@latte", usage="<member> [reason]")
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        embedkick = discord.Embed(title="Kicked Member", description=f'Member {member.mention} has been Kicked\nReason : {reason}',color=0xffffff)

        await member.kick(reason=reason)
        await ctx.send(embed=embedkick)

    #check_message
    async def do_removal(self, ctx, limit, predicate, *, before=None, after=None):
        if limit > 2000:
            return await ctx.send(f'Too many messages to search given ({limit}/2000)')

        if before is None:
            before = ctx.message
        else:
            before = discord.Object(id=before)

        if after is not None:
            after = discord.Object(id=after)

        try:
            deleted = await ctx.channel.purge(limit=limit, before=before, after=after, check=predicate)
        except discord.Forbidden as e:
            return await ctx.send('I do not have permissions to delete messages.')
        except discord.HTTPException as e:
            return await ctx.send(f'Error: {e} (try a smaller search?)')
    
    @commands.command(description="Cleanup the bot's messages",aliases=["clearbot"])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def cleanup(self, ctx , amount : int=15):        
        await self.do_removal(ctx=ctx, limit=amount, predicate=lambda e: e.author == ctx.me)
    
    @commands.command(description="clear message" , aliases=['purge'], help="20", usage="<amount>")
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: str):
        if amount == 'all':
            embed = discord.Embed(
            title=f"{ctx.author.name} purged: {ctx.channel.name}",
            description=f"{amount} messages were cleared",
            color=WHITE
        )
            await ctx.channel.purge()
            await ctx.send(embed=embed, delete_after=10)
        else:
            embed = discord.Embed(
            title=f"{ctx.author.name} purged: {ctx.channel.name}",
            description=f"{amount} messages were cleared",
            color=WHITE
        )
            await ctx.channel.purge(limit=(int(amount) + 1))
            await ctx.send(embed=embed, delete_after=10)

    @commands.command(aliases=["fmute"],description="mute member")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def forcemute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        if not mutedRole:
            mutedRole = await guild.create_role(name=MUTEROLE , colour=discord.Colour(COLORMUTE))
            embedcreate = discord.Embed(title="BOT SETTING UP",description=f"`your server don't have` **`Muted Role`**\n`creating role...`\n**Permissions** : `setting up...`\n\n**Role permission Syncing**\n`text channel :`\n`voice channel :`\n`category :`",color=0xffffff)
            msg = await ctx.send(embed=embedcreate)

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        embed = discord.Embed(description=f"**MUTED MEMBER**\n\n`You has been mute :` `{member.display_name}#{member.discriminator}`",color=0xffffff)
        embed.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)

        embedmute = discord.Embed(description=f"**SERVER MUTED**\n\n`You are muted on the server : {ctx.guild.name}\nReason : {reason} `\n\n",color=0xffffff, timestamp=datetime.now(timezone.utc))
        embedmute.set_footer(text=f"{self.bot.user.name}",icon_url=self.bot.user.avatar.url)

        embedfinish = discord.Embed(title="BOT SETTING SUCCESS",description=f"{mutedRole.mention}\n**Permissions**\n`speak : false`\n`send message : false`\n\n**Role permission sync**\n`text channel : sync`\n`voice channel : sync`\n`category : sync`\n\n `please move` **`Muted Role`** `above other role.`",color=0xffffff)
        await ctx.send(embed = embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(embed=embedmute)
        await msg.edit(embed = embedfinish)

    @commands.command(description="Mute member", help="@latte 20m", usage="<member> [duration]")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def mute(self, ctx, member: discord.Member,*, time: utils.TimeConverter=None , reason=None):
        role = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        if not role:
            embeddh = discord.Embed(title="MUTE ROLE",description=f"Your server don't have : **`Muted Role`**",color=0xffffff)
            await ctx.send(embed=embeddh)
            return
            
        if member == ctx.author:
            embed = discord.Embed(description="You cannot mute yourself." , color=WHITE)
            await ctx.send(embed=embed)

        check_member_role = discord.utils.get(member.roles, name=MUTEROLE)
        if check_member_role:
            embed = discord.Embed(description="member's already have a mute role.", color=WHITE)
            return await ctx.send(embed=embed)
        
        embed = discord.Embed(description=f"**MUTED MEMBER**",color=WHITE)
        embed.add_field(name="Muted:", value=f"```{member.name}#{member.discriminator}```" , inline=False)
        if reason is not None:
            embed.add_field(name="Reason:", value=f"```{reason}```" , inline=False)
        embed.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)

        #            embedmute = discord.Embed(description=f"**SERVER MUTED**\n\n`You are muted on the server`: {ctx.guild.name}\n`Reason` : {reason} \n\n",color=0xffffff, timestamp=datetime.now(timezone.utc))
        #            embedmute.set_footer(text=f"{self.bot.user.name}",icon_url=self.bot.user.avatar.url)

        if not time:
            await member.add_roles(role, reason=reason)
            await ctx.send(embed = embed)                
        else:
            await member.add_roles(role, reason=reason)
            minutes, seconds = divmod(time, 60)
            hours, minutes = divmod(minutes, 60)
            if int(hours):
                embed.add_field(name="Time:", value=f"```{int(hours)} hours, {int(minutes)} minutes```" , inline=False)
            elif int(minutes):
                embed.add_field(name="Time:", value=f"```{int(minutes)} minutes and {int(seconds)} seconds```" , inline=False)
            elif int(seconds):
                embed.add_field(name="Time:", value=f"```{int(seconds)} seconds```" , inline=False)
            await ctx.send(embed = embed) 

        data = utils.json_loader.read_json("latte")
        log = data["server-log"]
        self.log_mute = self.bot.get_channel(log)

        if self.log_mute:
            minutes, seconds = divmod(time, 60)
            hours, minutes = divmod(minutes, 60)

            embed_log = discord.Embed(title="MUTED MEMBER" , color=0xffffff)
            embed_log.add_field(name=f"Target:" , value=f"```{member.name}```" , inline=False)
            embed_log.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)
            if reason:
                embed_log.add_field(name=f"Reason:" , value=f"```{reason}```" , inline=False)
            if int(hours):
                embed_log.add_field(name="Time:", value=f"```{int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds```" , inline=False)
            elif int(minutes):
                embed_log.add_field(name="Time:", value=f"```{int(minutes)} minutes and {int(seconds)} seconds```" , inline=False)
            elif int(seconds):
                embed_log.add_field(name="Time:", value=f"```{int(seconds)} seconds```" , inline=False)
            embed_log.set_footer(text=f"Muted by {ctx.author}", icon_url = ctx.author.avatar.url)

            await self.log_mute.send(embed=embed_log)
        
        if time and time < 300:
            await asyncio.sleep(time)

            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(f"Unmuted `{member.display_name}`")

    @commands.command(description="Unmuted member", help="@latte", usage="<member>")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        embed = discord.Embed(description=f"**UNMUTED MEMBER**\n\n`You has been unmute :` `{member.name}#{member.discriminator}`",color=0xffffff)
        embed.set_footer(text=f"Unmuted by {ctx.author}", icon_url = ctx.author.avatar.url)

        await member.remove_roles(mutedRole)
        await ctx.send(embed=embed)
    
    @commands.command(description="create mute role")
    @commands.has_permissions(administrator = True)
    @commands.guild_only()
    async def muterole(self, ctx):
        guild = ctx.guild
        mutedRole = discord.utils.get(ctx.guild.roles, name=MUTEROLE)

        if not mutedRole:
            mutedRole = await guild.create_role(name=MUTEROLE , colour=discord.Colour(COLORMUTE))
            embedmute = discord.Embed(title="CREATE MUTE ROLE",description="`creating role...`\n`please wait 10-20 seconds`",color=0xffffff)
            msg = await ctx.send(embed = embedmute)

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        
            embed = discord.Embed(title="CREATE MUTE ROLE",description=f"{mutedRole.mention}\n**Permissions**\n`speak : false`\n`send message : false`\n\n**Role permission sync**\n`text channel : sync`\n`voice channel : sync`\n`category : sync`\n\n `please move` **`Muted Role`** `above other role.`",color=0xffffff)
            await msg.edit(embed = embed)
        else:
            embedhm = discord.Embed(title="MUTE ROLE", description=f"{utils.emoji_converter('xmark')}Your server has a muted role.",color=0xffffff)
            await ctx.channel.send(embed=embedhm)

    @commands.command(description="join voice channel")
    @commands.guild_only()
    async def _join_(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command(description="leave voice channel")
    @commands.guild_only()
    async def _leave_(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(description="lockdown or unlock text channel" , aliases=['lock', 'lockdown'], help="#channel", usage="[channel]")
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    #@commands.bot_has_guild_permissions(manage_channels=True)
    async def lock_down(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel
        if ctx.guild.default_role not in channel.overwrites:
            embed1 = discord.Embed(description=f"{channel.name} is **lockdown.**",color=0xffffff)
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send(embed=embed1 , delete_after=15)
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            embed2 = discord.Embed(description=f"{utils.emoji_converter('check')}{channel.name} is **lockdown.**",color=0xffffff)
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(embed=embed2, delete_after=15)
        else:
            embed3 = discord.Embed(description=f"{utils.emoji_converter('check')}{channel.name} : **Removed lockdown!**",color=0xffffff)
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send(embed=embed3, delete_after=15)

    @commands.command(aliases=["nick"], help="@latte coffe", usage="<member> [new_name]")
    @commands.has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def changenick(self, ctx , member: discord.Member, nick):
        embed = discord.Embed(description=f"Nickname was changed for {member.display_name}",color=0xffffff)
        await member.edit(nick=nick)
        await ctx.channel.send(embed=embed)
    
    @commands.command(aliases=["slow"], help="10", usage="[seconds]")
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def slowmode(self, ctx ,*, seconds: int= None):
            if seconds == None:
                embed = discord.Embed(title="SLOW MODE",description=f"Disable slowmode this channel",color=0xffffff)
                await ctx.channel.edit(slowmode_delay=0)
                await ctx.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="SLOW MODE",description=f"Set the slowmode delay in this channel to {seconds} **seconds!**",color=0xffffff)
                await ctx.channel.edit(slowmode_delay=seconds)
                await ctx.channel.send(embed=embed)

    #spam_alert
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        def _check(m):
            return (m.author == message.author
					and len(m.mentions)
					and (datetime.now(timezone.utc)-m.created_at).seconds < 60)
        
        if not message.author.bot:
            if len(list(filter(lambda m: _check(m), self.bot.cached_messages))) >= 4:
                embedspam = discord.Embed(description="Don't spam mentions!",color=0xffffff)
                await message.channel.send(embed=embedspam, delete_after=10)
                                               
        counter = 0
        with open("data/spam_detect.txt", "r+") as file:
            for lines in file:
                if lines.strip("\n") == str(message.author.id):
                    counter+=1

            file.writelines(f"{str(message.author.id)}\n")
            if counter > 5:
                if not message.author.bot:
                    embedmute = discord.Embed(title="Spam Alert",description=f"Mute {message.author.mention} **1 minutes**",color=0xffffff)
                    member = message.author
                    muter = discord.utils.get(message.guild.roles, name = MUTEROLE) 
                    if not muter:
                        guild = message.guild
                        await guild.create_role(name=MUTEROLE , colour=discord.Colour(COLORMUTE))
                        for channel in guild.channels:
                            await channel.set_permissions(muter, speak=False, send_messages=False, read_message_history=True, read_messages=False)
                    await member.add_roles(muter)
                    await message.channel.send(embed=embedmute, delete_after=10)
                    await asyncio.sleep(60)
                    await member.remove_roles(muter)
                else:
                    pass

                
                
        #            elif counter > 5:
        #                await message.guild.ban(message.author, reason="spam")
        #                await asyncio.sleep(20)
        #                await message.guild.unban(message.author)     


        #                unmutes = await self.mute(message, [message.author], reason="Mention spam")

        #                if len(unmutes):
        #                    await message.channel.send("You can't use that word here.", delete_after=10)
                    
        #            elif message.channel.id not in self.links_allowedr and seach(self.url_regex, message.content):
        #                await message.delete()
        #                await message.channel.send("You can't send links in this channel.", delete_after=10)
                    
        #            elif (message.channel.id not in self.images_allowed
        #			 	and any([hasattr(a, "width") for a in message.attachments])):
        #                await message.delete()
        #                await message.channel.send("You can't send images here.", delete_after=10)

        ##########################
        #            if (message.channel.id in self.only_images
        #			 	and any([hasattr(a, "width") for a in message.attachments])):             
        #                return
        #            else:
        #                if message.channel.id in self.only_images:
        #                    em = discord.Embed(description="You can't send message in this channel.",color=PTRED2)
        #                    await message.delete()
        #                    await message.channel.send(embed=em , delete_after=10)
        #                else:
        #                    return
    
    @commands.command(aliases=["tban"], help="@latte 10h", usage="<member> [duration]")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member: utils.BetterMemberConverter, duration: utils.DurationConverter):
        multiplier = {'s': 1, 'm': 60, 'd': 86400, 'w': 604800, 'm': 2629746, 'y': 31556952 }
        amount, unit = duration
        embed = discord.Embed(title="Banned Member", description=f'{member.name} has been banned from server\n\n`Duration` : {amount}{unit}',timestamp=datetime.now(timezone.utc),color=0xffffff)
        embed.set_footer(text=f"Banned by {ctx.author}" , icon_url = ctx.author.avatar.url)
        await ctx.guild.ban(member)
        await ctx.send(embed=embed)
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)
    
    @commands.command(aliases=["create_emoji", "add_emoji"], description="Create emoji from url", usage="<url type: .png .gif>")
    @commands.guild_only()
    @commands.has_permissions(manage_emojis=True)
    async def createemoji(self, ctx, url: str, *, name):
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    img_or_gif = BytesIO(await r.read())
                    b_value = img_or_gif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=b_value, name=name)
                        await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')
                        await ses.close()
                    else:
                        await ctx.send(f'Error when making request | {r.status} response.')
                        await ses.close()
                except discord.HTTPException:
                    await ctx.send('File size is too big!')

    @commands.command(aliases=["delete_emoji", "del-ei"], description="delete custom emoji from server", usage="<emoji>")
    @commands.guild_only()
    @commands.has_permissions(manage_emojis=True)
    async def deleteemoji(self, ctx, emoji: discord.Emoji):
        try:
            await ctx.send(f'Successfully deleted : {emoji}')
            await emoji.delete()
        except:
            await ctx.send('error delete emoji!')
    
    @commands.command(description="Audit logs")
    @commands.guild_only()
    @commands.has_permissions(view_audit_log=True)
    async def audit(self,ctx, num: int=None):
        embed=discord.Embed(title='Audit Logs',description="", color=0xffffff)
        embed.set_footer(text=f"Requested by {ctx.author}" , icon_url=ctx.author.avatar.url)
        if num is None: num=5
        async for entry in ctx.guild.audit_logs(limit=num):
            action_str = str(entry.action)
            category_str = str(entry.category)
            embed.description += f'**User:** `{entry.user}` **Action:** `{action_str[15:]}`  **Target:** `{entry.target}` **Time:** `{entry.created_at.strftime("%a, %#d %B %Y, %I:%M %p")}\n\n`'
            #**Category:** `{category_str[23:]}`
        await ctx.reply(embed=embed, mention_author=False) 

def setup(bot):
    bot.add_cog(Moderation(bot))