from flask import Blueprint
from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('canal_bp',__name__)

canal_bp.route('/canales/<int:id_canal>', methods = ['GET'])(CanalController.get_canal)         # Solicita los datos de el canal.
canal_bp.route('/canales', methods = ['POST'])(CanalController.create_canal)                      # Crea un nuevo canal
canal_bp.route('/canales/<int:id_canal>', methods = ['PUT'])(CanalController.update_canal)     # Edita(modifica, actualiza) un canal. SI HAY Q HACERLA
canal_bp.route('/canales/<int:id_canal>', methods = ['DELETE'])(CanalController.delete_canal)  # Elimina un canal SERIA EN PERFIL ELIMINAR CUENTA. # Warning: Hay q modificar la BD p/q si se elimina a un canal que tiene servidores (y seguramente canales, chats tambien) creados da ERROR
