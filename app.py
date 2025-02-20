from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
MY_RAPID_API_KEY = os.getenv("MY_RAPID_API_KEY")
app = Flask(__name__)

# Function to get response from OpenAI API via RapidAPI
def get_oracle_answer(question):

    url = "https://free-chatgpt-api.p.rapidapi.com/chat-completion-one"

    querystring = {"prompt": question}

    headers = {
        "x-rapidapi-key": MY_RAPID_API_KEY,
        "x-rapidapi-host": "free-chatgpt-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        try:
            answer = response.json().get("response")  # Extracting expected field
            return answer
        except:
            return "I am not in a mood to answer right now!"
    else:
        return "ohh! it such a hard question!"


@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    question = None
    if request.method == "POST":
        question = request.form.get("question")
        #print(question)
        if question:
            answer = get_oracle_answer(question)  # Now using API for real answers
    return render_template("index.html", question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)