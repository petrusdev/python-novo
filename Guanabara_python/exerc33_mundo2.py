'''
Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor da prestão mensal sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''
print('\033[32m*\033[m'*25)
print('PEDROBANK FINANCIAMENTOS')
print('\033[32m*\033[m'*25)
print('')

nome = str(input('Digite seu nome: '))
valor_casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite sua renda mensal: R$ '))
parcela = int(input('Quantos anos de financiamento? '))

nomes = {'Nartan': 'Sexo Paia'}
parcela_meses = parcela * 12
salario_porcentagem = salario * 30 / 100
valor_prestacao = valor_casa / parcela_meses
print('')
if valor_prestacao <= salario_porcentagem:
    print(f'Olá! Prazer em conhecer você {nomes}.')
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {parcela} anos a prestação será de R${valor_prestacao:.2f}')
    print('Empréstimo pode ser \033[32mCONCEDIDO!\033[m')
else:
    print(f'Olá Sr {nome}! Foi uma infelicidade conhecer você.')
    print('Sua situação está \033[31mPRECÁRIA\033[m, tem que fazer um extra com UBER!')
    print(f'Para pagar uma casa de R${valor_casa:.2f} em {parcela} anos a prestão será de R${valor_prestacao:.2f}')
    print(f'Empréstimo \033[31mNEGADO\033[m!')





