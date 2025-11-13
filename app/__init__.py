from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # ⚙️ Configurações principais
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 
        'sqlite:///fechamentos.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-secreta')

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # 🔄 Aplica migrações automaticamente no Render
    with app.app_context():
        try:
            upgrade()
            print("✅ Migrações aplicadas com sucesso.")
        except Exception as e:
            print(f"⚠️ Erro ao aplicar migrações: {e}")

    # Importa e registra rotas
    from app.routes import main
    app.register_blueprint(main)

    return app
