import random

from flask import Flask
import datetime
from flask import render_template
import sqlite3

app = Flask(__name__)


@app.route('/cat/')
def cat():
    return render_template('cat.html')


@app.route('/save/')
def save():
    # params = {
    #     "access_key":"4d91959726bbcd2a849e39f3cb7dccf1",
    #     "export":'ftp',
    #     'url':
    # }
    return render_template('save.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/board/')
def board():
    return render_template('board.html')

@app.route('/Prediction/')
def Prediction():
    list_prediction = ["За твоей дверью уже стоит счастье.",
                       "В любом начинании тебя будет преследовать удача.",
                       "Найдешь новое интересное занятие."]
    a = datetime.datetime(2025, 1 ,1)-datetime.datetime.now()
    context = {
        'days':a.days,
        'hours': a.seconds // 60 // 60,
        'minutes': a.seconds // 60 % 60,
        'text_prediction': random.choice(list_prediction)
    }
    return render_template('Prediction.html', **context)


"/static/доска.png"
@app.route('/coloring/')
def coloring():
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    cur.execute("select * from coloring_base")
    coloring_list = []
    for id, img in cur.fetchall():
        coloring_list.append({"id" : id, "img" : img})
    con.close()
    context = {'img_list': coloring_list}
    return render_template('coloring.html', **context)


@app.route('/img/<int:id>/')
def img (id):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    cur.execute("select img from coloring_base where id == ?;", (id,))
    for  img in cur.fetchall():
        picture = img[0]
    con.close()
    # print (id)
    # print (picture)
    return render_template("img.html", img = picture)









# @app.route('/<name>/')
# def hello ( name = 'незнакомец'):  # put application's code here
#     if name == 'незнакомец':
#         return '<h2>' + name + ', введи своё имя в адресной строке <h2>'
#     else:
#         return'Привет ' + name

# my_str = "('text',)"
# plain_str = my_str.replace("('", "").replace("',)", "")

if __name__ == '__main__':
    app.run()
