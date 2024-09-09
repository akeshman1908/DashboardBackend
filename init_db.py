import sqlite3
from werkzeug.security import generate_password_hash

# Maak de users tabel aan en voeg dummy data toe
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Maak een tabel voor gebruikers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Voeg dummy gebruikers toe
    users = [
        ('user1', generate_password_hash('password1')),
        ('user2', generate_password_hash('password2')),
        ('user3', generate_password_hash('password3')),
    ]
    
    # Voeg de gebruikers toe aan de tabel
    cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
