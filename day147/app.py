from flask import Flask, render_template

app = Flask(__name__)

@app.route('/show')
def index():
    users=['123','456','789','000']





    return render_template('index.html' ,title='陕西西安',data_list=users)

if __name__ == '__main__':
    app.run()