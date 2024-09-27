import pandas as pd
import plotly.express as px

# Função para carregar e processar os dados
def carregar_dados(caminho_arquivo):
    dados = pd.read_csv(caminho_arquivo)
    dados['Data'] = pd.to_datetime(dados['Data'])
    dados['Lucro'] = dados['Receita'] - dados['Despesa']
    return dados

# Função para gerar gráficos interativos
def gerar_graficos(dados):
    # Gráfico de receitas e despesas por mês
    fig1 = px.line(dados, x='Data', y=['Receita', 'Despesa'], title='Receitas e Despesas Mensais')
    fig1.show()

    # Gráfico de lucro por mês
    fig2 = px.bar(dados, x='Data', y='Lucro', title='Lucro Mensal')
    fig2.show()

# Caminho do arquivo CSV (você pode mudar para o caminho do seu arquivo)
caminho_arquivo = 'dados_financeiros.csv'

# Carregar e processar os dados
dados_financeiros = carregar_dados(caminho_arquivo)

# Gerar os gráficos
gerar_graficos(dados_financeiros)
