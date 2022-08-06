n1 = float(input('Digite uma distancia em Metros'))

km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000

print(f'A média de {n1} corresponde a: ')
print(f'{km:.2f}km')
print(f'{hm:.2f}hm')
print(f'{dam:.1f}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
