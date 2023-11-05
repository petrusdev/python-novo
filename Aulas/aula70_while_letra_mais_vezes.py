# barra investida serve para continuar a frase sem ficar grande o espaço da linha como esse comentário
frase = 'O Python é uma linguagem de programçao'\
'multiparadigma.' \
'Python foi criado por Guido '.lower() #lower para colocar tudo em minúsculo para verificar toda variação

# print(frase.count('python')) #funciona só em str, count mostra a quantidade de palavras que apareceu.

i = 0 # i seria o 'contador'
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi "{}" que apareceu {}x'.format(letra_apareceu_mais_vezes, qtd_apareceu_mais_vezes))