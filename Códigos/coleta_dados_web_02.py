# Coleta de dados Web
# Importar bibliotecas necessárias


import requests
from bs4 import BeautifulSoup

# Definir variáveis
url = 'https://python.org.br/web/'
requisicoes = requests.get(url)
extracao = BeautifulSoup(requisicoes.content, 'html.parser')

# Exibir o texto retirando os espaços vazios.
#print(extracao.text.strip())

#Filtrar a exibição pela tag.
#for linha_in_texto in extracao.find_all('h2'):
    #titulo = linha_in_texto.text.strip()
    #print("Titulo: ", titulo)

#Definindo variáveis:
#contar_titulos = 0
#contar_paragrafos = 0

#Contar ocorrências de 'h2' e 'p'
#for linha_texto in extracao.find_all ('h2'):
    #if linha_texto.name == 'h2':
        #contar_titulos +=1
    #elif linha_texto.name == 'p':
        #contar_paragrafos +=1

#Exibir contagem de h2 e p
#print ("Total de títulos:" , contar_titulos )
#print ("Total de paragrafos:", contar_paragrafos )

#Exibir conteúdo do h2 e p
#for linha_texto in extracao.find_all (['h2', 'p']):
#   if linha_texto.name == 'h2':
#        titulo = linha_texto.text.strip()
#        print("Título:\n", titulo)
#        elif linha_texto.name == 'p':
#         paragrafo = linha_texto.text.strip()
#         print("Paragrafo:\n", paragrafo)

#Exibir tag aninhada
for titulo in extracao.find_all('h2'):
    print ("\n Título: ", titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all ('a', href=True):
            print ('Texto: ', a.text.strip(), " | URL : ", a['href'])
