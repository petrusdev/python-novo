# VERIFICAÇÃO SE A SENHA ESTÁ CORRETA OU NÃO COM REPETIÇÃO

senha_salva = '123456' # Para essa comparação o usuário tem que já ter uma senha salva
senha_digita = '' # Variável para repetição quando o usuário digitar dentro do while
repeticoes = 0 # inicia o contador no 0, chamo de contador ou indicia

while senha_salva != senha_digita: # ENQUANTO senha salvadiferente da senha digitada, volta a pedir a senha
    senha_digita = input(f'Sua senha ({repeticoes}x): ') # Depois pedimos a senha ao usuário 
    # Usuário acertou a senha? sistema sai do While e imprime o que está fora do While
    repeticoes += 1 # Usuário não acertou a senha, repete novamente.

print('Aquele laço acima pode ter repetições infinitas')