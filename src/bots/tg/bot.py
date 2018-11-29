from aiotg import Bot, Chat

# This one looks strange, but it's copied from aiotg
# NOTE, we could vendor it...
MESSAGE_TYPES = [
    "location",
    "photo",
    "document",
    "audio",
    "voice",
    "sticker",
    "contact",
    "venue",
    "video",
    "game",
    "delete_chat_photo",
    "new_chat_photo",
    "delete_chat_photo",
    "new_chat_member",
    "left_chat_member",
    "new_chat_title",
    "group_chat_created",
    "successful_payment",
]

# Update types for
MESSAGE_UPDATES = [
    "message",
    "edited_message",
    "channel_post",
    "edited_channel_post",
    "successful_payment",
]


# COMMAND
def echo(chat: Chat, match):
    """Echoing user message back to him"""
    return chat.reply(match.group(1))


# HANDLER
def greeter(chat: Chat, message):
    return chat.reply("Hello where!")


def register(api_token: str) -> Bot:
    bot = Bot(api_token=api_token)

    # register commands
    bot.add_command(r"/echo (.+)", echo)
    # TODO: register handlers
    bot.handle("text")(greeter)
    # callbacks

    # default

    return bot
