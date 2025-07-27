from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 1 接收用户通过post形式发来的数据
        username = request.form.get('username')
        password = request.form.get('password')
        gender = request.form.get('gender')
        hobby_list = request.form.get('hobby')
        city = request.form.get('city')
        skills_list = request.form.get('skills')
        details = request.form.get('details')
        print(username, password, gender, hobby_list, city, skills_list, details)

        # 2将结果返回给用户
        return "注册成功！！！"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return "登录成功"

@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()