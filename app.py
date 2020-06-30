from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


@app.route('/')
def index():
    with open('data/data.json', 'r', encoding='UTF-8') as f:
        quiz_data = json.load(f)
    return render_template('quiz_answers.html', quiz=quiz_data)


@app.route('/json')
def json_api():
    with open('data/data.json', 'r', encoding='UTF-8') as f:
        quiz_data = json.load(f)
    return quiz_data


@app.route('/posts')
def posts():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    return render_template('posts.html', posts=posts)


@app.route('/photo')
def photo():
    photos = requests.get('https://jsonplaceholder.typicode.com/photos?_limit=10').json()
    return render_template('gallery.html', photos=photos)


if __name__ == '__main__':
    app.run()
