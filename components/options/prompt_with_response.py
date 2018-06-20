from components.options.prompt import Prompt


class PromptWithResponse(Prompt):
    def __init__(self, client, message, on_confirmation, on_dimsissal):
        super().__init__(client, message)
        self.on_confirmation = on_confirmation
        self.on_dimsissal = on_dimsissal

    async def after_dismissal(self, option):
        if option == self.CONFIRM:
            await self.client.send_message(self.rendered_message.channel, self.on_confirmation)
        elif option == self.DISMISS:
            await self.client.send_message(self.rendered_message.channel, self.on_dimsissal)
