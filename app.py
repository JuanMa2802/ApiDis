from flask import Flask



app = Flask(__name__)


#Ruta base
@app.route("/")
def home():
    return "Api"


if __name__ == "__main__":
    app.run()