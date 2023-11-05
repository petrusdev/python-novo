abaixo_16 = 0
entre_16_e_24 = 0
entre_24_e_34 = 0
acima_34 = 0

print('-'*25 + '**'*2 + '-'*25)
print('   Seja bem-vindo ao Supermercado TEO DE AÇUCAR')
print('        Quem entrou, experimentou, gostou!')

while True:
    print('-'*25 + '**'*2 + '-'*25)
    print('Atenção: deixe o nome em branco para fechar o programa')
    print('-'*25 + '**'*2 + '-'*25)
    nome = input('Nome e sobrenome: ')
    if nome == '':
        break
    
    idade = int(input('Idade: '))
    cpf = input('CPF: ')
    
    if idade < 16:
        abaixo_16 += 1
    elif 16 <= idade < 24:
        entre_16_e_24 += 1
    elif 24 <= idade <= 34:
        entre_24_e_34 += 1
    else:
        acima_34 += 1

total_pessoas = abaixo_16 + entre_16_e_24 + entre_24_e_34 + acima_34

porcentagem_abaixo_16 = (abaixo_16 / total_pessoas) * 100
porcentagem_entre_16_e_24 = (entre_16_e_24 / total_pessoas) * 100
porcentagem_entre_24_e_34 = (entre_24_e_34 / total_pessoas) * 100
porcentagem_acima_34 = (acima_34 / total_pessoas) * 100

print(f'total de pessoas: {total_pessoas}')
print(f'Pessoas abaixo de 16 anos: {porcentagem_abaixo_16:.2f}%')
print(f'Pessoas entre 16 e 24 anos: {porcentagem_entre_16_e_24:.2f}%')
print(f'Pessoas entre 24 e 24 anos: {porcentagem_entre_24_e_34:.2f}%')
print(f'Pessoas acima de 34 anos: {porcentagem_acima_34:.2f}%')

