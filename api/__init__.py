from flask import Flask
from config import Config

from .routes.usuarios_bp import usuario_bp
from .routes.servidores_bp import servidor_bp
from .routes.canales_bp import canal_bp
from .routes.chats_bp import chat_bp

def inicializar_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(usuario_bp)  ## app.register_blueprint(usuario_bp, url_prefix = '/usuario') #MODIFICAR EL ACTOR_BP
                                      ## AGREGAR LOS DEMAS BLUEPRINTS (uno por c/clase)
    app.register_blueprint(servidor_bp)
    app.register_blueprint(canal_bp)
    app.register_blueprint(chat_bp)

    return app