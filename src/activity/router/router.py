from discord import Client, Intents, Interaction, app_commands
from discord.app_commands.commands import Group

from src.activity.service.service import ActivityService


class DiscordClient:
    def __init__(self, token: str, intents: Intents, ase: ActivityService):
        self.token = token
        self.intents = intents
        self.intents.members = True
        self.intents.presences = True  # メンバーのステータスを取得するために必要
        self.client = Client(intents=intents)
        self.tree = app_commands.CommandTree(self.client)
        self.ase = ase

        @self.client.event
        async def on_ready():
            await self.tree.sync()
            print("Bot is ready")

        @self.tree.command(name="run", description="Run activity bot")
        async def run(
            _group: Group, interaction: Interaction, *_args, **_kwargs
        ) -> None:
            guild = interaction.guild

            if guild is None:
                await interaction.response.send_message("Guild not found")
                return

            print("Running activity bot")
            members = list(guild.members)
            message = self.ase.StoreActivity(members)
            await interaction.response.send_message(message)

    def run(self):
        self.client.run(self.token)
