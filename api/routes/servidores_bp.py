from flask import Blueprint
from ..controllers.servidor_controller import ServidorController

servidor_bp = Blueprint('servidor_bp',__name__)

servidor_bp.route('/servidores/<int:id_servidor>', methods = ['GET'])(ServidorController.get_servidor)        # Solicita los datos de el servidor.
servidor_bp.route('/servidores', methods = ['POST'])(ServidorController.create_servidor)                      # Crea un nuevo servidor
servidor_bp.route('/servidores/<int:id_servidor>', methods = ['PUT'])(ServidorController.update_servidor)     # Edita(modifica, actualiza) un servidor. SI HAY Q HACERLA
servidor_bp.route('/servidores/<int:id_servidor>', methods = ['DELETE'])(ServidorController.delete_servidor)  # Elimina un servidor SERIA EN PERFIL ELIMINAR CUENTA. 
                                                                                                              # Warning: Hay q modificar la BD p/q si se elimina a un servidor que tiene
                                                                                                              # servidores (y seguramente canales, chats tambien) creados da ERROR