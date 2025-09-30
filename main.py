# main.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return "Hello, World! The CI/CD Pipeline Worked! Version 66.0"
=======
    return "Hello, DevOps Students! Version 3.0"
>>>>>>> df6316e6a98da1c805a53fccd616404e6eb36af1
