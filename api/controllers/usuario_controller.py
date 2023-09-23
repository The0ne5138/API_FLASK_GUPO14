
##  ESTO ES de actores, hay q modificarlo para USUARIOS

from ..model.usuarios import Usuario
from flask import request
from flask import jsonify


class UsuarioController:
    @classmethod
    def create_usuario(self):
        
        usuario = Usuario(
        nombre_usuario = request.args.get('nombre_usuario', ''),
        clave = request.args.get('clave', ''),
        email = request.args.get('email', ''),
        nombre = request.args.get('nombre', ''),
        apellido = request.args.get('apellido', ''),
        imagen_perfil = request.args.get('imagen_perfil', '')
        )

        Usuario.create_usuario(usuario)
        return {'message': 'usuario creado con exito'}, 200
    
    @classmethod
    def get_usuario(cls, id_usuario):
        usuario_instance = Usuario.get_usuario(id_usuario)

        if usuario_instance:
            response_data = {"id": usuario_instance.id_usuario,
                             "nombre_usuario": usuario_instance.nombre_usuario,
                             "clave": usuario_instance.clave,
                             "email" : usuario_instance.email,
                             "nombre" : usuario_instance.nombre,
                             "apellido" : usuario_instance.apellido,
                             "imagen_perfil" : usuario_instance.imagen_perfil
                            }
            
            return jsonify(response_data), 200
        
        else:
    
            return {"msg": "No se encontró el usuario"}, 404
    




    
    # @classmethod
    # def get_actors(self):
    #     results = Actor.get_actors
    #     actors = []
    #     for result in results:
    #         actors.append({
    #             "id": result[0],
    #             "nombre": result[1],
    #             "apellido": result[2],
    #             "ultima_actualizacion": result[3]
    #     })
    #     return actors, 200
        

    # @classmethod
    # def update_actor(self, actor):
    # #Implementación del método
    #     pass

    # @classmethod
    # def delete_actor(self, actor):
    # #Implementación del método
    #     pass

    # @classmethod
    # def delete_actors(self):
    # #Implementación del método
    #     pass