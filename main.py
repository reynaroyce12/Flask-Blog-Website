from smtplib import *
import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv('MY_EMAIL')
password = os.getenv('PASSWORD')
their_email = os.getenv('THEIR_EMAIL')

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


@app.route("/Success", methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        sent_mail(username, email, phone, message)
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


def sent_mail(username, email, phone, message):
    with SMTP('smtp.gmail.com', 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=their_email,
                            msg=f"Subject:There's a message for you!\n\n"
                                f"Name - {username}\n Email - {email}\n phone - {phone}\n Message - {message}")
        print("Mail sent")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
