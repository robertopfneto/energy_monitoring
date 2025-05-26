from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Funcionario(AbstractUser):
    email = models.EmailField(unique=True)
    setor = models.ForeignKey('Setor', on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=20, choises=[
        ('médico','Médico'),
        ('chefe','Chefe de Setor'),
        ('gerente', 'Gerente'),
        ('funcionario', 'Funcionario')
    ])

    data_cadastro = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Medico(models.Model):
    funcionario = models.OneToField(Funcionario)