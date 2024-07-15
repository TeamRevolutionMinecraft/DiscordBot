from .ApiListener import Listener
from .Delete import Delete
from .DiscordListener import DiscordListener


def load_all_commands(bot, extras) -> list:
    """
    Creates all tasks and custom_commands the discord bot needs

    Args:
        bot: the discord Bot
        extras: a dict of necessary info for some functions e.g. IPC hub

    Returns:
        a list of Cogs to be activated
    """

    list_of_ops = [
            Delete(bot),
            Listener(bot, extras["hub"]),
            DiscordListener(bot, extras["hub"])
        ]

    return list_of_ops
