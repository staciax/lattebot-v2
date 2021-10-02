# Standard 
import discord
from discord.ext import commands

# Local
from utils.paginator import SimplePages

class roleinfo_view(discord.ui.View):
    def __init__(self, ctx, embed, entries, role):
        super().__init__(timeout=600)
        self.ctx = ctx
        self.embed = embed
        self.entries = entries
        self.role = role
        self.message = ""

    async def on_timeout(self):
        self.clear_items()
        await self.message.edit(view=self)
        self.stop()

    @discord.ui.button(label="Member list", style=discord.ButtonStyle.blurple)
    async def member_list(self, button: discord.ui.Button, interaction: discord.Interaction):
        p = SimplePages(entries=self.entries, per_page=10, ctx=self.ctx)
        p.embed.title = f"{self.role.name} : members list"
        p.embed.color = self.role.color
        self.message = await p.start()

    @discord.ui.button(label='Quit', style=discord.ButtonStyle.red)
    async def stop_pages(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.delete_original_message()
        self.stop()
    
    async def start(self):
        if not self.entries:
            if self.children[0].label == 'Member list':
                self.children[0].disabled = True
        self.message = await self.ctx.reply(embed=self.embed, view=self , mention_author=False)


class channel_info_view(discord.ui.View):
    def __init__(self, ctx, embed, channel , role_list, member_list):
        super().__init__(timeout=600)
        self.ctx = ctx
        self.embed = embed
        self.channel = channel
        self.role_list = role_list
        self.member_list = member_list
        self.message = ""

    async def on_timeout(self):
        self.clear_items()
        await self.message.edit(view=self)
        self.stop()
    
    @discord.ui.button(label="Roles access", style=discord.ButtonStyle.blurple)
    async def roles_list(self, button: discord.ui.Button, interaction: discord.Interaction):
        p = SimplePages(entries=self.role_list, per_page=10, ctx=self.ctx)
        p.embed.title = f"Roles in {self.channel.name}"
        p.embed.color = 0xffffff
        await p.start()
    
    @discord.ui.button(label="Member access", style=discord.ButtonStyle.blurple)
    async def member_list(self, button: discord.ui.Button, interaction: discord.Interaction):
        p = SimplePages(entries=self.member_list, per_page=10, ctx=self.ctx)
        p.embed.title = f"Members in {self.channel.name}"
        p.embed.color = 0xffffff
        await p.start()

    @discord.ui.button(label='Quit', style=discord.ButtonStyle.red)
    async def stop_pages(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        await interaction.delete_original_message()
        self.stop()
    
    async def start_text(self):
        if not self.role_list:
            if self.children[0].label == 'Roles access':
                self.remove_item(item=self.children[0])
        if not self.member_list:
            if self.children[0].label == 'Member access':
                self.remove_item(item=self.children[0])

        self.message = await self.ctx.reply(embed=self.embed, view=self, mention_author=False)
    
    async def start_voice(self):
        for item in self.children:
            if item.label == 'Member access':
                self.remove_item(item)
        self.message = await self.ctx.reply(embed=self.embed, view=self, mention_author=False)