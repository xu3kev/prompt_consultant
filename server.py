from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/ask": {"origins": ["http://localhost:5000", "http://127.0.0.1:5000"]}})

def answer(user_question: str) -> str:
    # Your implementation here
    return "hello hello"


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
