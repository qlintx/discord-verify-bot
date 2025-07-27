import disnake
from disnake.ext import commands

TOKEN = "DEIN_BOT_TOKEN" #gebe hier deinen bot token ein

GUILD_ID = 123       # Hier deine Server Id Einfügen
CHANNEL_ID = 123     # Kanal wo die Verifikations Nachricht gesendet wird
ROLE_TO_ADD_ID = 123 # Rolle nach dem drücken
ROLE_TO_REMOVE_ID = 0  # Optional: Rolle, die entfernt werden soll (0 = ignorieren)

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


class VerifyView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="✅ Verify", style=disnake.ButtonStyle.green)
    async def verify(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        guild = inter.guild
        member = inter.author

        role_to_add = guild.get_role(ROLE_TO_ADD_ID)
        role_to_remove = guild.get_role(ROLE_TO_REMOVE_ID) if ROLE_TO_REMOVE_ID else None

        if not role_to_add:
            await inter.response.send_message("❌ Rolle zum Hinzufügen nicht gefunden!", ephemeral=True)
            return

        try:
            await member.add_roles(role_to_add)
            if role_to_remove and role_to_remove in member.roles:
                await member.remove_roles(role_to_remove)
            await inter.response.send_message("✅ Du wurdest erfolgreich verifiziert!", ephemeral=True)
        except Exception as e:
            await inter.response.send_message(f"Fehler beim Verifizieren: {e}", ephemeral=True)


@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")
    guild = bot.get_guild(GUILD_ID)
    channel = guild.get_channel(CHANNEL_ID)

    if channel:
        view = VerifyView()
        await channel.send("Klicke auf den Button, um dich zu verifizieren:", view=view)
    else:
        print("Kanal nicht gefunden. Bitte überprüfe die CHANNEL_ID.")


bot.run(TOKEN)
