from flask import Flask,request,redirect
app = Flask(__name__)
@app.get("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/a")
def hello_world2():
    return "Hello" + request.args.get("a")
app.run(host="python",port=8080,debug=True)
