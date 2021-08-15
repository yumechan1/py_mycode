from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return "你好 flask!"

app.run()