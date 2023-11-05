'''
Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informa que não é um número inteiro.
'''
'''
try:
    # Solicita ao usuário que digite um número
    numero_inteiro = int(input('Digite um número inteiro: '))

    # Verifica se o número é par ou impar
    if numero_inteiro % 2 == 0:
        print(f'Este número é par.')
    else:
        print(f'Este número é ímpar.')

except:
    print('Isso não é um número inteiro.')
'''

'''
Faça um porograma que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex. Bom  dia 0_11, Boa tarde 12-17 e Boa noite 18-23.
'''
# Solicita ao usuário que digite a hora (0-23)
#try:
 #   hora = int(input('Digite a hora (0-23): '))

 #   if 0<= hora <=11: 
 #      print('Bom dia!')
 #   elif 12<= hora <=17:
 #       print('Boa tarde!')
 #   elif 18<= hora <=23:
 #       print('Boa noite!')

#except ValueError:
#    print('Hora inválida')

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva 'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva 'Seu nome é normal'; 
maior que 6 escreva 'Seu nome é muito grande'
'''

nome = (input('Digite seu primeiro nome: '))
quantidade_letras = len(nome)

print(f'O nome {nome} possui {quantidade_letras} letras.')

if quantidade_letras > 1:
    if quantidade_letras <=4:
        print('Seu nome é curto.')
    elif 5 <= quantidade_letras <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Digite pelo mais de uma letra.')

