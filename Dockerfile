# Use uma imagem base do Python
FROM python:3.7-slim

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie o código do projeto para o contêiner
COPY . .

# Inicie o aplicativo Flask
CMD ["python", "primos.py"]