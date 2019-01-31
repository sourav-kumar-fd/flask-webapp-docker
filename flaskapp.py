from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
	return "Welcome To Python World"
 
@app.route("/docker")
def hello():
	return "Hello Docker!"
 
@app.route("/members")
def members():
	return "Members of docker learners from mumshad sir are realy excited."
 
@app.route("/members/<string:name>/")
def getMember(name):
	return "MY name is :" + name
 
if __name__ == "__main__":
	app.run()