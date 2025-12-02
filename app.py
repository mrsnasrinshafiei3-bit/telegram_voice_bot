from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id

    if update.message.voice:
        bot.send_message(chat_id, "Voice received!")
    else:
        bot.send_message(chat_id, "Send me a voice message.")

    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!"

if __name__ == "__main__":
    app.run()
