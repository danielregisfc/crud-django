# Django REST API - Users

API simples desenvolvida em **Django + Django REST Framework** para gerenciamento de usuários.  
O projeto implementa um CRUD básico e permite integração com frontend via JSON.

---

## 🚀 Tecnologias
- Python 3
- Django
- Django REST Framework
- django-cors-headers
- SQLite (banco padrão do Django)

---

## ⚙️ Instalação e Configuração

### 1. Clonar o repositório
```bash
git clone https://github.com/danielregisfc/crud-django.git
cd crud-django

## ⚙️ Criar e ativar ambiente virtual

python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate


## ⚙️ Instalar Dependencias
pip install -r requirements.txt

## Aplicar Migrações
py manage.py makemigrations
py manage.py migrate


# Criar superusuario para acessar o Django Admin (opcional)
py manage.py createsuperuser

## Rodar servidor local
py manage.py runserver


📌 Endpoints

Admin Django: http://127.0.0.1:8000/admin
API Users (GET todos usuários): http://127.0.0.1:8000/api/users/

Obs.: demais métodos de CRUD podem ser adicionados em views.py e configurados em urls.py.


📂 Estrutura do Projeto
api_root/
│── api_rest/        # Aplicação principal
│   ├── models.py    # Definição do modelo User
│   ├── serializers.py
│   ├── views.py
│   └── ...
│── api_root/        # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── ...
requirements.txt
manage.py


✅ Próximos Passos

Adicionar rotas completas no urls.py

Implementar endpoints POST, PUT, DELETE para CRUD completo

Conectar frontend para consumir a API