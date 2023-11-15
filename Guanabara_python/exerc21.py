'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 
'SANTO'.
'''
cidade = input('Digite sua cidade: ').upper().strip()
print(f'{cidade[:5] == 'SANTO'}')

'''if cidade.startswith('SANTO'):
    print(f'A cidade {cidade} começa com "SANTO"')

else: 
    print(f'A cidade {cidade} não começa com "SANTO"')'''