from flask import Flask # importing flask 
from flask_cors import CORS 

# to setup our pyton backend API, we are first setting
# up a normal flask app. We will have a route called members
# and this route will basiczally return a JSON array of members
# then once we set this up, we will connect the frontend to the 
# Backend and then get that JSON array of members and then
# we will display that array of members on to the screen. 


# creating the flask app instance: 
app = Flask(__name__)
CORS(app) # allow all origins for develooment purposes)

# Members API route: 

@app.route("/members")
def members(): 
    return {"members": ["Member1", "Member2", "Member3"]}



if __name__ == "__main__": 
    app.run(debug =True, host="0.0.0.0", port=8000)