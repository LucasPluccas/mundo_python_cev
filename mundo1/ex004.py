#Exercício Python 4: 
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

variavel = input('Digite algo: ')
print(f'Você digitou: {variavel}')
print(f'O tipo primitivo é: {type(variavel)}')#testa o tipo de dado inserido
print(f'Só tem espaços? {variavel.isspace()}')#testa se só tem espaços
print(f'É um número? {variavel.isnumeric()}')#testa se é um número
print(f'É alfabético? {variavel.isalpha()}')#testa se é uma letra
print(f'É alfanumérico? {variavel.isalnum()}')#testa se é letra ou número
print(f'Está em maiúsculas? {variavel.isupper()}')#testa se está em maiúsculas
print(f'Está em minúsculas? {variavel.islower()}')#testa se está em minúsculas
print(f'Está capitalizada? {variavel.istitle()}')#testa se está capitalizada (maiuscula com minuscula)

