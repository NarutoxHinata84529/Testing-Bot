import telebot
from telebot import types
import time
import random
import logging
from datetime import datetime
from telebot.types import ChatMember, ChatPermissions

API_TOKEN = '5594382721:AAGGNx_42Xhd1rfyDh3t_YhYOaXD2mdirsA'

bot = telebot.TeleBot(API_TOKEN)
warnings = {}
warn_limit = 3
warn_mode = 'mute'
afk_users = {}
brb_users = {}

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why was the math book sad? It had too many problems.",
    "Why don't some couples go to the gym? Because some relationships don't work out.",
    "I would avoid the sushi if I was you. It’s a little fishy.",
    "Want to hear a joke about construction? I'm still working on it.",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call cheese that isn't yours? Nacho cheese."
]

insults = [
    "You're as bright as a black hole and twice as dense.",
    "I'd agree with you but then we'd both be wrong.",
    "I see you've set aside this special time to humiliate yourself in public.",
    "Your secrets are always safe with me. I never even listen when you tell me them.",
    "You bring everyone so much joy when you leave the room.",
    "I thought of you today. It reminded me to take out the trash.",
    "You're not stupid; you just have bad luck thinking.",
    "You're like a software update. Whenever I see you, I think, 'Not now.'",
    "I'd explain it to you but I left my crayons at home.",
    "Your family tree must be a cactus because everybody on it is a prick.",
    "Haan, you're like my telegram notification, better muted",
    "You know there's a very thin line in being smart and attractive? Can't blame you though.",
    "You know what the doctors told your parents after you were born? April fools! Although it wasn't even April to begin with.",
    "You know, god never makes anyone ugly, and you're the most paradoxical proof to that.",
    "When Will Smith slapped Chris, he thought it was your mama's bum cheeks."
]

def is_admin(user_id, chat_id):
    admins = bot.get_chat_administrators(chat_id)
    for admin in admins:
        if admin.user.id == user_id:
            return True
    return False

def admin_only(func):
    def wrapper(message, *args, **kwargs):
        if is_admin(message.from_user.id, message.chat.id):
            return func(message, *args, **kwargs)
        else:
            bot.reply_to(message, "You don't have permission to use this command.")
    return wrapper

#SETTING NEW WELCOME MESSAGE
# Define the /start command to send a simple welcome message

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = (
        "🎉✨ Welcome to @NarutoxHinata_Bot! ✨🎉\n\n"
        "👋 Hello, {}! We're excited to have you join.\n"
        "Use `/help` to get a list of commands and features available."
    ).format(message.from_user.first_name)  # Adding user's first name dynamically

    bot.reply_to(message, welcome_message)

'''@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Here are the commands you can use:\n"
        "/start - Welcome message\n"
        "/help - List of commands\n"
        "/ban - Ban a user\n"
        "/unban - Unban a user\n"
        "/kick - Kick a user\n"
        "/mute - Mute a user\n"
        "/unmute - Unmute a user\n"
        "/tmute - Temporarily mute a user\n"
        "/adminlist - Show the admins in the group\n"
        "/warn - Warn a user\n"
        "/unwarn - Remove a warning from a user\n"
        "/warns - Check a user's warnings\n"
        "/warnmode - Set the mode for warn limit\n"
        "/warnlimit - Set the number of warnings before action is taken\n"
        "/joke - Tell a joke\n"
        "/kang - Steal a sticker or gif\n"
        "/afk - Mark yourself as away\n"
        "/brb - Mark yourself as away with a reason\n"
        "/insult - Insult the replied user\n"
        "/promote <reply/username/mention/userid> - Promotes a member to admin\n"
        "/fullpromote <reply/username/mention/userid> - Promotes a member to admin with full rights\n"
        "/demote <reply/username/mention/userid> - Demotes an admin to member\n"
        "/lock all - Lock all chats in the group\n"
        "/unlock all - Unlock all chats in the group"
    )
    bot.reply_to(message, help_text)'''

#adding New HELP CMD

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "💬 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗬𝗼𝘂 𝗖𝗮𝗻 𝗨𝘀𝗲 💬\n\n"

        "🚀 /start - 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 \n"
        "ℹ️ /help - 𝗟𝗶𝘀𝘁 𝗼𝗳 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀  \n"
        "⛔ /ban - 𝗕𝗮𝗻 𝗮 𝘂𝘀𝗲𝗿 \n"
        "✅ /unban - 𝗨𝗻𝗯𝗮𝗻 𝗮 𝘂𝘀𝗲𝗿\n"
        "👢 /kick - 𝗞𝗶𝗰𝗸 𝗮 𝘂𝘀𝗲𝗿 \n"
        "🔇 /mute - 𝗠𝘂𝘁𝗲 𝗮 𝘂𝘀𝗲𝗿  \n"
        "🔊 /unmute - 𝗨𝗻𝗺𝘂𝘁𝗲 𝗮 𝘂𝘀𝗲𝗿  \n"
        "⏳ /tmute - 𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝗶𝗹𝘆 𝗺𝘂𝘁𝗲 𝗮 𝘂𝘀𝗲𝗿  \n"
        "👥 /adminlist - 𝗦𝗵𝗼𝘄 𝘁𝗵𝗲 𝗮𝗱𝗺𝗶𝗻𝘀 𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽 \n\n"

        "⚠️ 𝗪𝗮𝗿𝗻𝗶𝗻𝗴𝘀 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 ⚠️ \n\n"
        "📛 /warn - 𝗪𝗮𝗿𝗻 𝗮 𝘂𝘀𝗲𝗿  \n"
        "🛑 /unwarn - 𝗥𝗲𝗺𝗼𝘃𝗲 𝗮 𝘄𝗮𝗿𝗻𝗶𝗻𝗴 𝗳𝗿𝗼𝗺 𝗮 𝘂𝘀𝗲𝗿\n"
        "🚨 /warns - 𝗖𝗵𝗲𝗰𝗸 𝗮 𝘂𝘀𝗲𝗿'𝘀 𝘄𝗮𝗿𝗻𝗶𝗻𝗴𝘀  \n"
        "🔒 /warnmode - 𝗦𝗲𝘁 𝘁𝗵𝗲 𝗺𝗼𝗱𝗲 𝗳𝗼𝗿 𝘄𝗮𝗿𝗻 𝗹𝗶𝗺𝗶𝘁  \n"
        "📊 /warnlimit - 𝗦𝗲𝘁 𝘁𝗵𝗲 𝗻𝘂𝗺𝗯𝗲𝗿 𝗼𝗳 𝘄𝗮𝗿𝗻𝗶𝗻𝗴𝘀 𝗯𝗲𝗳𝗼𝗿𝗲 𝗮𝗰𝘁𝗶𝗼𝗻 𝗶𝘀 𝘁𝗮𝗸𝗲𝗻  \n\n"

        "🎭 𝗙𝘂𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 🎭  \n\n"
        "🤣 /joke - 𝗧𝗲𝗹𝗹 𝗮 𝗷𝗼𝗸𝗲  \n"
        "🦊 /kang - 𝗦𝘁𝗲𝗮𝗹 𝗮 𝘀𝘁𝗶𝗰𝗸𝗲𝗿 𝗼𝗿 𝗴𝗶𝗳  \n"
        "🛌 /afk - 𝗠𝗮𝗿𝗸 𝘆𝗼𝘂𝗿𝘀𝗲𝗹𝗳 𝗮𝘀 𝗮𝘄𝗮𝘆  \n"
        "🔙 /brb - 𝗠𝗮𝗿𝗸 𝘆𝗼𝘂𝗿𝘀𝗲𝗹𝗳 𝗮𝘀 𝗮𝘄𝗮𝘆 𝘄𝗶𝘁𝗵 𝗮 𝗿𝗲𝗮𝘀𝗼𝗻\n"
        "💥 /insult - 𝗜𝗻𝘀𝘂𝗹𝘁 𝘁𝗵𝗲 𝗿𝗲𝗽𝗹𝗶𝗲𝗱 𝘂𝘀𝗲𝗿 \n \n"

        "📈 𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 📈\n\n"
        "⏫ /promote <reply/username/mention/userid> - 𝗣𝗿𝗼𝗺𝗼𝘁𝗲 𝗮 𝗺𝗲𝗺𝗯𝗲𝗿 𝘁𝗼 𝗮𝗱𝗺𝗶𝗻  \n"
        "🔱 /fullpromote <reply/use\nrname/mention/userid> - 𝗣𝗿𝗼𝗺𝗼𝘁𝗲 𝗮 𝗺𝗲𝗺𝗯𝗲𝗿 𝘁𝗼 𝗮𝗱𝗺𝗶𝗻 𝘄𝗶𝘁𝗵 𝗳𝘂𝗹𝗹 𝗿𝗶𝗴𝗵𝘁𝘀  \n"
        "⬇️ /demote <reply/username/mention/userid> - 𝗗𝗲𝗺𝗼𝘁𝗲 𝗮𝗻 𝗮𝗱𝗺𝗶𝗻 𝘁𝗼 𝗮 𝗺𝗲𝗺𝗯𝗲𝗿  \n\n"

        "🔐 𝗟𝗼𝗰𝗸 & 𝗨𝗻𝗹𝗼𝗰𝗸 🔐  \n\n"
        "🔒 /lock all - 𝗟𝗼𝗰𝗸 𝗮𝗹𝗹 𝗰𝗵𝗮𝘁𝘀 𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽  \n"
        "🔓 /unlock all - 𝗨𝗻𝗹𝗼𝗰𝗸 𝗮𝗹𝗹 𝗰𝗵𝗮𝘁𝘀 𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽\n"
   )
    bot.reply_to(message, help_text)


def get_user_from_message(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Please reply to the user's message to use this command.")
        return None
    return message.reply_to_message.from_user

def get_user_from_args(message):
    args = message.text.split()[1:]
    if not args and not message.reply_to_message:
        bot.reply_to(message, "Please reply to a user's message or specify a user by username/ID.")
        return None

    if message.reply_to_message:
        return message.reply_to_message.from_user
    else:
        try:
            user_id = int(args[0])
            return bot.get_chat_member(message.chat.id, user_id).user
        except (ValueError, IndexError, telebot.apihelper.ApiException):
            bot.reply_to(message, "Invalid username/ID.")
            return None

@bot.message_handler(commands=['ban'])
@admin_only
def ban_user(message):
    user = get_user_from_message(message)
    if user:
        bot.kick_chat_member(message.chat.id, user.id)
        bot.reply_to(message, f"User {user.first_name} has been banned.")

@bot.message_handler(commands=['unban'])
@admin_only
def unban_user(message):
    user = get_user_from_args(message)
    if user:
        try:
            bot.unban_chat_member(message.chat.id, user.id)
            bot.reply_to(message, f"User {user.first_name} has been unbanned.")
        except telebot.apihelper.ApiException as e:
            bot.reply_to(message, f"Failed to unban user {user.first_name}. Reason: {e}")

'''@bot.message_handler(commands=['promote'])
@admin_only
def promote(message):
    user = get_user_from_args(message)
    if user:
        try:
            bot.promote_chat_member(
                message.chat.id, user.id,
                can_change_info=True, can_delete_messages=True, can_invite_users=True,
                can_restrict_members=True, can_pin_messages=True, can_post_stories=True, can_edit_stories=True,
                can_delete_stories=True, can_manage_voice_chats=True
            )
            bot.reply_to(message, f"𝚙𝚛𝚘𝚖𝚘𝚝𝚎𝚍 {user.first_name} 𝚝𝚘 𝚊𝚍𝚖𝚒𝚗!")
        except telebot.apihelper.ApiTelegramException as e:
            if 'user is an administrator of the chat' in str(e):
                bot.reply_to(message, f"User {user.first_name} is already an admin.")
            else:
                bot.reply_to(message, f"Failed to promote user {user.first_name}. Reason: {e}")
'
@bot.message_handler(commands=['fullpromote'])
@admin_only
def fullpromote(message):
    user = get_user_from_args(message)
    if user:
        try:
            bot.promote_chat_member(
                message.chat.id, user.id,
                can_change_info=True, can_post_messages=True, can_edit_messages=True,
                can_delete_messages=True, can_invite_users=True, can_restrict_members=True,
                can_pin_messages=True, can_promote_members=True, can_manage_voice_chats=True,
                can_manage_video_chats=True, can_post_stories=True, can_edit_stories=True,
                can_delete_stories=True
            )
            bot.reply_to(message, f"Promoted {user.first_name} to admin with full rights!")
        except telebot.apihelper.ApiTelegramException as e:
            if 'user is an administrator of the chat' in str(e):
                bot.reply_to(message, f"User {user.first_name} is already an admin.")
            else:
                bot.reply_to(message, f"Failed to promote user {user.first_name}. Reason: {e}")


#new admin command with no rights

@bot.message_handler(commands=['respromote'])
@admin_only
def respromote(message):
    user = get_user_from_args(message)
    if user:
        bot.promote_chat_member(
            message.chat.id, user.id,
            can_change_info=False, can_post_messages=False, can_edit_messages=False,
            can_delete_messages=False, can_invite_users=False, can_restrict_members=False,
            can_pin_messages=True, can_promote_members=False, can_manage_voice_chats=False,
            can_manage_video_chats=False, can_post_stories=False, can_edit_stories=False,
            can_delete_stories=False
        )
        bot.reply_to(message, f"Respromoted {user.first_name} to member.")
'''

#New admins code

@bot.message_handler(commands=['promote', 'fullpromote', 'respromote'])
def promote_user(message):
    chat_id = message.chat.id
    from_user = message.from_user
    replied_msg = message.reply_to_message

    # Fetch chat admin details
    chat_admins = bot.get_chat_administrators(chat_id)

    # Check if the command sender is an admin and has the permission to promote
    sender_is_admin = False
    sender_can_promote = False

    for admin in chat_admins:
        if admin.user.id == from_user.id:
            sender_is_admin = True
            sender_can_promote = admin.can_promote_members
            break

    if not sender_is_admin:
        bot.reply_to(message, "❌ You must be an admin to use this command!")
        return

    if not sender_can_promote:
        bot.reply_to(message, "❌ You don't have the required permission to promote users!")
        return

    # Ensure the command is used as a reply to a message
    if not replied_msg:
        bot.reply_to(message, "⚠️ Reply to the user you want to promote!")
        return

    user_to_promote = replied_msg.from_user.id

    # Define permissions for each command
    if message.text.startswith("/promote"):
        bot.promote_chat_member(chat_id, user_to_promote, can_change_info=True, can_delete_messages=True,
                                can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_delete_stories=True,
                                can_post_stoties=True,can_edit_stories=True)
        bot.reply_to(message, f"✅ User [{replied_msg.from_user.first_name}](tg://user?id={user_to_promote}) has been promoted!")

    elif message.text.startswith("/fullpromote"):
        bot.promote_chat_member(chat_id, user_to_promote, can_change_info=True, can_delete_messages=True,
                                can_invite_users=True, can_restrict_members=True, can_pin_messages=True,
                                can_promote_members=True,can_delete_stories=True,
                                can_post_stoties=True,can_edit_stories=True)
        bot.reply_to(message, f"✅ User [{replied_msg.from_user.first_name}](tg://user?id={user_to_promote}) has been fully promoted!")

    elif message.text.startswith("/respromote"):
        bot.promote_chat_member(chat_id, user_to_promote, can_change_info=False, can_delete_messages=False,
                                can_invite_users=False, can_restrict_members=False, can_pin_messages=True,
                                can_promote_members=False, can_delete_stories=False,
                                can_post_stoties=False, can_edit_stories=False)
        bot.reply_to(message, f"✅ User [{replied_msg.from_user.first_name}](tg://user?id={user_to_promote}) has been re-promoted!")


@bot.message_handler(commands=['checkadmin'])
def check_admin_status(message):
    chat_id = message.chat.id
    from_user = message.from_user

    sender_info = bot.get_chat_member(chat_id, from_user.id)

    admin_status = f"""
👤 **Your Admin Info:**
🔹 Status: `{sender_info.status}`
🔹 Can Promote Members: `{sender_info.can_promote_members}`
🔹 Can Change Info: `{sender_info.can_change_info}`
🔹 Can Delete Messages: `{sender_info.can_delete_messages}`
🔹 Can Invite Users: `{sender_info.can_invite_users}`
🔹 Can Restrict Members: `{sender_info.can_restrict_members}`
🔹 Can Pin Messages: `{sender_info.can_pin_messages}`
🔹 Can add admins: `{sender_info.can_add_admins}'
"""
    bot.reply_to(message, admin_status, parse_mode="Markdown")



@bot.message_handler(commands=['demote'])
@admin_only
def demote(message):
    user = get_user_from_args(message)
    if user:
        bot.promote_chat_member(
            message.chat.id, user.id,
            can_change_info=False, can_post_messages=False, can_edit_messages=False,
            can_delete_messages=False, can_invite_users=False, can_restrict_members=False,
            can_pin_messages=False, can_promote_members=False, can_manage_voice_chats=False,
            can_manage_video_chats=False, can_post_stories=False, can_edit_stories=False,
            can_delete_stories=False
        )
        bot.reply_to(message, f"Demoted {user.first_name} to member.")
#new joke and insult cmd


# Command to send a joke
'''@bot.message_handler(commands=['joke'])
def send_joke(message):
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
        joke = random.choice(jokes)
        bot.send_message(
            message.chat.id,
            f"{target_user.first_name},\n{joke}",
            reply_to_message_id=message.reply_to_message.message_id  # Reply to the original message
        )
    else:
        bot.send_message(
            message.chat.id,
            "Reply to someone with /joke to send them a funny joke!"
        )'''

# Command to send an insult
@bot.message_handler(commands=['insult'])
def send_insult(message):
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
        insult = random.choice(insults)
        bot.send_message(
            message.chat.id,
            f"{target_user.first_name}, {insult}",
            reply_to_message_id=message.reply_to_message.message_id  # Reply to the original message
        )
    else:
        bot.send_message(
            message.chat.id,
            "Reply to someone with /insult to give them a witty burn!"
        )
'''@bot.message_handler(commands=['insult'])
def insult(message):
    insult_text = random.choice(insults)
    bot.reply_to(message, insult_text)'''

@bot.message_handler(commands=['afk'])
def afk(message):
    user_id = message.from_user.id
    reason = message.text.split(' ', 1)[1] if len(message.text.split(' ')) > 1 else 'AFK'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    afk_users[user_id] = (reason, timestamp)
    bot.reply_to(message, f"{message.from_user.first_name} is now AFK: {reason} (since {timestamp})")

@bot.message_handler(commands=['brb'])
def brb(message):
    user_id = message.from_user.id
    reason = message.text.split(' ', 1)[1] if len(message.text.split(' ')) > 1 else 'BRB'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    brb_users[user_id] = (reason, timestamp)
    bot.reply_to(message, f"{message.from_user.first_name} will be right back: {reason} (since {timestamp})")

@bot.message_handler(commands=['joke'])
def joke(message):
    joke_text = random.choice(jokes)
    bot.reply_to(message, joke_text)

@bot.message_handler(commands=['warn'])
@admin_only
def warn_user(message):
    user = get_user_from_message(message)
    if user:
        user_id = user.id
        if user_id not in warnings:
            warnings[user_id] = 0
        warnings[user_id] += 1
        bot.reply_to(message, f"User {user.first_name} has been warned. Warning count: {warnings[user_id]}")
        if warnings[user_id] >= warn_limit:
            if warn_mode == 'ban':
                bot.kick_chat_member(message.chat.id, user_id)
                bot.reply_to(message, f"User {user.first_name} has been banned due to exceeding the warning limit.")
            elif warn_mode == 'mute':
                until_date = time.time() + 3600  # 1 hour mute
                bot.restrict_chat_member(message.chat.id, user_id, until_date=until_date, can_send_messages=False)
                bot.reply_to(message, f"User {user.first_name} has been muted for 1 hour due to exceeding the warning limit.")
            warnings[user_id] = 0  # Reset warnings after action

@bot.message_handler(commands=['unwarn'])
@admin_only
def unwarn_user(message):
    user = get_user_from_message(message)
    if user:
        user_id = user.id
        if user_id in warnings:
            warnings[user_id] = max(0, warnings[user_id] - 1)
            bot.reply_to(message, f"User {user.first_name}'s warning has been removed. Warning count: {warnings[user_id]}")
        else:
            bot.reply_to(message, f"User {user.first_name} has no warnings.")

@bot.message_handler(commands=['warns'])
def check_warns(message):
    user = get_user_from_message(message)
    if user:
        user_id = user.id
        count = warnings.get(user_id, 0)
        bot.reply_to(message, f"User {user.first_name} has {count} warnings.")

@bot.message_handler(commands=['warnmode'])
@admin_only
def set_warnmode(message):
    global warn_mode
    mode = message.text.split()[1].lower()
    if mode in ['ban', 'mute']:
        warn_mode = mode
        bot.reply_to(message, f"Warning mode set to {warn_mode}.")
    else:
        bot.reply_to(message, "Invalid mode. Use 'ban' or 'mute'.")

@bot.message_handler(commands=['warnlimit'])
@admin_only
def set_warnlimit(message):
    global warn_limit
    limit = message.text.split()[1]
    try:
        warn_limit = int(limit)
        bot.reply_to(message, f"Warning limit set to {warn_limit}.")
    except ValueError:
        bot.reply_to(message, "Invalid limit. Please enter a number.")

@bot.message_handler(commands=['lock'])
@admin_only
def lock_all(message):
    bot.set_chat_permissions(
        message.chat.id,
        types.ChatPermissions(can_send_messages=False)
    )
    bot.reply_to(message, "All chats have been locked.")

@bot.message_handler(commands=['unlock'])
@admin_only
def unlock_all(message):
    bot.set_chat_permissions(
        message.chat.id,
        types.ChatPermissions(can_send_messages=True)
    )
    bot.reply_to(message, "All chats have been unlocked.")


@bot.message_handler(func=lambda message: True)
def handle_afk_users(message):
    if message.from_user.id in afk_users:
        del afk_users[message.from_user.id]
        bot.reply_to(message, f"Welcome back, {message.from_user.first_name}! You are no longer AFK.")
    if message.reply_to_message and message.reply_to_message.from_user.id in afk_users:
        reason, timestamp = afk_users[message.reply_to_message.from_user.id]
        bot.reply_to(message, f"{message.reply_to_message.from_user.first_name} is AFK: {reason} (since {timestamp})")

@bot.message_handler(func=lambda message: True)
def handle_brb_users(message):
    if message.from_user.id in brb_users:
        del brb_users[message.from_user.id]
        bot.reply_to(message, f"Welcome back, {message.from_user.first_name}! You are no longer brb.")
    if message.reply_to_message and message.reply_to_message.from_user.id in afk_users:
        reason, timestamp = brb_users[message.reply_to_message.from_user.id]
        bot.reply_to(message, f"{message.reply_to_message.from_user.first_name} is Brb: {reason} (since {timestamp})")
#New cmd

@bot.message_handler(commands=['kick'])
@admin_only
def kick_command(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Reply to the user you want to kick.")
        return
    user_to_kick = message.reply_to_message.from_user
    bot.ban_chat_member(message.chat.id, user_to_kick.id)
    bot.unban_chat_member(message.chat.id, user_to_kick.id)
    bot.reply_to(message, f"Kicked {user_to_kick.first_name}.")

'''# /mute command
@bot.message_handler(commands=['mute'])
@admin_only
def mute_command(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Reply to the user you want to mute.")
        return
    user_to_mute = message.reply_to_message.from_user
    bot.restrict_chat_member(
        message.chat.id,
        user_to_mute.id,
        ChatPermissions(can_send_messages=False)
    )
    bot.reply_to(message, f"Muted {user_to_mute.first_name}.")

# /unmute command
@bot.message_handler(commands=['unmute'])
@admin_only
def unmute_command(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Reply to the user you want to unmute.")
        return
    user_to_unmute = message.reply_to_message.from_user
    bot.restrict_chat_member(
        message.chat.id,
        user_to_unmute.id,
        ChatPermissions(can_send_messages=True)
    )
    bot.reply_to(message, f"Unmuted {user_to_unmute.first_name}.")'''

#Demote from private chat
# Function to demote a user
def demote_user(group_chat_id, user_id):
    try:
        bot.promote_chat_member(
            chat_id=group_chat_id,
            user_id=user_id,
            can_manage_chat=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_promote_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
        )
        return True
    except telebot.apihelper.ApiTelegramException as e:
        logging.error(f"Failed to demote user: {e}")
        return False

#Handler for the /demote command in private chat
@bot.message_handler(commands=["demote"])
def handle_demote(message):
    try:
        # Parse the command: /demote <group_chat_id> <user_id>
        args = message.text.split()
        if len(args) != 3:
            bot.reply_to(message, "Usage: /demote <group_chat_id> <user_id>")
            return

        group_chat_id = int(args[1])
        user_id = int(args[2])

        if demote_user(group_chat_id, user_id):
            bot.reply_to(message, f"User {user_id} has been demoted in group {group_chat_id}.")
        else:
            bot.reply_to(message, "Failed to demote the user. Make sure the bot is an admin in the group.")
    except ValueError:
        bot.reply_to(message, "Invalid input. Use /demote <group_chat_id> <user_id>.")
    except Exception as e:
        logging.error(f"Error handling /demote command: {e}")
        bot.reply_to(message, "An unexpected error occurred.")

#Mute code not working
'''@bot.message_handler(commands=['mute'])
@admin_only
def mute_command(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Reply to the user you want to mute.")
        return
    user_to_mute = message.reply_to_message.from_user
    bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=user_to_mute.id,
        permissions={
            can_send_messages==False,
            can_send_media_messages==False,
            can_send_polls==False,
            can_send_other_messages==False,
            can_add_web_page_previews==False,
            can_change_info==False,
            can_invite_users==False,
            can_pin_messages==False,
        }
    )
    bot.reply_to(message, f"Muted {user_to_mute.first_name}.")

@bot.message_handler(commands=['unmute'])
@admin_only
def unmute_command(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Reply to the user you want to unmute.")
        return
    user_to_unmute = message.reply_to_message.from_user
    bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=user_to_unmute.id,
        permissions={
            can_send_messages==True,
            can_send_media_messages== True,
            can_send_polls==True,
            can_send_other_messages==True,
            can_add_web_page_previews==True,
            can_change_info==False,
            can_invite_users==True,
            can_pin_messages==False,
        }
    )
    bot.reply_to(message, f"Unmuted {user_to_unmute.first_name}.")

#New mute code
@bot.message_handler(commands=['mute'])
@admin_only
def mute_user(message):
    user = get_user_from_message(message)
    if user:
        until_date = time.time() + (24 * 60 * 60)
        bot.restrict_chat_member(message.chat.id, user.id, until_date=until_date, can_send_messages=False)
        bot.reply_to(message, f"User {user.first_name} has been muted for 24 hours.")

@bot.message_handler(commands=['unmute'])
@admin_only
def unmute_user(message):
    user = get_user_from_args(message)
    if user:
        bot.restrict_chat_member(message.chat.id, user.id, can_send_messages=True)
        bot.reply_to(message, f"User {user.first_name} has been unmuted.")
'''
@bot.message_handler(commands=['tmute'])
@admin_only
def tmute_user(message):
    user = get_user_from_message(message)
    if user:
        args = message.text.split()
        if len(args) > 1 and args[1].isdigit():
            duration = int(args[1]) * 60  # in minutes
            until_date = time.time() + duration
            bot.restrict_chat_member(message.chat.id, user.id, until_date=until_date, can_send_messages=False)
            bot.reply_to(message, f"User {user.first_name} has been muted for {args[1]} minutes.")


#MUTE & UNMUTE CODE
@bot.message_handler(commands=['mute'])
@admin_only
def mute_user(message):
    user = get_user_from_message(message)
    if user:
        user_id = user.id
        until_date = time.time() + 3600  # Mute for 1 hour
        bot.restrict_chat_member(message.chat.id, user_id, until_date=until_date, can_send_messages=False)
        muted_users[user_id] = until_date
        bot.reply_to(message, f"User {user.first_name} has been muted for 1 hour.")

@bot.message_handler(commands=['unmute'])
@admin_only
def unmute_user(message):
    user = get_user_from_args(message)
    if user:
        user_id = user.id
        bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=True)
        if user_id in muted_users:
             del muted_users[user_id]
        bot.reply_to(message, f"User {user.first_name} has been unmuted.")


# Polling to keep the bot running
def main():
    bot.infinity_polling()
print ( 'bot is working' )
if __name__ == "__main__":
    main()