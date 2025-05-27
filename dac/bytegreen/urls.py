from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

router.register(r'hospitais', HospitalViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'chefes', ChefeSetorViewSet)
router.register(r'gerentes', GerenteViewSet)
router.register(r'setores', SetorViewSet)
router.register(r'equipamentos', EquipamentoViewSet)
router.register(r'leituras_equipamento', HospitalViewSet)
router.register(r'leituras_setor', HospitalViewSet)
router.register(r'leituras_hospital', HospitalViewSet)
router.register(r'hospitais', HospitalViewSet)


urlpatterns = [
    path ('',router.urls)
]