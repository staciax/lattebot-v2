import discord
from discord import ui , ButtonStyle
from discord.ext import menus

class Base_page(ui.View, menus.MenuPages):
    def __init__(self, source):
        super().__init__()
        self.ctx = None
        self.message = None
        self._source = source
        self.current_page = 0

    async def start(self, ctx):
        self.ctx = ctx
        self.message = await self.send_initial_message(ctx, ctx.channel)

    @ui.button(emoji='⏮️', style=ButtonStyle.blurple)
    async def t1(self, _, interaction):
        await self.show_page(0)

    @ui.button(emoji='◀️', style=ButtonStyle.blurple)
    async def t2(self, _, interaction):
        await self.show_checked_page(self.current_page - 1)

    @ui.button(emoji="⏹️", style=ButtonStyle.grey)
    async def t3(self, _, interaction):
        self.clear_items()
        await interaction.response.edit_message(view=self)
#        self.stop()

    @ui.button(emoji='▶️', style=ButtonStyle.blurple)
    async def t4(self, _, interaction):
        await self.show_checked_page(self.current_page + 1)

    @ui.button(emoji='⏭️', style=ButtonStyle.blurple)
    async def t5(self, _, interaction):
        await self.show_page(self._source.get_max_pages() - 1)

    async def _get_kwargs_from_page(self, page):
        value = await super()._get_kwargs_from_page(page)
        value.update({'view': self})
        return value

class Page_format_(menus.ListPageSource):
    async def format_page(self, view, entry):
        return str(entry)
