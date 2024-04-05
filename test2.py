# テーブルの作成
import mysql.connector

# MySQLに接続
conn = mysql.connector.connect(
    port='3316',
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

# カーソルを取得
cursor = conn.cursor()

# テーブル作成のクエリ
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
)
"""

# テーブル作成
cursor.execute(create_table_query)

# 接続を閉じる
cursor.close()
conn.close()
