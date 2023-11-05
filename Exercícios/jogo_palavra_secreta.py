'''
Fazer um jogo para o usuário adivinhar qual a palavra secreta.
- Propror uma palavra secreta para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a palavra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba '*'.
 Faça uma contagem de tentativas do seu usário.
'''
import os

palavra_secreta = 'perfume' # colocamos fora do while para ele não zerar com a repetição e condição.
letras_acertadas  = '' # colocamos fora do while para não zerar com a repetição e 'salvar' elas.
numero_tentativas = 0

while True: # Primeiro vamos fazer um loop para que rode o jogo inteiro
    letra_digitada = input('Digite uma letra: ') # recebe uma letra digita do jogador
    numero_tentativas += 1

    # VERIFICA SE O JOGADOR DIGITA MAIS DE UMA LETRA
    if len(letra_digitada) > 1: # SE len(pega quantidade de letra digita) for MAIOR que 1, faça:.
        print('Digite apenas uma letra.') # Exibe essa mensagem para o jogador
        continue # Continue volta para a condição para verificar se o jogador digita apenas 1 letra.

    # VERIFICA SE A LETRA DIGITADA ESTÁ DENTRO DA PALAVRA SECRETA
    if letra_digitada in palavra_secreta: # SE letra digitada ESTÁ na palavra secreta, faça:
        letras_acertadas += letra_digitada # concatenção, quando voltar no inicio do while ele vai voltar + letra acertada

    palavra_formada = ''
    for letra_secreta in palavra_secreta: # (For pecorre a palavra) PARA cada letra secreta (variavel formada no for) em palavra secreta FAÇA
        if letra_secreta in letras_acertadas: # Se letra secreta está em letra acerta, FAÇA
            palavra_formada += letra_digitada # concatenação, vai preenchendo as palavras formadas até forma a frase toda correta.
        else: # SE não, FAÇA # Se colocarmos print vai ficar uma letra abaixo da outra no FOR.
            palavra_formada += '*'

    print('Palavra formada:'.format(palavra_formada))

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU')
        print('A palavra era:'.format(palavra_secreta))
        print('Tentativas: '.format(numero_tentativas))