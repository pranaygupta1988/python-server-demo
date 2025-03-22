from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["Get"])
def root():
  return "Welcom to the server Pranay Gupta"

@app.route("/version", methods=["Get"])
def version():
  return "<h1>1.1</h1>"

if __name__=="__main__":
  app.run(host="0.0.0.0", port=5000)
