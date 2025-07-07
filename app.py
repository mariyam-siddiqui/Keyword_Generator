# %%
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

openai = OpenAI(base_url = "http://localhost:11434/v1", api_key = "ollama")

system_prompt = """You are an assistant who has been tasked with reading content and coming up with tags that can be used for marking that document.
Return the list of tags as a comma separated value
"""

@app.route("/")

def index():
    return render_template('index.html')

@app.route("/get_tags", methods = ['POST'])

def get_tags():
    user_input = request.json['prompt']
    
    messages = [
        {"role" : "system", "content" : system_prompt},
        {"role" : "user", "content" : user_input}
    ]

    response = openai.chat.completions.create(
        model = "llama3.2",
        messages = messages
    )

    tags = response.choices[0].message.content

    return jsonify({"tags" : tags})


if __name__ == '__main__':
    app.run(debug = True)
