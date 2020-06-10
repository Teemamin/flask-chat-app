import os
from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "<h1> hello from flask func</h1>"

app.run(host=os.getenv("IP"),port=int(os.getenv("PORT")),debug=True)
#  We're going to use os.getenv('IP') to get the IP address.
# That's an environment variable set by gitpod, also one that we set for ourselves in Heroku during deploymnt