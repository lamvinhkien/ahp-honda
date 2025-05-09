from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Đăng ký các Blueprints
    from app.routes.main import main_bp
    from app.routes.chiphi import chiphi_bp
    from app.routes.tknl import tknl_bp
    from app.routes.dongco import dongco_bp
    from app.routes.thietke import thietke_bp
    from app.routes.tienich import tienich_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(chiphi_bp, url_prefix="/chi-phi")
    app.register_blueprint(tknl_bp, url_prefix="/tknl")
    app.register_blueprint(dongco_bp, url_prefix="/dong-co")
    app.register_blueprint(thietke_bp, url_prefix="/thiet-ke")
    app.register_blueprint(tienich_bp, url_prefix="/tien-ich")

    return app
