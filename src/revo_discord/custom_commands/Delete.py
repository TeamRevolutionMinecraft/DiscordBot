from typing import Optional

import nextcord
from nextcord import SlashOption
from nextcord.ext import commands

from .. import utils


class Delete(commands.Cog):
    def __init__(self, bot, *_):
        self.bot = bot

    def __repr__(self):
        return "Delete Command"

    @nextcord.slash_command(description="Deletes Messages")
    async def delete(self, interaction: nextcord.Interaction, count: Optional[int] = SlashOption(required=True)):

        if utils.user_has_perm_for(interaction.user, "delete"):
            if count > 100:
                await interaction.send(utils.CONFIG["messages"]["to_many_messages"])
                return

            await interaction.channel.purge(limit=count)

            await interaction.send(f"Ich habe nun {count} Nachrichten gelöscht",
                                   ephemeral=False, delete_after=3)

        else:
            await interaction.send(utils.CONFIG["messages"]["no_permission"],
                                   ephemeral=False, delete_after=3)


def setup(bot: nextcord.Client, hub):
    bot.add_cog(Delete(bot, hub))
