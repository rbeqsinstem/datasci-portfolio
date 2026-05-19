#Estudo de Data Frame
import pandas as pd

#Lista: Uma coleção ordenada de elementos que podem ser de qualquer tipo.
lista_nomes = ['Ana', 'Pedro', 'Maria']
print ('Lista de nomes:\n', lista_nomes)
print ('Primeiro elemento da lista:\n', lista_nomes[0])

#Dicionário: Estrutura composta de pares chave-valor.
dicionario_pessoa = {
    'nome' :'Ana',
    'idade' :25,
    'cidade' : 'Rio de Janeiro',
}
print ('Dicionário de uma pessoa:\n', dicionario_pessoa)
print ('Atributo do Dicionário:\n', dicionario_pessoa.get ('nome'))

#Lista de dicionários: Estrutura de dados que combina lista e dicionários.
dados = [
    {'nome' :'Ana','idade' :25,'cidade' : 'Rio de Janeiro'},
    {'nome' :'Pedro','idade' :20,'cidade' : 'São Paulo'},
    {'nome' :'Maria','idade':17,'cidade' : 'Minas Gerais'}

]

#DataFrame: Estrutura de dados bidimensional
df = pd.DataFrame(dados)
print ('Data frame:\n', df)

#Selecionar Coluna
print (df['nome'])

#Selecionar mais de uma coluna
print (df[['nome','idade']])

#Selecionar linhas pelo índice
print ('Primeira linha:\n', df.iloc[0])

#Adicionar uma nova coluna
df['estado'] = ['RJ', 'SP', 'MG']

#Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'Ana',
    'idade': 25,
    'cidade': 'Rio de Janeiro',
    'estado': 'RJ'
}
print('DataFrame Atual\n',df)

#Removendo uma coluna
df.drop(labels=['cidade'], axis=1, inplace=True)

#Filtrando pessoa por estado
filtro_estado = df ['estado']=='SP'
print('Filtro:\n', filtro_estado)

#Salvando um data_frame em arquivo CSV
df.to_csv(path_or_buf='dados.csv', index=False)

#Lendo um arquivo CSV em um data frame
df_lido = pd.read_csv ('dados.csv')
print ('\n Leitura do CSV \n', df_lido)



