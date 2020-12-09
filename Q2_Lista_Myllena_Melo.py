'''
Joana deseja fazer uma festa, para isso ela quer fazer uma lista com todos os seus amigos como convidados,
mas joana tem muitos e muitos amigos e se perdeu quando colocou os nomes e já não sabe qual nome adicionou. 
Faça um programa que ajude joana a listar todos os seus amigos, caso já tenha um nome na lista mostrar uma
mensagem para avisar que o nome já existe. No final mostrar a lista completa e quantos convidados joana listou. 
'''
amigo=''
listaFesta=list()
listaFesta = ('Maria','José','João','Terezinha','Pedro','Juca','Mônica','Chico','Magali')
opcao = int(input('''Escolha uma opção: 
        1 - listar convidados
        2 - verificar convidado
        3 - mostrar Nº de convidados
        Digite sua escolha: '''))
if (opcao != 1) and (opcao != 2) and (opcao != 3):
    print('Escolha inválida.')
if (opcao == 1):
    print('LISTA DE CONVIDADOS:')
    print (listaFesta)
if (opcao == 2):
    amigo = str(input("Deseja verificar qual amigo(a)? "))
    if amigo in listaFesta:
        print(f'O convidado(a) {amigo} já está na sua lista.')
    else: print(f'O convidado(a) {amigo} ainda não está na sua lista.')
if (opcao == 3):
    Quantidade = len(listaFesta)
    print ('Você tem ',Quantidade,' amigos(as) na sua lista.')


        
