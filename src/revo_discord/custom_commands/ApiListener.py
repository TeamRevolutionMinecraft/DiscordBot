import asyncio
from queue import Empty

import nextcord
from nextcord.ext import commands, tasks


class Listener(commands.Cog):
    def __init__(self, bot, hub):
        self.bot = bot
        self.hub = hub
        self.api_listener.start()

    def __repr__(self):
        return "WebApi Listener Tasks"

    @tasks.loop(seconds=1, reconnect=False)
    async def api_listener(self):
        try:
            message = self.hub.get_bus_from_hub("DISCORD").get_msg_from_bus(timeout=0.1)
            if int(message.target_id) != 1:
                return
            channel = self.bot.get_channel(int(message.data["channel"]))

            # message.data["content"]
            await asyncio.wait_for(channel.send(embed=Message(content=message.data["content"], embed=True,
                                                              color=message.data["color"],
                                                              message_author=message.data["author"],
                                                              head_url=message.data["author_picture"])
                                                .build_message()), 2)
        except Empty:
            return
        except asyncio.TimeoutError:
            print("Time out")

    @api_listener.before_loop
    async def api_listener_before(self):
        await self.bot.wait_until_ready()


class Message:
    def __init__(self, content: str, embed: bool, **kwargs):
        self.content = content
        self.embed = embed
        self.config = {}

        if embed:
            self.config |= {"color": int(kwargs["color"])}
            self.config |= {"message_author": kwargs["message_author"]}
            self.config |= {"head_url" : kwargs["head_url"]}

    def __get_embed(self):
        embed = nextcord.Embed(colour=self.config["color"], description=self.content)
        embed.set_author(
            icon_url=self.config["head_url"],
            name=self.config["message_author"])

        return embed

    def build_message(self):
        return self.__get_embed()


def setup(bot: nextcord.Client, hub):
    bot.add_cog(Listener(bot, hub))
