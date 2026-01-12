#operadores aritméticos
# +, -, *, /, //, **, %
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
exponenciacao = 2 ** 3
divisao_inteira = 10 // 3
modulo = 10 % 3

#ordem de precedência
#1º - ()
#2º - **
#3º - *, /, //, %
#4º - +, -
resultado = 10 + 5 * 2 ** 2 - (3 + 1)
print(resultado)

#se houver mais de um operador com a mesma precedência, a avaliação 
# é feita da esquerda para a direita
resultado2 = 20 / 5 * 2
print(resultado2)

'''
abs(x)	valor absoluto	abs(-7)	7
round(x, n)	arredonda	round(3.14159, 2)	3.14
pow(x, y)	potência	pow(2, 5)	32
sum(iterável)	soma elementos	sum([1,2,3])	6
divmod(a, b)	quociente + resto	divmod(7,2)	(3,1)
max(...)	maior valor	max(3,7,2)	7
min(...)	menor valor	min(3,7,2)	2
'''