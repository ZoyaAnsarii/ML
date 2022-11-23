from flask import Flask

app=Flask(__name__)

@app.route("/user/<name>")
def home(name):
    return f"Hello Dear, {name}"

app.run(debug= True)
