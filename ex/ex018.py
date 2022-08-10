from math import cos, sin, tan, radians
ang = float(input('Digite o ângulo que você deseja:'))
sen = sin(radians(ang))
tan = tan(radians(ang))
cos = cos(radians(ang))

print(f' O angulo de {ang:.2f} tem o SENO de {sen:.2f}')
print(f' O angulo de {ang:.2f} tem o COSSENO de {cos:.2f}')
print(f' O angulo de {ang:.2f} tem a TANGENTE de {tan:.2f}')

