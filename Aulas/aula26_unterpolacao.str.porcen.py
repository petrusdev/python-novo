'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''
nome = 'Pedro'
preco = 1000.965364
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

# IMPORTANTE: esse é um dos modelso que pode se usar, o professor disse que gosta
# de usar f-strings que ele vai ensinar próxima aula, se for mais fácil eu fico com ela.