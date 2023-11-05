''' Calculadora com while '''
while True:
    # Solicitar ao usuário que digite dois números inteiros
    numero_1 = input('Digite um número: ') # entrada
    numero_2 = input('Digite outro número: ') # entrada

    # Verificar se as entradas não estão vazias
    if not numero_1 or not numero_2: # SE(if) não é igual n1 ou não é igual n2 = print fala o erro.
        print('Por favor, insira valores válidos.') 

    # CONVERTER AS ENTRADAS EM VALORES INTEIROS
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)

    # ESCOLHA UMA OPERAÇÃO
    print('Escolha uma operação')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    operacao = input('Digite o número da operação: ')
    
    # Realizar/desenvolver operação selecionada
    if operacao == '1':
        resultado = numero_1 + numero_2
    elif operacao == '2':
       resultado = numero_1 - numero_2
    elif operacao == '3':
        resultado = numero_1 * numero_2
    elif operacao == '4':
        resultado = numero_1 / numero_2 
        if numero_2 == 0:
            print('Erro: divisão por zero.')
            continue
    else:
       print('Operação inválida.')
       continue
        
    # Exibir resultado
    print('Resultado: {}'.format(resultado))

    # Pergunta se o usuário deseja continuar
    continuar = (input('Deseja continuar? (sim/não): '))
    if continuar.lower() != 'sim':
        break