# Standard 
import discord , asyncio , json
from discord import Embed
import datetime
from discord.ext import commands , tasks
from datetime import datetime, timezone , timedelta

# Third party
from difflib import get_close_matches
from discord.ext import menus

# Local
import utils
from utils.ButtonRef import Base_page
from utils.paginator import SimplePages
from config import PTGREEN

class All_tag_view(menus.ListPageSource):
    async def format_page(self, view, entry):
        #format_page
        offset = view.current_page * 10
        #fix_enumerate_start_at_0
        if offset == 0: offset = 1
        elif offset >= 10: offset = offset + 1
        
        #enumerate_list
        list_per_page = '\n'.join(f'{i}. {v}' for i, v in enumerate(entry, start=offset))
        return Embed(title="Tags list", description=f"{list_per_page}",color=0xBFA2DB)

class Search_tag_view(menus.ListPageSource):
    async def format_page(self, view, entry):
        #format_page
        offset = view.current_page * 10
        if offset == 0: offset = 1
        elif offset >= 10: offset = offset + 1

        list_per_page = '\n'.join(f'{i}. {v}' for i, v in enumerate(entry, start=offset))
        return Embed(title="Tags search", description=f"{list_per_page}",color=0xBFA2DB)

class Tags(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-{self.__class__.__name__}")

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    async def tag(self, ctx, *, name):
        
        #check_int_or_str
        isInt = True
        try:
            int(name)
        except ValueError:
            isInt = False

        #check_int_true_or_false
        if isInt:
            check_data = await self.bot.tagdb.find_by_custom({"guild_id": ctx.guild.id, "tag_id": int(name)})
        else:
            check_data = await self.bot.tagdb.find_by_custom({"guild_id": ctx.guild.id, "tag": str(name)})
        
        #found_or_not_found
        if check_data is not None:
            message = check_data['content']
        else:
            not_found = await self.bot.tagdb.find_many_by_custom({"guild_id": ctx.guild.id})
            names = (r['tag'] for r in not_found)
            matches = get_close_matches(name , names)
            i = 0
            if matches:
                i += 1
                matches = "\n".join(matches)
                message = f"Tag not found. Did you mean...\n`{matches}`"

        await ctx.send(message)
    
    @tag.command(aliases=['add'])
    @commands.guild_only()
    async def tag_add(self, ctx, name:str, *, content: commands.clean_content):
        #find_data
        data_check = await self.bot.tagdb.find_by_custom({"guild_id": ctx.guild.id, "tag": name})

        #data_count
        data_count = await self.bot.tagdb.find_many_by_custom({})
        num_list = []
        for x in data_count:     
            num = x['tag_id']
            num_list.append(num)
        next_num = max(num_list)

        #check_data
        if bool(data_check) == True:
            await ctx.send("can't use this tag!", delete_after=15)
            return

        #when_content_more_2000
        if len(content) > 2000:
            return await ctx.send('Tag content is a maximum of 2000 characters.', delete_after=15)

        #create_data
        data = {
            "user_id": ctx.author.id,
            "guild_id": ctx.guild.id,
            "tag": name,
            "content": content,
            "tag_id": next_num + 1
        }

        #update_data
        await self.bot.tagdb.update_by_custom(
            {"user_id": ctx.author.id, "guild_id": ctx.guild.id, "tag": name}, data
        )

        #reponse
        embed = Embed(description=f"`{name}` is added", color=PTGREEN)
        await ctx.send(embed=embed)

    @tag.command(aliases=["alias"])
    @commands.guild_only()
    async def tag_alias(self, ctx, name_old:str, name_new:str):
        #find_data
        data_check = await self.bot.tagdb.find_by_custom({"guild_id": ctx.guild.id, "tag": name_old})
        
        #check_data
        if bool(data_check) == False:
            await ctx.send("tag not found", delete_after=15)
            return

        #check_owner_tag
        if str(data_check["user_id"]) != str(ctx.author.id):
            await ctx.send("You are not the owner of the tag", delete_after=15)
            return

        #find_again
        data = await self.bot.tagdb.find_by_custom({"user_id": ctx.author.id, "guild_id": ctx.guild.id, "tag": name_old})
        
        #update_data
        data["tag"] = name_new                 
        await self.bot.tagdb.update_by_custom(
            {"user_id": ctx.author.id, "guild_id": ctx.guild.id, "tag": name_old}, data
        )

        #reponse
        embed = Embed(description=f"{ctx.author.mention} is edited alias `{name_old}` to `{name_new}`", color=0xFCFFA6)
        await ctx.send(embed=embed, delete_after=15)
    
    @tag.command(aliases=["edit"])
    @commands.guild_only()
    async def tag_edit(self, ctx, name:str, *, content: commands.clean_content):
        #find_data
        data_check = await self.bot.tagdb.find_by_custom({"guild_id": ctx.guild.id, "tag": name})
        
        #check_data
        if bool(data_check) == False:
            await ctx.send("tag not found", delete_after=15)
            return

        #check_owner_tag
        elif data_check["user_id"] != ctx.author.id:
            await ctx.send("You are not the owner of the tag", delete_after=15)
            return

        data = await self.bot.tagdb.find_by_custom({"guild_id": ctx.guild.id, "tag": name})
                    
        data["content"] = content

        await self.bot.tagdb.update_by_custom(
            {"guild_id": ctx.guild.id, "tag": name}, data
        )

        #reponse
        embed = Embed(description=f"`{name}` is edited message by {ctx.author.mention}", color=0xFCFFA6)
        await ctx.send(embed=embed, delete_after=15)

    @tag.command(aliases=["remove"])
    @commands.guild_only()
    async def tag_remove(self, ctx, name:str):
        #find_data
        data_check = await self.bot.tagdb.find_by_custom({"guild_id": ctx.guild.id, "tag": name})

        #check_data
        if bool(data_check) == False:
            await ctx.send("tag not found", delete_after=15)
            return

        #check_owner_tag
        if data_check["user_id"] != ctx.author.id:
            await ctx.send("You are not the owner of the tag" , delete_after=15)
            return

        #deletd_data
        data_deleted = await self.bot.tagdb.delete_by_custom({"guild_id": ctx.guild.id, "tag": name})

        #check_data_deleted?
        if bool(data_deleted) == False:
            print("data deleted false")
            return
        
        #delete_is_true_or_false
        if data_deleted and data_deleted.acknowledged:
            embed_del = Embed(description=f"{ctx.author.mention} is deleted tag `{name}`", color=0xFF7878)
            await ctx.send(embed=embed_del)
        else:
            await ctx.send(
                f"I could not find tag"
            , delete_after=15)

    @tag.command(name="all" , aliases=["list"])
    @commands.guild_only()
    async def tag_all(self, ctx):

        #sort_tag
        data = await self.bot.tagdb.find_many_by_custom({"guild_id": ctx.guild.id})
        
        #count_tag
        all_tag = []
        for x in data:
            tags = f'{x["tag"]} (ID : {x["tag_id"]})'
            all_tag.append(tags)
        
        #view_button
        if all_tag:
            p = SimplePages(entries=all_tag, per_page=10, ctx=ctx)
            p.embed.color = 0xBFA2DB
            await p.start()
        else:
            #reponse
            embed = Embed(description=f"Tags is not found", color=PTGREEN)
            await ctx.send(embed=embed , delete_after=15)

#        m = Base_page(All_tag_view(all_tag, per_page=10))
#        await m.start(ctx)
       
    @tag.command(name="search", aliases=["find"])
    @commands.guild_only()
    async def tag_search(self, ctx, name:str):

        #find_name_tag
        not_found = await self.bot.tagdb.find_many_by_custom({"guild_id": ctx.guild.id})
        
        total:int = len(not_found)
        names = (r['tag'] for r in not_found)
        matches = get_close_matches(name , names , n=total)

        #coverter_to_string
        tag_found = []
        for x in matches:
            data = await self.bot.tagdb.find_many_by_custom({"guild_id": ctx.guild.id, "tag": x})
            find_id = '\n'.join(f'{i["tag_id"]}' for i in data)
            tag_name_id = f'{x} (ID : {find_id})'
            tag_found.append(tag_name_id)

        if tag_found:
            #view_button
            p = SimplePages(entries=tag_found, per_page=10, ctx=ctx)
#            p.embed.title = "Tags search"
            p.embed.color = 0xBFA2DB
            await p.start()
        else:
            #reponse
            embed = Embed(description=f"`{name}` is not found", color=PTGREEN)
            await ctx.send(embed=embed , delete_after=15)

    @commands.command()
    @commands.is_owner()
    async def tagcount(self, ctx, guild_id:int=None):
        if guild_id:
            not_found = await self.bot.tagdb.find_many_by_custom({"guild_id": guild_id})
        else:
            not_found = await self.bot.tagdb.find_many_by_custom({})
        
        if not not_found:
            return await ctx.send("data not found")
        
#        max_num = []
#        for x in not_found:     
#            num = x['tag_id']
#            max_num.append(num)

        embed = discord.Embed(description=f"Total tags : `{len(not_found)}`",color=PTGREEN)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Tags(bot))