from flask import Flask, render_template,request

url = "https://free-chatgpt-api.p.rapidapi.com/chat-completion-one"
headers = {
        "x-rapidapi-key": "my_api_key",
        "x-rapidapi-host": "free-chatgpt-api.p.rapidapi.com"
    }

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        return render_template('index.html', question=question)
    else:
        return render_template('index.html')


    querystring = {"prompt": question}

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

if __name__ == '__main__':
    app.run()