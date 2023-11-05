# ESTUDANDO FOR E IN
texto = 'Python'

novo_texto = '' # Não tem nada escrito por que vai ser criado entre letra + *

for letra in texto: # PARA cada LETRA em TEXTO eu vou fazer uma iteração / Variavel (letra) criada no FOR.
    novo_texto += f'*{letra}' # vai repetir o * até o final do texto
    print(letra) # Imprime o nome Python repetindo

print(novo_texto) # Fica fora do laço por que ele está sendo criado dentro do while P*y*... repetindo até finalziar o texto completo.