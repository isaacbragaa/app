import sqlite3

def init_db():
    conn = sqlite3.connect('/app/data/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cadastros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            sinopse TEXT NOT NULL,
            tipo TEXT NOT NULL,
            
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
