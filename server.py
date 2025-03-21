from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["Get"])
def root():
  return "Welcom to the server"

@app.route("/version", methods=["Get"])
def version():
  return "1.0"

if __name__=="__main__":
  app.run(host="0.0.0.0", port=5000)
