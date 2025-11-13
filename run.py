import os
from app import create_app
from flask_migrate import upgrade

app = create_app()

# 🔄 Atualiza o banco automaticamente (em produção, pode manter assim no Render)
with app.app_context():
    try:
        upgrade()
        print("✅ Migrações aplicadas com sucesso.")
    except Exception as e:
        print(f"⚠️ Erro ao aplicar migrações: {e}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
