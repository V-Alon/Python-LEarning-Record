import pymysql

while True:
    username=input("username:")
    if username=="":
        break
    password=input("password:")
    mobile=input("mobile:")




#1 连接数据库
    conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="123456",charset="utf8mb4",db="unicom")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

#2 发送指令（不要用字符串格式化去做SQL的拼接)
    sql="insert into admin(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql,[username,password,mobile])



# sql="insert into admin(username,password,mobile) values(%(n1)s,%(n2)s,%(n3)s)"
# cursor.execute(sql,{"n1":"陕西","n2":"sssxxx","n3":"sssxxx"})



    conn.commit()

# 3关闭
    cursor.close()
    conn.close()