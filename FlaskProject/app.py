from flask import Flask, redirect, url_for   # This imports the flask,redirect and url_for class from Flask Library

app = Flask(__name__)  # This creates an instance of Flask class

@app.route('/')   # This is a decorator that tells flask which URL should trigger the function that follows.
def hello_world():  # This is the main function that runs when URL is accessed
    return "Hello, World!"   # This will be the statement that will be displayed on the browser when URL is accessed

@app.route('/home')
def home_page():
    return "This is the Home Page."

@app.route('/<name>')
def user(name):
    return f"Hello {name}, How are You?"
    
@app.route('/home/trial')
def trial_page():
    return redirect(url_for("home_page"))  # This function will redirect home/trial to home_page 

if __name__ == '__main__':  
    app.run(debug = True)  # This runs the app on the local server and debug=True allows possible Python errors to appear on the web page.
