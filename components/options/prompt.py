from abc import abstractmethod

from components.options.options import OptionsInterface


class Prompt(OptionsInterface):
    DISMISS = '\u274E'  # ❎
    CONFIRM = '\u2705'  # ✅

    def __init__(self, client, message):
        super().__init__(client, message, [self.DISMISS, self.CONFIRM])

    async def _on_click(self, option, user, is_removal):
        await self.client.delete_message(self.rendered_message)
        await self.after_dismissal(option.emoji)

    @abstractmethod
    async def after_dismissal(self, option):
        pass

