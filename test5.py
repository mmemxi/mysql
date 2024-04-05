# テーブルを更新する
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

# データ更新のクエリ
update_data_query = "UPDATE users SET email = %s WHERE username = %s"

# データ更新
new_email = "Tanaka.new@example.com"
cursor.execute(update_data_query, (new_email, "Tanaka"))

# 変更を確定
conn.commit()


# 接続を閉じる
cursor.close()
conn.close()
