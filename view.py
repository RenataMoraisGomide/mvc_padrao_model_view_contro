from controller import PessoaController

while True:
    decisao =int(input('Digite 1 para salvar uma pessoa ou digite 2 para ver a pessoa salva e 3 para sair: '))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade: ')
        cpf = input('Digite o seu CPF: ')

        if PessoaController.cadastrar(nome, idade, cpf):
            print('Usuário cadastrado com sucesso!')
        else:
            print('Digite valores válidos')