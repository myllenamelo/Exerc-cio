#(DICIONARIO) Uma funcionária do DETRAN está organizando no sistema os alunos e as categorias que estão 
# se formando. No dia das provas ela precisa apresentar os alunos por categoria para que os avaliadores 
# se preparem para aplicação. Segue a lista de alunos:
#Maria - B /Joana - A /Tereza - B /João - A e B /Pedro- C /José-A /Paulo- B /Bruna-B /Beatriz-A e B

alunos=list()
alun1 ={'nome':'Maria','categoria':'B'}
alun2 ={'nome':'Joana','categoria':'A'}
alun3 ={'nome':'Tereza','categoria':'B'}
alun4 ={'nome':'João','categoria':'A e B'}
alun5 ={'nome':'Pedro','categoria':'C'}
alun6 ={'nome':'José','categoria':'A'}
alun7 ={'nome':'Paulo','categoria':'B'}
alun8 ={'nome':'Bruna','categoria':'B'}
alun9 ={'nome':'Beatriz','categoria':'A e B'}

alunos.append(alun1)
alunos.append(alun2)
alunos.append(alun3)
alunos.append(alun4)
alunos.append(alun5)
alunos.append(alun6)
alunos.append(alun7)
alunos.append(alun8)
alunos.append(alun9)

print('---------------------------------')
print('|          CATEGORIA A          |')
print('---------------------------------')
print('|NOME:',alunos[1]['nome'],'\t\t\t|')
print('|NOME:',alunos[3]['nome'],'\t\t\t|')
print('|NOME:',alunos[5]['nome'],'\t\t\t|')
print('|NOME:',alunos[8]['nome'],'\t\t\t|')
print('---------------------------------')
print('---------------------------------')
print('|          CATEGORIA B          |')
print('---------------------------------')
print('|NOME:',alunos[0]['nome'],'\t\t\t|')
print('|NOME:',alunos[2]['nome'],'\t\t\t|')
print('|NOME:',alunos[3]['nome'],'\t\t\t|')
print('|NOME:',alunos[6]['nome'],'\t\t\t|')
print('|NOME:',alunos[7]['nome'],'\t\t\t|')
print('|NOME:',alunos[8]['nome'],'\t\t\t|')
print('---------------------------------')
print('---------------------------------')
print('|          CATEGORIA C          |')
print('---------------------------------')
print('|NOME:',alunos[4]['nome'],'\t\t\t|')
print('---------------------------------')