'''
Desafio 09 - Caixa eletrônico (saque)
Simular serviço de saque no caixa eletrônico:
Regras:
Vamos ter notas de R$ 50, 20, 10, 1.
Tem que informar pro usuários quantas notas ele vai receber de casa valor, 
conforme o que ele está sacando
Ex. Saquei R$ 175 :Ele vai me retornar 
Você vai receber 3 notas de 50 reais
1 nota de 20 reais
5 notas de 1 real
'''

while True:
    saque = int(input('Valor do saque: '))

    notas_caixa = [50, 20, 10, 1]

    for nota in notas_caixa:
        qtd_notas = saque // nota
        saque %= nota

        print('Você vai receber {} notas de {} reais.'.format(qtd_notas, nota))
    
    continuar = input('Deseja sacar novamente? (sim/não): ')
    if continuar.lower() != 'sim':
        break




    



