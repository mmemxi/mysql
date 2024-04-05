# テーブルからレコードを削除する
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

# データ削除のクエリ
delete_data_query = "DELETE FROM users WHERE username = %s;"

# データ削除
cursor.execute(delete_data_query, ["Inoue"])

# 変更を確定
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()
