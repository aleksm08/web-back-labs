import sqlite3

# Подключение к базе данных (или создание новой)
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Создание таблицы users
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Создание таблицы articles
cur.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        article_text TEXT NOT NULL,
        is_public BOOLEAN DEFAULT FALSE,
        is_favorite BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

# Создание таблицы favorites (если используется)
cur.execute('''
    CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        article_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (article_id) REFERENCES articles (id)
    )
''')

# Создание таблицы films
cur.execute('''
    CREATE TABLE IF NOT EXISTS films (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        title_ru TEXT NOT NULL,
        film_year INTEGER NOT NULL,
        description TEXT NOT NULL
    )
''')


# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных успешно инициализирована.")