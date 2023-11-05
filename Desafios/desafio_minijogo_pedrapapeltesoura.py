# IMPORTA FUNÇÃO RANDOM
from random import randint
from time import sleep

# APRESENTAÇÃO DO JOGO
print('*-*-'*8)
print('   PETRUS GAMES - MINIJOGOS   ')
print('*-*-'*8)
print('Vamos uma partida de pedra, papel e tesoura!!')

# ESCOLHA DO USUÁRIO + VERIFICAÇÃO SE O NUMERO ESTÁ DENTRO DAS OPÇÕES OU NÃO É UM NÚMERO
while True:
    jogador = str(input('Escolha sua jogada \n[1] Pedra\n[2] Papel\n[3] Tesoura\n>> ')).lstrip().rstrip() #.strip() apaga o espaço antes e depois do texto
# espaço aqui
    if jogador.isdigit():
        jogador = int(jogador) # Jogador STRING se transforma em JOGADOR INTEIRO
        if 1 <= jogador <= 3: # Se jogador estiver entre 1 e 3, faça.
            break # quebro o while e continuo programa
        else:
            sleep(1)
            print('Você digitou uma opção inválida, leia com atenção e escolha novamente')
    else:
        sleep(1)
        print('Você digitou uma letra, as opções são númericas')

sleep (1)
print('Pedraaaa...')
sleep (1)
print('Papeeeel...')
sleep (1)
print('Tesouraa!!!')
sleep(2)

# ESCOLHA DA MAQUINA
maquina = randint(1,3)

# TRANSFORMANDO NÚMEROS EM NOME USANDO UM DICIONÁRIO
mapeamento = {
1: 'PEDRA', 
2: 'PAPEL', 
3: 'TESOURA'
}
# NÚMERO CORRESPONDENDO A NOME
nome_pc = mapeamento[maquina]
nome_jogador = mapeamento[jogador]

print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('Computador escolheu {}'.format(nome_pc))
print('Você escolheu {}'.format(nome_jogador))
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

if jogador == maquina:
    print('EMPATE TÉCNICO!!!')
elif nome_jogador == 'PEDRA' and nome_pc == 'TESOURA' or nome_jogador == 'TESOURA' and nome_pc == 'PAPEL' or nome_jogador == 'PAPEL' and nome_pc == 'PEDRA':
    print('VOCÊ VENCEU!!!')
else:
    print('A MÁQUINA VENCEU')
    