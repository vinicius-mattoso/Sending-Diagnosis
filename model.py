# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df_diabetes=pd.read_csv('Base-diabetes.csv');
# Colocando o nome das colunas do Dados
df_diabetes.columns=['Num. Gravid','Conc. Glicose','Pressao Diast.','Dobra Cut.','Insulina','IMC','Historic','Idade','Result']

#carregando as bibliotecas necessárias para dividir os dados e normalizar os mesmos

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

normaliza = MinMaxScaler() #objeto para a normalização

#transforma os dados em array
entradas= df_diabetes.iloc[:, :-1].values  #dados de entrada
saida= df_diabetes.iloc[:, 8].values  # saídas ou target

entradas_normalizadas=normaliza.fit_transform(entradas)

X_train, X_test, y_train, y_test =train_test_split(entradas_normalizadas, saida, test_size=0.30,random_state=42)

#definição da biblioteca
from sklearn.neural_network import MLPClassifier
#Algoritmo Rede MLP
clf_mlp = MLPClassifier(solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(5, 5), random_state=1,max_iter=1000)
#Realiza o treinamento do classificador
clf_mlp= clf_mlp.fit(X_train,y_train)

# Saving model to disk
pickle.dump(clf_mlp, open('model.pkl','wb'))

'''
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6]]))
'''