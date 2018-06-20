from abc import ABCMeta, abstractmethod


class OptionsInterface(metaclass=ABCMeta):
    def __init__(self, ui_manager, message, options):
        ui_manager.register_ui_element(self)
        self.client = ui_manager.client
        self.message = message
        self.options = options
        self.rendered_message = None

    async def render(self, channel):
        self.rendered_message = await self.client.send_message(channel, self.message)
        for option in self.options:
            await self.client.add_reaction(self.rendered_message, option)

    async def on_click(self, option, user, is_removal):
        if option.message.id != self.rendered_message.id:
            return

        if option.emoji not in self.options:
            return
        await self._on_click(option, user, is_removal)

    @abstractmethod
    async def _on_click(self, option, user, is_removal):
        pass