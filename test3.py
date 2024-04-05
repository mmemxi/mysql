# テーブルにデータを挿入
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

# データ挿入のクエリ
insert_data_query = """
INSERT INTO users (username, email) VALUES (%s, %s)
"""

# データ挿入
user_data = ("Inoue", "inoue@example.com")
cursor.execute(insert_data_query, user_data)

# 変更を確定
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()
