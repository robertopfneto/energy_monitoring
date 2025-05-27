from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
import numpy as np
import torch
from bytegreen.models import LeituraSetor as leitura, Previsao, Setor
from bytegreen.predictive_model.model_lstm import EnergyLSTM

class PredictAPIView(APIView):
    def get(self, request, setor_id):
        dias =  int(request.GET.get('dias',30))

        try:
            setor = Setor.objects.get(id=setor_id)
        except Setor.DoesNotExist:
            return Response({'erro' : 'Setor não encontrado'}, 
                            status=404)
        
        leituras = (leitura.objetcs.order_by('-data_leitura')[:dias])

        if len(leituras) < dias:
            return Response({'erro' : 'Leituras insuficientes para previsão'},
                            status=400)
        
        leituras = list(leituras)[::-1] #invertendo a lista, ordenando do mais antigo pro mais recente

        dados = np.array([
            [l.consumo_kwh, l.custo_estimado, l.co2_estimado] for l in leituras
        ], dtype=np.float32)

        tensor = torch.tensor(dados).unsqueeze(0) #1, dias, 3

        #carregando modelo treinado

        model = EnergyLSTM()
        model.load_state_dict(torch.load('bytegreen/predictive_model/pesos.pth', map_location='gpu')) #trocar aq se quiser rodar cm cpu
        model.eval()

        with torch.no_grad():
            pred = model(tensor).numpy()[0]
        
        # Atribuo os valores preditos as variaveis
        consumo_previo = float(pred[0]) #primeiro elemento de predicao eh o consumo
        co2_previo = float(pred[1]) # o segundo o co2
        data_prevista = timezone.now().date + timedelta(days=1)

        #Criando o registro deles no banco
        previsao =  Previsao.objets.create(
            setor=setor,
            data_prevista=data_prevista,
            consumo_previsto=consumo_previo,
            co2_previsto=co2_previo
        )

        #retornando json
        return Response({
            'setor' :  setor.nome,
            'data_prevista' : str(data_prevista),
            'consumo_previsto' : consumo_previo,
            'co2_previsto' : co2_previo,
            'salvo_em' : previsao.id
        })