from flask import Flask, render_template
app = Flask(__name__)

#创建的网址/show/info和函数index的对应关系
#在浏览器上访问/show/info，网站自动执行index
@app.route('/show/info')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()