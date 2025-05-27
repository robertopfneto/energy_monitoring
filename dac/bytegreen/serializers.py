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
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        user = Funcionario.objects.create_user(**validated_data)
        return user

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

class LeituraEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeituraEquipamento
        fields = '__all__'

class LeituraSetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeituraSetor
        fields = '__all__'

class LeituraHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeituraHospital
        fields = '__all__'

class PrevisaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Previsao
        fields = '__all__'