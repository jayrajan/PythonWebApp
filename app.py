#  Code written by Jerin Rajan on 15th April 2019
# import Flask
from flask import Flask

# create an app instance
app = Flask(__name__)

# at the end point /
@app.route("/")

# call method hello
def hello():
    # returns "Hello world"
    return "Hello World!"

# on running python app.py
if __name__ == '__main__':
    # run the flask app
    app.run()
