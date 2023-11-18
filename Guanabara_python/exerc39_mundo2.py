'''
Faça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- Equilátero: todos os lados são iguais.
- Isósceles: dois lados iguais
- Escaleno: Todos os lados são diferentes.
Estrutura aninha um pouco diferente.
'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA um \033[33mtriângulo\033[m.')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('O triângulo formado é: EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado: ISÓSCELES.')
    else:
        print('O triângulo formado: ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')