
from ..database import DatabaseConnection
class Usuario:
    def __init__(self, id_usuario = None, nombre_usuario = None, clave = None, email = None, nombre = None, apellido = None, imagen_perfil = None):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.email = email
        self.nombre = nombre
        self.apellido = apellido        
        self.imagen_perfil = imagen_perfil

    @classmethod
    def create_usuario(self, usuario):
        query = "INSERT INTO TIF_grupo_14.usuarios (nombre_usuario, clave, email, nombre, apellido, imagen_perfil) VALUES (%s,%s,%s,%s,%s,%s);"
        params = (usuario.nombre_usuario, usuario.clave, usuario.email, usuario.nombre, usuario.apellido, usuario.imagen_perfil)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_usuario(self,id_usuario):
        query = "SELECT nombre_usuario, clave, email, nombre, apellido, imagen_perfil FROM TIF_Grupo_14.usuarios WHERE id_usuario = %s;"
        params = (id_usuario,)
        result = DatabaseConnection.fetch_one(query, params)
        print(type(result))
        if result is not None:
            return Usuario(
                            id_usuario = id_usuario,
                            nombre_usuario = result[0],
                            clave = result[1],
                            email = result[2],
                            nombre = result[3],
                            apellido = result[4],        
                            imagen_perfil = result[5]
                            )
        else:
            return None
        




    # @classmethod
    # def get_usuarios():
    #     query = "SELECT first_name, last_name, last_update FROM TIF_Grupo_14.actor;"
    #     result = DatabaseConnection.fetch_all(query)
    #     if result is not None:
    #         return Actor(
    #             actor_id = result[0],
    #             first_name = result[1],
    #             last_name = result[2],
    #             last_update = result[3]
    #     )
    #     else:
    #         return None