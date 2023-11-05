'''
Eu e minha noiva fomos almoçar no mercado dos peixes, 
comemos camarão, comemos batata frita, um peixe e baião, compramos também uma coquinha gelada.
No fim de tudo chegou a nossa temida conta, 
e além da nossa conta teria que pagar o serviço que seria de 14%, fora o couvert de 5 reais.
Então ficamos na duvida de como calcular, seria mt legal ter um programa que pegasse o valor da conta, 
o valor que tenho que pagar de gorjeta o couvert se tiver. e ja me desse a resposta. 
'''

# RECEBE OS VALORES DOS ITENS
total = float(input('Digite valor conta: '))

# CONVERTE VPORCENTAGEM
porcentagem_gorjeta = int(input('Taxa de Serviço (%): '))
total_com_gorjeta = total * (1+ (porcentagem_gorjeta/100))

# EXIBE VALOR COUVERT
couvert = float(input('Valor Couvert: '))

# TOTAL GERAL COM PORCENTAGEM + GORJETA
total_geral = total_com_gorjeta + couvert

print('='*16 + 'xx'*2 + '='*16)
print('Conta: R$ {:.2f}'.format(total))
print('Taxa de serviço: {}%'.format(porcentagem_gorjeta))
print('Couvert R$ {:.2f}'.format(couvert))
print('Valor total a pagar: R$ {:.2f}'.format(total_geral))
print('='*16 + 'xx'*2 + '='*16)



