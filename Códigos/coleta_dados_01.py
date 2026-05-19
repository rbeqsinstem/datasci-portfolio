# https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/41984-em-2023-expectativa-de-vida-chega-aos-76-4-anos-e-supera-patamar-pre-pandemia

import bs4
import pandas
import requests

dados = 'https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/41984-em-2023-expectativa-de-vida-chega-aos-76-4-anos-e-supera-patamar-pre-pandemia'

print ('Request:  ')
response = requests.get(dados)
print (response.text[:600])

print ('BeautifulSoup: ')
soup = bs4.BeautifulSoup(response.text, 'html.parser')
print (soup.prettify()[:1000])

print ('Pandas: ')
url_dados = pandas.read_html(dados)
print (url_dados [0].head(10))
