#(DICIONÁRIO)O dono de uma locadora está organizando no sistema a lista de lançamentos. Ele está organizando da
# seguinte maneira: Nome do filme / gênero / valor de locação por 24h. Ao final da organização o dono deseja 
# exibir  uma placa de maneira que os clientes consigam visualizar esses três dados e queiram efetuar a locação. Organize os filmes no sitema dessa forma e apresente em forma de lista.Segue a lista de filmes:
#Mar em fúria - Ação - R$12,00 /24h
#Duelo de Titãs-Drama-R$10,00/24h
#A corrente do bem-Romance-R$13,00/24h
#Homens de Honra-Drama-R$12,00
#A nova onda do imperador-Comédia-R$12,00

locadora=list()
filme1 ={'titulo':'Mar em fúria','genero':'Ação','valor':12.00}
filme2 ={'titulo':'Duelo de Titãs','genero':'Drama','valor':10.00}
filme3 ={'titulo':'A corrente do bem','genero':'Romance','valor':13.00}
filme4 ={'titulo':'Homens de Honra','genero':'Drama','valor':12.00}
filme5 ={'titulo':'A nova onda do imperador','genero':'Comédia','valor':12.00}
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
locadora.append(filme4)
locadora.append(filme5)
print('---------------------------------')
print('|            FILMES             |')
print('---------------------------------')
print('|TITULO:',locadora[0]['titulo'],'\t\t|')
print('|GÊNERO:',locadora[0]['genero'],'\t\t\t|')
print('|VALOR R$:',locadora[0]['valor'],'\t\t|')
print('---------------------------------')
print('|TITULO:',locadora[1]['titulo'],'\t|')
print('|GÊNERO:',locadora[1]['genero'],'\t\t\t|')
print('|VALOR R$:',locadora[1]['valor'],'\t\t|')
print('---------------------------------')
print('|TITULO:',locadora[2]['titulo'],'\t|')
print('|GÊNERO:',locadora[2]['genero'],'\t\t|')
print('|VALOR R$:',locadora[2]['valor'],'\t\t|')
print('---------------------------------')
print('|TITULO:',locadora[3]['titulo'],'\t|')
print('|GÊNERO:',locadora[3]['genero'],'\t\t\t|')
print('|VALOR R$:',locadora[3]['valor'],'\t\t|')
print('---------------------------------')
print('|TITULO:',locadora[4]['titulo'],'|')
print('|GÊNERO:',locadora[4]['genero'],'\t\t|')
print('|VALOR R$:',locadora[4]['valor'],'\t\t|')
print('---------------------------------')