from flask import Flask

app = Flask(__name__)



@app.route('/')

def hello_world():

    return 'Hello, World!'

def more_info():

    return "Pleased to meet you!"
    