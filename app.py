


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog/')
def blog():
 context = {
 'title': 'Блог',
 'name': 'Nikita',
 }
 return render_template('blog.html', **context)

@app.route('/base/')
def base():
    return render_template('base.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

@app.route('/main/')
def main():
    context = {
        'title': 'Главная',
        'username': 'Nikita',
        'time': 17
    }
    return render_template('main.html', **context)

if __name__ == '__main__':
    app.run()


