import os
import sys
import asyncio
from pyrogram import Client, idle
from config import Config
from pyrogram.raw import functions, types

Bot = Client(
    ":memory:",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="bot.safone"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")

Bot.start()
print("\nVideo Player Bot Started, Join @SLBotsOfficial!")

idle()
Bot.stop()
print("\nVideo Player Bot Stopped, Join @SLBotsOfficial!")
