import pandas as pd

#%% Definindo variável para arquivo CSV
df = pandas.read_csv ("C:\Users\cruzr\OneDrive\Documentos\Cursos Livres\Profissão - Cientista de Dados - EBAC\Dados\clientes.csv")
print (df)

#%%
#Verificar os primeiros registros
print (df.head().to_string())