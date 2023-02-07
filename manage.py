import os 
import subprocess
from os import system
from flask import Flask, request, abort, render_template
from subprocess import Popen
from pathlib import Path
from getpass import getuser


aplicacion = Flask(__name__, template_folder="templates")

directoriobase = Path(__file__).resolve().parent.parent.parent
usuario = getuser()
directorioScript = "usuario"



con = os.path.join(directoriobase)


# print(con)

#Ruta base
@aplicacion.route("/")
def home():
    return render_template("index.html")

@aplicacion.route("/Api/v2/Contratos/<string:Id>")
def Contratos(Id):
    respuesta = subprocess.run(['python', r'.//scripts//login.py', Id])
    return respuesta.stdout


@aplicacion.route("/Api/v2/U6uExY9bdDKQmmUTwes/contratistasArconsa/<string:Id>")
def ContratistasCentralizados(Id):
    respuesta = subprocess.Popen([r'C:\Users\Juan Manuel Gaviria\Documents\ejecutables\Contratistas\dist\Contratistas\Contratistas.exe', Id])
    # respuesta = subprocess.call(['python', r"C:\Users\Juan Manuel Gaviria\Documents\DesarrollosX\Contratistas.py", Id])
    
    return "Ejecución en proceso..."


@aplicacion.route("/Api/v2/U6uExY9bdDKQmmUTwes/CreacionProveedores/<string:Id>")
def CreacionProveedores(Id):
    respuesta = subprocess.Popen([r'C:\Users\Juan Manuel Gaviria\Documents\ejecutables\CreacionProveedores\dist\CreacionProveedores\CreacionProveedores.exe', Id])
    # respuesta = subprocess.call(['python', r"C:\Users\Juan Manuel Gaviria\Documents\DesarrollosX\Contratistas.py", Id])
    
    return "Ejecución en proceso..."


if __name__ == "__main__":
    aplicacion.run(debug=True, port=9500)