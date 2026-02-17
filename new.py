# مشکل 1: متغیر تعریف نشده استفاده می‌کنه
def add_numbers(a, b):
    return a + b + c  # 'c' تعریف نشده

# مشکل 2: SQL Injection شبیه‌سازی
import sqlite3

def get_user(username):
    conn = sqlite3.connect("db.sqlite")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return conn.execute(query).fetchall()

# مشکل 3: استاندارد کد رعایت نشده (PEP8)
def multiply(x,y):return x*y
