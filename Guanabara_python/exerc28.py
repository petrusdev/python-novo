'''
Desenvolva um programa que a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens de até 200km
e R$ 0.45 para viagens mais longas.
'''
distancia_viagem = int(input('Qual é a distância da sua viagem?: '))
print(f'Você está prestes a começar uma viagem de {distancia_viagem}km.')
if distancia_viagem <= 200:
    preco = distancia_viagem * 0.50
else:
    preco = distancia_viagem * 0.45

print(f'E o preço da sua passagem será de R${preco:.2f}')