# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos da aplicação
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Execute o script de inicialização do banco de dados e inicie o servidor Flask
CMD ["sh", "-c", "python init_db.py && flask run --host=0.0.0.0"]
