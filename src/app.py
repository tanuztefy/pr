from flask import Flask
from flask_cors import CORS

from config import config
from modelo.UsuarioModel import UsuarioModel

app = Flask(__name__)

# HABILITAR EL INTERCAMBIO DE RECUROS  DE ORIGEN CRUZADOS para las peticiones
# GET, POST, DELETE, PUT en especial
#CORS(app, resources={r"/usuarios/*": {"origins": "http://http://localhost"}})
CORS(app, resources={r"/usuarios/*": {"origins": "https://proyecto-modulo3.onrender.com"}})


# RUTA PARA PETICION GET
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    x= UsuarioModel.listar_usuarios()
    return x

# RUTA paar peticiones GET  usuario especifico
@app.route('/usuarios/:<codigo>', methods=['GET'])
def lista_usuari(codigo):
    x= UsuarioModel.lista_usuario(codigo)
    return x

# RUTA PARA PETICION POST insertar usuario
@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    x= UsuarioModel.registrar_usuario()
    return x

# RUTA PARA PETICION DELETE borrar  usuario
@app.route('/usuarios/:<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    x= UsuarioModel.eliminar_usuario(codigo)
    return x

# RUTA PARA PETICION PUT actualiza usuario
@app.route('/usuarios/:<codigo>', methods=['PUT'])
def actulalizar_usuario(codigo):
    x= UsuarioModel.actualizar_usuario(codigo)
    return x

# RUTA PARA PETICION GET informacio de la API
@app.route('/estado', methods=['GET'])
def estado():
    x= UsuarioModel.estado()
    return x


#capturar error de pagina
def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0',debug=True)
