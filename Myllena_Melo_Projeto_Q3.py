#(TUPLA) Um bibliotecário precisa indexar a posição de alguns livros novos que chegaram no sistema da biblioteca.
#Após finalizar a indexação, o mesmo precisa localizar a posição dos livros Dom Casmurro e Vidas Secas para informar
#a um determinado usuário. Segue a lista de livros com suas respectivas estantes:
#Dom casmurro- estante 1 /O cortiço - estante 2/ Vidas secas - estante 3/O alienista - estante 4/Macunaíma - estante 5


biblioteca =('Dom Casmurro','Estante 1','O cortiço','Estante 2','Vidas Secas','Estante 3','O Alienista','Estante 5','Macunaíma','Estante 5')
i = 0
n = ""

print('---------------------------------')
print('|     Biblioteca Softlivros     |')
print('---------------------------------')
#leitura da tupla
for c in range(0, len(biblioteca)):
    if(i != len(biblioteca)):
        print('|',biblioteca[i],'=>',biblioteca[i+1],'\t|')
        i += 2
print('----------------------------------')
#busca por valores na tupla
for j in range(0, len(biblioteca)):
    if biblioteca[j] == 'Vidas Secas' in biblioteca:
        print("Vidas Secas pertence a estante: ", j-1)
    if biblioteca[j] == 'Dom Casmurro' in biblioteca:
        print("Dom Casmurro pertence a estante: ", j+1)
