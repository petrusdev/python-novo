'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
'''
condicao = True # tenho que sempre colocar condicao True?

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair': # interessante que tem uma condicao if para quando a pessoa digitar 'sair'.
        break 

print('Acabou') # Depois que acaba o bloco de cima em break ele continua o restante e para nessa print.