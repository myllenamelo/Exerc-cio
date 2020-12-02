#(LISTA) Um aluno deseja saber suas médias antes da postagem de seu professor para planejar com 
#antecedencia as suas férias. O aluno deseja criar um sistema que receba os nomes das disciplinas, 
# suas duas notas e apresente em um boletim os nomes das disciplinas e suas respectivas médias.

notas = list()
notasComposta = list()
quantdisc = 0
i = 0
media = 0

quantdisc = int(input('Você deseja ver a sua situação em quantas disciplinas?'))

for j in range(0, quantdisc):
    notas.append(str(input('Qual disciplina? ')))
    notas.append(float(input('Insira a 1ª nota: ')))
    notas.append(float(input('Insira a 2ª nota: ')))
    media = (float(notas[i+1])+float(notas[i+2]))/2
    notas.append(float(media))
    notasComposta.append(notas[i:])
    i += 4

i = 0
print("Disc.\t\t\tMédia")
print('#-------------------------------#')
for a in range(0, len(notasComposta)):
    print("%s\t\t%.2f" %
          (notasComposta[a][i], notasComposta[a][3]))
print('#-------------------------------#')
