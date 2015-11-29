from flask import Flask, render_template, request, session, redirect, url_for
import google, bs4, urllib2, re, names

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/home", methods = ["GET", "POST"])

#Basic home page that allows anyone to submit a question
def home():
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
    #Normalize the question's case
    q = q.upper()
    print q
    #Create rlist that holds all the urls
    rlist = []
    for r in results:
        rlist.append(r)
    #Set up a header for the URLs- Prevents sites from blocking us for using a Sript
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    #If the question is a who question
    if "WHO" in q:
        for x in rlist:
            url = urllib2.urlopen(urllib2.Request(x,headers=hdr))
            page = url.read()
            soup = bs4.BeautifulSoup(page, 'html')
            raw = soup.get_text()
            #Setup a regular expression to filter names out
            #pattern = "(([A-Z]{1})([a-z]*) ([A-Z]{1})([a-z]*))"
            #result = re.findall(pattern,raw)
            array_of_names = names.names(raw,10)
            print array_of_names
    return render_template("results.html", links = rlist)



if __name__ == "__main__":
    app.debug = True
    app.secret_key = "query"
    app.run(host='0.0.0.0', port=8000)
