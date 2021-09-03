import os
import time
import ffmpeg
import asyncio
import requests
import youtube_dl
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME


@Client.on_message(filters.command(["video", f"video@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def video(_, message: Message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    k = await message.reply_text("🔍 **Searching, Please Wait...**")
    ydl_opts = {
        "format": "best[ext=mp4]",
        "geo-bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "downloads/%(id)s.%(ext)s",
        }
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count > 0:
                await time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = int(float(results[0]["duration"]))
            views = results[0]["views"]
            channel = results[0]["channel"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
        except Exception as e:
            print(e)
            await k.edit('❌ **Found Literary Noting! \nPlease Try Another Video or Use Correct Spelling.**')
            return
    except Exception as e:
        await k.edit(
            "❗ **Enter An Video Name!** \nFor Example: `/video Avengers`"
        )
        print(str(e))
        return
    await k.edit("📥 **Downloading, Please Wait...**")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            video_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        caption = f'🏷 <b>Video Name:</b> <code>{title}</code>\n🔅 <b>Video Channel:</b> <code>{channel}</code>\n👀 <b>Video Views:</b> <code>{views}</code>\n🎧 <b>Requested By:</b> {message.from_user.mention()} \n📤 <b>Uploaded By: <a href="https://t.me/SLBotsOfficial">🇧🇩 Ｓ１ ＢＯＴＳ</a></b>'
        buttons = InlineKeyboardMarkup([[InlineKeyboardButton("Watch On YouTube", url=f'{link}')]])
        await k.edit("📤 **Uploading, Please Wait...**")
        await message.reply_video(video_file, caption=caption, parse_mode='HTML', file_name=title, duration=duration, thumb=thumb_name, reply_markup=buttons, supports_streaming=True)
        await k.delete()
    except Exception as e:
        await k.edit(f'❌ **An Error Occured!** \n`{e}`')
        pass
    try:
        os.remove(video_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        pass
