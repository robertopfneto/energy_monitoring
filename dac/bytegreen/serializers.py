from rest_framework import serializers
from .models import *

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
    
class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields =  '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ChefeSetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefeSetor
        fields = '__all__'

class GerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = '__all__'

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'

class LeituraEquipamentoSerializer(models.Model):
    class Meta:
        models = LeituraEquipamento
        fields = '__all__'

class LeituraSetorSerializer(models.Model):
    class Meta:
        models = LeituraEquipamento
        fields = '__all__'

class LeituraHospitalSerializer(models.Model):
    class Meta:
        models = LeituraEquipamento
        fields = '__all__'

class PrevisaoSerializer(models.Model):
    class Meta:
        models = Previsao
        fields = '__all__'