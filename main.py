import telebot
from telebot import types
import random

BOT_TOKEN = "7880080240:AAHUBpbJ58ZQ33uPekAsu2coyiGHMDTo_xc"
bot = telebot.TeleBot(BOT_TOKEN)

AFK_STATUS = {}

JOKES = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I'm on a seafood diet. I see food and I eat it.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call fake spaghetti? An impasta.",
    "I would tell you a construction joke, but I'm still working on it.",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "What do you call cheese that isn't yours? Nacho cheese!"
]

INSULTS = [
    "You're as useless as the 'g' in lasagna.",
    "If I had a face like yours, I'd sue my parents.",
    "You have something on your chin… no, the third one down.",
    "You're the reason shampoo has instructions.",
    "You're like a cloud. When you disappear, it’s a beautiful day.",
    "Your secrets are always safe with me. I never even listen when you tell me them.",
    "You bring everyone so much joy… when you leave the room.",
    "You're not stupid; you just have bad luck thinking.",
    "You're like a software update. Whenever I see you, I think, 'Not now.'",
    "You're as bright as a black hole."
]

# /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Hello! I'm your Manager Bot.\nUse /help to see what I can do.")

# /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "📖 *Available Commands:*\n\n"
        "/start - Welcome message\n"
        "/help - Show this help menu\n"
        "/joke - Get a random joke 😂\n"
        "/kang - Steal sticker/gif to your pack 📦\n"
        "/afk [reason] - Set yourself as AFK 💤\n"
        "/brb [reason] - Set BRB status 🚶‍♂️\n"
        "/insult - Send a funny insult 😈\n"
        "/promote - Promote a user 🛡️\n"
        "/fullpromote - Full admin rights 🔱\n"
        "/demote - Demote a user ❌"
    )
    bot.reply_to(message, help_text, parse_mode="Markdown")

# /joke
@bot.message_handler(commands=['joke'])
def joke(message):
    bot.reply_to(message, random.choice(JOKES))

# /insult
@bot.message_handler(commands=['insult'])
def insult(message):
    bot.reply_to(message, random.choice(INSULTS))

# /afk and /brb
@bot.message_handler(commands=['afk', 'brb'])
def afk_brb(message):
    user = message.from_user
    reason = message.text.split(' ', 1)[1] if ' ' in message.text else "No reason provided"
    AFK_STATUS[user.id] = reason
    bot.reply_to(message, f"🔕 {user.first_name} is now AFK.\n💬 Reason: {reason}")

# /kang (Sticker/GIF Stealer)
@bot.message_handler(commands=['kang'])
def kang(message):
    if message.reply_to_message and (message.reply_to_message.sticker or message.reply_to_message.animation):
        file_id = message.reply_to_message.sticker.file_id if message.reply_to_message.sticker else message.reply_to_message.animation.file_id
        bot.send_sticker(message.chat.id, file_id) if message.reply_to_message.sticker else bot.send_animation(message.chat.id, file_id)
        bot.reply_to(message, "✅ Stolen successfully!")
    else:
        bot.reply_to(message, "⚠️ Reply to a sticker or GIF to steal it.")

# /promote
@bot.message_handler(commands=['promote'])
def promote(message):
    user = get_target_user(message)
    if user:
        bot.promote_chat_member(
            message.chat.id,
            user.id,
            can_change_info=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_invite_users=True
        )
        bot.reply_to(message, f"✅ Promoted [{user.first_name}](tg://user?id={user.id})", parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ Could not find the user to promote.")

# /fullpromote
@bot.message_handler(commands=['fullpromote'])
def fullpromote(message):
    user = get_target_user(message)
    if user:
        bot.promote_chat_member(
            message.chat.id,
            user.id,
            can_manage_chat=True,
            can_change_info=True,
            can_delete_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_manage_video_chats=True,
            can_manage_topics=True,
            can_post_stories=True,
            can_edit_stories=True,
            can_delete_stories=True
        )
        bot.reply_to(message, f"🔱 Full promoted [{user.first_name}](tg://user?id={user.id})", parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ Could not find the user to full promote.")

# /demote
@bot.message_handler(commands=['demote'])
def demote(message):
    user = get_target_user(message)
    if user:
        bot.promote_chat_member(
            message.chat.id,
            user.id,
            can_manage_chat=False,
            can_change_info=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_video_chats=False,
            can_manage_topics=False,
            can_post_stories=False,
            can_edit_stories=False,
            can_delete_stories=False
        )
        bot.reply_to(message, f"❌ Demoted [{user.first_name}](tg://user?id={user.id})", parse_mode="Markdown")
    else:
        bot.reply_to(message, "❌ Could not find the user to demote.")

# Helper function to identify user
def get_target_user(message):
    if message.reply_to_message:
        return message.reply_to_message.from_user
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        identifier = args[1].strip()
        try:
            if identifier.startswith("@"):
                user = bot.get_chat(identifier)
            else:
                user = bot.get_chat(int(identifier))
            return user
        except:
            return None
    return None

# Run the bot
bot.infinity_polling()