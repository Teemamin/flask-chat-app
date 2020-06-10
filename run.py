import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []
def add_messages(username,message):
    """takes username ,message and adds it to the list above (messages)""" 
    messages.append("{} : {}".format(username,message))

def get_all_messages():
    """get all messages and separetes them with a br"""
    return "<br>".join(messages)

@app.route("/")

def index():
    """main page instruction"""
    return "to send a message use /USERNAME/MESSAGE"

@app.route("/<username>") # remebr that wen written like so "<username>" anything btw that is considered a variable

def user(username):
    """display chat messages"""
    return "<h1>welcome {0} </h1> {1}" .format(username, get_all_messages()) #note the numb in the{} is optional index ref,u can leave the{}empty

@app.route("/<username>/<message>")
def send_message(username,message):
    """"create new message and redirect back to chat page"""
    add_messages(username,message)
    return redirect("/" + username) # redirect will redirect us to the users personalized welcom page


app.run(host=os.getenv("IP"),port=int(os.getenv("PORT")),debug=True)
#  We're going to use os.getenv('IP') to get the IP address.
# That's an environment variable set by gitpod, also one that we set for ourselves in Heroku during deploymnt