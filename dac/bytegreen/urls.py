from rest_framework import routers
from django.urls import path, include

from bytegreen.predictive_model.predict_view import PredictAPIView, PredictHospitalAPIView
from .views import *

router = routers.DefaultRouter()

router.register(r'hospitais', HospitalViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'chefes', ChefeSetorViewSet)
router.register(r'gerentes', GerenteViewSet)
router.register(r'setores', SetorViewSet)
router.register(r'equipamentos', EquipamentoViewSet)
router.register(r'leituras_equipamento', LeituraEquipamentoViewSet)
router.register(r'leituras_setor', LeituraSetorViewSet)
router.register(r'leituras_hospital', LeituraHospitalViewSet)

urlpatterns = [
    path('', include(router.urls)), 
     path('predict/setor/<int:setor_id>/', PredictAPIView.as_view(), name='predict-setor'),
    path('predict/hospital/<int:hospital_id>/', PredictHospitalAPIView.as_view(), name='predict-hospital'),
   
]
