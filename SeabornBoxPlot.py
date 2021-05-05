import seaborn as sns
import matplotlib.pyplot as plt

#Renomea toda a coluna 'droga' para 'composto'
mapa = {'droga':'composto'}
dados.rename(columns=mapa, inplace=True)

#Pega os cinco primeiros elementos, somente o nome
cod_compostos = dados['composto'].value_counts().index[0:5]

#Ordenando crescentemente os valores
composto_order = cod_compostos.sort_values(ascending=True)

#Plotando o gráfico
plt.figure(figsize=(8, 6))
sns.set()
ax = sns.countplot(x='composto', hue='composto', order=composto_order, 
                   data=dados.query('composto in @cod_compostos'))
ax.set_title('Compostos', fontsize=15, fontweight='bold')
ax.set_xlabel('Nome do Composto', fontsize=10)
ax.set_ylabel('Quantidade', fontsize=10)

#Formatando o topo do gráfico
plt.show()

#Descrevendo os dados dos compostos
dados.loc[:, 'g-0':'g-771'].describe().T

#Descrevendo os dados (mean) dos compostos com um histograma
ax = dados.loc[:, 'c-0':'c-99'].describe().T['mean'].hist(bins=20)

ax.set_title('Compostos C-0 até C-99', fontsize=15, fontweigth='bold')
plt.show()

#Gráfico boxplot
#sns.boxplot(x='g-0', data=dados)

ax = sns.boxplot(x='tempo', y='g-4', data=dados, linewidth=1.5)
ax.set_title('Boxplot')
plt.show()