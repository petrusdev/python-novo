# in not

nome = input('Digite seu nome:')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

print('dro' in nome) #dro está no nome Pedro.
print('zero' in nome) #zero não está no nome Pedro.