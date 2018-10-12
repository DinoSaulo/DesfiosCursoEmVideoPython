#exercicio 938 valores para a
#link do exercicio : https://www.thehuxley.com/problem/938?locale=pt_BR

contador = int(0)
zero = 0

for i in range(5):
    num = float(input('Digite um valor:\n'))
    if 0 > num :
        contador += 1

print('Foram digitados ', end='')
print(contador, end='')
print(' numeros negativos')