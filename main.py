from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! The CI/CD Pipeline Worked! Version 66.0"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Cloud Run sets $PORT
    app.run(host="0.0.0.0", port=port)

