# pode-se usar aspas simples '' ou duplas "", usa-se mais as simples
# toda mensagem tem que estar entre aspas
mensagem = 'Olá, Mundo!'
print(mensagem)
print('Olá, Mundo!')
print(type(mensagem))  # str = string (texto)
numero = 10
print(numero)
print(10)
print(type(numero))  # int = inteiro (número sem vírgula)

# diferenças
print(7+4)
print('7' + '4')  # concatenação ou seja, juntas os textos
nome = 'Lucas'
sobrenome = 'Pereira'
saudacao = 'Olá, seja bem vindo!'
print(saudacao + ' ' + nome + ' ' + sobrenome)#textos concatenados

# + ou , para concatenar, depende do contexto
'''print('ola' + 5)  # erro, não pode concatenar texto com número'''
print('ola', 5)

#variaveis
nome = 'Lucas' # = em python significa atribuição de valor, nome recebe o valor Lucas
idade = 32 #a variavel idade recebe o valor 32
peso = 70.7
print( nome, idade, peso)

#função INPUT é usada para receber dados do usuário
# por padrão o input sempre recebe como texto (string), por isso é preciso converter
# para outros tipos de dados, como int (inteiro) ou float (número com vírgula)
nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
peso = float(input('Qual é o seu peso? '))

#DESAFIO: crie um script que pergunte o nome do usuario e mostre uma mensagem de boas vindas
#Ex: Olá, seja bem vindo Lucas!
nome1 = input('Qual é o seu nome? ')
mensagem1 = 'Olá, seja bem vindo '
print(mensagem1 + nome1 + '!')

#DESAFIO 2: crie um script que pergunte o ano de nascimento do usuario e mostre a idade dele formatada
dia = int(input('Em que dia você nasceu? '))
mes = int(input('Em que mês você nasceu? '))
ano = int(input('Em que ano você nasceu? '))
mensagem3 = f'Você nasceu em {dia}/{mes}/{ano}'
print(mensagem3)