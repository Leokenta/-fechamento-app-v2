from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Corrige URLs de conexão antigas (necessário em alguns casos com Render)
    database_url = os.getenv('DATABASE_URL', 'sqlite:///fechamentos.db')
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-secreta')

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa e registra blueprints
    from app.routes import main
    app.register_blueprint(main)

    return app
