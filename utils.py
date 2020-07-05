from models import Pessoas, db_session

def insere_pessoa():
    pessoa = Pessoas(nome='Costa', idade=47)
    print(pessoa)
    pessoa.save()

### CRUD na tabelas

def consulta_pessoa():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Daniel').first()
    print(pessoa.nome, pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Daniel').first()
    pessoa.idade = 50
    pessoa.save()
    print(pessoa.nome, pessoa.idade)

def exclui_pessoa():
    pessoa = Pessoas. query.filter_by(nome='Clovis').first()
    pessoa.delete()

###

if __name__ == '__main__':
    #insere_pessoa()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoa()
