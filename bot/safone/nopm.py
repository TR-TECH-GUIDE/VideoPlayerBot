import asyncio
from pyrogram import Client, filters
from config import Config
from pyrogram.errors import BotInlineDisabled

ADMINS = Config.ADMINS
USERNAME = Config.BOT_USERNAME
REPLY_MESSAGE = Config.REPLY_MESSAGE

User = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH
)

@User.on_message(filters.private & filters.incoming & ~filters.bot & ~filters.service & ~filters.me & ~filters.edited)
async def nopm(client, message):
    if REPLY_MESSAGE is not None:
        try:
            inline = await client.get_inline_bot_results(USERNAME, "SLBotsOfficial")
            await client.send_inline_bot_result(
                message.chat.id,
                query_id=inline.query_id,
                result_id=inline.results[0].id,
                hide_via=True
            )
        except BotInlineDisabled:
            for admin in ADMINS:
                try:
                    await client.send_message(chat_id=admin, text=f"Hey 🙋‍♂️,\nInline Mode Isn't Enabled For @{USERNAME} Yet. A Nibba Is Spaming Me In PM, Enable Inline Mode For @{USERNAME} From @Botfather To Reply Him 😉!")
                except Exception as e:
                    print(e)
                    pass
        except Exception as e:
            print(e)
            pass
