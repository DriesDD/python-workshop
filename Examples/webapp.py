"""
Flask is a microframework. It can serve web applications with minimal code compared to well known frameworks like react, vue, angular, ruby on rails, or django (django is a python framework as well).
However, if you want to do more advanced things you will need to create new folders, files, routes and install new modules.

Exercises:
1. Show different text on different pages of the same site.
2. When you go to localhost:5000/myname, the code should say 'Hello Myname!' and it should work for arbitrary names.
3. Use templates to serve html on your flask site
4. Use the same HTML header on every page but a different main HTML section

"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello BeCode!"

if __name__ == "__main__":
    app.run(debug=True)