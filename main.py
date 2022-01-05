from flask import Flask, render_template
import requests

posts = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()


app = Flask(__name__)


@app.route('/')
def show_home():
    return render_template('index.html', posts=posts)


@app.route('/post/<int:index>')
def show_post(index):
    user_post = None
    for blog in posts:
        if blog['id'] == index:
            user_post = blog
    return render_template('post.html', post=user_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
