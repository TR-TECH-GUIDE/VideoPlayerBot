echo "[INFO] - FETCHING UPSTREAM REPO ..."
git clone https://github.com/TR-TECH-GUIDE/VideoPlayerBot.git /VideoPlayerBot
cd /VideoPlayerBot
echo "[INFO] - INSTALLING REQUIREMENTS ..."
pip3 install -U -r requirements.txt
echo "[INFO] - STARTED VIDEO PLAYER BOT ..."
python3 -m bot
