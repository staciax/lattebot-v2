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
    async def tag(self, ctx, *, name:str):
        #find_data
        check_data = await self.bot.tagdb.find_by_custom({"guild_id": ctx.guild.id, "tag": name})
        
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
            "content": content
        }

        #update_data
        await self.bot.tagdb.update_by_custom(
            {"user_id": ctx.author.id, "guild_id": ctx.guild.id, "tag": name}, data
        )

        #reponse
        embed = Embed(description=f"`{name}` is added", color=0xC1FFD7)
        await ctx.send(embed=embed, delete_after=15)
    
    @tag.command(name="alias")
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
        embed = Embed(description=f"{ctx.author} is edited alias `{name_old}` to `{name_new}`", color=0xFCFFA6)
        await ctx.send(embed=embed, delete_after=15)
    
    @tag.command(name="edit")
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

    @tag.command(name="remove")
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
            embed_del = Embed(description=f"{ctx.author} is deleted tag `{name}`", color=0xFF7878)
            await ctx.send(embed=embed_del)
        else:
            await ctx.send(
                f"I could not find tag"
            , delete_after=15)

    @tag.command(name="all" , alias=["list"])
    @commands.guild_only()
    async def tag_all(self, ctx):

        #sort_tag
        data = await self.bot.tagdb.find_many_by_custom({"guild_id": ctx.guild.id})
        data = sorted(data, key=lambda x: x["tag"] ,  reverse=True)
        
        #count_tag
        all_tag = []
        for x in data:
            tags = x["tag"]
            all_tag.append(tags)

        #view_button
        m = Base_page(All_tag_view(all_tag, per_page=10))
        await m.start(ctx)
       
    @tag.command(name="search", alias=["find"])
    @commands.guild_only()
    async def tag_search(self, ctx, name:str):

        #find_name_tag
        not_found = await self.bot.tagdb.find_many_by_custom({"guild_id": ctx.guild.id})
        names = (r['tag'] for r in not_found)
        matches = get_close_matches(name , names , n=25)
        print(matches)

        #coverter_to_string
        tag_found = []
        for x in matches:
            print(x)
            tag_found.append(x)

        if len(tag_found) > 5:
            #view_button
            message = Base_page(Search_tag_view(tag_found, per_page=10))
            await message.start(ctx)
        elif tag_found:
            i = 0
            embed = Embed(title="Tags search", description="",color=0xBFA2DB)
            for x in tag_found:
                i += 1
                embed.description += f"{i}. {x}\n"

            await ctx.send(embed=embed)
        else:
            #reponse
            embed = Embed(description=f"`{name}` is not found", color=0xC1FFD7)
            await ctx.send(embed=embed , delete_after=15)


def setup(bot):
    bot.add_cog(Tags(bot))