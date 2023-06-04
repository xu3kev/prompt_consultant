from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from prompt import prompt_claude


MOCK = False

app = Flask(__name__, static_url_path='/static')
CORS(app, resources={r"/ask": {"origins": ["http://localhost:5000", "http://127.0.0.1:5000"]}})


def answer(user_question: str) -> str:
    # Your implementation here
    # sleep for a while and then return a string
    if MOCK:
        import time
        time.sleep(1)
        return "hello hello"

    result = prompt_claude(user_question)
    str_result = result["completion"]

    # make str_result into a proper html paragraph
    #str_result = str_result.replace("\n", "<br>")
    
    return str_result


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    return jsonify({
        'answer': answer(question)
    })

if __name__ == '__main__':
    app.run(debug=True)
