# テーブルからデータを全て取り出す
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

# データ取得のクエリ
select_all_data_query = "SELECT * FROM users"

# データ取得
cursor.execute(select_all_data_query)

# 結果を取得
result = cursor.fetchall()

# 結果を表示
for row in result:
    print(row)

# 接続を閉じる
cursor.close()
conn.close()
