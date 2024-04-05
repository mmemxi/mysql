import mysql.connector

# MySQLに接続
conn = mysql.connector.connect(
    port='3316',
    host="localhost",
    user="root",
    password="root"
)

# カーソルを取得
cursor = conn.cursor()

# データベース作成
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# 接続を閉じる
cursor.close()
conn.close()
