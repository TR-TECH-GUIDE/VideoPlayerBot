# Telegram Video Player Bot
![GitHub Repo stars](https://img.shields.io/github/stars/TR-TECH-GUIDE/VideoPlayerBot?color=blue&style=flat)
![GitHub forks](https://img.shields.io/github/forks/TR-TECH-GUIDE/VideoPlayerBot?color=green&style=flat)
![GitHub issues](https://img.shields.io/github/issues/TR-TECH-GUIDE/VideoPlayerBot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/TR-TECH-GUIDE/VideoPlayerBot)
![GitHub pull requests](https://img.shields.io/github/issues-pr/TR-TECH-GUIDE/VideoPlayerBot)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/TR-TECH-GUIDE/VideoPlayerBot)
![GitHub contributors](https://img.shields.io/github/contributors/TR-TECH-GUIDE/VideoPlayerBot?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/TR-TECH-GUIDE/VideoPlayerBot?color=red)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/TR-TECH-GUIDE/VideoPlayerBot)
![GitHub](https://img.shields.io/github/license/TR-TECH-GUIDE/VideoPlayerBot)
[![Bot Updates](https://img.shields.io/badge/VideoPlayerBot-Updates%20Channel-green)](https://t.me/SLBotsOfficial)
[![Bot Support](https://img.shields.io/badge/VideoPlayerBot-Support%20Group-blue)](https://t.me/trtechguide)

An Telegram Bot By [@TharukRenuja](https://t.me/TharukRenuja) To Stream Videos in Telegram Voice Chat.

## Main Features

- Supports Live Streaming.
- Supports YouTube Streaming.
- Supports Live Radio Streaming.
- Supports Video Files Streaming.
- Supports YouTube Live Streaming.
- User Account Protection (PM Guard)

## Deploy Own Bot

### Railway (Recommended)
<p><a href="https://railway.app/new/template?template=https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FTR-TECH-GUIDE%2FVideoPlayerBot&envs=API_ID%2CAPI_HASH%2CBOT_TOKEN%2CSESSION_STRING%2CCHAT_ID%2CAUTH_USERS%2CREPLY_MESSAGE&optionalEnvs=REPLY_MESSAGE&API_IDDesc=User+Account+Telegram+API_ID+get+it+from+my.telegram.org%2Fapps&API_HASHDesc=User+Account+Telegram+API_HASH+get+it+from+my.telegram.org%2Fapps&BOT_TOKENDesc=Your+Telegram+Bot+Token%2C+get+it+from+%40Botfather+XD&SESSION_STRINGDesc=Pyrogram+Session+String+of+User+Account%2C+get+it+from+%40genStr_robot&CHAT_IDDesc=ID+of+your+Channel+or+Group+where+the+bot+will+works+or+stream+videos&AUTH_USERSDesc=ID+of+Auth+Users+who+can+use+Admin+commands+%28for+multiple+users+seperated+by+space%29&REPLY_MESSAGEDesc=A+reply+message+to+those+who+message+the+USER+account+in+PM.+Make+it+blank+if+you+do+not+need+this+feature.&REPLY_MESSAGEDefault=Hello+Sir%2C+I%27m+a+bot+to+stream+videos+on+telegram+voice+chat%2C+not+having+time+to+chat+with+you+%F0%9F%98%82%21&referralCode=SAFONE"><img src="https://img.shields.io/badge/Deploy%20To%20Railway-blueviolet?style=for-the-badge&logo=railway" width="200""/></a></p>

### Heroku (Don't Complain)
<p><a href="https://heroku.com/deploy?template=https://github.com/TR-TECH-GUIDE/VideoPlayerBot"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>

## Commands (Botfather)
```sh
start - Start The Bot
help - Show Help Message
play - Start Audio Playback
stream - Start Video Streaming
pause - Pause The Current Stream
resume - Resume The Paused Stream
endstream - Stop Streaming & Left VC
```

## Config Vars
1. `API_ID` : User Account Telegram API_ID, get it from my.telegram.org
2. `API_HASH` : User Account Telegram API_HASH, get it from my.telegram.org
3. `BOT_TOKEN` : Your Telegram Bot Token, get it from @Botfather
4. `SESSION_STRING` : Pyrogram Session String of User Account, get it from [@StringSessiongenslbot](http://t.me/StringSessiongenslbot)
5. `CHAT_ID` : ID of Channel/Group where the bot will works or stream videos (for multiple chats seperated by space).
6. `AUTH_USERS` : ID of Users who can use Admins commands (for multiple users seperated by space).
7. `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature.

## Requirements
- Python 3.6 or Higher.
- Latest [FFmpeg Python](https://www.ffmpeg.org/).
- [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api).
- Pyrogram [String Session](http://t.me/StringSessiongenslbot) Of The Account.
- The User Account Needs To Be An Admin In The Group / Channel.

## Self Host
```sh
$ git clone https://github.com/TR-TECH-GUIDE/VideoPlayerBot.git
$ cd VideoPlayerBot
$ sudo apt-get install python3-pip ffmpeg
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
# <create .env variables appropriately>
$ python3 -m bot
```


## License
```sh
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
```

## Credits

- [Me](https://github.com/TR-TECH-GUIDE) for [Created All Repo](https://github.com/TR-TECH-GUIDE/VideoPlayerBot) 😬
- [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram) ❤️
- And Thanks To All [Contributors](https://github.com/TR-TECH-GUIDE/VideoPlayerBot/graphs/contributors)! ❤️
