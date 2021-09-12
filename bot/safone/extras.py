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
import asyncio
from config import Config
from pyrogram import Client

bot = Client(
    "VideoPlayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)
bot.start()
ok = bot.get_me()
USERNAME = ok.username
