import sqlite3

def create_db():
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()

    # Create expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_db()
    print("Database and table created successfully.")
