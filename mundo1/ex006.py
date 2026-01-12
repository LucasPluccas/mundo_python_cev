#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, 
# triplo e raiz quadrada.
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz_quadrada = n ** (1/2)
print(f'O número digitado foi {n}. Seu dobro é {dobro}. Seu triplo é {triplo}. Sua raiz quadrada é {raiz_quadrada:.2f}.')