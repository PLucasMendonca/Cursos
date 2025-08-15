""" Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retronar um dicionário com as seguintes informações: 
-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação(opicional)

Adicione também as docstrings da função
"""

def notas(*notas, sit=False):
    maior = menor = media = 0
    nota = dict()

    for c in notas:
