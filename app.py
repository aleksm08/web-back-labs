from flask import Flask, url_for, redirect, render_template, abort, request ,redirect
from flask_sqlalchemy import SQLAlchemy
from db.models import users
from flask_login import LoginManager
from db import db
import os
from os import path
from db.models import users, articles



app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Aleksm')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

# Регистрация Blueprint для лабораторных работ
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)


if app.config['DB_TYPE'] == 'postgres':
    db_name = 'aleksandr_martynov_orm'
    db_user = 'aleksandr_martynov_orm'
    db_password = 'Aleksm0122'
    host_ip = '127.0.0.1'
    host_port = '5432'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, 'aleksandr_martynov_orm.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

with app.app_context():
    db.create_all()


# Главная страница
@app.route("/")
@app.route("/index")
def index():
    lab1_url = url_for("lab1.lab1_main")
    lab2_url = url_for("lab2.lab2_main")
    lab3_url = url_for("lab3.lab3_main")
    lab4_url = url_for("lab4.lab4_main")
    lab5_url = url_for("lab5.lab")
    lab6_url = url_for("lab6.lab")
    lab7_url = url_for("lab7.lab")
    lab8_url = url_for("lab8.lab")
    lab9_url = url_for("lab9.lab")
    css_path = url_for("static", filename="lab1/lab1.css")
    return f'''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" type="text/css" href="{css_path}">
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>
        <ul>
            <li><a href="{lab1_url}">Первая лабораторная</a></li>
            <li><a href="{lab2_url}">Вторая лабораторная</a></li>
            <li><a href="{lab3_url}">Третья лабораторная</a></li>
            <li><a href="{lab4_url}">Четвертая лабораторная</a></li>
            <li><a href="{lab5_url}">Пятая лабораторная</a></li>
            <li><a href="{lab6_url}">Шестая лабораторная</a></li>
            <li><a href="{lab7_url}">Седьмая лабораторная</a></li>
            <li><a href="{lab8_url}">Восьмая лабораторная</a></li>
            <li><a href="{lab9_url}">Девятая лабораторная</a></li>
        </ul>
        <footer>
            <p>ФИО: Мартынов Александр Дмитриевич</p>
            <p>Группа: ФБИ-24</p>
            <p>Курс: 3</p>
            <p>Год: 2024</p>
        </footer>
    </body>
</html>
'''

# Обработчики ошибок
@app.errorhandler(400)
def bad_request(err):
    css_path = url_for("static", filename="lab1/lab1.css")
    return render_template('error.html', error_code=400, error_message="Неверный запрос (Bad Request)", css_path=css_path), 400

@app.errorhandler(401)
def unauthorized(err):
    css_path = url_for("static", filename="lab1/lab1.css")
    return render_template('error.html', error_code=401, error_message="Неавторизованный доступ (Unauthorized)", css_path=css_path), 401

@app.errorhandler(403)
def forbidden(err):
    css_path = url_for("static", filename="lab1/lab1.css")
    return render_template('error.html', error_code=403, error_message="Доступ запрещен (Forbidden)", css_path=css_path), 403

@app.errorhandler(404)
def not_found(err):
    css_path = url_for("static", filename="lab1/lab1.css")
    return render_template('error.html', error_code=404, error_message="Страница не найдена (Not Found)", css_path=css_path), 404

@app.errorhandler(405)
def method_not_allowed(err):
    css_path = url_for("static", filename="lab1/lab1.css")
    return render_template('error.html', error_code=405, error_message="Метод не разрешен (Method Not Allowed)", css_path=css_path), 405

@app.errorhandler(500)
def internal_server_error(err):
    css_path = url_for("static", filename="lab1/lab1.css")
    return render_template('error.html', error_code=500, error_message="Внутренняя ошибка сервера (Internal Server Error)", css_path=css_path), 500

if __name__ == "__main__":
    app.run(debug=True)