'''
AULA EXPLICANDO COMO O FOR FUNCIONA POR TRÁS DO FUNCIONAMENTO DELE
COMPARAÇÃO ENTRE FOR E WHILE PARA ENTENDER POR QUE O FOR É MAIS PRÁTICO
PRATICAMENTE ELE FAZ AUTOMATICO O QUE O WHILE TEM QUE DETALHAR PARA O SISTEMA

Iterável -> str, range, etc 
Iterador -> quem sabe entregar um valor por vez
net -> me entregue o próximo valor
iter -> me entregue seu iterador
'''
# for letra in texo - O for precisa somente fazer isso para escrever o nome.
texto = 'Luiz'

iteratador = iter(texto) # variavel para o laço utilizando o WHILE

while True: # Começa o laço de repetição
    try: # Precisamos utilizar o try para o programa parar quando acabar a contagem com o except BREAK
        letra = next(iteratador) # letra = next que ele vai repetir sempre para a próxima letra
        print(letra)
    except StopIteration: # Quando acabar todas as letras o sistema para sem mostrar o erro StopIteration
        break