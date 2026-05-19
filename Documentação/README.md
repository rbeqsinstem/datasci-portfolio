# Configurações e boas práticas com IDE
## Projeto de teste

### Código fora da função (Menos robusto):
Inicia-se definindo a variável `nome`, que irá receber o valor digitado pelo usuário por meio da função `input ()`: 

- `nome = input ("Digite o seu nome:")`

Em seguida, o conteúdo armazenado na variável é exibido na tela utilizando a função `print()`:

- `print(nome)`

## Porque é considerado "menos robusto" ?

- O código executa diretamente no "fluxo principal" do programa.
- Não organiza a lógica em módulos condicionais/funcionais, dificultando a reutilização.


### Função para exibir nome:

Em um código mais robusto, podemos ver a utilização de funções para dividir os módulos de funcionalidade, como, por exemplo, a função`exibir_nome()`: 

- Exemplo: `def exibir_nome ():`
- Dentro da função, é definida a funcionalidade responsável por solicitar o nome do usuário, por meio do comando `input():`
- `nome = input ("Digite o seu nome:")`
- Para que o código seja executado corretamente, a função deve conter o comando responsável por exibir o valor da variável, como neste caso:
`print (nome)`.
- Em seguida, se define o módulo principal do programa utilizando a estrutura `main`, garantindo que a função seja executada apenas quando o arquivo for executado diretamente.

- `if __name__ == '__main__':`
- `exibir_nome()`

