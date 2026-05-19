import requests


def enviar_arquivo():
    #Caminho do arquivo para Upload
    caminho = 'C:/Users/cruzr/OneDrive/Documentos/Ciência de Dados/produtos_informatica.xlsx'

    #Enviar arquivo
    requisicao = requests.post(url = 'https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json ()

    print (saida_requisicao)
    url= saida_requisicao ['data'] ['downloadPage']
    print ("Arquivo enviado. Link para acesso:", url)

def receber_arquivo(file_url):
    #Receber arquivo
    requisicao = requests.get(file_url)

    #Salvar arquivo:
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
            print ("Arquivo baixado")

    else:
        print ("Erro ao baixar arquivo", requisicao.json())



#Chama Função
#enviar_arquivo()
#receber_arquivo ('https://gofile.io/d/9XCVsb')
#receber_arquivo_chave
#Para usar o token é necessária uma conta premium.


