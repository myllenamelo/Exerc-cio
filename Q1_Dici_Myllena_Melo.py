'''
Em faculdades é normal os alunos trabalharem para a instituição para ganhar descontos na mensalidade e seu salário.
é comum esses estudantes tratalharem divulgando a instituição e procurando pessoas para efetuarem matriculas e 
participarem de vestibulares para entrar nos cursos que escolheram.
Normalmente o cadastro inicial é feito com caneta e papel, já que é mais facil, rapido e mais seguro quando
se trabalha na rua. Levando em consideração isso, faça um programa que simule a entrada desses dados:
nome,idade, sexo.
o programa deve rodar até o usuario não querer mais. 
- é necessária a validação caso o sexo seja digitado errado. 
-mostrar quantas pessoas cadastradas, a média das idades, quem está acima dessa média. 

'''
cadastro=dict()
cadastros=list()
idades=media=0
while True:
    cadastro ={'Nome':'none','Idade':0,'Sexo':0}
    cadastro['Nome'] = str(input('Insira o nome: '))
    cadastro['Idade'] = int(input('Insira a idade: '))
    idades+=cadastro['Idade']
    cadastro['Sexo'] = str(input('Insira M para mulher ou H para homem: ')).upper()
    if (cadastro['Sexo'] == 'M') or (cadastro['Sexo']== 'H') :
        print('Sexo válido')
    else: print('Sexo inválido')
    cadastros.append(cadastro.copy())
    while True:
        opcao = str(input('Cadastrar +1 usuário? 0-SIM 1-NÃO:'))
        if opcao in '01':
            break
        print ('Você inseriu um valor inválido. Insira novamente o que deseja:')
    if opcao == '1':
        break
print(cadastros)
media=idades / len(cadastros)
print ('Você cadastrou ',len(cadastros),'pessoas.')
print ('A média das idades é ',media)
print ('Pessoas que estão acima da média:')
for i in cadastros:
    if i['Idade']  >= media:
        print ('    ', end='')
        for k,v in i.items():
            print(f' {k} = {v}; ',end='')
        print()
