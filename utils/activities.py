import discord

from discord.ext import commands

async def create_text_channel(guild, channel_name):
        """
        Creates a new channel in the category "Game"
        """
        category = get_category_by_name(guild, "Games")
        await guild.create_text_channel(channel_name, category=category)
        channel = get_channel_by_name(guild, channel_name)
        return channel

async def create_voice_channel(guild, channel_name , category_name="PRIVATELATTE" , user_limit=None):
        category = get_category_by_name(guild, category_name)
        await guild.create_voice_channel(channel_name, category=category , user_limit=user_limit)
        channel = get_channel_by_name(guild, channel_name)
        return channel

async def voice_move_user(guild, channel_name , category_name):
        channel = get_channel_by_name(guild, channel_name)
        return channel
        
def get_channel_by_name(guild, channel_name):
        channel = None
        for c in guild.channels:
            if c.name == channel_name.lower():
                channel = c
                break
        return channel

def get_category_by_name(guild, category_name):
        category = None
        for c in guild.categories:
            if c.name == category_name:
                category = c
                break
        return category

async def upsert_custom(
        self, filter_dict, update_data, option="set", *args, **kwargs
        ):
        await self.update_by_custom(
                filter_dict, update_data, option, upsert=True, *args, **kwargs
        )

def find_invite_by_code(invite_list, code):
        for inv in invite_list:
            if inv.code == code:
                return inv

async def edited(self, ctx, channel: discord.TextChannel, *, new_name):
        await channel.edit(name=new_name)


async def welcome_chat(ctx, guild):
        print('test')
