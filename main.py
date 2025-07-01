import telebot

# Your manager bot token
BOT_TOKEN = "7880080240:AAHUBpbJ58ZQ33uPekAsu2coyiGHMDTo_xc"

bot = telebot.TeleBot(BOT_TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
        "👋 Hello! I'm your Manager Bot.\n\n"
        "Use /help to see what I can do."
    )

# /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,
        "📖 *Available Commands:*\n\n"
        "/start - Welcome message\n"
        "/help - Show this help menu\n"
        "/joke - Get a random joke\n"
        "/kang - Steal a sticker/gif to your pack\n"
        "/afk [reason] - Set yourself as AFK\n"
        "/brb [reason] - Set BRB status\n"
        "/insult - Send a funny insult\n"
        "/promote - Promote a user\n"
        "/fullpromote - Full admin rights\n"
        "/demote - Demote a user\n",
        parse_mode="Markdown"
    )

bot.infinity_polling()