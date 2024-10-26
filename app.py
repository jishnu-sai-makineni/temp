from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(str(list((request.cookies.values()))))
    return 'Hello, World! flag: ' + str(list((request.cookies.values())))