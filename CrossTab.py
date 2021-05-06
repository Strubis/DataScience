import pandas as pd
import seaborn as sns
import numpy as np

url_data = 'https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true'

dados = pd.read_csv(url_data, compression='zip')

# Proporção dos valores pela linha
pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], normalize='index')

#Normalizando pela coluna
pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], normalize='columns')

#Usando o groupby()
pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], normalize='index').groupby('dose').count()

com_droga = dados[dados['tratamento']=='com_droga'].groupby(['dose','tempo']).count()['tratamento']
com_controle = dados[dados['tratamento']=='com_controle'].groupby(['dose','tempo']).count()['tratamento']

concat = pd.concat([com_controle, com_droga], axis=1) #Juntando as duas tabelas
concat.columns = ['com_controle', 'com_droga'] #Renomeando as colunas
concat.div(concat.sum(axis=1), axis=0) #Dados normalizados

pd.crosstab([dados['tratamento'], dados['dose']], dados['tempo'], normalize='index')
pd.crosstab(dados['tratamento'], dados['tempo'], normalize='index').groupby('tratamento').mean()

#Usando a aggfunc para pegar os valores menores para o g-10
pd.crosstab(dados['dose'], dados['tempo'], values=dados['g-10'], aggfunc='min')

#Usando melt()
pd.melt(frame=dados, id_vars='g-0', value_vars=['tempo', 'dose'])

sns.scatterplot(x='g-0', y='g-8', data=dados)
sns.lmplot(data=dados, x='g-44', y='c-13', line_kws={'color': 'red'})

#Correlação G e C
corr = dados.loc[:,'g-0':'c-99'].corr()
corr_cel_gen = corr.loc['g-0':'g-50','c-0':'c-50']

mask = np.triu(np.ones_like(corr_g, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_cel_gen, cmap=cmap, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
