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

    async def show_page(self, interaction: discord.Interaction, page_number: int) -> None:
        page = await self._source.get_page(page_number)
        self.current_page = page_number

    def _update_labels(self, page_number: int) -> None:
        self.first_page.disabled = page_number == 0
        print("test")
        max_pages = self._source.get_max_pages()
        self.last_page.disabled = max_pages is None or (page_number + 1) >= max_pages
        self.next_page.disabled = max_pages is not None and (page_number + 1) >= max_pages
        self.back_page.disabled = page_number == 0
        return

        self.current.label = str(page_number + 1)
        self.back_page.label = str(page_number)
        self.next_page.label = str(page_number + 2)
        self.next_page.disabled = False
        self.back_page.disabled = False
        self.first_page.disabled = False

        max_pages = self._source.get_max_pages()
        if max_pages is not None:
            self.last_page.disabled = (page_number + 1) >= max_pages
            if (page_number + 1) >= max_pages:
                self.next_page.disabled = True
                self.next_page.label = '…'
            if page_number == 0:
                self.back_page.disabled = True
                self.back_page.label = '…'

    async def start(self, ctx):
        self.ctx = ctx
        self.message = await self.send_initial_message(ctx, ctx.channel)

    @ui.button(label='≪', style=ButtonStyle.blurple)
    async def first_page(self, button: ui.Button, interaction: discord.Interaction):
        await self.show_page(0)

    @ui.button(label='Back', style=ButtonStyle.blurple)
    async def back_page(self, button: ui.Button, interaction: discord.Interaction):
        await self.show_checked_page(self.current_page - 1)

    @ui.button(label="current", style=ButtonStyle.grey)
    async def current_page(self, button: ui.Button, interaction: discord.Interaction):
        self.clear_items()
        await interaction.response.edit_message(view=self)

    @ui.button(label='Next', style=ButtonStyle.blurple)
    async def next_page(self, button: ui.Button, interaction: discord.Interaction):
        await self.show_checked_page(self.current_page + 1)

    @ui.button(label='≫', style=ButtonStyle.blurple)
    async def last_page(self, button: ui.Button, interaction: discord.Interaction):
        await self.show_page(self._source.get_max_pages() - 1)
    
    async def _get_kwargs_from_page(self, page):
        value = await super()._get_kwargs_from_page(page)
        value.update({'view': self})
        return value

class Page_format_(menus.ListPageSource):
    async def format_page(self, view, entry):
        return str(entry)
