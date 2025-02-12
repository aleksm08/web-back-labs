from flask import Flask, url_for, redirect, abort
from werkzeug.exceptions import HTTPException

class PaymentRequired(HTTPException):
    code = 402
    description = "Необходима оплата (Payment Required)"
    
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    styles_path = url_for("static", filename="lab1.css")
    lab1_url = url_for('lab1')  # Ссылка на первую лабораторную (/lab1/oak)
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" type="text/css" href="''' + styles_path + '''">
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>
        <main>
            <li>
                <a href="''' + lab1_url + '''">Лабораторная работа №1</a>
            </li>
        </main>
        <footer>
            Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route('/lab1')
def lab1():
    styles_path = url_for("static", filename="lab1.css")
    home_url = url_for('index')  # Ссылка на корень сайта (/)
    web_url = url_for('web')  # Ссылка на /lab1/web
    author_url = url_for('author')  # Ссылка на /lab1/author
    oak_url = url_for('oak')  # Ссылка на /lab1/oak
    story_url = url_for('story')  # Ссылка на /lab1/story
    counter_url = url_for('counter')  # Ссылка на /lab1/counter
    reset_counter_url = url_for('reset_counter')  # Ссылка на /lab1/counter/reset
    created_url = url_for('created')  # Ссылка на /lab1/created
    info_url = url_for('info')  # Ссылка на /lab1/info
    error400_url = url_for('error_400')  # Ссылка на /error400
    error401_url = url_for('error_401')  # Ссылка на /error401
    error402_url = url_for('error_402')  # Ссылка на /error402
    error403_url = url_for('error_403')  # Ссылка на /error403
    error404_url = url_for('error_404')  # Ссылка на /error404
    error405_url = url_for('error_405')  # Ссылка на /error405
    error418_url = url_for('error_418')  # Ссылка на /error418
    error500_url = url_for('error_500')  # Ссылка на /error500


    return f'''
<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="{styles_path}">
    </head>
    <body>
        <main>
            <h1>Лабораторная 1</h1>
            <p>
                Flask — фреймворк для создания веб-приложений на языке программирования Python, 
                использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. 
                Относится к категории так называемых микрофреймворков — минималистичных каркасов 
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </p>
            <p><a href="{home_url}">Вернуться на главную</a></p>
            <h2>Список роутов</h2>
            <ul>
                <li><a href="{home_url}">Главная (/) или (/index)</a></li>
                <li><a href="{web_url}">Web-сервер на Flask (/lab1/web)</a></li>
                <li><a href="{author_url}">Автор (/lab1/author)</a></li>
                <li><a href="{oak_url}">Дуб (/lab1/oak)</a></li>
                <li><a href="{story_url}">История (/lab1/story)</a></li>
                <li><a href="{counter_url}">Счётчик (/lab1/counter)</a></li>
                <li><a href="{reset_counter_url}">Сбросить счётчик (/lab1/counter/reset)</a></li>
                <li><a href="{created_url}">Создано (/lab1/created)</a></li>
                <li><a href="{info_url}">Информация (/lab1/info)</a></li>
                <li><a href="{error400_url}">Ошибка 400 (/error400)</a></li>
                <li><a href="{error401_url}">Ошибка 401 (/error401)</a></li>
                <li><a href="{error402_url}">Ошибка 402 (/error402)</a></li>
                <li><a href="{error403_url}">Ошибка 403 (/error403)</a></li>
                <li><a href="{error404_url}">Ошибка 404 (/error404)</a></li>
                <li><a href="{error405_url}">Ошибка 405 (/error405)</a></li>
                <li><a href="{error418_url}">Ошибка 418 (/error418)</a></li>
                <li><a href="{error500_url}">Ошибка 500 (/error500)</a></li>
            </ul>
        </main>
    </body>
</html>
'''



@app.route("/lab1/web")
def web():
    styles_path = url_for("static", filename="lab1.css")
    return f"""<!doctype html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="{styles_path}">
        </head>
            <body>
                <main>
                    <h1>web-сервер на Flask</h1>
                    <a href='/author'>author</a>
                </main>
            </body>
        </html>""", 200, {
            "X-Server": "sample",
            'Content-Type': 'text/plain; charset=utf-8'
            }

@app.route("/lab1/author")
def author():
    styles_path = url_for("static", filename="lab1.css")
    name = 'Мартынов Александр Дмитриевич'
    group = 'ФБИ-24'
    faculty = 'ФБ'

    return f"""<!doctype html>
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="{styles_path}">
            </head>
            <body>
                <main>
                    <p>Студент: """ + name + """</p>
                    <p>Группа: """ + group + """</p>
                    <p>Факультет: """ + faculty + """</p>
                    <a href='/lab1/web'>web</a>
                </main>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path = url_for("static", filename="oak.jpg")
    styles_path = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<head>
    <link rel="stylesheet" type="text/css" href="''' + styles_path + '''">
</head>
<html>
    <body>
        <main>
            <h1>Дуб</h1>
            <img src=" ''' + path + ''' ">
        </main>
    </body>
</html>
'''

@app.errorhandler(400)
def bad_request(err):
    css_path = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <title>Ошибка 400 - Неверный запрос</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Ошибка 400</h1>
        </header>
        <main>
            <p>Неверный запрос (Bad Request)</p>
        </main>
        <footer>
            <p>Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024</p>
        </footer>
    </body>
</html>
''', 400

@app.errorhandler(401)
def unauthorized(err):
    css_path = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <title>Ошибка 401 - Неавторизован</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Ошибка 401</h1>
        </header>
        <main>
            <p>Неавторизованный доступ (Unauthorized)</p>
        </main>
        <footer>
            <p>Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024</p>
        </footer>
    </body>
</html>
''', 401

@app.errorhandler(PaymentRequired)
def payment_required(err):
    css_path = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <title>Ошибка 402 - Необходима оплата</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Ошибка 402</h1>
        </header>
        <main>
            <p>Необходима оплата (Payment Required)</p>
        </main>
        <footer>
            <p>Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024</p>
        </footer>
    </body>
</html>
''', 402


@app.errorhandler(403)
def forbidden(err):
    css_path = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <title>Ошибка 403 - Доступ запрещен</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Ошибка 403</h1>
        </header>
        <main>
            <p>Доступ запрещен (Forbidden)</p>
        </main>
        <footer>
            <p>Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024</p>
        </footer>
    </body>
</html>
''', 403

@app.errorhandler(404)
def not_found(err):
    path = url_for("static", filename="404.jpg")
    css_path = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Ошибка 404</h1>
        </header>
        <main>
            <p>вы кто такие, я вас не звал, идите дальше</p>
            <img src="{path}" alt="нет такой страницы">
        </main>
        <footer>
            <p>Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024</p>
        </footer>
    </body>
</html>
''', 404    

@app.errorhandler(405)
def method_not_allowed(err):
    css_path = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <title>Ошибка 405 - Метод не разрешен</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Ошибка 405</h1>
        </header>
        <main>
            <p>Метод не разрешен (Method Not Allowed)</p>
        </main>
        <footer>
            <p>Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024</p>
        </footer>
    </body>
</html>
''', 405

@app.errorhandler(418)
def im_a_teapot(err):
    css_path = url_for("static", filename="lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <title>Ошибка 418 - Я чайник</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Ошибка 418</h1>
        </header>
        <main>
            <p>Я чайник (I'm a teapot)</p>
        </main>
        <footer>
            <p>Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024</p>
        </footer>
    </body>
</html>
''', 418

@app.route('/lab1/story')
def story():
    styles_path = url_for("static", filename="lab1.css")
    image_path = url_for("static", filename="story_image.jpg")

    title = "Интересная история"
    paragraph1 = "Это первый абзац истории. Он рассказывает о начале приключения, где главный герой отправляется в путешествие по незнакомым землям."
    paragraph2 = "Во втором абзаце рассказывается о том, как герой встретил на своем пути необычных существ, которые помогли ему разгадать старинные загадки."
    paragraph3 = "Третий абзац подводит итог приключениям героя. Он возвращается домой, обогащенный новым опытом и знаниями, и делится своими историями с друзьями."

    return f'''
<!doctype html>
<html lang="ru">
    <head>
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="{styles_path}">
    </head>
    <body>
        <header>
            <h1>{title}</h1>
        </header>
        <main>
            <p>{paragraph1}</p>
            <p>{paragraph2}</p>
            <p>{paragraph3}</p>
            <img src="{image_path}" alt="Картинка для истории" style="width: 50%; margin-top: 20px;">
        </main>
        <footer>
            <p>Мартынов Александр Дмитриевич, ФБИ-24, 3 курс, 2024</p>
        </footer>
    </body>
</html>
''', 200, {
        'Content-Language': 'ru',  # Устанавливаем заголовок Content-Language
        'X-Custom-Header': 'MyCustomValue',  # Нестандартный заголовок 1
        'X-Another-Custom-Header': 'AnotherValue'  # Нестандартный заголовок 2
    }

count = 0

@app.route('/lab1/counter')
def counter():
    styles_path = url_for("static", filename="lab1.css")
    global count
    count += 1
    reset_link = url_for('reset_counter')
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + styles_path + '''">
    </head>
    <body>
        <main>
            <div>Сколько раз вы сюда заходили: ''' + str(count) + '''</div>
            <a href="''' + reset_link + '''">Сбросить счётчик</a>
        </main>
    </body>
</html>
'''

@app.route('/lab1/counter/reset')
def reset_counter():
    styles_path = url_for("static", filename="lab1.css")
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + styles_path + '''">
    </head>
    <body>
        <main>
            <h1>Счётчик сброшен!</h1>
            <p>Счётчик теперь равен: ''' + str(count) + '''</p>
            <a href="''' + url_for('counter') + '''">Назад к счётчику</a>
        </main>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    styles_path = url_for("static", filename="lab1.css")
    return redirect("/lab1/author")

@app.route("/lab1/created")
def created():
    styles_path = url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + styles_path + '''">
    </head>
    <body>
        <main>    
            <h1>Создано успешно</h1>
            <div><i>Что-то создано...</i></div>
        </main>
    </body>
</html>
''', 201

# Маршруты для генерации ошибок
@app.route('/error400')
def error_400():
    abort(400)  # Вызов ошибки 400

@app.route('/error401')
def error_401():
    abort(401)  # Вызов ошибки 401

@app.route('/error402')
def error_402():
    raise PaymentRequired()  # Вызов ошибки 402 через созданный класс

@app.route('/error403')
def error_403():
    abort(403)  # Вызов ошибки 403

@app.route('/error404')
def error_404():
    abort(404)  # Вызов ошибки 404

@app.route('/error405')
def error_405():
    abort(405)  # Вызов ошибки 405

@app.route('/error418')
def error_418():
    abort(418)  # Вызов ошибки 418

@app.route('/error500')
def error_500():
    result = 1 / 0  # Это вызовет ZeroDivisionError
    return str(result)

# Перехватчик для ошибки 500 с сообщением на русском языке
@app.errorhandler(500)
def internal_server_error(err):
    return "Ошибка 500: Внутренняя ошибка сервера. Пожалуйста, повторите попытку позже.", 500

@app.route('/lab2/a')
def a():
    return 'Без слеша'

@app.route('/lab2/a/')
def a2():
    return 'Со слешем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок:" + flower_list(flower_id)
    
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Добавлен новый цветок</h1>
        <p>Название нового цветка: {name}</p>
        <p>Всего цветов: {len(flower_list)}</p>
        <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)