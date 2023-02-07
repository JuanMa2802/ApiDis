from flask import Flask



app = Flask(__name__)


#Ruta base
@app.route("/")
def home():
    return "<h1 style='color:red;'>Api</h1>"

@app.route("/Api/v3/Contratistas")
def Contratistas():
    return "Contratistas"

if __name__ == "__main__":
    app.run()