'''
Criar um programa que calcula a média de três notas.
O programa tem que pedir nome do aluno e inserir as 3 notas.
'''
print('Portal do Aluno!')

# SOLICITA O NOME COMPLETO DO ALUNO
nome_aluno = input('insira seu nome: ') # recebe o nome do aluno

while True:
    # SOLICITA AS TRÊS NOTAS
    n1 = (input('Insira a nota 1: '))
    n2 = (input('Insira a nota 2: '))
    n3 = (input('insira a nota 3: '))

     # CONVERTER AS ENTRADAS EM VALORES INTEIROS
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)

    # CALCULAR A MÉDIA
    media_aluno = (n1 + n2 + n3) / 3 # variavel media aluno para calcular a média e jogar na condição
    print('A sua média é {:.2f}'.format(media_aluno)) # :.2f acrescentar duas casas decimais

    # CONDIÇÃO SE É APROVADO, RECUPERAÇÃO E REPROVADO
    if media_aluno >= 7:
        print('Aprovado com êxito, o {} pode continuar para a próxima disciplina.'.format(nome_aluno))
    elif 5 < media_aluno < 7:
        print('Recuperação, o aluno {} deve fazer uma nova prova para medir suas habilidades.'.format(nome_aluno))
    else:
        print('Reprovado, o aluno {} deverá refazer toda a disciplina.'.format(nome_aluno))

    # PERGUNTAR SE O USUÁRIO DESEJA CONTINUAR
    continuar = input('Deseja fazer a média de um novo aluno? (sim/não): ')
    if continuar.lowerr() != 'sim':
        break


