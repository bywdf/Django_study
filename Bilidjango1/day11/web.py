from flask import Flask,render_template

app = Flask(__name__)

@app.route('/show/info')
def index():
    return render_template('index.html')

@app.route('/get/news')
def get_news():
    return render_template('get_news.html')

@app.route('/goods/list')
def goods_list():
    return render_template('goods_list.html')

@app.route('/user/list')
def user_listt():
    return render_template('user_list.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()