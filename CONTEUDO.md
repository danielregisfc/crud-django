Criar ambiente virtual
python -m venv venv
Ativar ambiente virtual
.\venv\Scripts\activate
Ativar Interpretador Python

Criar o requirements.txt
django
djangorestframework
django-cors-headers


Instalar os requisitos
pip install -r requirements.txt

Conferir instalações
pip list

Pode utilizar o freeza para fixar as versões no requirements.txt
pip freeze > requirements.txt

No nosso exemplo ficou assim:
asgiref==3.9.1
Django==5.2.5
django-cors-headers==4.7.0
djangorestframework==3.16.1
sqlparse==0.5.3
tzdata==2025.2

Agora vamos iniciar o projeto django, rode o comando (api_root é o nome da aplicação, nome do diretório que será criado)
django-admin startproject api_root . 

Criar uma nova aplicação dentro do projeto.
py manage.py startapp api_rest

Em settings.py da api_root em INSTALLED APPS acrescentar rest_framework e corsheaders
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

e adiciona a middleware do corsheaders
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

Adicionar tbm 

CORS_ALLOW_ORIGINS = [
    'http://localhost:8000'
]

Criar Models
Arquivo models.py já existe na estrutura do projeto django

from django.db import models

# Create your models here.
class User(models.Model):
    user_nickname = models.CharField(max_length=50, primary_key=True, default='')
    user_name = models.CharField(max_length=100, default='')
    user_email = models.CharField(max_length=100, default='@')
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | email: {self.user_email}'

Criar o modelo no nosso banco de dados. 
py manage.py makemigrations


Verifica se tem a extensão SQLlite viewer
Depois py manage.py migrate

Em admin.py registrar o modelo Users
from django.contrib import admin

from .models import User

# Register your models here.
admin.site.register(User)

Em seguida criar um superusuário
py manage.py createsuperuser
admin
- 
admin
admin

Depois executar o servidor
py manage.py runserver

Acessar
http://127.0.0.1:8000/admin
Logar e criar um novo User


Criar serializers.py dentro de api_rest
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#Devolver para o front só o email (exemplo)

class UserMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_email']


Vamos agora para o views.py para criar o CRUD da aplicação

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

Agora iremos adicionar as rotas
Em urls.py do api_root

