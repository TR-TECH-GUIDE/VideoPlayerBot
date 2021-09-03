import asyncio
from pyrogram.handlers import InlineQueryHandler
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, errors
from config import Config

USERNAME = Config.BOT_USERNAME
REPLY_MESSAGE = Config.REPLY_MESSAGE

buttons = [
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/SLBotsOfficial"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/trtechguide"),
            ]
         ]

@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "SLBotsOfficial":
        answers.append(
            InlineQueryResultArticle(
                title="Video Player Bot",
                input_message_content=InputTextMessageContent(f"{REPLY_MESSAGE}\n\n<b>© Powered By : \n@SLBotsOfficial</b>", disable_web_page_preview=True),
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)
        return

__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]