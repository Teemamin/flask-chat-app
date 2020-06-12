import os
from flask import Flask, redirect,render_template,request,session 
# session module is to handle our session variables
from datetime import datetime

app = Flask(__name__)
app.secret_key = "somerandom123"
# to generate a session ID we need to give our app a secret key,which is just a random string of letters,num,charctrs
# in production we'd have it set as enviroment variable, like we did with the IP address
messages = []
def add_messages(username,message):
    """takes username ,message and adds it to the list above (messages)""" 
    now = datetime.now().strftime("%H:%M:%S") # The strftime() method takes a date/time object and then converts that to a string according to a given format.
    message_dict = {"timestamp" : now, "from" : username, "message" : message}
    messages.append(message_dict)



@app.route("/",methods=["GET","POST"])

def index():
    """main page instruction"""
    if request.method == "POST" :
        session["username"] = request.form["username"]
# if request is POST then we want to create a new variable in our session called username and we want it to be = to username typed from our form input
    if "username" in session:
# if username var is set redirect to the content of username session var(take the user to thr page) as routed in the belw ("/<username>")
        return redirect(session["username"])
    return render_template("index.html")


@app.route("/<username>") # remebr that wen written like so "<username>" anything btw that is considered a variable

def user(username):
    """display chat messages"""
    return render_template("chat.html",username=username,chat_messages= messages)

@app.route("/<username>/<message>")
def send_message(username,message):
    """"create new message and redirect back to chat page"""
    add_messages(username,message)
    return redirect("/" + username) # redirect will redirect us to the users personalized welcom page


app.run(host=os.getenv("IP"),port=int(os.getenv("PORT")),debug=True)
#  We're going to use os.getenv('IP') to get the IP address.
# That's an environment variable set by gitpod, also one that we set for ourselves in Heroku during deploymnt