import pandas as pd
import seaborn as sns

#Dados do arquivo resultado
dados_resultado = pd.read_csv('https://github.com/alura-cursos/imersao-dados-desafio-final/blob/main/Dados/dados_resultados.csv?raw=true')
dados_resultado

#Exibe a soma total de cada coluna, exceto a primeira coluna -> drop.('id', axis=1)
#em ordem decrescente -> ascending=False
dados_resultado.drop('id', axis=1).sum().sort_values(ascending=False)

#Cria mais duas colunas contendo o número de MOA e se é ativo ou não
dados_resultado['n_moa'] = dados_resultado.drop('id', axis=1).sum(axis=1)
dados_resultado['ativo_moa'] = (dados_resultado['n_moa'] != 0)

#Merge de dados ('n_moa', 'ativo_moa') considerando como chave o 'id' (on='id')
merge_dados = pd.merge(dados, dados_resultado[['id', 'n_moa', 'ativo_moa']], on='id')
merge_dados.head()

#Exibe os valores contidos na combinação de dados, considerando os que tiveram
#tratamento com controle
merge_dados.query('tratamento == "com_controle"')['ativo_moa'].unique()

#Seleciona os valores dos 5 primeiros compostos e depois plota o boxplot
composto_principal = merge_dados['droga'].value_counts().index[:5]
plt.figure(figsize=(10, 8))
sns.boxplot(data=merge_dados.query('droga in @composto_principal'), y='g-0', x='droga', hue='ativo_moa')

#Coluna eh_controle indicando se teve um tratamento com controle ou não
merge_dados['eh_controle'] = (merge_dados['tratamento'] == 'com_controle')
merge_dados

#Criando mais três colunas para indicar qual foi o tempo exposto
merge_dados['tempo_24'] = (merge_dados['tempo'] == 24)
merge_dados['tempo_48'] = (merge_dados['tempo'] == 48)
merge_dados['tempo_72'] = (merge_dados['tempo'] == 72)
merge_dados.head()

#Analisando o composto g-3 de acordo com o tempo e dose
plt.figure(figsize=(10, 8))
sns.boxplot(data=merge_dados.query('droga in @composto_principal'), y='g-3', x='tempo', hue='dose')
#Outlier do g-3
merge_dados['g-3'].max()

#Dependendo da forma do experimento o MOA(s) é ativado ou não para o mesmo g
merge_dados[['g-3', 'tratamento', 'tempo', 'ativo_moa', 'n_moa']]

#O tipo do top 10 de compostos/drogas existentes
#Comecei pelo 2 pelo fato de ter adicionado o 'n_moa' e 'ativo_moa'
top_dados = pd.Series(dados_resultado.drop('id', axis=1).sum().sort_values(ascending=False))
top_dados = top_dados.index[2:12].str.split('_')
for i in top_dados:
  print(i[-1])