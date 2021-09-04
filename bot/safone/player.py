import os
import time
import ffmpeg
import asyncio
from asyncio import sleep
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pytgcalls import GroupCallFactory
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ADMINS = Config.ADMINS
CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME

STREAM = {6}
VIDEO_CALL = {}

# PyTgCalls Client
group_call_factory = GroupCallFactory(GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)

@Client.on_message(filters.command(["stream", f"stream@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def stream(client, m: Message):
    if 1 in STREAM:
        await m.reply_text("🤖 **Please Stop The Existing Stream!**")
        return
    media = m.reply_to_message
    if not media:
        await m.reply_text("❗ **Reply To An Video To Stream!**")
        return
    elif media.video or media.document:
        msg = await m.reply_text("🔄 **Downloading, Please Wait...**")
        if os.path.exists(f'stream-{CHAT_ID}.raw'):
            os.remove(f'stream-{CHAT_ID}.raw')
        try:
            video = await client.download_media(media)
            await msg.edit("🔄 **Transcoding, Please Wait...**")
            os.system(f'ffmpeg -i "{video}" -vn -f s16le -ac 2 -ar 48000 -acodec pcm_s16le -filter:a "atempo=0.81" stream-{CHAT_ID}.raw -y')
        except Exception as e:
            await msg.edit(f"❌ **An Error Occoured!** \n`{e}`")
            pass
        await sleep(5)
        group_call = group_call_factory.get_file_group_call(f'stream-{CHAT_ID}.raw')
        try:
            await group_call.start(CHAT_ID)
            await group_call.set_video_capture(video)
            VIDEO_CALL[CHAT_ID] = group_call
            await msg.edit("▶️ **Started Streaming!**")
            try:
                STREAM.remove(0)
            except:
                pass
            try:
                STREAM.add(1)
            except:
                pass
        except FloodWait as e:
            await sleep(e.x)
            if not group_call.is_connected:
                await group_call.start(CHAT_ID)
                await group_call.set_video_capture(video)
                VIDEO_CALL[CHAT_ID] = group_call
                await msg.edit("▶️ **Started Streaming!**")
                try:
                    STREAM.remove(0)
                except:
                    pass
                try:
                    STREAM.add(1)
                except:
                    pass
        except Exception as e:
            await msg.edit(f"❌ **An Error Occoured!** \n`{e}`")
            return
    else:
        await m.reply_text("❗ **Reply To An Video To Stream!**")
        return


@Client.on_message(filters.command(["mute", f"mute@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def mute(_, m: Message):
    if 0 in STREAM:
        await m.reply_text("🤖 **Please Start The Stream First!**")
        return
    try:
        VIDEO_CALL[CHAT_ID].pause_playout()
        await m.reply_text("🔇 **Muted Streamer!**")
    except Exception as e:
        await m.reply_text(f"❌ **An Error Occoured!** \n`{e}`")
        return

@Client.on_message(filters.command(["unmute", f"unmute@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def unmute(_, m: Message):
    if 0 in STREAM:
        await m.reply_text("🤖 **Please Start The Stream First!**")
        return
    try:
        VIDEO_CALL[CHAT_ID].resume_playout()
        await m.reply_text("🔉 **Unmuted Streamer!**")
    except Exception as e:
        await m.reply_text(f"❌ **An Error Occoured!** \n`{e}`")
        return

@Client.on_message(filters.command(["endstream", f"endstream@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def endstream(client, m: Message):
    if 0 in STREAM:
        await m.reply_text("🤖 **Please Start The Stream First!**")
        return
    try:
        await VIDEO_CALL[CHAT_ID].stop()
        await m.reply_text("⏹️ **Stopped Streaming!**")
        try:
            STREAM.remove(1)
        except:
            pass
        try:
            STREAM.add(0)
        except:
            pass
    except Exception as e:
        await m.reply_text(f"❌ **An Error Occoured!** \n`{e}`")
        return


admincmds=["stream", "pause", "resume", "endstream", f"stream@{USERNAME}", f"pause@{USERNAME}", f"resume@{USERNAME}", f"endstream@{USERNAME}"]

@Client.on_message(filters.command(admincmds) & ~filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def notforu(_, m: Message):
    k = await m.reply_sticker("CAACAgUAAxkBAAEBpyZhF4R-ZbS5HUrOxI_MSQ10hQt65QACcAMAApOsoVSPUT5eqj5H0h4E")
    await sleep(5)
    await k.delete()
    try:
        await m.delete()
    except:
        pass

allcmd = ["start", "help", f"start@{USERNAME}", f"help@{USERNAME}"] + admincmds

@Client.on_message(filters.command(allcmd) & filters.group & ~filters.chat(CHAT_ID))
async def not_chat(_, m: Message):
    buttons = [
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/SLBotsOfficial"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/trtechguide"),
            ],
            [
                InlineKeyboardButton("Create Your Own Bot", url="https://github.com/TR-TECH-GUIDE/VideoPlayerBot"),
            ]
         ]
    await m.reply_text(text="**Sorry, You Can't Use This Bot In This Group! 🤷‍♂ but you can stream using your own bot, click on create your own to create bot.**", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

