# Função para exibir nome:
def exibir_nome ():
    nome = input ("Digite seu nome: ") # Receber nome.
    print (nome)

# Módulo Principal:
if __name__ == '__main__':
    exibir_nome()

#Código fora da função (Menos robusto):
nome = input ("Digite seu nome: ")  # Receber nome.
print (nome)