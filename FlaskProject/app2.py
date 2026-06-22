from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)  # This creates an instance of Flask class

@app.route('/')   # This is a decorator that tells flask which URL should trigger the function that follows.
def hello_world():  # This is the main function that runs when URL is accessed
    return "Hello, World!"   # This will be the statement that will be displayed on the browser when URL is accessed

@app.route('/home')
def home_page():
    return render_template('test.html')



if __name__ == '__main__':  
    app.run(debug = True)  # This runs the app on the local server and debug=True allows possible Python errors to appear on the web page.
