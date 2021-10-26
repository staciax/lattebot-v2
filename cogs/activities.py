# Standard 
import discord
import datetime
import time
import os
import io
import random
from time import time
from discord.ext import commands , tasks
from datetime import datetime, timedelta, timezone
from discord.channel import TextChannel
from asyncio import sleep

# Third party
import json
import requests

# Local
import utils
import utils.json_loader
from config import *
from utils import create_voice_channel , get_channel_by_name

class Activities(commands.Cog):

    current_streamers = list()

    def __init__(self, bot):
        self.bot = bot
        self.invites = {}
        self.invite_code = utils.json_loader.read_json("latte")["tempinvite"]
        self.total_ = 0
        self.member_ = 0
        self.bot_ = 0
        self.role_ = 0
        self.channel_ = 0
        self.text_ = 0
        self.voice_ = 0
        self.boost_ = 0
        self.code_bypass = {}
        self.counted.start()
    
    def cog_unload(self):
        self.counted.cancel()
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        self.join_guild = self.bot.get_channel(893695417320087573)
        self.leave_guild = self.bot.get_channel(893695447309369345)
    #        guild = self.bot.get_guild(MYGUILD)
    #        self.invites[guild.id] = await guild.invites()
        for guild in self.bot.guilds:
            self.invites[guild.id] = await guild.invites()

    #channel_stats
    @tasks.loop(minutes=30)
    async def counted(self):
        guild = self.bot.get_guild(840379510704046151)

        total_count = guild.member_count
        if self.total_ != total_count:
            self.total_ = total_count
            total_channel = guild.get_channel(876738880282431489)
            total_name = f"ᴛᴏᴛᴀʟ‌・{self.total_}"
            await total_channel.edit(name=total_name)
        
        member_count = len([member for member in guild.members if not member.bot])
        if self.member_ != member_count:
            self.member_ = member_count
            member_channel = guild.get_channel(876712142160678923)
            member_name = f"ᴍᴇᴍʙᴇʀs・{self.member_}"
            await member_channel.edit(name=member_name)

        bot_count = len([Member for Member in guild.members if Member.bot])
        if self.bot_ != bot_count:
            self.bot_ = bot_count
            bot_channel = guild.get_channel(876724022686150687)
            bot_name = f"ʙᴏᴛs‌・{self.bot_}"
            await bot_channel.edit(name=bot_name)
        
        role_count = len(guild.roles)
        if self.role_ != role_count:
            self.role_ = role_count
            role_channel = guild.get_channel(876712169662742588)
            role_name = f"ʀᴏʟᴇs‌・{self.role_}"
            await role_channel.edit(name=role_name)
        
        channel_count = len(guild.channels)
        if self.channel_ != channel_count:
            self.channel_ = channel_count
            channel_channel = guild.get_channel(876712200214024192)
            channel_name = f"ᴄʜᴀɴɴᴇʟs・{self.channel_}"
            await channel_channel.edit(name=channel_name)
        
        text_channel_count = len(guild.text_channels)
        if self.text_ != text_channel_count:
            self.text_ = text_channel_count
            text_channel = guild.get_channel(876740437505871922)
            text_name = f"ᴛᴇxᴛ・{self.text_}"
            await text_channel.edit(name=text_name)
        
        voice_channel_count = len(guild.voice_channels)
        if self.voice_ != voice_channel_count:
            self.voice_ = voice_channel_count
            voice_channel = guild.get_channel(876740515863879711)
            voice_name = f"ᴠᴏɪᴄᴇ・{self.voice_}"
            await voice_channel.edit(name=voice_name)
        
        boost_count = guild.premium_subscription_count
        if self.boost_ != boost_count:
            self.boost_ = boost_count
            boost_channel = guild.get_channel(876737270051389470)
            boost_name = f"ʙᴏᴏꜱᴛꜱ・{self.boost_}"
            await boost_channel.edit(name=boost_name)

    @counted.before_loop
    async def before_counted(self):
        await self.bot.wait_until_ready()

    #    @commands.Cog.listener()
    #    async def on_member_join(self, member):
    #        if member.guild.id == 867729118308204564:
    #	        await sleep(60*10)
    #	        for channel in member.guild.channels:
    #		        if channel.name.startswith('♢・latte'):
    #			        await channel.edit(name=f'♢・latte・{member.guild.member_count}')
    #			        break

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == MYGUILD:
            """welcome log"""

            user_update = utils.json_loader.read_json("latte")
            self.server_log = self.bot.get_channel(user_update["server-log"])

            if self.server_log is None:
                return

            #invte_code
            try:
                invites_before_join = self.invites[member.guild.id]
                invites_after_join = await member.guild.invites()
                for invite in invites_before_join:
                    if invite.uses < utils.find_invite_by_code(invites_after_join, invite.code).uses:

                        self.code_bypass[str(member.id)] = invite.code
                        
                        embed_log = discord.Embed(
                            title="Member join",
                            color=PTGREEN,
                            timestamp=datetime.now(timezone.utc)
                        )
                        embed_log.add_field(name="Name:", value=f"{member.name}", inline=False)
                        embed_log.add_field(name="Invite Code:", value=f"||{invite.code}||", inline=False)
                        if member.avatar.url is not None:
                            embed_log.set_thumbnail(url=member.avatar.url)
                        if invite.inviter.avatar.url is not None:
                            embed_log.set_footer(text=f"Invited by {invite.inviter.name}", icon_url=invite.inviter.avatar.url)
                        else:
                            embed_log.set_footer(text=f"Invited by {invite.inviter.name}")
                        await self.server_log.send(embed=embed_log)
                        self.invites[member.guild.id] = invites_after_join

                        #latte_role
                        if invite.code == self.bot.latte_latte:
                            try:
                                latte_roles = discord.utils.get(member.guild.roles, id = 842309176104976387) #name="Latte・・ ♡")
                                bar_role = discord.utils.get(member.guild.roles, id = 854503426977038338) #name="・ ───────꒰ ・ ♡ ・ ꒱─────── ・")
                                lvl_bar_role = discord.utils.get(member.guild.roles, id = 854503041775566879) #name="・ ──────꒰ ・ levels ・ ꒱────── ・")
                                await member.add_roles(latte_roles , bar_role, lvl_bar_role)
                            except:
                                pass
                        
                        #temp_invite
                        if invite.code == self.invite_code:
                            try:
                                role = discord.utils.get(member.guild.roles, id=879258879987449867)
                                await member.add_roles(role)
                                return
                            except:
                                pass
            except:
                pass

            """welcome embed"""

            welcome_ch = utils.json_loader.read_json("welcome")
            data = welcome_ch[str(member.guild.id)]
            latte_json = utils.json_loader.read_json('latte')
            wel_picture = latte_json['welcomepic']
            
            #check_data
            if data is None:
                return
            
            #get_channel
            guild = self.bot.get_guild(member.guild.id)
            channel = guild.get_channel(data)
            # chat_channel = guild.get_channel(861883647070437386)

            embed=discord.Embed(
                        description=f"ʚ˚̩̥̩ɞ ◟‧Welcome‧ *to* **{member.guild}!** <a:ab__purplestar:854958903656710144>\n　。\nෆ ₊˚don’t forget to check out . . .\n\n♡ ꒷ get latte roles~︰𓂃 ꒱\n⸝⸝﹒<#861774918290636800> \n⸝⸝﹒<#840380566862823425>\n\n⸝⸝﹒||{member.mention}|| ꒱ {utils.emoji_converter('3rd')}", #⊹₊˚**‧Welcome‧**˚₊⊹ 
                        timestamp=datetime.now(timezone.utc),
                        color=0xc4cfcf
    
            )
            if member.avatar.url is not None:
                embed.set_author(name=member, icon_url=member.avatar.url)
                embed.set_thumbnail(url=member.avatar.url)
            else:
                embed.set_author(name=member)

            if wel_picture: embed.set_image(url=wel_picture)
            embed.set_footer(text=f"You're our {member.guild.member_count} members ෆ")
           
            if member.bot:
                role = discord.utils.get(member.guild.roles, id=840677855460458496)
                if role:
                    await member.add_roles(role)

            # await chat_channel.send(f'୨୧・━━⋄✩ ₊ ˚・\nwelcome to our latte . .\n⸝⸝・{member.mention}')
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        if member.guild.id == MYGUILD:
            user_update = utils.json_loader.read_json("latte")
            self.server_log = self.bot.get_channel(user_update["server-log"])

            if self.server_log is None:
                print("on_member_ban channel is None")
                return

            embed = discord.Embed(
                description=f"**Member ban\n`{member}`**",
                color=PTRED
            )
            if member.avatar.url is not None:
                embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text="—・good bye bro")
            embed.timestamp = datetime.now(timezone.utc)

            await self.server_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == MYGUILD: #only my guild
            user_update = utils.json_loader.read_json("latte")
            self.server_log = self.bot.get_channel(user_update["server-log"])

            if self.server_log is None:
                print("on_member_remove channel is None")
                return

            embed_log = discord.Embed(
                        title="Member leave",
                        color=PTRED2,
                        timestamp=datetime.now(timezone.utc))
            embed_log.add_field(name="Name:", value=f"{member.name}#{member.discriminator}", inline=False)
            if member.avatar.url is not None:
                embed_log.set_thumbnail(url=member.avatar.url)
            await self.server_log.send(embed=embed_log)
            self.invites[member.guild.id] = await member.guild.invites()

            """leave embed"""
            leave_ch = utils.json_loader.read_json("leave")
            data = leave_ch[str(member.guild.id)]
            
            #check
            if data is None:
                return
            
            guild = self.bot.get_guild(member.guild.id)
            channel = guild.get_channel(data)
            embed = discord.Embed(
                        description=f"**Leave Server\n`{member}`**",
                        color=0xdbd7d2)
            if member.avatar.url is not None:
                embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text="—・see ya good bye")
            embed.timestamp = datetime.now(timezone.utc)

            await channel.send(embed = embed) 
    
    @commands.Cog.listener()
    async def on_invite_create(self, invite: discord.Invite):
        user_update = utils.json_loader.read_json("latte")
        self.server_log = self.bot.get_channel(user_update["server-log"])

        if self.server_log is None:
            print("on_invite_create channel is None")
            return
            
        if invite.guild.id == MYGUILD:
            now = datetime.now(timezone.utc)
            max_use_count = "Unlimited" if invite.max_uses == 0 else invite.max_uses
            embed = discord.Embed(title=f"{invite.inviter} created an invite.", timestamp=now, colour=WHITE)
            embed.add_field(name="Max Uses:", value=f"{max_use_count}")
            embed.add_field(name="Channel:", value=f"#{invite.channel}")
            embed.add_field(name="Inivte Code:", value=f"||{invite.code}||")
            if invite.inviter.avatar.url is not None:
                embed.set_footer(text = f'Created by {invite.inviter.name}', icon_url =invite.inviter.avatar.url)
            else:
                embed.set_footer(text = f'Created by {invite.inviter.name}')
            await self.server_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
            #load_json
            user_update = utils.json_loader.read_json("latte")
            self.server_log = self.bot.get_channel(user_update["server-log"])

            if self.server_log is None:
                print("on_user_update channel is None")
                return

            #username_log
            if before.name != after.name:
                embed = discord.Embed(title="Username change",colour=after.colour,timestamp=datetime.now(timezone.utc))

                fields = [("**Before**", f"```{before.name}```", False),
					    ("**After**", f"```{after.name}```", False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                if after.avatar.url is not None:
                    embed.set_thumbnail(url=after.avatar.url)
                    embed.set_footer(text=after, icon_url=after.avatar.url)
                else:
                    embed.set_footer(text=after)
            
                await self.server_log.send(embed=embed)

            #discriminator_log
            if before.discriminator != after.discriminator:
                embed = discord.Embed(title="Discriminator change",
                                    colour=0xffffff, #after.colour
                                    timestamp=datetime.now(timezone.utc))

                fields = [("**Before**",f"```#{before.discriminator}```", False),
					    ("**After**",f"```#{after.discriminator}```", False)]
            
                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    
                if after.avatar.url is not None:  
                    embed.set_footer(text=after, icon_url=after.avatar.url)
                else:
                    embed.set_footer(text=after)
            
                await self.server_log.send(embed=embed)

            #avatar_log
            if before.avatar.url != after.avatar.url:
                embed = discord.Embed(title="Avatar change",description="New image is below, old to the right.",
						    colour=0xf3d4b4,
						    timestamp=datetime.now(timezone.utc))
                embed.set_thumbnail(url=before.avatar.url)
                if after.avatar.url is not None:
                    embed.set_image(url=after.avatar.url)
                embed.set_footer(text=after, icon_url=after.avatar.url)

                await self.server_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild.id == MYGUILD:
            #load_json
            member_update = utils.json_loader.read_json("latte")
            self.server_log = self.bot.get_channel(member_update["server-log"])
            self.roles_log = self.bot.get_channel(member_update["role-log"])

            if self.server_log is None:
                print("server_log is None")
                return
                
            if self.roles_log is None:
                print("roles_log is None")
                return

            #nickname_log
            if before.display_name != after.display_name:
                embed = discord.Embed(title="Nickname change",
                                    colour=0xFFDF00, #colour=after.colour,
						            timestamp=datetime.now(timezone.utc))

                fields = [("**Before**", f"```{before.display_name}```", False),
					    ("**After**", f"```{after.display_name}```", False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                if after.avatar.url is not None:    
                    embed.set_thumbnail(url=after.avatar.url)
                # embed.set_footer(text="", icon_url=after.avatar.url)

                await self.server_log.send(embed=embed)

            #role_log
            elif before.roles != after.roles:
                new_roles = [x.mention for x in after.roles if x not in before.roles]
                old_roles = [x.mention for x in before.roles if x not in after.roles]
                if new_roles:
                    role_update = "**Add role**"
                    nr_str = str(new_roles)[2:-2]
                    nr_valur = " ".join(reversed([r.mention for r in after.roles]))
                    color = 0x52D452
                else:
                    role_update = "**Remove role**"
                    nr_str = str(old_roles)[2:-2]
                    nr_valur = " ".join(reversed([r.mention for r in after.roles])) #' '.join(reversed([r.mention for r in member.roles][1:]))
                    
                    color = 0xFF6961
                offline = ['<@&886193080997384222>']
                if new_roles == offline:
                    return
                if old_roles == offline:
                    return
                embed = discord.Embed(colour=color, #colour=after.colour,
						            timestamp=datetime.now(timezone.utc))
                
                if after.avatar.url is not None:
                    embed.set_author(name=f"{after.display_name} | Role updates", icon_url=after.avatar.url)
                else:
                    embed.set_author(name=f"{after.display_name} | Role updates")

                if role_update and nr_valur and nr_str:
                    embed.add_field(name="**Role**",value=nr_valur[:-22],inline=False)
                    embed.add_field(name=role_update,value=nr_str,inline=False)
                else:
                    return

                if new_roles == ['<@&842309176104976387>']:
                    if self.bot.new_member[str(after.id)] is True:
                        chat_channel = after.guild.get_channel(861883647070437386)
                        await chat_channel.send(f'୨୧・━━⋄✩ ₊ ˚・\nwelcome to our latte . .\n⸝⸝・{after.mention}')

                await self.roles_log.send(embed=embed)
            
            elif before.display_avatar != after.display_avatar:
                try:
                    embed = discord.Embed(title="Server Avatar change",description="New image is below, old to the right.",
                                colour=0xf3d4b4,
                                timestamp=datetime.now(timezone.utc))
                    embed.set_thumbnail(url=before.display_avatar.url)
                    embed.set_image(url=after.display_avatar.url)
                    embed.set_footer(text=after, icon_url=after.display_avatar.url)

                    await self.server_log.send(embed=embed)
                except:
                    pass

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.channel.id in PRIVATE_LOGS:
            message_channel = utils.json_loader.read_json("latte")
            self.message_log = self.bot.get_channel(message_channel["message-log"])

            if self.message_log is None:
                print("message_log is None")
                return

            if not after.author.bot:
                if before.content != after.content:
                    embed = discord.Embed(description=f"**Edited in**: {after.channel.mention}\n**Message link:** ||[click]({after.jump_url})||",
                                colour=0xFF8C00, #after.author.colour,
                                timestamp=datetime.now(timezone.utc))
                    if after.author.avatar.url is not None:           
                        embed.set_author(name=after.author.display_name , url=after.jump_url ,icon_url=after.author.avatar.url)
                    else:
                        embed.set_author(name=after.author.display_name , url=after.jump_url)
                    embed.set_footer(text="Message edit")
                
                    fields = [("**Before**", f"```{before.content}```" , False),
						    ("**After**", f"```{after.content}```", False)]
                
                    for name, value, inline in fields:
                        embed.add_field(name=name, value=value, inline=inline)
                    
                    #load_json
                    message_channel = utils.json_loader.read_json("latte")
                    await self.message_log.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.channel.id in PRIVATE_LOGS:
            message_channel = utils.json_loader.read_json("latte")
            self.message_log = self.bot.get_channel(message_channel["message-log"])

            if self.message_log is None:
                print("message_log is None")
                return

            if message.guild: #if message.guild.id:
                if not message.author.bot:

                    em = discord.Embed(color=0xDC143C , timestamp=datetime.now(timezone.utc))
                    if message.author.avatar.url is not None:
                        em.set_author(name=message.author.display_name, url=message.jump_url ,icon_url=message.author.avatar.url)
                    else:
                        em.set_author(name=message.author.display_name, url=message.jump_url)

                    if message.attachments is not None:
                        if len(message.attachments) > 1:
                            im = [x.proxy_url for x in message.attachments]
                            em.add_field(name='\uFEFF',value = f"This Message Contained {len(message.attachments)} Message Attachments, Please See Below")
                            await self.message_log.send(' '.join(im))

                        elif message.attachments:
                            image = message.attachments[0].proxy_url
                            em.description = f"**Deleted in:** {message.channel.mention}"
                            em.set_image(url=image)
                            em.set_footer(text="Message delete")
                        else:
                            em.description = f"**Deleted in:** {message.channel.mention}"
                            em.add_field(name=f"**Content:**", value=f"```{message.clean_content}```", inline=False)
                            em.set_footer(text="Message delete")

                    await self.message_log.send(embed=em)
                else:
                    pass
    #            else:
    #                delem = discord.Embed(color=0xDC143C , timestamp=datetime.now(timezone.utc))
    #                delem.set_author(name=message.author.display_name,icon_url=message.author.avatar.url)
    #                delem.description = f"**Message deleted in:** {message.channel}"
    #                delem.add_field(name=f"**Content:**", value=f"```{message.clean_content}```", inline=False)
    #                delem.set_footer(text="Message delete")

    #                await self.message_log.send(embed=delem)
    
    @commands.Cog.listener()
    async def on_voice_state_update(self , member, before, after):
        #load_json
        voice_channel = utils.json_loader.read_json("latte")
        self.voice_log = self.bot.get_channel(voice_channel["voice-log"])

        if self.voice_log is None:
            print("voice_log is None")
            return

        if member.guild.id == MYGUILD:
            
            embed = discord.Embed(timestamp=datetime.now(timezone.utc))
            if member.avatar.url is not None:
                embed.set_footer(text=member , icon_url=member.avatar.url)
            else:
                embed.set_footer(text=member)

            # if member.bot:
            #     return

            #voice_log
            if not before.channel:
                embed.description = f"**JOIN CHANNEL** : `{after.channel.name}`"
                embed.color=PTGREEN            
                await self.voice_log.send(embed=embed)
        
            if before.channel and not after.channel:
                embed.description = f"**LEFT CHANNEL** : `{before.channel.name}`"
                embed.color=PTRED2
                await self.voice_log.send(embed=embed)
        
            if before.channel and after.channel:
                if before.channel.id != after.channel.id:
                    embed.description = f"**SWITCHED CHANNELS** : `{before.channel.name}` to `{after.channel.name}`"
                    embed.color=PTYELLOW2
                    await self.voice_log.send(embed=embed)
                
                else:
                    if member.voice.self_stream:

                        embed.description = f"**STREAMING in** : `{before.channel.name}`"
                        embed.colour=PURPLE
                        self.current_streamers.append(member.id)
                        await self.voice_log.send(embed=embed)

                    elif member.voice.mute:
                        embed.description = f"**SERVER MUTED** in `{after.channel.name}`"
                        embed.colour=PTRED
                        await self.voice_log.send(embed=embed)

                    elif member.voice.deaf:
                        embed.description = f"**SERVER DEAFEN** in `{after.channel.name}`"
                        embed.colour=PTRED
                        await self.voice_log.send(embed=embed)

                    else:
                        if member.voice.deaf:
                            pass
                            # print("unmuted")
                        for streamer in self.current_streamers:
                            if member.id == streamer:
                                if not member.voice.self_stream:
                                        # print("user stopped streaming")
                                    self.current_streamers.remove(member.id)
                                break        
        else:
            return

        #privete_temp_channel
        if after.channel is not None:
            if after.channel.id == self.bot.underworldx[0]:
                underworld_vc = member.guild.get_channel(self.bot.underworldx[1])
                return await member.move_to(underworld_vc)
                
            if after.channel.id == self.bot.moonlightx[0]:
                moonlight_vc = member.guild.get_channel(self.bot.moonlightx[1])
                return await member.move_to(moonlight_vc)
            
            if after.channel.id == self.bot.angelx[0]:
                angel_vc = member.guild.get_channel(self.bot.angelx[1])
                return await member.move_to(angel_vc)
            
            if after.channel.id == self.bot.deathx[0]:            
                death_vc = member.guild.get_channel(self.bot.deathx[1])
                return await member.move_to(death_vc)
            
            if after.channel.id == bad_channel:
                if member.id in bad_id:
                    return
                else:
                    await member.move_to(channel=None)

            # if after.channel.name == "・ᵁᴺᴰᴱᴿᵂᴼᴿᴸᴰ・":
            #     chname = "ᵁᴺᴰᴱᴿᵂᴼᴿᴸᴰ"
            #     checkvoice = get_channel_by_name(after.channel.guild, channel_name=chname)
            #     if checkvoice is None:
            #         channel = await create_voice_channel(after.channel.guild, f'{chname}'.lower() , category_name="୨୧ ━━━━ ・Private")
                    
            #         if channel is not None:
            #             await member.move_to(channel)
                    
            #     elif checkvoice:
            #         await member.move_to(checkvoice)
            #     else:
            #         return
                    
            # if after.channel.name == "・ᴹᴼᴼᴺᴸᴵᴳᴴᵀ・":
            #     chname = "ᴹᴼᴼᴺᴸᴵᴳᴴᵀ"
            #     checkvoice = get_channel_by_name(after.channel.guild, channel_name=chname)
            #     if checkvoice is None:
            #         channel = await create_voice_channel(after.channel.guild, f'{chname}'.lower() , category_name="୨୧ ━━━━ ・Private")
                    
            #         if channel is not None:
            #             await member.move_to(channel)
                    
            #     elif checkvoice:
            #         await member.move_to(checkvoice)
            #     else:
            #         return
            
            # if after.channel.name == "・ᴬᴺᴳᴱᴸ・":
            #     chname = "ᴬᴺᴳᴱᴸ"
            #     checkvoice = get_channel_by_name(after.channel.guild, channel_name=chname)
            #     if checkvoice is None:
            #         channel = await create_voice_channel(after.channel.guild, f'{chname}'.lower() , category_name="୨୧ ━━━━ ・Private")
                    
            #         if channel is not None:
            #             await member.move_to(channel)
                    
            #     elif checkvoice:
            #         await member.move_to(checkvoice)
            #     else:
            #         return
            
            # if after.channel.name == "・ᴰᴱᴬᵀᴴ・":
            #     chname = "ᴰᴱᴬᵀᴴ"
            #     checkvoice = get_channel_by_name(after.channel.guild, channel_name=chname)
            #     if checkvoice is None:
            #         channel = await create_voice_channel(after.channel.guild, f'{chname}'.lower() , category_name="୨୧ ━━━━ ・Private")
                    
            #         if channel is not None:
            #             await member.move_to(channel)
                    
            #     elif checkvoice:
            #         await member.move_to(checkvoice)
            #     else:
            #         return
            
            # if after.channel.id == bad_channel:
            #     if member.id in bad_id:
            #         return
            #     else:
            #         await member.move_to(channel=None)

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        guild = self.bot.get_guild(MYGUILD)
        role = discord.utils.find(lambda r: r.name == 'ᴴ ᴱ ᴸ ᴬ・・ ♡', guild.roles)

        #add_offline_role
        if before.guild.id == MYGUILD:
            if str(after.status) == "online" or "dnd" and "idle":
                await before.remove_roles(role)
            if str(after.status) == "offline":
                await after.add_roles(role)

            #server_log
            user_update = utils.json_loader.read_json("latte")
            self.status_log = self.bot.get_channel(user_update["status-log"])

            #status
            if before.status != after.status:
                embed = discord.Embed(
                    colour=after.colour,
                    timestamp=datetime.now(timezone.utc)
                )
                if after.avatar is not None:
                    embed.set_author(name=after, icon_url=after.avatar.url)
                else:
                    embed.set_author(name=after)
                embed.set_footer(text=f"{str(after.status)}", icon_url=utils.status_icon(after.status))
                await self.status_log.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channels = [channel for channel in guild.channels]
        roles = roles= [role for role in guild.roles]
        embed = discord.Embed(title="Bot just joined: "+str(guild.name), color=random.randint(0,16777215))
        embed.set_thumbnail(url = guild.icon.url)
        embed.add_field(name='Server Name:',value=f'{guild.name}')
        embed.add_field(name='Server ID:',value=f'{guild.id}')
        embed.add_field(name='Server region:',value=f'{guild.region}')
        embed.add_field(name='Server Creation Date:',value=f'{guild.created_at.strftime(r"%d/%m/%Y %H:%M")}')
        embed.add_field(name='Server Owner:',value=f'{guild.owner}')
        embed.add_field(name='Server Owner ID:',value=f'{guild.owner_id}')
        embed.add_field(name='Member Count:',value=f'{guild.member_count}')
        embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
        embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
        await self.join_guild.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        channels = [channel for channel in guild.channels]
        roles = roles= [role for role in guild.roles]
        embed = discord.Embed(title="Bot just left: "+str(guild.name), color=random.randint(0,16777215))
        embed.set_thumbnail(url = guild.icon.url)
        embed.add_field(name='Server Name:',value=f'{guild.name}')
        embed.add_field(name='Server ID:',value=f'{guild.id}')
        embed.add_field(name='Server region:',value=f'{guild.region}')
        embed.add_field(name='Server Creation Date:',value=f'{guild.created_at.strftime(r"%d/%m/%Y %H:%M")}')
        embed.add_field(name='Server Owner:',value=f'{guild.owner}')
        embed.add_field(name='Server Owner ID:',value=f'{guild.owner_id}')
        try:
            embed.add_field(name='Member Count:',value=f'{guild.member_count}')
        except:
            pass
        embed.add_field(name='Amount of Channels:',value=f"{len(channels)}")
        embed.add_field(name='Amount of Roles:',value=f"{len(roles)}")
        await self.leave_guild.send(embed=embed)

    #    @commands.Cog.listener() #activity = role
    #    async def on_presence_update(self, before, after):
    #        games = ["game1", "game2", "game3"]
    #        if after.activity and after.activity.name.lower() in games:
    #            role = discord.utils.get(after.guild.roles, name=after.activity)
    #            await after.add_roles(role)
    #        elif before.activity and before.activity.name.lower() in games and not after.activity:
    #            role = discord.utils.get(after.guild.roles, name=after.activity)
    #            if role in after.roles: 
    #                await after.remove_roles(role)

def setup(bot):
    bot.add_cog(Activities(bot))