'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listas valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
'''
import os

lista = [] #lista fora do while para ir adicionando os itens na lista

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ') # organizar para inserir, apagar e listar.

    if opcao == 'i': # SE a opção do usuário for i FAÇA
        os.system('cls') # 'importei os' para limpar o terminal e aparecer a próxima opção.
        valor = input('Produto: ') # Entrada o usuário digita um produto
        lista.append(valor) # append para adicionar a 'lista ='
 
    elif opcao == 'a': #Se ele escolher opçao a, faça:
        indice_str = input('Escolha o índice para apagar: ')

        try: # Evitar letras e da erro de conversão str para int e del list caso não tenha o indice. 2 indice e a pessoa digita 3
            indice = int(indice_str) 
            del lista[indice] 
        except ValueError: # Sempre informar o except qual o erro para tratar
            print('Por favor, digite um número inteiro.') 
        except IndexError: 
            print('Índice não existe na lista.')

    elif opcao == 'l':
        if len(lista) == 0: # len vai saber a quantidade de elementos na lista e se for 0 printar a linha abaixo.
            print('Nada para listar.')
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print('Por favor, escolha i, a ou l.')
    
    
