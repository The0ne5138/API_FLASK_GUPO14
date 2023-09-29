
from ..database import DatabaseConnection

class Servidor:
    def __init__(self, id_Servidor = None, nombreServidor = None, descripcion = None):
        self.id_Servidor = id_Servidor
        self.nombreServidor = nombreServidor
        self.descripcion = descripcion

    @classmethod
    def create_servidor(self, servidor):
        query = "INSERT INTO TIF_grupo_14.servidores (nombreServidor, descripcion) VALUES (%s,%s);"
        params = (servidor.nombreServidor, servidor.descripcion)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_servidor(self,id_servidor):
        query = "SELECT nombreServidor, descripcion FROM TIF_Grupo_14.servidores WHERE id_Servidor = %s;"
        params = (id_servidor,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Servidor(
                            id_servidor = id_servidor,
                            nombreServidor = result[0],
                            descripcion = result[1]
                            )
        else:
            return None
      
    @classmethod
    def update_servidor(self, servidor):
        query = """
                UPDATE servidores
                SET nombreServidor = %s, descripcion = %s
                WHERE id_servidor = %s
                """
        params = (servidor.nombreServidor, servidor.descripcion, servidor.id_Servidor)
        DatabaseConnection.execute_query(query, params)
        return None


    @classmethod
    def delete_servidor(self,id_servidor):  # Warning: Hay q modificar la BD p/q si se elimina a un servidor que tiene usuarios (y seguramente canales, chats tambien) creados da ERROR
        query = "DELETE FROM servidores WHERE id_servidor = %s"
        params = (id_servidor,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Servidor borrado con exito'},204
    
    @classmethod
    def get_servidoresPorUsuario(cls, id_usuario):
        query = """SELECT servidores.*FROM DB_TIF_Grupo_14.servidores INNER JOIN DB_TIF_Grupo_14.usuario_Servidor
                   ON servidores.id_Servidor = usuario_Servidor.id_server WHERE usuario_Servidor.id_user = 5;"""
        params = (id_usuario,)
        result = DatabaseConnection.fetch_all(query, params)
        listaServidores =[]
        if result is not None:
            for server in result:
                listaServidores.append(
                Servidor(
                actor_id = server[0],
                first_name = server[1],
                last_name = server[2],
                last_update = server[3]
                ))
                
            return listaServidores
        else:
            return None
