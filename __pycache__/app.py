from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello Shubham, how are you"

@app.route("/home")
def welcometohome():
    return "2ndd time learning for welcoming at home page"
    
import Controller.User_Controller as User_Controller

