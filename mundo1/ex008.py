#Exercício Python 8: Escreva um programa que leia um valor em metros e o 
# exiba convertido em centímetros e milímetros.
medida_metros = float(input("Digite uma medida em metros: "))
medida_centimetros = medida_metros * 100
medida_milimetros = medida_metros * 1000    
print(f"A medida digitada foi {medida_metros} metros. \nSua equivalente em centímetros é {medida_centimetros} centímetros. \nSua equivalente em milímetros é {medida_milimetros} milímetros.")