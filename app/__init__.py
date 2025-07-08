from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.routes_auth import auth_bp
    from app.routes_admin import admin_bp
    from app.routes_questions import qst_bp
    from app.routes_stats import stats_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(qst_bp, url_prefix='/questions')
    app.register_blueprint(stats_bp, url_prefix='/stats')

    return app
