##MODELO PARA REALIZAR LAS DISTINTAS CONSULTAS
##
from flask import jsonify, request
from modelo.coneccion import db_connection

#funcion que busca a un determinado usuario: reporte y   borrar
def buscar_usuario(codigo):
    try:
        conn = db_connection()
        cur = conn.cursor()
        cur.execute("""select ci,nombre,apellido,procedencia,
        to_char(fecha_nacimiento,'YYYY-MM-DD') as fecha_nacimiento FROM usuarios WHERE ci = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()
        if datos != None:
            usuario = {'ci': datos[0], 'nombre': datos[1],'apellido': datos[2], 'procedencia': datos[3],'fecha_nacimiento': datos[4]
}
            return usuario
        else:
            return None
    except Exception as ex:
            raise ex

class UsuarioModel():
    @classmethod
    def listar_usuarios(self):
        try:
            conn = db_connection()
            cur = conn.cursor()
            cur.execute("""select ci , nombre, apellido, procedencia,
             to_char(fecha_nacimiento,'YYYY-MM-DD') as fecha_nacimiento from usuarios""")
            datos = cur.fetchall()
            usuarios = []
            for fila in datos:
                usuario = {'ci': fila[0],
                       'nombre': fila[1],
                       'apellido': fila[2],
                       'procedencia': fila[3],
                       'fecha_nacimiento': fila[4],
                       }
                usuarios.append(usuario)
            conn.close()
            return jsonify({'usuarios': usuarios, 'mensaje': "Usuarios listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr", 'exito': False})

    @classmethod
    def lista_usuario(self,codigo):
        try:
            usuario = buscar_usuario(codigo)
            if usuario != None:
                return jsonify({'usuarios': usuario, 'mensaje': "usuario encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def registrar_usuario(self):
        try:
            usuario = buscar_usuario(request.json['ci'])
            if usuario != None:
                return jsonify({'mensaje': "Cedula de identidad  ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute('INSERT INTO usuarios values(%s,%s,%s,%s,%s)', (request.json['ci'], request.json['nombre'], request.json['apellido'],
                                                                            request.json['procedencia'], request.json['fecha_nacimiento']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def eliminar_usuario(self,codigo):
        try:
            usuario = buscar_usuario(codigo)
            if usuario != None:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute("DELETE FROM usuarios WHERE ci = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def actualizar_usuario(self,codigo):
        try:
            usuario = buscar_usuario(codigo)
            if usuario != None:
                conn = db_connection()
                cur = conn.cursor()
                cur.execute("""UPDATE usuarios SET nombre=%s, apellido=%s, procedencia=%s,
                fecha_nacimiento=%s  WHERE cedula_identidad=%s""",
                        (request.json['nombre'], request.json['apellido'], request.json['procedencia'], request.json['fecha_nacimiento'],  codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "Usuario actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "Usuario no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})


    @classmethod
    def estado(self):
        return jsonify({"nameSystem": "api-users", "version": "0.0.1", 
                        "developer": "Orlando Choque Ayma", "email":"orlando_choque@hotmail.com",
                        'exito': True})
        