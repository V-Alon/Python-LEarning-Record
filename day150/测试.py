import pymysql





conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", charset="utf8mb4", db="userlist")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2执行sql语句
sql = "select * from list1"
cursor.execute(sql)
data_list = cursor.fetchall()

    # 3关闭连接
cursor.close()
conn.close()

print(data_list)