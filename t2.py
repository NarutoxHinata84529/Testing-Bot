import telebot
import os

# Read token from Railway Environment Variable
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚂 Hello! Your bot is running on Railway!")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "ℹ️ Available commands: /start, /help")

if __name__ == "__main__":
    print("✅ Bot started on Railway...")
    bot.infinity_polling()