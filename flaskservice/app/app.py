from flask import Flask,jsonify
from . import send_socket, send_msg

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def local_socket():
    for i in range(10):
        print(f'message {i}')
        send_socket("process1","/xtest",10,"test","hello socket")
    return jsonify({"msg":"api_data"})

@app.route("/aws_test")
def aws_socket():
    for i in range(10):
        print(f'message {i}')
        send_msg("process1","/xtest",'HRpLedbAIAMCL8Q=',"hello socket")
    return jsonify({"msg":"api_data"})


if __name__ != '__main__':
  app.run()