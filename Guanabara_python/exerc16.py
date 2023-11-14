'''
O professor que sortear um dos seus quatro alunos para apagar o quadra.
Faça um prograna que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
from random import choice

aluno1 = (input('Digite primeiro aluno: '))
aluno2 = (input('Digite segundo aluno: '))
aluno3 = (input('Digite terceiro aluno: '))
aluno4 = (input('Digite quarto aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(alunos)

print(f'O aluno sorteado: {sorteio}')
