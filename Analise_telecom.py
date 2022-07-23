Análise de Dados

Case:

Uma empresa de Telecom que tem diversos clientes e presta serviços dos mais variados, entre os principais: internet e telefonia.<br>

Analisando o histórico dos clientes dos últimos anos, observou-se que a empresa está com CHURN de mais de 26% dos clientes.<br>

Isso representa uma perda de milhões para a empresa.<br>

Qual ação a empresa precisa fazer para resolver o problema?

obs.Essa é uma base de dados pública extraída do Kaggle e traduzida para o português.<br>
Link:https://www.kaggle.com/radmirzosimov/telecom-users-dataset


Etapa 1: Importar a base de dados

# Importando Bibliotecas
import pandas as pd
import plotly.express as px

Etapa 2: Visualizar a base de dados

# Carregando o dataset
df_telecom = pd.read_csv("telecom_users.csv")
df_telecom.head()

# Visualizando a forma do dataset
df_telecom.shape

Etapa 3: Tratamento da base de dados

# Removendo colunas inúteis
df_telecom = df_telecom.drop("Unnamed: 0", axis=1)
df_telecom.head()

# Pegando as informações do dataset
df_telecom.info()

# Tratando colunas com valores reconhecido de forma incorretas
df_telecom["TotalGasto"] = pd.to_numeric(df_telecom["TotalGasto"], errors="coerce")

# o COERCE diz para eliminar os erros
df_telecom.info()