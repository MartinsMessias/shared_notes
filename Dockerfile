# Defina a imagem base que vai ser usada na construção
FROM python:3.8

# Variáveis de ambiente
# Python não gerar .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Python não armazenar logs em buffer
ENV PYTHONUNBUFFERED 1

# Define o nosso diretório de trabalho
WORKDIR /code

# O ponto(.) é o nosso WORKDIR
# Copia o requirements.txt para o WORKDIR
COPY requirements.txt .
# Executa a instalação das dependencias
RUN pip install -r requirements.txt

# Copia tudo do local atual para a pasta do WORKDIR
COPY . .