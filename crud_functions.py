import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.dp')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('products.dp')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products

def add_product(title, description, price):
    initiate_db()
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (title, description, price))
    conn.commit()
    conn.close()

add_product('Product1', '1', 100)
add_product('Product2', '2', 200)
add_product('Product3', '3', 300)
add_product('Product4', '4', 400)