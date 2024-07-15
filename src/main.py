import argparse
import logging
import time

import revo_discord.discord_main as dc
import revo_api.api_main as api
import ipc
from config_manager import config_manager


def get_parser():
    """
    Generate an argument parser
    :return: New argument parser
    """
    new_parser = \
        argparse.ArgumentParser(description='Team Revolution Discord Bot', formatter_class=argparse.RawTextHelpFormatter,
                                epilog="See more info: www.team-revolution.net")

    new_parser.add_argument('-v', '--verbosity', required=False, action='count', default=False,
                            help='increase output verbosity (e.g.: -vv is more than -v).')

    return new_parser


def shutdown_procedure(*applications) -> None:
    for application in applications:
        application.shutdown()


def discord_run(hub) -> None:
    """
    Starts the discord bot
    Args:
        hub: IPC hub

    """
    dc.main(hub)


def api_run(hub) -> None:
    """
    Starts the API webserver
    Args:
        hub: IPC hub

    """
    api.main(hub)


def init_ipc_hub():
    """
    Initialize the IPC hub, the IPC hub has to be parsed
    as an object to every process that needs access to it

    Returns:
        IPC_HUB
    """

    discord_bus = ipc.hub.Bus("DISCORD")
    minecraft_bus = ipc.hub.Bus("MINECRAFT")

    hub = ipc.hub.Hub()
    hub.add_bus_to_hub(discord_bus)
    hub.add_bus_to_hub(minecraft_bus)

    return hub


def main(args):
    start_time = time.time()
    hub = init_ipc_hub()
    # discord_bot = mp.Process(target=discord_run, args=(hub, ))
    # api_bot = mp.Process(target=api_run, args=(hub, ))

    # discord_bot.start()
    # api_bot.start()
    configs = config_manager.ConfigManager(
        "/home/felix/git/02_revo/01_repos/revolution-bot-discord/data")
    while True:
        try:
            time.time()
        except KeyboardInterrupt:
            duration = time.time() - start_time
            minutes, seconds = divmod(duration, 60)
            hours, minutes = divmod(minutes, 60)
            shutdown_procedure(configs)
            logging.info(
                f"DiscordBot ran for {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds.")
            break


if __name__ == "__main__":
    parser = get_parser()
    parsed_args = parser.parse_args()
    LOG_FORMAT = '[%(asctime)s.%(msecs)03d|%(levelname)s|%(name)s] %(message)s'
    # level is set to 10 (DEBUG) if -v is given, 9 if -vv, 8 if -vvv and so on. Otherwise to 20 (INFO)
    level = logging.DEBUG - parsed_args.verbosity + \
        1 if parsed_args.verbosity > 0 else logging.INFO
    logging.basicConfig(format=LOG_FORMAT, datefmt='%H:%M:%S', level=level)
    main(args=parsed_args)
