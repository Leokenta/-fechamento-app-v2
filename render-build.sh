#!/usr/bin/env bash
set -o errexit

echo "🚀 Iniciando build do Render..."

# Instalar dependências do sistema necessárias para o WeasyPrint
apt-get update && apt-get install -y \
    libcairo2 \
    pango1.0-tools \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info

echo "📦 Instalando dependências Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "⚙️ Aplicando migrações no banco de dados..."
flask db upgrade || python run.py

echo "✅ Build finalizado com sucesso!"
