from flask import Flask
from flask import render_template
from flask import request
from config import true_pass
import sqlite3
app = Flask(__name__)
@app.route('/edit/', methods = ['GET', 'POST'])
@app.route('/edit/<int:db_id>/')
def edit(db_id=None):
    if request.method == 'POST':
        if request.form.get('password') != true_pass:
            return 'Доступ закрыт, залогинтесь'

        db_id = request.form.get('db_id')
        caption = request.form.get('caption')
        author = request.form.get('author')
        visible = True if request.form.get('visible') else False

        conn = sqlite3.connect('db.sqlite')
        cur = conn.cursor()

        cur.execute("""update stories set caption = ?, author = ?, visible = ? where id == ?;""",
                    (caption, author, visible, db_id))

        conn.commit()
        conn.close()
        return 'Информация обновлена'
    if db_id is None:
        return "Введи номер истории"
    # Получаем истории из бд
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()

    cur.execute("""select id, caption, author, visible from stories where id == ?;""",
                (db_id,))
    context = None

    for db_id, caption, author, visible in cur.fetchall():
        context = {'db_id': db_id, 'caption': caption, 'author': author, 'visible': visible}
    conn.close()

    if context is None:
        return 'Такой книги нет'
    return render_template('test.html', **context)

if __name__ == '__main__':
 app.run(debug=True)











































#import sqlite3
#
#conn = sqlite3.connect('db.sqlite')
#cur = conn.cursor()
#
#cur.execute("""create table if not exists stories
#(
# id integer primary key autoincrement,
# caption text,
# story text,
# author text,
# visible blob default TRUE
#);""")
#
#cur.execute("""insert into stories (caption, story, author, visible) values(?, ?, ?, ?);""", ('Тестовая история', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Delectus enim est illo illum ipsam nisi!', 'Марк Туллий Цицерон', True))
#
#cur.execute("""select caption, story, author from stories;""")
#print(cur.fetchone())
#
#conn.commit()
#conn.close()
#























































#from flask import Flask, render_template
#
#app = Flask(__name__)
#
#@app.route('/')
#def index():
#    return render_template('index.html')
#
#@app.route('/blog/')
#def blog():
# context = {
# 'title': 'Блог',
# 'name': 'Nikita',
# }
# return render_template('blog.html', **context)
#
#@app.route('/base/')
#def base():
#    return render_template('base.html')
#
#@app.route('/contacts')
#def contacts():
#    return render_template('contacts.html')
#
#@app.route('/main/')
#def main():
#    context = {
#        'title': 'Главная',
#        'username': 'Nikita',
#        'time': 17
#    }
#    return render_template('main.html', **context)
#
#if __name__ == '__main__':
#    app.run()