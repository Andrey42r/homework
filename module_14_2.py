import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance TEXT NOT NULL
)
''')
#
# cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# for i in range(1, 11):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                   (f"User{i}", f"example{i}@gmail.com", f"{i*10}", 1000))
#
cursor.execute("UPDATE Users SET balance = 500 WHERE id IN (SELECT id FROM Users WHERE id % 2 == 1)")

cursor.execute("DELETE FROM Users WHERE id IN (SELECT id FROM Users WHERE id % 3 ==1)")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age <> 60")
result = cursor.fetchall()

for row in result:
    print(f"Имя: {row[0]}| Почта: {row[1]}| Возраст: {row[2]}| Баланс: {row[3]}")

cursor.execute("SELECT COUNT(*) FROM Users WHERE age > ?", (10,))

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT SUM(balance) FROM Users")
total1 = cursor.fetchone()[0]
print(total1)

cursor.execute("SELECT COUNT(*) FROM Users")
total2 = cursor.fetchone()[0]
print(total1/total2)

#
# cursor.execute("SELECT SUM(age) FROM Users")
# total1 = cursor.fetchone()[0]
# cursor.execute("SELECT COUNT(*) FROM Users")
# total2 = cursor.fetchone()[0]
# print(total1, total1/total2)
#
# cursor.execute("SELECT MAX(age) FROM Users")
# avg_age = cursor.fetchone()[0]
# print(avg_age)
connection.commit()
connection.close()
