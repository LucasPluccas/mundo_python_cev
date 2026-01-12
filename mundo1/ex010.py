#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
# e mostre quantos dólares ela pode comprar.
dinheiro = float(input("Digite quanto dinheiro você tem na carteira: "))
dolar = dinheiro / 3.27
print(f"Com R$ {dinheiro} você pode comprar US$ {dolar:.2f}.")