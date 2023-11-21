'''
Crie um programa que leia uma frase qualquer e diga se ela é palíndromo,
desconsiderando os espaços.
Ex: 
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
'''
frase = str(input('Digite sua frase: ')).upper().strip()
palavra = frase.split()
juntar_palavra = ''.join(palavra)
inverso_palavra = ''

for letra in range(len(juntar_palavra) -1, -1, -1):
    inverso_palavra += juntar_palavra[letra]

print(f'O inverso de {juntar_palavra} é {inverso_palavra}')
if inverso_palavra == juntar_palavra:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
    

