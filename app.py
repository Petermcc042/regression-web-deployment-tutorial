from flask import Flask, render_template, request
import simplemodel as sm

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        hrs = request.form["hours"]
        markpred = sm.marksprediction(hrs)
    else:
        markpred = 0
    return render_template("index.html", mymark = markpred)
 
if __name__ == "__main__":
    app.run(debug=True)