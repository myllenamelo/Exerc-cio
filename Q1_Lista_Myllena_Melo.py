'''
Com o passar do tempo os signos ganharam bastante popularidade, vindo de encontro também temos os Zodíaco Chinês
levando em conta que não é muito visto no nosso cotidiano, faça um programa que ajude as pessoas a descobrirem
seu signo do Zodíaco Chinês.
Levando em cosideração que ele é composto por animais com ciclo de 12 anos uma maneira simples de identificar é 
com o ano do nascimento.
ano do nascimento % 12, sendo
0- macaco
1-galo
2-Cão
3-Porco
4-Rato
5-Boi
6- Tigre
7-coelho
8-Dragão
9-Serpente
10-Cavalo
11-Carneiro
'''
i=0
horoscopo=float
zodiaco=list()
zodiaco = ('Macaco','Galo','Cão','Porco','Rato','Boi','Tigre','Coelho','Dragão','Serpente','Cavalo','Carneiro')


def zodiacochines(year):
    horoscopo=year%12
    return (horoscopo)
       

ano = int(input("Seu ano de nascimento: "))
horoscopo=zodiacochines(ano)

if horoscopo==0:
    print ('Seu signo chinês é:',zodiaco[0])
elif horoscopo==1:
    print ('Seu signo chinês é:',zodiaco[1])
elif horoscopo==2:
    print ('Seu signo chinês é:',zodiaco[2])
elif horoscopo==3:
    print ('Seu signo chinês é:',zodiaco[3])
elif horoscopo==4:
    print ('Seu signo chinês é:',zodiaco[4])
elif horoscopo==5:
    print ('Seu signo chinês é:',zodiaco[5])
elif horoscopo==6:
    print ('Seu signo chinês é:',zodiaco[6])
elif horoscopo==7:
    print ('Seu signo chinês é:',zodiaco[7])
elif horoscopo==8:
    print ('Seu signo chinês é:',zodiaco[8])
elif horoscopo==9:
    print ('Seu signo chinês é:',zodiaco[9])
elif horoscopo==10:
    print ('Seu signo chinês é:',zodiaco[10])
else:
    print ('Seu signo chinês é:',zodiaco[11])
