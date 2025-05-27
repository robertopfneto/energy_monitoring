import torch
import torch.nn as nn

class EnergyLSTM(nn.Module):
    def __init__ (self, 
                  input_size=3, #consumo kWh, custo estimado e emissão de Co2,
                  hidden_size= 64, #64 neuronios na camada oculta, para treinamentos mais precisos aumentar esse valor
                  num_layers=2, # duas camadas
                  output_size=2): # 2 valores de saída: consumo kWh e emissão CO2
        super(EnergyLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True) #criando a camada LSTM
        self.fc = nn.Linear(hidden_size,output_size) #camada fully connected - traduz a saida LSTM em uma previsão concreta

    def forward(self, x):
        out, _ = self.lstm(x) 
        last = out[: ,-1, :]
        pred = self.fc(last)
        return pred