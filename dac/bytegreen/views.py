from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = HospitalSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class ChefeSetorViewSet(viewsets.ModelViewSet):
    queryset = ChefeSetor.objects.all()
    serializer_class = ChefeSetorSerializer

class GerenteViewSet(viewsets.ModelViewSet):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class LeituraEquipamento(models.Model):
    queryset = LeituraEquipamento.objects.all()
    serializer_class = LeituraEquipamentoSerializer

class LeituraSetor(models.Model):
    queryset = LeituraSetor.objects.all()
    serializer_class = LeituraSetorSerializer

class LeituraHospital(models.Model):
    queryset = LeituraHospital.objects.all()
    serializer_class = LeituraHospitalSerializer