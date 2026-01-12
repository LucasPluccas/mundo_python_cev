#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na
# tela o seu sucessor e seu antecessor.
n = int(input('Digite um número inteiro: '))
ant = n - 1
suc = n + 1
print(f'O número digitado foi {n}. \nSeu antecessor é {ant} \nSeu sucessor é {suc}.')