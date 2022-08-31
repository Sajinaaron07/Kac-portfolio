from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template ("index.html")




if __name__ == "__main__":
    port = int(os.getenv('PORT'))
    app.run(Debug = False,port = int(os.getenv('PORT'))s)
