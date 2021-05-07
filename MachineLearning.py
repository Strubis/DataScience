#Importando as bibliotecas responsáveis pelo Machine Learning
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#Selecionando do nosso conjunto de dados tudo o que for float
x = merge_dados.select_dtypes('float64')
#Selecionando o nosso target, o resultado de acordo com os nossos dados
y = merge_dados['ativo_moa']

#Pega os dados que são treinados, usando 20%
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, stratify=y)

#Treinando nossa máquina de acordo com os nossos dados, usando Regressão Logística
modelo_rlog = LogisticRegression(max_iter=1000)
modelo_rlog.fit(x_treino, y_treino)
modelo_rlog.score(x_teste, y_teste)

#Modelo para avaliar a frequência que ocorreu os valores, usando um método mais simples
modelo_dummy = DummyClassifier('most_frequent')
modelo_dummy.fit(x_treino, y_treino)
previsao_dummy = modelo_dummy.predict(x_teste)
accuracy_score(y_teste, previsao_dummy)

#Árvore de Decisão, com um certo tamanho de nós
teste=[]
treino=[]
for i in range(1, 15):
   modelo_arv = DecisionTreeClassifier(max_depth=i)
   modelo_arv.fit(x_treino, y_treino)
   teste.append(modelo_arv.score(x_teste, y_teste))
   treino.append(modelo_arv.score(x_treino, y_treino))
   
#Plotando um gráfico para exemplificar o resultado
sns.lineplot(x=range(1, 15), y=teste, label='teste')
sns.lineplot(x=range(1, 15), y=treino, label='treino')

x = merge_dados.drop(['id', 'n_moa', 'ativo_moa', 'droga'], axis=1)
x = pd.get_dummies(x, columns=['tratamento', 'tempo', 'dose'])
y = merge_dados['ativo_moa']
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, stratify=y, random_state=376)
modelo_ranForest = RandomForestClassifier()
modelo_ranForest.fit(x_treino, y_treino)
modelo_ranForest.score(x_teste, y_teste)

#Desafio 01 - Utilizando o método dos vizinhos
from sklearn.neighbors import KNeighborsClassifier

num_neigh = 3

neigh_fun = KNeighborsClassifier(num_neigh)
neigh_fun.fit(x_treino, y_treino)
neigh_fun.score(x_teste, y_teste)

#Desafio 04 - Testando outros problemas
x = merge_dados.loc[:, 'g-0':'c-99']
y = merge_dados['tempo'].map({24:0, 48:1, 72:2})

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.2, stratify=y, random_state=376)

modelo_rlog2 = LogisticRegression(solver='newton-cg')
modelo_rlog2.fit(x_treino, y_treino)
modelo_rlog2.score(x_teste, y_teste)

#Desafio 05 - Testes com a droga mais utilizada
merge_dados['droga'].value_counts() #Para achar os compostos que mais aparecem

#As duas drogas possuem um valor muito parecido, por isso é mais fácil de
#chegar num resultado favorável
dt_temp = merge_dados.query('droga in ["8b87a7a83", "5628cb3ee"]')

x = dt_temp.loc[:, 'g-0':'g-12']
y = dt_temp['droga'].map({'8b87a7a83':0, '5628cb3ee':1})
sns.countplot(x=y)
y.value_counts(normalize=True) #Porcentagem muito parecida

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.2, stratify=y,random_state=376)

#Aqui modificamos o x. Se colocamos mais colunas de g e c o algoritmo consegue 
#100% de taxa de acerto. A diferença da ativação entre as duas drogas é muito 
#grande e fácil do algoritmo identificar.
modelo_rlog3 = LogisticRegression()
modelo_rlog3.fit(x_treino, y_treino)
modelo_rlog3.score(x_teste, y_teste)