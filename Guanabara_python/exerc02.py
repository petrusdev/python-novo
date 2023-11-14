'''
Crie um algoritmo que leia um número e mostre seu 
dobro e triplo e raiz quadrada
'''

n = float(input('Digite um número: '))
print('O número {} tem seu dobro {}, \nseu triplo {} e sua raiz quadrada de {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))