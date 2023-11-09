while True:
    num = int(input('Digite um número que deseja ver a tabuada: '))
    print('-' * 44)

    if num >= 0:
        for i in range(1,11):
            resultado = num * i
            print('{} x {} = {}'.format(num, i, resultado))
        
    else:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    print('-' * 44)





