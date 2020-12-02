#(TUPLA)Um novo funcionário de supermercado quer saber em qual posição se encontra o produto 
#omo 400g no sistema. No sistema existem os seguintes produtos:
#detergente IPE 500ML/ Detergente em Pó Advanced 2,5kg/ Secante para lava louças Finish 250ml / Omo 400g
#O funcionário precisa encontrar a posição do produto para ajudar o cliente em sua compra.
prateleiras =('Detergente IPE 500ML','Detergente em Pó Advanced 2,5kg','Secante para lava louças Finish 250ml','Omo 400g',)
for j in range(0, len(prateleiras)):
    if prateleiras[j] == 'Omo 400g' in prateleiras:
        print("O produto Omo 400g está na prateleira ", j+1)

