'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while
'''
print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo} ->', end= ' ')
    termo += razao
    c += 1
print('FIM')