from flask import Flask, render_template, Markup, json, session, redirect, url_for, request
import random
import json
from difflib import get_close_matches

## Website rendering ##

app=Flask(__name__)

data = json.load(open("cdn.json"))

def translate(word):
    if word in data:
        return str(data[word])[2:-2]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean '%s'? " % get_close_matches(word, data.keys(), cutoff=0.6)[0]
    else:
        return "We don't have that word, please check spelling or submit it!"




@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
            if request.form['action'] == 'Submit':
                searchterm = request.form.get("userword")
                word = searchterm.lower()
                return render_template("home.html", initialword = word+":", result = translate(word))
            
            elif request.form['action'] == 'Random':
                word, definition = random.choice(list(data.items()))
                return render_template("home.html", initialword = word+":", result = definition[0]) 
    else:
        return render_template("home.html")


        

@app.route('/about/')
def about():
    return render_template("about.html")



@app.route('/submit/')
def submit():
    return render_template("submit.html")

# if __name__=="__main__":
#     app.run(debug=True)




    