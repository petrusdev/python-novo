'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
'''
nascimento = int(input('Data nascimento em ano: '))
data_nascimento = 2023 - nascimento

if data_nascimento < 18:
    print(f'Você ainda vai se alistar no serviço militar.')
elif data_nascimento == 18:
    print('Está na hora do seu alistamento.')
else:
    print('Já passou o prazo do seu alistamento. Regularize com o serviço militar.')