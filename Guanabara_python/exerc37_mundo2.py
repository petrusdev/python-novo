'''
Crie um programa que leia duas notas de um aluno e calcule sua  média, mostrando uma mensagem no final,
de acordo com a média atingida.
- Média abaixo de 5.0:
REPROVADO.
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO
'''
nota1 = float(input('Nota N1: '))
nota2 = float(input('Nota N2: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('\033[32mREPROVADO!\033[m')
elif 5 <= media < 7:
    print('RECUPERAÇÃO!')
elif media >= 7:
    print('\033[32mAPROVADO!\033[m')