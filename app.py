import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from flask import Markup
import markdown


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
#print(openai.api_key)
#print(openai.Model.list())
"""
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
"""
messages = [
    {"role": "user", "content": "write a python function to read a file"}
]

tmpContent= ""

# md转html的方法
def md2html(mdcontent):
    exts = ['markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.tables',
            'markdown.extensions.toc']
    html = markdown.markdown(mdcontent, extensions=exts)
    content = Markup(html)
    return content

@app.route("/", methods=("GET", "POST"))
def index():
    global tmpContent
    if request.method == "POST":
        animal = request.form["iSay"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=generate_prompt(animal)
        )
        #print(response)
        data = response.choices[0].message.content
        tmpContent = md2html(data)
        return redirect(url_for("index"))
    return render_template("index.html", result=tmpContent)

@app.route("/chatdemo", methods=("GET", "POST"))
def chatdemo():
    return render_template("chat_app.html")

@app.route("/chatgpt", methods=("GET", "POST"))
def chatgpt():
    return render_template("chattmp.html")

def generate_prompt(animal):
    messages[0]["content"] = animal.capitalize()
    return messages

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)