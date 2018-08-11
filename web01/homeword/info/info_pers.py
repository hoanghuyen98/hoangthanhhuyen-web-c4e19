import os
from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('info.html')

@app.route('/about-me')

def info():
    info_personal = [
        {
        'name': '1: Hoang Thanh Huyen',
        'work': '2: Student',
        'school': '3: Academy of cryptography techniques',
        'hobbies': '4: dance, game, eat,...',
        'crush': '5: (:|'
        }
    ]
    return render_template("info.html", info_personal = info_personal)

@app.route('/school')
def school():
    return redirect("http://techkids.vn/", code = 302)


if __name__ == '__main__':
  app.run(debug=True)
 