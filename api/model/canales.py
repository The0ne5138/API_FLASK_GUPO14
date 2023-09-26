
from ..database import DatabaseConnection

class Canal:
    def __init__(self, id_canal = None, nombreCanal = None, descripcion = None, id_user_creo_canal = None, id_server= None):
        self.id_canal = id_canal
        self.nombreCanal = nombreCanal
        self.descripcion = descripcion
        self.id_user_creo_canal = id_user_creo_canal
        self.id_server= id_server


    @classmethod
    def create_canal(self, canal):
        query = "INSERT INTO DB_TIF_grupo_14.canales (nombreCanal, descripcion, id_user_creo_canal, id_server) VALUES (%s,%s,%s,%s);"
        params = (canal.nombreCanal, canal.descripcion, canal.id_user_creo_canal, canal.id_server)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_canal(self,id_canal):
        query = "SELECT nombreCanal, descripcion, id_user_creo_canal, id_server FROM DB_TIF_Grupo_14.canales WHERE id_canal = %s;"
        params = (id_canal,)
        result = DatabaseConnection.fetch_one(query, params)
        
        if result is not None:
            return Canal(
                            id_canal = id_canal,
                            nombreCanal = result[0],
                            descripcion = result[1],
                            id_user_creo_canal = result[2],
                            id_server= result[3]
                        )
        else:
            return None

    @classmethod
    def update_canal(self, canal):
        query = """
                UPDATE canales
                SET nombreCanal = %s, descripcion = %s, id_user_creo_canal = %s, id_server = %s
                WHERE id_canal = %s
                """
        
        params = (canal.nombreCanal, canal.descripcion, canal.id_user_creo_canal, canal.id_server, canal.id_canal)
        DatabaseConnection.execute_query(query, params)
        return None


    @classmethod
    def delete_canal(self,id_canal):  # Warning: Hay q modificar la BD p/q si se elimina a un canal que tiene servidores (y seguramente canales, chats tambien) creados da ERROR
        query = "DELETE FROM canales WHERE id_canal = %s"
        params = (id_canal,)
        DatabaseConnection.execute_query(query, params)
        return {'message': 'Canal borrado con exito'},204











