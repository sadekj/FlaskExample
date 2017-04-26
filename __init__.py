from flask import Flask, render_template, request
import db
app = Flask(__name__)
x=5
x="5"

@app.route("/")
def hello():
	x = db.search("Jane Doe")
	return render_template("index.html",laith=x)

@app.route("/presearch")
def presearch():
	return render_template("search.html")

@app.route("/search", methods=['POST', 'GET'])
def search():
	keyword = request.args.get('keyword')
	x = db.search()
	return render_template("index.html", laith=x)

@app.route("/presignup")
def presignup():
	return render_template("signup.html")
	
if __name__ == "__main__":
	app.run()