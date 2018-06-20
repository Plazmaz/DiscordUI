import asyncio


class DiscordUIManager:
    def __init__(self, client):
        self.client = client
        self.ui_elements = []
        self.client.add_listener(self.on_reaction_add, 'on_reaction_add')
        self.client.add_listener(self.on_reaction_remove, 'on_reaction_removed')
        self.client.add_listener(self.on_message_delete, 'on_message_delete')

    def register_ui_element(self, element):
        self.ui_elements.append(element)

    async def on_message_delete(self, message):
        for element in self.ui_elements[:]:
            if element.rendered_message.id == message.id:
                self.ui_elements.remove(element)

    async def on_reaction_add(self, reaction, user):
        if user.id == self.client.user.id:
            return

        for element in self.ui_elements:
            await element.on_click(reaction, user, False)

    async def on_reaction_remove(self, reaction, user):
        if user.id == self.client.user.id:
            return

        for element in self.ui_elements:
            await element.on_click(reaction, user, True)
