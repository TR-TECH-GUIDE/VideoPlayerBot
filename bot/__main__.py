"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  TR-TECH-GUIDE <https://github.com/TR-TECH-GUIDE>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import sys
import asyncio
from config import Config
from bot.safone.nopm import User
from pyrogram import Client, idle

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
print("\n[INFO] - STARTED VIDEO PLAYER BOT, JOIN @trtechguide !")

idle()
Bot.stop()
User.stop()
print("\n[INFO] - STOPPED VIDEO PLAYER BOT, JOIN @trtechguide !")
