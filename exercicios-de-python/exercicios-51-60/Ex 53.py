# Ex.53 - Peça nome e três notas de um aluno via input(), guarde em um dicionário, calcule a média e use if para imprimir 'Aprovado' ou 'Reprovado'.

nota1 = int(input('Digite a primeira nota do aluno: '))
nota2 = int(input('Digite a segunda nota do aluno: '))
nota3 = int(input('Digite a terceira nota do aluno: '))
media = (nota1+nota2+nota3)/3

notas = {'aluno': input('Digite o nome do aluno:'), 'média': media}

if media < 6:
    print('Reprovado')
else:
    print('Aprovado')

print(notas)