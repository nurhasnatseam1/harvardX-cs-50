from flask import Flask,render_template


app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/form",methods=["GET","POST"])
def form():
    return render_template("form.html")
if __name__=="__main__":
     app.run(port=3333) 