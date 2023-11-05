'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''
contador = 0 # Não funcionou igual a aula 62.

while contador <= 10:
    contador = contador + 1

    if contador == 10:
        print('Não vou mostrar o 6.')
        
        break

print('Acabou')