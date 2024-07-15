import os
import logging

import nextcord
from nextcord.ext import commands

from . import custom_commands


def main(hub) -> None:
    """
    Main task for the Discord bot
    it manages the start and loading of the commands
    Args:
        hub: Ipc Hub

    """
    intents = nextcord.Intents.default()

    intents.members = True
    intents.message_content = True
    intents.typing = True
    intents.presences = True

    bot = commands.Bot(intents=intents)

    @bot.event
    async def on_ready():
        logging.info("Monty is ready")

    for extension in custom_commands.load_all_commands(bot, {"hub": hub}):
        logging.info(f"{extension} was installed")
        bot.add_cog(extension)

    bot.run(os.getenv("TOKEN"))
