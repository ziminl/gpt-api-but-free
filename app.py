from flask import Flask, render_template, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    gpt_response = model.chat(user_input)
    return jsonify({'response': gpt_response})

if __name__ == '__main__':
    app.run(debug=True)