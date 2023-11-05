'''
Da mesma forma que usamos o while, usamos o for
'''

for i in range(10): # percorre os valores de 'i' de 0 a 9 (10 valores no total). cria uma sequencia de número de 0 a 9.
    if i == 2: # Quando i é igual a 2, ele imprime "i é 2, pulando..." e continua para a próxima iteração.
        print('i é 2, pulando...') # ... ele imprime 'i é 2, pulando...' // continua para a próxima iteração do loop for
    if i == 8: # Quando i é igual a 8, ele imprime "i é 8, seu else não executará" e sai do loop for prematuramente usando break. 
        print('i é 8, seu else não executará') # ... ele imprime "i é 8, seu else não executará"
        break # e, em seguida, usa a instrução break para sair do loop for imediatamente.

    for j in range(1, 3): # Este é um segundo loop for aninhado dentro do loop externo. Ele percorre os valores de j de 1 a 2 (dois valores no total) para cada valor de i
        print(i, j) # imprime os valores de i e j.

else:
    print('For completo com sucesso')