import pymysql

#1 连接数据库
conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="123456",charset="utf8mb4",db="unicom")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#2 发送指令（不要用字符串格式化去做SQL的拼接)
sql="update admin set mobile=%s where id=%s"
cursor.execute(sql,["123456",1,])

conn.commit()


cursor.close()
conn.close()