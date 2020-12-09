'''
seu carlos está abrindo uma lanchonete com apenas atendimento para delivery, 
levando em conta que não haverá loja fisica, o atendimento será online. 
Ajude seu Carlos a montar o cardápio da lanchonete. 
1- Ultilizando tuplas monte todo o cardápio com comidas e bebidas por enquanto não precisa do preço
2- deve mostrar quantos itens existem no cardápio 
3- o programa deve mostrar as comidas e bebidas separadas
'''

lanchonete =('Hamburguer','Coca cola','Cachorro quente','Fanta','Bolo de banana','Antártica','Batata frita','Suco de limão')
i = 0
n = ""

print('---------------------------------')
print('|    Lanchonete do seu Carlos   |')
print('---------------------------------')
print(' LANCHE                 BEBIDA   ')
print('---------------------------------')

#leitura da tupla

for c in range(0, len(lanchonete)):
    if(i != len(lanchonete)):
        print('|',lanchonete[i],'-',lanchonete[i+1],'\t|')
        i += 2
print('----------------------------------')
print('Total de itens do cardápio:',len(lanchonete))
print('----------------------------------')
