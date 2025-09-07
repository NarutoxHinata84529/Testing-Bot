from pyrogram import Client, filters
from pyrogram.types import Message

# Your manager bot token


bot = Client("manager_bot", bot_token=BOT_TOKEN)

# /start command
@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text(
        "👋 Hello! I'm your Manager Bot.\n\n"
        "Use /help to see what I can do."
    )

# /help command
@bot.on_message(filters.command("help"))
async def help_cmd(client, message: Message):
    await message.reply_text(
        "📖 <b>Available Commands:</b>\n\n"
        "/start - Welcome message\n"
        "/help - Show this help menu\n",
        parse_mode="html"
    )

bot.run()