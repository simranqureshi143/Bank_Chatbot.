from flask import Flask, render_template, request
from chatbot import BankingChatbot

app = Flask(__name__)
bot = BankingChatbot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return bot.get_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)
