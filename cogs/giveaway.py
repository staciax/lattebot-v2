# Standard 
import discord
import random
import datetime
import asyncio
import re
from discord.ext import commands
from datetime import datetime, timedelta, timezone

# Third party

# Local
from config import *
import utils

class Giveaway(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")
        
    @commands.command(aliases=['start', 'g'])
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True) #@commands.has_permissions(administrator = True)
    async def giveaway(self, ctx):
        await ctx.send("Select the channel.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        try:
            msg1 = await self.bot.wait_for('message', check=check, timeout=30.0)

            channel_converter = discord.ext.commands.TextChannelConverter()
            try:
                giveawaychannel = await channel_converter.convert(ctx, msg1.content)
            except commands.BadArgument:
                return await ctx.send("This channel doesn't exist, please try again.")
    
        except asyncio.TimeoutError:
            await ctx.send("You took to long, please try again!")
        
        if not giveawaychannel.permissions_for(ctx.guild.me).send_messages or not giveawaychannel.permissions_for(
            ctx.guild.me).add_reactions:
            return await ctx.send(
            f"Bot does not have correct permissions to send in: {giveawaychannel}\n **Permissions needed:** ``Add reactions | Send messages.``")

        await ctx.send("How many winners?")
        try:
            msg2 = await self.bot.wait_for('message', check=check, timeout=30.0)
            try:
                winerscount = int(msg2.content)
            except ValueError:
                return await ctx.send("You didn't specify a number of winners")

        except asyncio.TimeoutError:
            await ctx.send("You took to long, please try again!")  

        await ctx.send("Select an amount of time for the giveaway. `(s|m|h|d|w)`")
        try:
            since = await self.bot.wait_for('message', check=check, timeout=30.0)

        except asyncio.TimeoutError:
            await ctx.send("You took to long, please try again!")

        seconds = ("s", "sec", "secs", 'second', "seconds")
        minutes = ("m", "min", "mins", "minute", "minutes")
        hours = ("h", "hour", "hours")
        days = ("d", "day", "days")
        weeks = ("w", "week", "weeks")
        rawsince = since.content

        try:
            temp = re.compile("([0-9]+)([a-zA-Z]+)")
            if not temp.match(since.content):
                return await ctx.send("You did not specify a unit of time, please try again.")
            res = temp.match(since.content).groups()
            time = int(res[0])
            since = res[1]

        except ValueError:
            return await ctx.send("You did not specify a unit of time, please try again.")

        if since.lower() in seconds:
            timewait = time
        elif since.lower() in minutes:
            timewait = time * 60
        elif since.lower() in hours:
            timewait = time * 3600
        elif since.lower() in days:
            timewait = time * 86400
        elif since.lower() in weeks:
            timewait = time * 604800
        else:
            return await ctx.send("You did not specify a unit of time, please try again.")

        await ctx.send("What would you like the prize to be?")
        try:
            msg4 = await self.bot.wait_for('message', check=check, timeout=30.0)

        except asyncio.TimeoutError:
            await ctx.send("You took to long, please try again.")

        if ctx.guild.id == MYGUILD:
            logembed = discord.Embed(title="Giveaway Logged",
                                    description=f"**Prize:** ``{msg4.content}``\n**Winners:** ``{winerscount}``\n**Channel:** {giveawaychannel.mention}\n**Host:** {ctx.author.mention}",
                                    color=0xffffff)
            logembed.set_thumbnail(url=ctx.author.avatar.url)

            logchannel = ctx.guild.get_channel(GIVEAWAY_LOG) 
            await logchannel.send(embed=logembed)

        futuredate = datetime.utcnow() + timedelta(seconds=timewait)
        embed1 = discord.Embed(color=0xBFA2DB, # random color (color=discord.Color(random.randint(0x000000, 0xFFFFFF)),
                               title=f"🎉 LATTE GIVEAWAY 🎉", timestamp=futuredate,
                               description=f'React with 🎉 to enter!\nWinner(s) : **{winerscount}**\nHosted by: {ctx.author.mention}\n\n`{msg4.content}`\n')

        embed1.set_footer(text=f"Ends at")
        msg = await giveawaychannel.send(embed=embed1)
        await msg.add_reaction("🎉")
        await asyncio.sleep(timewait)
        message = await giveawaychannel.fetch_message(msg.id)
        for reaction in message.reactions:
            if str(reaction.emoji) == "🎉":
                users = await reaction.users().flatten()
                if len(users) == 1:
                    return await msg.edit(embed=discord.Embed(title="Nobody has won the giveaway."))
        try:
            winners = random.sample([user for user in users if not user.bot], k=winerscount)
        except ValueError:
            return await giveawaychannel.send("not enough participants")
        winnerstosend = "\n".join([winner.mention for winner in winners])

        newEmbed = discord.Embed(title=f'🎉GIVEAWAY ENDED🎉',description=f'Winner(s) : **{winnerstosend}**\nHosted By :{ctx.author.mention}\n\n`{msg4.content}`\n', color=0x2f3136,timestamp=futuredate)
        newEmbed.set_footer(text=f'Ends at')
        
        win = await msg.edit(embed=newEmbed)
        print(winnerstosend)
        embed_ended = discord.Embed(description=f"**Congrats {winnerstosend}!**\nPlease contact {ctx.author.mention} about your prize.\n [giveaway url]({win.jump_url})" , color=WHITE)
        await ctx.send(embed=embed_ended)

    @commands.command(description="reroll giveaway")
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    async def reroll(self, ctx):
        async for message in ctx.channel.history(limit=30, oldest_first=False):
            if message.author.id == self.bot.user.id and message.embeds:
                reroll = await ctx.fetch_message(message.id)
                users = await reroll.reactions[0].users().flatten()
                users.pop(users.index(self.bot.user))
                winner = random.choice(users)
    
                reEmbed = discord.Embed(title=f'🎉GIVEAWAY ENDED🎉',description=f'Winner(s) : {winner.mention}\nHosted By : {ctx.author.mention}\n', color=0x000001,timestamp=datetime.now(timezone.utc))
                reEmbed.set_footer(text=f'Ends at')
                
                await reroll.edit(embed=reEmbed)
                await ctx.send(f"You won giveaway **{winner.mention}** Please contact Host **{ctx.author.mention}**") #ctx.send(f"The new winner is {winner.mention}")
                break
        else:
            await ctx.send("No giveaways going on in this channel.")
            
def setup(bot):
    bot.add_cog(Giveaway(bot))