from flask import Flask,render_template,request
import pymysql
app = Flask(__name__)
@app.route('/add/user',methods=['POST','GET'])
def adduser():
    if request.method == 'GET':
        return render_template("templates/adduser.html")

    username = request.form.get('username')
    password = request.form.get('password')
    mobile = request.form.get('mobile')

    #1连接mysql
    conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="123456",charset="utf8mb4",db="userlist")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    #2执行sql语句
    sql = "insert into list1(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql,[username,password,mobile])
    conn.commit()

    #3关闭连接
    cursor.close()
    conn.close()

    return "添加成功"


@app.route('/show/user',methods=['POST','GET'])
def showuser():
    # 1连接mysql
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", charset="utf8mb4", db="userlist")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2执行sql语句
    sql = "select * from list1"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    # 3关闭连接
    cursor.close()
    conn.close()


    return render_template("templates/showuser.html", data_list=data_list)








if __name__ == '__main__':
    app.run()