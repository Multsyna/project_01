

#файл для тестов

#framework flask создание вэб сайтов
# conda install flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'hello, world!'