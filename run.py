from app import create_app
from flask_migrate import upgrade

app = create_app()

# Atualiza o banco automaticamente (cuidado: em produção, prefira migrar manualmente)
with app.app_context():
    try:
        upgrade()
    except Exception:
        # evita que erro de migração impeça a aplicação de subir; logue se quiser
        pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
