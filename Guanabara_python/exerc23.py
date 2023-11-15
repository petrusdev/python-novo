'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'.
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez
'''

frase = 'Vou me tornar um programar, custe o que custar!'.lower()
quantidade_a = frase.count('a')
primeira_posicao = frase.find('a')
ultima_posicao = frase.rfind('a')

print(f'A letra "A" aparece {quantidade_a} vezes.')
print(f'A primeira posição da letra "A" é {primeira_posicao}')
print(f'A última posição da letra "A" é {ultima_posicao}')