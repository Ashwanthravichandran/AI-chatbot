from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response
from document_processor import process_document
from badwords import contains_bad_words
import os

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

chat_history = []
uploaded_text = ""

@app.route("/")
def home():
    return render_template("chatbot.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data["message"]

    if contains_bad_words(user_message):
        return jsonify({"response": "⚠ Please use respectful language."})

    bot_response = get_bot_response(user_message, uploaded_text)

    chat_history.append({
        "user": user_message,
        "bot": bot_response
    })

    return jsonify({"response": bot_response})


@app.route("/clear", methods=["POST"])
def clear_chat():

    global chat_history
    chat_history = []

    return jsonify({"status": "cleared"})


@app.route("/upload", methods=["POST"])
def upload_file():

    global uploaded_text

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    summary, keywords = process_document(file)

    uploaded_text = summary

    return jsonify({
        "summary": summary,
        "keywords": keywords
    })


if __name__ == "__main__":
    print("Server running → http://127.0.0.1:5000")
    app.run(debug=True)