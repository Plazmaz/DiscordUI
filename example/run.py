import discord
from discord.ext.commands import Bot

from discord_ui_manager import DiscordUIManager
from components.options.prompt_with_response import PromptWithResponse

client = Bot(command_prefix='!')


@client.event
async def on_ready():
    discord_ui = DiscordUIManager(client)
    interface = PromptWithResponse(discord_ui, 'Allow Trader to visit?', 'Trader allowed into your village.',
                                   'Trader was told to turn away for other lands.')
    interface2 = PromptWithResponse(discord_ui, 'Allow Trader to visit?', 'Trader allowed into your village.',
                                    'Trader was told to turn away for other lands.')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client.get_all_channels())
    general_channel = discord.utils.get(client.get_all_channels(), name='general')
    print(general_channel.id)
    await interface.render(general_channel)
    await interface2.render(general_channel)

client.run('example_token')
