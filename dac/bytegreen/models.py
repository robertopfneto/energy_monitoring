from django.db import models
from django.contrib.auth.models import AbstractUser

class Funcionario(AbstractUser):
    email = models.EmailField(unique=True)
    setor = models.ForeignKey('Setor', on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=20, choices=[
        ('médico','Médico'),
        ('chefe','Chefe de Setor'),
        ('gerente', 'Gerente'),
        ('funcionario', 'Funcionario')
    ])

    data_cadastro = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Medico(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    crm = models.CharField(max_length=20)

class ChefeSetor(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    setor_gerenciado = models.OneToOneField('Setor', on_delete=models.CASCADE)

class Gerente(models.Model):
    funcionario = models.OneToOneField(Funcionario, on_delete=models.CASCADE)
    hospital = models.OneToOneField('Hospital', on_delete=models.CASCADE)

class Hospital(models.Model):
    nome = models.CharField(max_length=100)
    cnpg = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

class Setor(models.Model):
    nome = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    
class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo_energia = models.CharField(max_length=50)
    fator_consumo = models.FloatField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

class LeituraEquipamento(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_leitura = models.DateTimeField()
    consumo_kwh = models.FloatField()
    consumo_co2 = models.FloatField()
    
class LeituraSetor(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    data_leitura = models.DateTimeField()
    consumo_kwh = models.FloatField()
    consumo_co2 = models.FloatField()
    

class LeituraHospital(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    data_leitura = models.DateTimeField()
    consumo_kwh = models.FloatField()
    consumo_co2 = models.FloatField()

class Previsao(models.Model):
    setor = models.ForeignKey('Setor', on_delete=models.SET_NULL, null=True, blank=True)
    hospital = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True, blank=True)
    data_previsao = models.DateTimeField()
    consumo_previsto = models.FloatField()
    co2_previsto = models.FloatField()