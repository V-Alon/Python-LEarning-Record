from flask import Flask, render_template

app=Flask(__name__,template_folder='templates')
# app=Flask(__name__,template_folder='templates')
# 在template_folder=“”内写页面代码的路径


#创建网址/show/info 和函数index的对应关系
#在浏览器上访问/show/info 网站自动执行 index
@app.route('/show/info')
def index():
    # return "Hello World!"
    return render_template('index.html')


if __name__ == '__main__':
    app.run()