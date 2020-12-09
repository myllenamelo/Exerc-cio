'''
é comum no jogo de dominó ter uma rodada antes de iniciar o jogo na qual todos os integrantes escolhem
apenas uma pedra e quem retirar o maior valor inicia o jogo,
outra situação é quando o jogo fecha e inicia a contagem de pontos, aquele que tiver a menor pontuação vence.
simule um jogo de dominó com quatro jogadore onde deve entrar na tupla os valores para iniciar e outra para
a contagem de pontos no final deve mostrar a maior e menor peça, os valor ordenados.
'''
import random

maiorpedra=()
menorpedra=()
ganhou1=0
ganhou2=0
ganhou3=0
ganhou4=0
#jogadas
jogador1 = random.randint(0, 6)
jogador2 = random.randint(0, 6)
jogador3 = random.randint(0, 6)
jogador4 = random.randint(0, 6)
    
pontos=(jogador1,jogador2,jogador3,jogador4)
print(f'O jogador 1 tirou a pedra {jogador1},o jogador 2 tirou a pedra {jogador2},o jogador 3 tirou a pedra {jogador3} e o jogador 4 tirou a pedra {jogador4} .')

#verifica inicio do jogo
if (jogador1 > jogador2) and (jogador1 > jogador3) and (jogador1 > jogador4):
    print('O jogador 1 iniciou o jogo.')
if (jogador2 > jogador1) and (jogador2 > jogador3) and (jogador2 > jogador4):
    print('O jogador 2 iniciou o jogo.')
if (jogador3 > jogador1) and (jogador3 > jogador2) and (jogador3 > jogador4):
    print('O jogador 3 iniciou o jogo.')
if (jogador4 > jogador1) and (jogador4 > jogador2) and (jogador4 > jogador3):
    print('O jogador 4 iniciou o jogo.')

#verifica pontos
if (jogador1 < jogador2) and (jogador1 < jogador3) and (jogador1 < jogador4):
    ganhou1=1
    print('O jogador 1 ganhou o jogo.')
if (jogador2 < jogador1) and (jogador2 < jogador3) and (jogador2 < jogador4):
    ganhou2=1
    print('O jogador 2 ganhou o jogo.')
if (jogador3 < jogador1) and (jogador3 < jogador2) and (jogador3 < jogador4):
    ganhou3=1
    print('O jogador 3 ganhou o jogo.')
if (jogador4 < jogador1) and (jogador4 < jogador2) and (jogador4 < jogador3):
    ganhou4=1
    print('O jogador 4 ganhou o jogo.')

pontos=(jogador1,jogador2,jogador3,jogador4)
#verifica maior pedra
if jogador1>jogador2 and jogador1>jogador3 and jogador1>jogador4:
    maiorpedra= jogador1   
if jogador2>jogador1 and jogador2>jogador3 and jogador2>jogador4:
    maiorpedra=jogador2
if jogador3>jogador1 and jogador3>jogador2 and jogador3>jogador4:
    maiorpedra=jogador3
if jogador4>jogador1 and jogador4>jogador2 and jogador4>jogador3:
    maiorpedra=jogador4 
#verifica menor pedra
if jogador1<jogador2 and jogador1<jogador3 and jogador1<jogador4:
    menorpedra=jogador1   
if jogador2<jogador1 or jogador2<jogador3 or jogador2<jogador4:
    menorpedra=jogador2
if jogador3<jogador1 or jogador3<jogador2 or jogador3<jogador4:
    menorpedra=jogador3
if jogador4<jogador1 or jogador4<jogador2 or jogador4<jogador3:
    menorpedra=jogador4

#exibe maior, menor e pontos ordenados
pontosordenados=sorted(pontos)
print('A maior pedra foi: ',maiorpedra)
print('A menor pedra foi: ',menorpedra)
print('Pontos ordenados:',pontosordenados)



