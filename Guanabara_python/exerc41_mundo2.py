'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/pix: 10 % desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
valor = float(input('Valor total do produto: R$ '))

print('Escolha a forma de pagamento: \n1 - à vista 10% desconto\n2 - cartão à vista 5% desconto \n3 - cartão em até 2x preço normal \n4 - cartão parcelado 3x ou mais 20% juros')

escolha = int(input('Digite sua opção: '))

desconto_10 = 10
desconto_5 = 5
juros_20 = 20

if escolha == 1:
    valor_com_desconto_10 = valor - (valor * 10 / 100)
    print(f'Sua compra à vista com 10% desconto ficou por apenas R${valor_com_desconto_10} reais.')
elif escolha == 2:
    valor_com_desconto_5 = valor - (valor * 5 / 100)
    print(f'Sua compra no cartão à vista com 5% desconto ficou por apenas R${valor_com_desconto_5} reais.')
elif escolha == 3:
    print(f'Sua compra parcelada em 2x no cartão ficou com preço normal de apenas R${valor} reais.')
elif escolha == 4:
    juros_20 = valor + (valor * 20 / 100)
    print(f'Sua compra parcelada no cartão 3x ou mais teve juros da máquina de 20% e ficou por R${juros_20} reais.')
else:
    print('Opção inválida.')