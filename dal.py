# A estrutura DAL é a que salva e lê do banco de dados.
# O metodo salva tem que receber um tipo de dado que vai ser o seu model


from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + ' ' + str(pessoa.idade) + ' ' + pessoa.cpf)
    @classmethod
    def ler(cls):
        nome = 'renata'
        idade = 36
        cpf = '234234234356'

        return Pessoa(nome, idade, cpf)

