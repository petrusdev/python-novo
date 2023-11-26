'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quandl ele disser que quer mostrar 0 termos.
'''
print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} ->', end= ' ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('FIM')