from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/search4", methods=['post'])
def do_search() -> str:
    return f"表单填入结果为：{request.form['user_name']}, {request.form['age']}"


@app.route("/entry")
def entry_page() -> "html":
    return render_template('entry.html',the_title="普通标题")

app.run(debug=True)