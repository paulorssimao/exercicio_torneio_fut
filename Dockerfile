# Usar imagem base do Python
FROM python:3.10-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos para o container
COPY . .

# Comando de execução
CMD ["python", "main.py"]
