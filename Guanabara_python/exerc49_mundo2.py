'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
pa = int(input('Digite o primeiro termo PA: '))
razao = int(input('Digite a razão do PA: '))

print('Os 10 primeiros termos da PA são:')
for c in range(10):
    termo = pa + c * razao
    print(termo, '->', end= ' ')
print('Acabou')
