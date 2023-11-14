'''
Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessário para
pintá-la, sabendo que cada tinta, punta uma area de 2m ao quadrado.
'''

'''largura = 6
altura = 10
tinta = 2

metro_quadrado = largura * altura
qtd_tinta = metro_quadrado / tinta

print('A quantidade de tintas que vamos precisar para pintar sua casa é {:.0f}'.format(qtd_tinta))'''

def calcular_area(largura, altura):
    return largura * altura

def calcular_tinta(area):
    litros_por_metro_quadrado = 2
    return area / litros_por_metro_quadrado

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a alterua da parece em metros: '))

area_parede = calcular_area(largura, altura)
qtd_tinta = calcular_tinta(area_parede)

print('A área da parede é {:.2f}m².'.format(area_parede))
print('Serão necessário {:.2f} litros de tinta para pintar a parede.'.format(qtd_tinta))
