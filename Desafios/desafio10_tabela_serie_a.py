'''
Criar uma tupla que mnostre os 20 times da série A, na ordem da colocação.
- Mostrar os 5 primeiros times.
- Os últimos 4 colocados para ser rebaixado
- Times em ordem alfabética
- Em que posição está o São Paulo
'''
tabela_serie_a = ('Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino', 'Flamengo',
                   'Atlético-MG', 'Athletico-PR', 'Fluminese', 'São Paulo',
                     'Cuiabá','Internacional', 'Santos', 'Corinthians', 'Bahia',
                     'Vasco da Gama','Cruzeiro', 'Goias', 'Coritiba', 'América-MG')

print('5 primeiros colocados: ', tabela_serie_a[0:5])
print('4 últimos colocados: ', tabela_serie_a[-4:])
print('Os times em ordem alfabética: ', sorted(tabela_serie_a))
print(f'Em que posição está o São Paulo: {tabela_serie_a.index('São Paulo') +1}º')
