from django.db import models

# Modelo de Usuário (usuário, nome, email e idade)
class User(models.Model):
    user_nickname = models.CharField(max_length=50, primary_key=True, default='')
    user_name = models.CharField(max_length=100, default='')
    user_email = models.CharField(max_length=100, default='@')
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | email: {self.user_email}'
    