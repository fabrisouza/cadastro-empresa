# Para rodar o projeto é necessario instalar os pacotes que estão em: requirements.txt
Criar o novo ambiente: python3 -m venv venv

Copiar o projeto para o diretório do ambiente, incluindo o arquivo requirements.txt ;

Ativar o ambiente: . venvbin/activate

Instalar as dependências do projeto: pip install -r requirements.txt.

# Aplicar as migrações:
$ python manage.py migrate

# Servidor:
localhost:8000/v1/swagger

localhost:8000/v1/admin
usuario: admin@admin.com
senha: admin
