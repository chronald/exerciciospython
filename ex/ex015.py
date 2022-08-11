n1 = int(input('Quantos dias alugados?'))
n2 = float(input('Quantos KM rodados?'))
r1 = n1 * 60
r2 = n2 * 0.15
r3 = r1 + r2

print(f'O Total a pagar é R${r3}')
