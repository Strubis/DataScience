import pandas as pd
import matplotlib.pyplot as plt

url_data = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'

#Lê um arquivo csv zipado a partir de uma url
dados = pd.read_csv(url_data, compression='zip')

dados.head() #Primeiras 5 linhas dos dados
dados.tail() #Últimas 5 linhas dos dados

dados.shape() #Quantidade de linhas e colunas dos dados

#Plotando o gráfico (tempo) formatado pela biblioteca matplotlib
graf = dados['tempo'].value_counts().plot.bar()
graf.set_title('Experiment Time')
graf.set_xlabel('Hours')
graf.set_ylabel('Value')

#Quantidade de drogas testadas
dados['droga'].value_counts().shape

#Substituindo o hífen para usar na query: 'g-0' -> 'g0'
dados_formatados = dados['g-0'].replace("-", "")
dados.query('@dados_formatados > 0')