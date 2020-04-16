#  Code written by Jerin Rajan on 15th April 2020
#  app.py - this file contains code that handles the
# entry & exit point to our application (View)

# import Flask
from flask import Flask

# create an app instance
app = Flask(__name__)

# # at the end point /
# @app.route("/")
#
# # call method hello
# def hello_():
#     # returns "Hello world"
#     return "Hello World!"

# at the end point /<name>
@app.route("/<name>")
# call method hello_name
def hello_name(name):
    # which returns "hello + name"
    return "Hello "+ name

# on running python app.py
if __name__ == '__main__':
    # run the flask app
    # app.run()
    Schema()
    app.run(debug=True)
