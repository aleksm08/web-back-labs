from flask import Blueprint, url_for, redirect, abort, make_response, render_template_string, request
from werkzeug.exceptions import HTTPException

lab1 = Blueprint('lab1', __name__)

class PaymentRequired(HTTPException):
    code = 402
    description = "Необходима оплата (Payment Required)"  # 402 нестандартная ошибка

@lab1.route("/lab1")
def lab1_main():
    css_path = url_for("static", filename="lab1/lab1.css")
    root_url = url_for("index")
    routes = [
        ('lab1', url_for('lab1.lab1_main')),
        ('Автор', url_for('lab1.author')),
        ('Web', url_for('lab1.start')),
        ('Счетчик', url_for('lab1.counter')),
        ('Сброс счетчика', url_for('lab1.reset_counter')),
        ('Info', url_for('lab1.info')),
        ('Oak', url_for('lab1.oak')),
        ('Created', url_for('lab1.created')),
        ('Custom Page', url_for('lab1.custom_page')),
        ('Ошибка 400', url_for('lab1.error_400')),
        ('Ошибка 401', url_for('lab1.error_401')),
        ('Ошибка 402', url_for('lab1.error_402')),
        ('Ошибка 403', url_for('lab1.error_403')),
        ('Ошибка 404', url_for('lab1.error_404')),
        ('Ошибка 405', url_for('lab1.error_405')),
        ('Ошибка 500', url_for('lab1.error_500')),
    ]
    table_rows = ''.join([f'<tr><td>{name}</td><td><a href="{url}" style="color: blue;">{url}</a></td></tr>' for name, url in routes])
    
    return f'''
<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
        <style>
            body {{
                background-color: white;
                color: black;
                font-family: Arial, sans-serif;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid black;
                padding: 10px;
                text-align: left;
            }}
            th {{
                background-color: #000080;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            a {{
                color: blue;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            footer {{
                margin-top: 50px;
                text-align: center;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Лабораторная 1</h1>
        </header>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2.
        </p>
        <a href="{root_url}" style="color: blue;">Вернуться на главную</a>
        <h2>Список роутов</h2>
        <table>
            <thead>
                <tr>
                    <th>Название маршрута</th>
                    <th>Ссылка</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
        <footer>
            <p>ФИО: Мартынов Александр Дмитриевич</p>
            <p>Группа: ФБИ-24</p>
            <p>Курс: 3</p>
            <p>Год: 2024</p>
        </footer>
    </body>
</html>
'''

@lab1.route("/lab1/web")
def start():
    css_path = url_for("static", filename="lab1/lab1.css")
    return f'''<!doctype html> 
    <html> 
        <head>
            <link rel="stylesheet" type="text/css" href="{css_path}">
        </head>
        <body>
            <header>
                <h1>web-сервер на flask</h1>
            </header>
            <footer>
                <p>ФИО: Мартынов Александр Дмитриевич</p>
                <p>Группа: ФБИ-24</p>
                <p>Курс: 3</p>
                <p>Год: 2024</p>
            </footer>
        </body> 
    </html>''', 200, {
        'X-Server': 'sample',
        'Content-Type': 'text/plain; charset=utf-8'
    }

@lab1.route("/lab1/author")
def author():
    name = "Мартынов Александр Дмитриевич"
    group = "ФБИ-24"
    faculty = "ФБ"
    css_path = url_for("static", filename="lab1/lab1.css")
    return f'''<!doctype html>
        <html>
            <head>
                <link rel="stylesheet" type="text/css" href="{css_path}">
            </head>
            <body>
                <header>
                    <h1>Студент</h1>
                </header>
                <p>Студент: {name}</p>
                <p>Группа: {group}</p>
                <p>Факультет: {faculty}</p>
                <a href="{url_for('lab1.start')}">web</a>
                <footer>
                    <p>ФИО: Мартынов Александр Дмитриевич</p>
                    <p>Группа: ФБИ-24</p>
                    <p>Курс: 3</p>
                    <p>Год: 2024</p>
                </footer>
            </body>
        </html>'''

@lab1.route("/lab1/oak")
def oak():
    path = url_for("static", filename="lab1/oak.jpg")
    css_path = url_for("static", filename="lab1/lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Дуб</h1>
        </header>
        <img src="{path}" alt="Дуб">
        <footer>
            <p>ФИО: Мартынов Александр Дмитриевич</p>
            <p>Группа: ФБИ-24</p>
            <p>Курс: 3</p>
            <p>Год: 2024</p>
        </footer>
    </body>
</html>    
'''

count = 0

@lab1.route("/lab1/counter")
def counter():
    global count  
    count += 1
    reset_url = url_for("lab1.reset_counter")
    css_path = url_for("static", filename="lab1/lab1.css")
    return f'''
<!doctype html> 
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Счетчик посещений</h1>
        </header>
        <p>Сколько раз вы сюда заходили: {count}</p>
        <a href="{reset_url}">Очистить счетчик</a>
        <footer>
            <p>ФИО: Мартынов Александр Дмитриевич</p>
            <p>Группа: ФБИ-24</p>
            <p>Курс: 3</p>
            <p>Год: 2024</p>
        </footer>
    </body>
</html>
'''

@lab1.route("/lab1/reset_counter")
def reset_counter():
    global count 
    count = 0 
    counter_url = url_for("lab1.counter")
    css_path = url_for("static", filename="lab1/lab1.css")
    return f'''
<!doctype html> 
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Счетчик очищен</h1>
        </header>
        <p>Счетчик был сброшен.</p>
        <a href="{counter_url}">Вернуться к счетчику</a>
        <footer>
            <p>ФИО: Мартынов Александр Дмитриевич</p>
            <p>Группа: ФБИ-24</p>
            <p>Курс: 3</p>
            <p>Год: 2024</p>
        </footer>
    </body>
</html>
'''

@lab1.route("/lab1/info")
def info():
    return redirect(url_for("lab1.author"))

@lab1.route("/created")
def created():
    css_path = url_for("static", filename="lab1/lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>Создано успешно</h1>
        </header>
        <div><i>что-то созданно ...</i></div>
        <footer>
            <p>ФИО: Мартынов Александр Дмитриевич</p>
            <p>Группа: ФБИ-24</p>
            <p>Курс: 3</p>
            <p>Год: 2024</p>
        </footer>
    </body>
</html>
''', 201

@lab1.route('/custom-page')
def custom_page():
    # Путь к картинке
    image_url = url_for('static', filename='lab1/story_image.jpg')
    # Текст для страницы
    page_content = '''
    <!doctype html>
    <html>
        <head>
            <title>Кастомная страница</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                }}
                .content {{
                    margin: 20px;
                }}
            </style>
        </head>
        <body>
            <header>
                <h1>Добро пожаловать на кастомную страницу</h1>
            </header>
            <div class="content">
                <p>
                    Это пример страницы, которая демонстрирует работу с несколькими
                    абзацами текста. Веб-разработка может быть увлекательной и интересной, особенно
                    когда вы создаете что-то новое и функциональное.
                </p>
                <p>
                    Flask является мощным и гибким микрофреймворком для создания веб-приложений
                    на Python. Он предоставляет разработчикам возможность быстро и эффективно создавать
                    веб-сервисы, не перегружая их сложными библиотеками.
                </p>
                <p>
                    Помимо работы с текстом, веб-страницы часто содержат изображения, которые
                    делают их более привлекательными для пользователей. В нашем случае это пример
                    изображения ниже:
                </p>
                <img src="{image_url}" alt="Пример изображения">
                <p>
                    Этот текст демонстрирует работу с несколькими абзацами и изображениями,
                    а также добавление кастомных заголовков в ответ сервера.
                </p>
            </div>
            <footer>
                <p>ФИО: Мартынов Александр Дмитриевич</p>
                <p>Группа: ФБИ-24</p>
                <p>Год: 2024</p>
            </footer>
        </body>
    </html>
    '''.format(image_url=image_url)

    # Создаем ответ и добавляем заголовки
    response = make_response(page_content)
    
    # Добавляем заголовок Content-Language
    response.headers['Content-Language'] = 'ru'
    
    # Добавляем два своих нестандартных заголовка
    response.headers['X-Custom-Header-1'] = 'MyCustomHeaderValue1'
    response.headers['X-Custom-Header-2'] = 'MyCustomHeaderValue2'

    return response

@lab1.route('/error400')
def error_400():
    abort(400)  # Вызов ошибки 400

@lab1.route('/error401')
def error_401():
    abort(401)  # Вызов ошибки 401

@lab1.route('/error402')
def error_402():
    raise PaymentRequired()  # Вызов ошибки 402 через созданный класс

@lab1.route('/error403')
def error_403():
    abort(403)  # Вызов ошибки 403

@lab1.route('/error404')
def error_404():
    abort(404)  # Вызов ошибки 404

@lab1.route('/error405')
def error_405():
    abort(405)  # Вызов ошибки 405

@lab1.route('/error500')
def error_500():
    result = 1 / 0  
    return str(result)