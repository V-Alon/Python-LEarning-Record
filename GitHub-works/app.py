from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/do/reg',methods=['GET'])
def do_reg():
    print(request.args)
    return "success!!!"
@app.route('/post/reg',methods=['POST'])
def post_reg():
    print(request.form )
    return "success123"
if __name__ == '__main__':
    app.run()