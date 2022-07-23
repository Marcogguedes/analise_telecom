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

# Tratando Valores Vázios (colunas e linhas)
# Deletando Colunas Vázias
df_telecom = df_telecom.dropna(how="all", axis=1)

# Deletando Linhas Vázias
df_telecom = df_telecom.dropna(how="any", axis=0)
df_telecom.info()

Etapa 4: Análise Exploratória

# Investigando os cancelamentos dos clientes
df_telecom["Churn"].value_counts()

# Calculando o percentual da coluna
df_telecom["Churn"].value_counts(normalize=True)

# Transformando em percentual
df_telecom["Churn"].value_counts(normalize=True).map("{:.1%}".format)

Etapa 5: Análise Completa

# Realizando a compração de todas as colunas da tabela com a coluna de cancelamento
# Criando um gráfico de histograma
grafico = px.histogram(df_telecom, x="Dependentes", color="Churn", color_discrete_sequence=["green", "orange"])

# Exibir o gráfico de histograma
grafico.show()

# Criando gráficos trabalhando com o FOR
for coluna in df_telecom.columns:
    grafico = px.histogram(df_telecom, x=coluna, color="Churn", color_discrete_sequence=["green", "orange"])
    grafico.show()


Conclusões e Ações

**Tipo de Contrato do Cliente**

- Clientes com o tipo de contrato mensal **têm maiores chances** de realizar o cancelamento<br>
  **Ação sugerida:** Trabalhar promoções para que estes clientes possam ir para o tipo de contrato anual.


**Clientes que não são casados**

- Famílias maiores tendem a um menor cancelamento do que famílias menores<br>
  **Ação sugerida:** Realizar promoções para a pessoa obter uma linha adcional de telefone.


**Clientes novos**

- Novos clientes têm maiores chances de realizar o cancelamento<br>
- A primeira experiência do cliente com a operadora pode está sendo ruim<br>
- A empresa pode está captando clientes com baixa qualificação<br>
  **Ação sugerida:** A empresa pode criar um programa de incentivo para o cliente ficar mas tempo.


**Quantidade Serviços**

- O Cliente com o maior número de serviços tem menor probablidade de realizar o cancelamento<br>
  **Ação sugerida:** A empresa pode oferecer bônus com mais serviço para o cliente.


**Seviço de fibra**

- Há algum problema no serviço de fibra da empresa que está levando aos clientes cancelarem<br>
  **Ação sugerida:** A empresa deve melhorar o markting em relação ao serviço.  