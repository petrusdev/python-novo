numero_1 = int(input('Digite primeiro número: '))
numero_2 = int(input('Digite segundo número: '))
numero_3 = int(input('Digite terceiro número: '))

while True:
    print(
        'Digite: \n[1] - somar\n[2] - multiplicar\n[3] - maior\n[4] - novos números\n[5] - sair do programa'
        )
    opcao = str(input('Escolha opção: '))

    if opcao == '1':
        resultado = numero_1 + numero_2 + numero_3
        print(f'A soma de {numero_1} + {numero_2} + {numero_3} é igual: {resultado}')
    
    elif opcao == '2':
        resultado = numero_1 * numero_2 * numero_3
        print(f'A multiplicação de {numero_1} x {numero_2} x {numero_3} é igual: {resultado}')    

    elif opcao == '3':
        if numero_1 > numero_2 and numero_1 > numero_3:
            print(f'O número {numero_1} é maior que {numero_2} e {numero_3}')
        elif numero_2 > numero_1 and numero_2 > numero_3:
            print(f'O número {numero_2} é maior que {numero_1} e {numero_3}')
        elif numero_3 > numero_2 and numero_3 > numero_1:
            print(f'O número {numero_3} é maior que {numero_2} e {numero_1}')
        else:
            print('Os números são iguais.')
    
    elif opcao == '4':
        numero_1 = int(input('Digite primeiro número: '))
        numero_2 = int(input('Digite segundo número: '))
        numero_3 = int(input('Digite terceiro número: '))
    
    elif opcao == '5':
        continuar = (input('Deseja continuar? (sim/não): '))
        if continuar.lower() != 'sim':
            break
   