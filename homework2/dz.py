import json
import sqlite3

with open("catalog.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
conn= sqlite3.connect("shop.db")
cursor=conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")#поддержка внешних ключей

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE, 
    description TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY  (category_id) REFERENCES categories(id)
)
""")

for item in data:
    category = item["category"]
    
    #добавляем категорию
    cursor.execute("""
        INSERT OR IGNORE INTO categories (name, description)
        VALUES (?, ?)
    """, (category["name"], category["description"]))
    #получ айди категории
    cursor.execute("""
        SELECT id FROM categories WHERE name = ?
    """, (category["name"],))
    
    category_id = cursor.fetchone()[0]
    
    #доб товар с внешн ключом
    cursor.execute("""
        INSERT INTO products (name, price, category_id)
        VALUES (?, ?, ?)
    """, (
        item["product_name"],
        item["price"],
        category_id
    ))
    
    
conn.commit()
conn.close()
print("Gotovo")