import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)

    return connection

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(8, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) DEFAULT NULL
)
'''

def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def insert_products(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity_by_id(conn, id, new_quantity):
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, id))
        conn.commit()
        print('Quantity updated successfully')
    except sqlite3.Error as e:
        print(e)

def update_product_price(conn, id, new_price):
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product_by_id(conn, id):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_products_by_price_and_quantity(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT product_title, price, quantity FROM products WHERE price < 100 AND quantity > 5")
        rows = cursor.fetchall()
        print("Products with price less than 100 and quantity more than 5:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def search_products_by_title(conn, title):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE product_title LIKE '%' || ? || '%'", (title,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


connection = create_connection('hw.db')
if connection is not None:
    create_table(connection, sql_create_products_table)
    insert_products(connection, ('Вода', 10, 100))
    insert_products(connection, ('Хлеб', 20, 30))
    insert_products(connection, ('Молоко', 100, 10))
    insert_products(connection, ('Мыло', 50, 5))
    insert_products(connection, ('Сахар', 100, 10))
    insert_products(connection, ('Соль', 15, 50))
    insert_products(connection, ('Мясо', 500, 2))
    insert_products(connection, ('Колбаса', 300, 20))
    insert_products(connection, ('Сосиски', 199, 9))
    insert_products(connection, ('Курица', 400, 5))
    insert_products(connection, ('Чай', 45, 25))
    insert_products(connection, ('Кофе', 225, 44))
    insert_products(connection, ('Шампунь', 199, 49))
    insert_products(connection, ('Стиральный порошок', 49, 12))
    insert_products(connection, ('Пакет', 5, 50))
    print('Connected successfully')
    update_quantity_by_id(connection, 1, 50)
    update_product_price(connection, 1, 9.9)
    delete_product_by_id(connection, 2)
    select_products_by_price_and_quantity(connection)
    search_products_by_title(connection, 'Мыло')
    select_all_products(connection)
    print('Done')
    connection.close()