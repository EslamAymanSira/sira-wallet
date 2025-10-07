import disnake
from disnake.ext import commands
import os

TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID", 0))

bot = commands.InteractionBot(intents=disnake.Intents.default())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.slash_command(description="اختبار البوت", guild_ids=[GUILD_ID] if GUILD_ID else None)
async def ping(inter):
    await inter.response.send_message("🏓 البوت شغال تمام!")

bot.run(TOKEN)
