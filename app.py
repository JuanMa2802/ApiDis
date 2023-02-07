from flask import Flask
import subprocess


app = Flask(__name__)


#Ruta base
@app.route("/")
def home():
    return "<h1>Api Lambda <span style='color:red;'>v2.3</span></h1>"

@app.route("/Api/v3/Contratistas/<string:Id>")
def Contratistas(Id):
    respuesta = subprocess.run(["python", "./scripts/login.py", Id], capture_output=True)
    return respuesta.stdout

if __name__ == "__main__":
    app.run()