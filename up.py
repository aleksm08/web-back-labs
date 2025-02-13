import sqlite3

# Путь к вашей базе данных SQLite
db_path = 'database.db'

# Подключение к базе данных
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# SQL-запросы для добавления столбцов
try:
    cur.execute("ALTER TABLE articles ADD COLUMN is_public BOOLEAN DEFAULT FALSE")
    cur.execute("ALTER TABLE articles ADD COLUMN is_favorite BOOLEAN DEFAULT FALSE")
    conn.commit()
    print("Столбцы успешно добавлены.")
except sqlite3.OperationalError as e:
    print(f"Ошибка при добавлении столбцов: {e}")
finally:
    # Закрытие соединения
    cur.close()
    conn.close()