(Não finalizado)

# ⚡ Sistema de Monitoramento de Energia Hospitalar — ByteGreen

Este sistema é um projeto acadêmico que tem como objetivo monitorar, prever e otimizar o consumo de energia e a emissão de CO₂ em hospitais, com base em dados de equipamentos, setores e histórico energético. Ele permite análises por perfil (médico, chefe de setor, gerente e funcionário), e utiliza uma rede neural LSTM desenvolvida com PyTorch para previsões inteligentes de consumo.

---

## 📁 Estrutura Geral

- `bytegreen/`: App principal com os modelos, views e rotas da API
- `predictive_model/`: Diretório com o modelo LSTM (`EnergyLSTM`) e seu treinamento
- `dac/`: Configurações do projeto Django
- `pesos.pth`: Arquivo de pesos da IA, gerado pelo treinamento do LSTM

---

## ⚙️ Setup

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Criar ambiente Conda

```bash
conda create -n bytegreen python=3.10
conda activate bytegreen
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente com:

```bash
pip install \
    Django==4.2.21 \
    djangorestframework==3.16.0 \
    django-filter==25.1 \
    psycopg2-binary==2.9.10 \
    numpy==2.0.2 \
    torch==2.7.0 \
    torchvision==0.22.0 \
    pillow==11.2.1 \
    Markdown==3.8 \
    sqlparse==0.5.3
```

---

## ⚙️ Configurações no `settings.py`

Em `dac/settings.py`, adicione:

### 🔸 Definir o modelo de usuário:

```python
AUTH_USER_MODEL = 'bytegreen.Funcionario'
```

### 🔸 Registrar os apps:

```python
INSTALLED_APPS = [
    ...
    'bytegreen',
    'rest_framework',
]
```

---

## 🗄️ Banco de Dados

Você pode usar **PostgreSQL** (recomendado):

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'energy_monitoring',
        'USER': 'postgres',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Após configurar:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 Executar o servidor

```bash
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## 🤖 Treinar a IA (LSTM)

Você pode treinar o modelo com dados sintéticos para testes:

```bash
python -m dac.bytegreen.predictive_model.train_lstm
```

O modelo será salvo como `pesos.pth`. Certifique-se de que está rodando no diretório `energy_monitoring/`.

---

## 📊 Endpoints úteis

- `/api/hospitais/` – Lista/Cadastro de hospitais
- `/api/setores/` – Lista/Cadastro de setores
- `/api/funcionarios/` – Lista/Cadastro de funcionários
- `/api/equipamentos/` – Lista/Cadastro de equipamentos
- `/api/leituras_hospital/` – Registro de consumo do hospital
- `/api/predict/hospital/<id>/` – Previsão de consumo para hospital
- `/api/predict/setor/<id>/` – Previsão de consumo para setor

---

## ✅ Bibliotecas necessárias

| Biblioteca            | Versão      |
|------------------------|-------------|
| Django                | 4.2.21      |
| djangorestframework   | 3.16.0      |
| django-filter         | 25.1        |
| psycopg2-binary       | 2.9.10      |
| torch                 | 2.7.0       |
| torchvision           | 0.22.0      |
| numpy                 | 2.0.2       |
| pillow                | 11.2.1      |
| Markdown              | 3.8         |
| sqlparse              | 0.5.3       |

---

## 👤 Autores
Roberto Pereira de Freitas Neto (usuário: robertopfneto)
Mateus Zanário (usuário: mateus-zanario)

