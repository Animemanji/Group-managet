from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatPermissions 
import os

# Default welcome message and rules
WELCOME_MESSAGE = "Welcome to the group!"
RULES_TEXT = (
    "Group Rules:\n"
    "1. Be respectful to others.\n"
    "2. No spamming.\n"
    "3. No inappropriate content.\n"
    "4. Follow the admin instructions."
)

# Command: /start
def start(update, context):
    update.message.reply_text(f"Welcome to the Group Manager Bot, {update.message.from_user.full_name}! Type /help to see what I can do.")
    

# Command: /help
def help_command(update, context):
    commands = (
        "/start - Welcome message\n"
        "/help - List of commands\n"
        "/ban - Ban a user (Reply to a user's message)\n"
        "/mute - Mute a user (Reply to a user's message)\n"
        "/unmute - Unmute a user (Reply to a user's message)\n"
        "/kick - Kick a user (Reply to a user's message)\n"
        "/info - Get info about a user (Reply to a user's message)\n"
        "/rules - Display group rules\n"
        "/warn - Warn a user (Reply to a user's message)\n"
        "/promote - Promote a user to admin (Reply to a user's message)\n"
        "/demote - Demote an admin to user (Reply to a user's message)\n"
        "/config - Customize welcome message and rules"
    )
    update.message.reply_text(commands)
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /ban
def ban(update, context):
    user_id = update.message.reply_to_message.from_user.id
    context.bot.kick_chat_member(update.message.chat_id, user_id)
    update.message.reply_text(f"User {update.message.reply_to_message.from_user.full_name} (Username: @{update.message.reply_to_message.from_user.username}, User ID: {user_id}) has been banned!")
    
# Command: /mute
def mute(update, context):
    user_id = update.message.reply_to_message.from_user.id
    permissions = ChatPermissions(can_send_messages=False)
    context.bot.restrict_chat_member(update.message.chat_id, user_id, permissions=permissions)
    update.message.reply_text(f"User {update.message.reply_to_message.from_user.full_name} (Username: @{update.message.reply_to_message.from_user.username}, User ID: {user_id}) has been muted!")
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /unmute
def unmute(update, context):
    user_id = update.message.reply_to_message.from_user.id
    permissions = ChatPermissions(can_send_messages=True)
    context.bot.restrict_chat_member(update.message.chat_id, user_id, permissions=permissions)
    update.message.reply_text(f"User {update.message.reply_to_message.from_user.full_name} (Username: @{update.message.reply_to_message.from_user.username}, User ID: {user_id}) has been unmuted!")
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /kick
def kick(update, context):
    user_id = update.message.reply_to_message.from_user.id
    context.bot.kick_chat_member(update.message.chat_id, user_id)
    update.message.reply_text(f"User {update.message.reply_to_message.from_user.full_name} (Username: @{update.message.reply_to_message.from_user.username}, User ID: {user_id}) has been kicked out!")
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /info
def user_info(update, context):
    user = update.message.reply_to_message.from_user
    info = (
        f"User Info:\n"
        f"Name: {user.full_name}\n"
        f"Username: @{user.username}\n"
        f"User ID: {user.id}\n"
    )
    update.message.reply_text(info)
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /rules
def rules(update, context):
    update.message.reply_text(RULES_TEXT)
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /warn
def warn(update, context):
    user = update.message.reply_to_message.from_user
    update.message.reply_text(f"User {user.full_name} (Username: @{user.username}, User ID: {user.id}) has been warned!")
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /promote
def promote(update, context):
    user_id = update.message.reply_to_message.from_user.id
    context.bot.promote_chat_member(
        update.message.chat_id, user_id,
        can_manage_chat=True, can_change_info=True,
        can_delete_messages=True, can_invite_users=True,
        can_restrict_members=True, can_pin_messages=True,
        can_promote_members=True
    )
    update.message.reply_text(f"User {update.message.reply_to_message.from_user.full_name} (Username: @{update.message.reply_to_message.from_user.username}, User ID: {user_id}) has been promoted to admin!")
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /demote
def demote(update, context):
    user_id = update.message.reply_to_message.from_user.id
    context.bot.promote_chat_member(
        update.message.chat_id, user_id,
        can_manage_chat=False, can_change_info=False,
        can_delete_messages=False, can_invite_users=False,
        can_restrict_members=False, can_pin_messages=False,
        can_promote_members=False
    )
    update.message.reply_text(f"User {update.message.reply_to_message.from_user.full_name} (Username: @{update.message.reply_to_message.from_user.username}, User ID: {user_id}) has been demoted from admin!")
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: Welcome message for new members
def welcome(update, context):
    for member in update.message.new_chat_members:
        update.message.reply_text(f"{WELCOME_MESSAGE}, {member.full_name}!")
        update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Command: /config
def config(update, context):
    global WELCOME_MESSAGE, RULES_TEXT
    args = context.args
    if len(args) < 2:
        update.message.reply_text("Usage: /config <welcome|rules> <new_message>")
        return

    setting, new_message = args[0], " ".join(args[1:])
    if setting == "welcome":
        WELCOME_MESSAGE = new_message
        update.message.reply_text(f"Welcome message updated to: {WELCOME_MESSAGE}")
    elif setting == "rules":
        RULES_TEXT = new_message
        update.message.reply_text(f"Rules updated to: {RULES_TEXT}")
    else:
        update.message.reply_text("Invalid setting. Use 'welcome' or 'rules'.")
    
    update.message.reply_text(f"Your username is @{update.message.from_user.username} and your User ID is {update.message.from_user.id}.")

# Main function to set up the bot
def main():
    updater = Updater("7435867642:AAFRnC9ppz9ZZPq4KBefFQVbdRXCfoXnyXg", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("ban", ban))
    dp.add_handler(CommandHandler("mute", mute))
    dp.add_handler(CommandHandler("unmute", unmute))
    dp.add_handler(CommandHandler("kick", kick))
    dp.add_handler(CommandHandler("info", user_info))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("warn", warn))
    dp.add_handler(CommandHandler("promote", promote))
    dp.add_handler(CommandHandler("demote", demote))
    dp.add_handler(CommandHandler("config", config))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
