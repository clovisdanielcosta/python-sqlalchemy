from models import Pessoas, Usuarios

### CRUD nas tabelas

def insere_pessoa():
    pessoa = Pessoas(nome='Costa', idade=47)
    print(pessoa)
    pessoa.save()

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

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

###


if __name__ == '__main__':
    insere_usuario('clovis', '123')
    insere_usuario('daniel', '321')
    consulta_todos_usuarios()
    #insere_pessoa()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoa()
