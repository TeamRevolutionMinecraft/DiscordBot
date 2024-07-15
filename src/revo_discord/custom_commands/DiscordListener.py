
from nextcord.ext import commands
from ipc.message import IpcMessage
import nextcord

class DiscordListener(commands.Cog):
    def __init__(self, bot, hub):
        self.bot = bot
        self.hub = hub

    def __repr__(self):
        return "Discord Listener"

    @commands.Cog.listener()
    async def on_message(self, message):
        # Todo change channel id to the correct channel
        if message.author == self.bot.user or message.channel != self.bot.get_channel(1009849023991136268):
            return

        bus = self.hub.get_bus_from_hub("MINECRAFT")

        msg = IpcMessage(sender_id=2,
                         target_id=3,
                         keep_alive=None,
                         data={
                            "sender": message.author.display_name,
                            "msg": message.content
                          })
        msg.send_message(bus)


def setup(bot: nextcord.Client, hub):
    bot.add_cog(DiscordListener(bot, hub))
