## TODO ESTO ES de actores, hay q modificarlo para USUARIOS

from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController



usuario_bp = Blueprint('usuario_bp',__name__)



usuario_bp.route('/usuarios/<int:id_usuario>', methods = ['GET'])(UsuarioController.get_usuario)
usuario_bp.route('/usuarios', methods = ['POST'])(UsuarioController.create_usuario)
#Usuario_bp.route('/usuarios', methods = ['GET'])(UsuarioController.get_usuarios)
#Usuario_bp.route('/usuarios/<int:id_usuario>', methods = ['PUT'])(UsuarioController.update_Usuario)
#Usuario_bp.route('/usuarios', methods = ['DELETE'])(UsuarioController.delete_usuarios)
#Usuario_bp.route('/usuarios/<int:id_usuario>', methods = ['DELETE'])(UsuarioController.delete_usuario)
