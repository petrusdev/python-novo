'''
Maior Número:
Crie uma função chamada maior_numero que recebe três números como argumentos e retorna o maior deles.
'''

def maior_numero(a, b, c):
    maior_num = 0
    menor_num = 0
    
    if a > b and a > c:
        print(f'{a} é maior que {b} e {c}')
    
    elif b > a and b > c:
        print(f'{b} é maior que {a} e {c}')

    else:
        print(f'{c} é maior que {a} e {b}')

maior_numero(7, 9, 12)
