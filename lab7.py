from flask import Blueprint, render_template, request, jsonify, session, current_app
from lab5 import get_db_connection, close_db_connection
import datetime

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def lab():
    return render_template('lab7/lab7.html')

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    conn, cur = get_db_connection()
    cur.execute("SELECT * FROM films ORDER BY id")
    films = cur.fetchall()
    close_db_connection(conn, cur)
    return jsonify([dict(film) for film in films])

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    conn, cur = get_db_connection()
    cur.execute("SELECT * FROM films WHERE id = ?", (id,))
    film = cur.fetchone()
    close_db_connection(conn, cur)
    if film is None:
        return "Film not found", 404
    return jsonify(dict(film))

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    conn, cur = get_db_connection()
    cur.execute("DELETE FROM films WHERE id = ?", (id,))
    close_db_connection(conn, cur)
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    conn, cur = get_db_connection()
    cur.execute("SELECT * FROM films WHERE id = ?", (id,))
    film = cur.fetchone()
    if film is None:
        close_db_connection(conn, cur)
        return "Film not found", 404
    
    data = request.get_json()
    
    # Проверка названия (оригинального и русского)
    if not data.get('title') and not data.get('title_ru'):
        close_db_connection(conn, cur)
        return {'title': 'Заполните оригинальное или русское название'}, 400
    
    if not data.get('title_ru'):
        close_db_connection(conn, cur)
        return {'title_ru': 'Русское название не может быть пустым'}, 400
    
    # Проверка года
    try:
        film_year = int(data.get('film_year'))
        current_year = datetime.datetime.now().year
        if not (1895 <= film_year <= current_year):
            close_db_connection(conn, cur)
            return {'film_year': f'Год должен быть от 1895 до {current_year}'}, 400
    except (ValueError, TypeError):
        close_db_connection(conn, cur)
        return {'film_year': 'Год должен быть числом'}, 400
    
    # Проверка описания
    description = data.get('description', '').strip()
    if not description:
        close_db_connection(conn, cur)
        return {'description': 'Описание не может быть пустым'}, 400
    if len(description) > 2000:
        close_db_connection(conn, cur)
        return {'description': 'Описание должно быть не более 2000 символов'}, 400
    
    # Если оригинальное название пустое, устанавливаем его равным русскому названию
    if not data.get('title'):
        data['title'] = data['title_ru']
    
    cur.execute("UPDATE films SET title = ?, title_ru = ?, film_year = ?, description = ? WHERE id = ?",
                (data['title'], data['title_ru'], data['film_year'], data['description'], id))
    close_db_connection(conn, cur)
    return jsonify(data)

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    data = request.get_json()
    
    # Проверка названия (оригинального и русского)
    if not data.get('title') and not data.get('title_ru'):
        return {'title': 'Заполните оригинальное или русское название'}, 400
    
    if not data.get('title_ru'):
        return {'title_ru': 'Русское название не может быть пустым'}, 400
    
    # Проверка года
    try:
        film_year = int(data.get('film_year'))
        current_year = datetime.datetime.now().year
        if not (1895 <= film_year <= current_year):
            return {'film_year': f'Год должен быть от 1895 до {current_year}'}, 400
    except (ValueError, TypeError):
        return {'film_year': 'Год должен быть числом'}, 400
    
    # Проверка описания
    description = data.get('description', '').strip()
    if not description:
        return {'description': 'Описание не может быть пустым'}, 400
    if len(description) > 2000:
        return {'description': 'Описание должно быть не более 2000 символов'}, 400
    
    # Если оригинальное название пустое, устанавливаем его равным русскому названию
    if not data.get('title'):
        data['title'] = data['title_ru']
    
    conn, cur = get_db_connection()
    cur.execute("INSERT INTO films (title, title_ru, film_year, description) VALUES (?, ?, ?, ?)",
                (data['title'], data['title_ru'], data['film_year'], data['description']))
    new_film_id = cur.lastrowid
    close_db_connection(conn, cur)
    return {"id": new_film_id}, 201


