from flask import Flask, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

@app.route("/")
@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на Flask</h1>
                <a href='/author'>author</a>
            </body>
        </html>""", 200, {
            "X-Server": "sample",
            'Content-Type': 'text/plain; charset=utf-8'
            }

@app.route("/lab1/author")
def author():
    name = 'Мартынов Александр Дмитриевич'
    group = 'ФБИ-22'
    faculty = 'ФБ'

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href='/web'>web</a>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    styles = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<head>
    <link rel="stylesheet" type="text/css" href="''' + styles + '''">
</head>
<html>
    <body>
        <h1>Дуб</h1>
        <img src=" ''' + path + ''' ">
    </body>
</html>
'''

count = 0

@app.route('/lab1/counter')
def counter():
    global count
    count += 1
    reset_link = url_for('reset_counter')
    return '''
<!doctype html>
<html>
    <body>
        <div>Сколько раз вы сюда заходили: ''' + str(count) + '''</div>
        <a href="''' + reset_link + '''">Сбросить счётчик</a>
    </body>
</html>
'''

@app.route('/lab1/counter/reset')
def reset_counter():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        <h1>Счётчик сброшен!</h1>
        <p>Счётчик теперь равен: ''' + str(count) + '''</p>
        <a href="''' + url_for('counter') + '''">Назад к счётчику</a>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>Что-то создано...</i></div>
    </body>
</html>
''', 201