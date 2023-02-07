from flask import Flask



app = Flask(__name__)


#Ruta base
@app.route("/")
def home():
    return "Api"

# @app.route("/Api/v2/Contratos/<string:Id>")
# def Contratos(Id):
#     respuesta = subprocess.run(['python', r'.//scripts//login.py', Id])
#     return respuesta.stdout


# @app.route("/Api/v2/U6uExY9bdDKQmmUTwes/contratistasArconsa/<string:Id>")
# def ContratistasCentralizados(Id):
#     respuesta = subprocess.Popen([r'C:\Users\Juan Manuel Gaviria\Documents\ejecutables\Contratistas\dist\Contratistas\Contratistas.exe', Id])
#     # respuesta = subprocess.call(['python', r"C:\Users\Juan Manuel Gaviria\Documents\DesarrollosX\Contratistas.py", Id])
    
#     return "Ejecución en proceso..."


# @app.route("/Api/v2/U6uExY9bdDKQmmUTwes/CreacionProveedores/<string:Id>")
# def CreacionProveedores(Id):
#     respuesta = subprocess.Popen([r'C:\Users\Juan Manuel Gaviria\Documents\ejecutables\CreacionProveedores\dist\CreacionProveedores\CreacionProveedores.exe', Id])
#     # respuesta = subprocess.call(['python', r"C:\Users\Juan Manuel Gaviria\Documents\DesarrollosX\Contratistas.py", Id])
    
#     return "Ejecución en proceso..."


if __name__ == "__main__":
    app.run()