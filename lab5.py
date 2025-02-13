import os
from flask import Flask, Blueprint, render_template, request, session, redirect, url_for, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from psycopg2 import connect
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Установка конфигурации
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'Aleksm')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'sqlite')  # По умолчанию используем SQLite

def get_db_connection():
    db_type = current_app.config.get('DB_TYPE', 'sqlite')
    if db_type == 'postgres':
        conn = connect(
            host='127.0.0.1',
            database='aleksandr_martynov_knowledge_base',
            user='postgres',
            password='Aleksm0122',
            cursor_factory=RealDictCursor
        )
        cur = conn.cursor()
    else:
        db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def close_db_connection(conn, cur):
    if cur:
        cur.close()
    if conn:
        conn.commit()
        conn.close()

# Создание Blueprint
lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab():
    if 'login' not in session:  # Проверка авторизации
        return redirect(url_for('lab5.login'))  # Перенаправление на страницу авторизации
    return render_template('lab5/lab5.html', login=session.get('login'))

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Логин и пароль не могут быть пустыми')
            return render_template('lab5/login.html')
        
        conn, cur = get_db_connection()
        cur.execute("SELECT * FROM users WHERE login = ?", (username,))
        user = cur.fetchone()
        
        if user and check_password_hash(user['password'], password):
            session['login'] = username  # Сохраняем логин в сессии
            close_db_connection(conn, cur)
            return redirect(url_for('lab5.lab'))  # Перенаправляем на главную страницу lab5
        else:
            close_db_connection(conn, cur)
            flash('Неправильный логин или пароль')
    
    return render_template('lab5/login.html')

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Логин и пароль не могут быть пустыми')
            return render_template('lab5/register.html')
        
        conn, cur = get_db_connection()
        cur.execute("SELECT * FROM users WHERE login = ?", (username,))
        existing_user = cur.fetchone()
        
        if existing_user:
            close_db_connection(conn, cur)
            flash('Логин уже занят')
            return render_template('lab5/register.html')
        
        hashed_password = generate_password_hash(password)
        cur.execute("INSERT INTO users (login, password) VALUES (?, ?)", (username, hashed_password))
        close_db_connection(conn, cur)
        flash('Пользователь успешно зарегистрирован!')
        return redirect(url_for('lab5.login'))
    
    return render_template('lab5/register.html')

@lab5.route('/lab5/list_articles')
def list_articles():
    if 'login' not in session:  # Проверка авторизации
        flash('Пожалуйста, войдите в систему для просмотра статей.')
        return redirect(url_for('lab5.login'))
    
    conn, cur = get_db_connection()
    cur.execute("""
        SELECT articles.*, users.login 
        FROM articles 
        JOIN users ON articles.user_id = users.id 
        WHERE articles.user_id = (SELECT id FROM users WHERE login = ?)
    """, (session['login'],))
    articles = cur.fetchall()
    close_db_connection(conn, cur)
    
    if not articles:
        flash('У вас нет ни одной статьи.')
    
    return render_template('lab5/list.html', articles=articles)

@lab5.route('/lab5/create_article', methods=['GET', 'POST'])
def create_article():
    if 'login' not in session:  # Проверка авторизации
        flash('Пожалуйста, войдите в систему для создания статьи.')
        return redirect(url_for('lab5.login'))
    
    if request.method == 'POST':
        title = request.form['title']
        article_text = request.form['article_text']
        is_public = request.form.get('is_public') == 'on'
        is_favorite = request.form.get('is_favorite') == 'on'
        
        if not title or not article_text:
            flash('Заголовок и текст статьи не могут быть пустыми')
            return render_template('lab5/create.html')
        
        conn, cur = get_db_connection()
        cur.execute("SELECT id FROM users WHERE login = ?", (session['login'],))
        user_id = cur.fetchone()['id']
        
        cur.execute("INSERT INTO articles (user_id, title, article_text, is_public, is_favorite) VALUES (?, ?, ?, ?, ?)",
                    (user_id, title, article_text, is_public, is_favorite))
        close_db_connection(conn, cur)
        return redirect(url_for('lab5.list_articles'))
    
    return render_template('lab5/create.html')

@lab5.route('/lab5/articles')
def articles():
    conn, cur = get_db_connection()
    cur.execute("""
        SELECT articles.*, users.login 
        FROM articles 
        JOIN users ON articles.user_id = users.id
    """)
    articles = cur.fetchall()
    close_db_connection(conn, cur)
    return render_template('lab5/articles.html', articles=articles)

@lab5.route('/lab5/edit_article/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    if 'login' not in session:  # Проверка авторизации
        flash('Пожалуйста, войдите в систему для редактирования статьи.')
        return redirect(url_for('lab5.login'))
    
    conn, cur = get_db_connection()
    cur.execute("SELECT * FROM articles WHERE id = ? AND user_id = (SELECT id FROM users WHERE login = ?)", (article_id, session['login']))
    article = cur.fetchone()
    
    if not article:
        close_db_connection(conn, cur)
        return "Статья не найдена", 404
    
    if request.method == 'POST':
        title = request.form['title']
        article_text = request.form['article_text']
        is_public = request.form.get('is_public') == 'on'
        
        if not title or not article_text:
            flash('Заголовок и текст статьи не могут быть пустыми')
            return render_template('lab5/edit_article.html', article=article)
        
        cur.execute("UPDATE articles SET title = ?, article_text = ?, is_public = ? WHERE id = ?", (title, article_text, is_public, article_id))
        close_db_connection(conn, cur)
        return redirect(url_for('lab5.list_articles'))
    
    close_db_connection(conn, cur)
    return render_template('lab5/edit_article.html', article=article)

@lab5.route('/lab5/delete_article/<int:article_id>', methods=['POST'])
def delete_article(article_id):
    if 'login' not in session:  # Проверка авторизации
        flash('Пожалуйста, войдите в систему для удаления статьи.')
        return redirect(url_for('lab5.login'))
    
    conn, cur = get_db_connection()
    cur.execute("DELETE FROM articles WHERE id = ? AND user_id = (SELECT id FROM users WHERE login = ?)", (article_id, session['login']))
    close_db_connection(conn, cur)
    return redirect(url_for('lab5.list_articles'))

@lab5.route('/lab5/logout')
def logout():
    session.pop('login', None)  # Удаляем логин из сессии
    flash('Вы успешно вышли из системы.')
    return redirect(url_for('index'))

@lab5.route('/lab5/users')
def list_users():
    if 'login' not in session:  # Проверка авторизации
        flash('Пожалуйста, войдите в систему для просмотра пользователей.')
        return redirect(url_for('lab5.login'))
    
    conn, cur = get_db_connection()
    cur.execute("SELECT login FROM users")
    users = cur.fetchall()
    close_db_connection(conn, cur)
    return render_template('lab5/users.html', users=users)

@lab5.route('/lab5/public_articles')
def public_articles():
    conn, cur = get_db_connection()
    cur.execute("""
        SELECT articles.*, users.login 
        FROM articles 
        JOIN users ON articles.user_id = users.id 
        WHERE articles.is_public = True
    """)
    articles = cur.fetchall()
    close_db_connection(conn, cur)
    return render_template('lab5/public_articles.html', articles=articles)

@lab5.route('/lab5/favorite_articles')
def favorite_articles():
    if 'login' not in session:  # Проверка авторизации
        flash('Пожалуйста, войдите в систему для просмотра избранных статей.')
        return redirect(url_for('lab5.login'))
    
    conn, cur = get_db_connection()
    cur.execute("""
        SELECT articles.*, users.login 
        FROM articles 
        JOIN users ON articles.user_id = users.id 
        WHERE articles.is_favorite = True AND articles.user_id = (SELECT id FROM users WHERE login = ?)
    """, (session['login'],))
    articles = cur.fetchall()
    close_db_connection(conn, cur)
    return render_template('lab5/favorite_articles.html', articles=articles)

app.register_blueprint(lab5)

if __name__ == '__main__':
    app.run(debug=True)
