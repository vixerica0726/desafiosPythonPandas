# importar biblioteca pydataset para carregar dataset iris
from pydataset import data

# carregar o dataset iris usando uma função 
dataFrame = data('iris')

# printar na tela o dataset
print("Dataset Iris: ")
print(dataFrame)

# Informar o tipo de dados retornados 
tipoDado = type(dataFrame)
print("Tipos de dados retornados pela função:", tipoDado)

# Informar a quantidade de linhas e colunas 
linhas, colunas = dataFrame.shape # retorna as dimenções 
print("Quantidades de linhas, colunas", dataFrame.shape)

