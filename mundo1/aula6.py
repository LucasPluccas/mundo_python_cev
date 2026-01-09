#tipos primitivos em Python
#exemplo:
n1 = int(input('Digite um número: '))#convertendo a entrada para inteiro
n2 = int(input('Digite outro número: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale {s}')#saiu soma pois os numeros foram convertidos para int
print(type(n1))#mostra o tipo da variavel n1
print(type(n2))#mostra o tipo da variavel n2
print(type(s))#mostra o tipo da variavel s

#tipos
#int - números inteiros
#float - números reais (com vírgula)
#bool - valores lógicos (True ou False)
#str - textos (string)
#exemplos:
n3 = 7 #inteiro
n4 = 3.5#ponto flutuante ou numero real (sempre com ponto, nunca com virgula)
n5 = True #ou False - somente os 2 valores
n6 = 'Olá, Mundo!' #string - texto entre aspas simples ou duplas
n7 = '7' #string - mesmo que pareça um número, está entre aspas, então é texto
print(type(n3))