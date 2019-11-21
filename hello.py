from flask import Flask
from flask import make_response

"""The idea of the first parameter is to give Flask an idea of what
belongs to your application.  This name is used to find resources
on the filesystem, can be used by extensions to improve debugging
information and a lot more.
"""
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response("The page %s does not exist" %page_name, 404)
    return response

if __name__ == '__main__':
    app.run(debug=True)