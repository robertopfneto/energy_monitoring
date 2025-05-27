

import torch
import numpy as np

from bytegreen.predictive_model.model_lstm import EnergyLSTM

#criando um vetor com 100 amostras, 30 dias e 3 features(kWh, custo e co2)
# cada X[i] é uma sequencia de 30 dias com 3 colunas por dia
X = np.random.rand(100, 30, 3) #inputs
y = np.random.rand(100,2)#outputs

# Criando os tensores
tensor_x = torch.tensor(X.astype(np.float32))
tensor_y = torch.tensor(y.astype(np.float32))

# Importando modelo criado
model = EnergyLSTM()

criter = torch.nn.MSELoss() # Adotando Mean Squared Error -> padrao pra regressao
optimizer = torch.optim.Adam(model.parameters(), lr=0.001) #adotando o ADAM para optimizador com um learnin rate de 1x10^-3

for epoch in range(300):
    outputs = model(tensor_x) #outputs é o dado de entrada aplicado ao modelo
    loss = criter(outputs,tensor_y) #calculo o MSE
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    #acompanhar o treinamento
    if (epoch+1) % 50 == 0:
        print(f'Época {epoch+1}, Loss: {loss.item():.4f}')

torch.save(model.state_dict(), 'bytegreen/predictive_model/pesos.pth')