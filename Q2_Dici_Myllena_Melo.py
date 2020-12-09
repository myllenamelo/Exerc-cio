'''
Na rede SESI, alunos com pai ou mãe fincionário da industria possuem o direito de receber descontos na mensalidade,
digamos que o desconto seja de 10%, faça um programa que simule a matricula de um aluno, onde:
1- insira o nome, ano de nascimento
2- pergunte ao usuario se tem ou não pais fincionários da industria
    -caso não: mostrar nome, ano de nascimento, idade e quando iria terminar o ensino médio.
    -caso sim: continuar as perguntas tais como
        -Número da matricula de funcionário da industria
        -o salário
        -calcular o desconto de 10% na mensalidade com valor de 450 reais
        - mostrar mostrar nome, ano de nascimento, idade e quando iria terminar o ensino médio.
        - mostrar o valor do desconto e quanto vai ficar a mensalidade
'''
#calcula desconto
def desconto (valor=450):
    valordesconto=valor-45
    return valordesconto


nome=str
matricula ={'Nome':'none','Ano Nasc':0,'Idade':0,'Conclusao':0,'Matricula':0,'Salário':0,'Desconto':0,'Mensalidade':0}
matricula['Nome'] = str(input('Insira o nome: '))
matricula['Ano Nasc'] = int(input('Insira o ano de nasc: '))
opcao = int(input('''Tem pai funcionário da industria: 
        0 - SIM
        1 - NÃO
        Digite sua escolha: '''))

if opcao == 1:
    matricula['Idade'] = int(input('Insira sua idade: '))
    matricula['Conclusao'] = int(input('Insira o ano de conclusão: '))
    matricula['Mensalidade'] = 450
    print (matricula)

if opcao == 0:
    matricula['Idade'] = int(input('Insira sua idade: '))
    matricula['Conclusao'] = int(input('Insira o ano de conclusão: '))
    matricula['Matricula'] = int(input('Insira a matrícula de funcionário da indústria: '))
    matricula['Salário'] = int(input('Insira o salário do seu pai/mãe que trabalha na indústria: '))
    matricula['Desconto'] = '10%'
    matricula['Mensalidade'] = desconto(valor=450)
    print (matricula)
    
    
