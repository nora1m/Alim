from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import werkzeug

'''''
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init('5000', integrations=[FlaskIntegration()])
'''''
app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 500

# or, without the decorator
app.register_error_handler(500, handle_bad_request)


if __name__ == "__main__":
    app.run()