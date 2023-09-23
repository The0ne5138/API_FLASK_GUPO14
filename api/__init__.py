from flask import Flask
from config import Config

from .routes.usuarios_bp import usuario_bp  ## MODIFICAR EL ACTOR_BP

def inicializar_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(usuario_bp)  ## app.register_blueprint(usuario_bp, url_prefix = '/usuario') #MODIFICAR EL ACTOR_BP
                                      ## AGREGAR LOS DEMAS BLUEPRINTS (uno por c/clase)

    return app