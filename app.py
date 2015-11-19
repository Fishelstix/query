from flask import Flask, render_template, request, session, redirect, url_for
import google, bs4, urllib2, re

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods = ["GET", "POST"])

#Basic home page that allows anyone to submit a question
def home():
    """ 
	Takes a question submitted by the user and redirects to results.
	Returns a 405 error, method not allowed when trying to submit a question. (Fix?)
    """
    if request.method== "GET":
	return render_template("home.html")
    else: 
        session["question"] = request.form['question']
        return redirect(url_for("results"))

@app.route("/results")

#Shows the results from the search
def results():
    """
	Pulls 10 links somewhat related to the question. Does not search through the links
	and find relevant ones. Returns the urls in a list "rlist" and sends to the html.
    """
    q= session["question"]
    results = google.search(q,num=10,start=0,stop=10)
    rlist = []
    for r in results:
        rlist.append(r)
    return render_template("results.html", links = rlist)



if __name__ == "__main__":
    app.debug = True
    app.secret_key = "query"
    app.run(host='0.0.0.0', port=8000)
