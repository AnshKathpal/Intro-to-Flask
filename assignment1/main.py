from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the First Flask App!"

@app.route('/greet/<username>')
def greet(username):
    return f"Hello, {username}!"

@app.route('/farewell/<username>')
def farewell(username):
    return f"Goodbye, {username}!"

if __name__ == '__main__':
    app.run(debug=True)
