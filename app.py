import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"
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

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["iSay"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=generate_prompt(animal)
        )
        print(response)
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    messages[0]["content"] = animal.capitalize()
    return messages


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3389)