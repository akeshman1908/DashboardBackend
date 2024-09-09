import sqlite3
from werkzeug.security import check_password_hash

# Verbind met de SQLite-database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Functie om een gebruiker te valideren tijdens login
def check_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Zoek de gebruiker op basis van de gebruikersnaam
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    # Als gebruiker bestaat, controleer het wachtwoord
    if user and check_password_hash(user['password'], password):
        return True
    return False
