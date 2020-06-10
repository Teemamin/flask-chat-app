import os
from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    """main page instruction"""
    return "to send a message use /USERNAME/MESSAGE"

@app.route("/<username>") # remebr that wen written like so "<username>" anything btw that is considered a variable

def user(username):
    return "Hi " + username

@app.route("/<username>/<message>")
def send_message(username,message):
    return "{0}:  {1}" .format(username, message)


app.run(host=os.getenv("IP"),port=int(os.getenv("PORT")),debug=True)
#  We're going to use os.getenv('IP') to get the IP address.
# That's an environment variable set by gitpod, also one that we set for ourselves in Heroku during deploymnt