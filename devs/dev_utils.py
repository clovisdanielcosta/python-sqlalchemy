from devs.dev_models import Programadores, Habilidades, ProgramadorHabilidade

### CRUD na tabelas

# Inserir
def insere_programador(prog_nome, prog_idade, prog_email):
    programador = Programadores (nome=prog_nome, idade=prog_idade, email=prog_email)
    print(programador)
    programador.save()

def insere_habilidade(hab_nome):
    habilidade = Habilidades(nome=hab_nome)
    print(habilidade)
    habilidade.save()

def insere_programador_habilidade(ph_nome_programador, ph_nome_habilidade):
    prog_hab = ProgramadorHabilidade(ph_nome_programador, ph_nome_habilidade)
    print(prog_hab)

# Alterar
def altera_programador(prog_nome, prog_novo_email):
    programador = Programadores.query.filter_by(nome=prog_nome).first()
    programador.email = prog_novo_email
    programador.save()
    print(programador.nome, programador.idade, programador.email)

def altera_habilidade(hab_nome, hab_novo_nome):
    habilidade = Habilidades.query.filter_by(nome=hab_nome).first()
    habilidade.nome = hab_novo_nome
    habilidade.save()
    print(habilidade)

# Excluir
def exclui_programador(prog_nome):
    programador = Programadores.query.filter_by(nome=prog_nome).first()
    programador.delete()

def exclui_habilidade(hab_nome):
    habilidade = Habilidades.query.filter_by(nome=hab_nome).first()
    habilidade.delete()

# Consultar
def consulta_programador(prog_nome):
    programador = Programadores.query.all()
    print(programador)
    programador = Programadores.query.filter_by(nome=prog_nome).first()
    print(programador.nome, programador.idade, programador.email)

def consulta_habilidade(hab_nome):
    habilidade = Habilidades.query.all()
    print(habilidade)
    habilidade = Habilidades.query.filter_by(nome=hab_nome).first()
    print(habilidade.nome, habilidade.idade)

def consulta_programador_habilidade():
    programador_habilidade = ProgramadorHabilidade.query.all()
    print(programador_habilidade)
    programador_habilidade = ProgramadorHabilidade.query.filter_by(nome='Daniel').first()
    print(programador_habilidade.nome,
          programador_habilidade.idade,
          programador_habilidade.email,
          programador_habilidade.habilidade)


###


if __name__ == '__main__':
    insere_programador('Clovis', '47', 'clovis@dev.com')
    insere_programador('Daniel', '38', 'daniel@dev.com')
    insere_programador('Costa', '18', 'costa@dev.com')
    insere_programador('Marcia', '46', 'marcia@dev.com')
    insere_programador('Luísa', '22', 'luisa@dev.com')
    insere_habilidade('Javascript')
    insere_habilidade('Python')
    insere_habilidade('React')
    insere_habilidade('Ruby')
    insere_habilidade('C++')
    insere_habilidade('.Net')
    insere_programador_habilidade('Clovis', 'VBA')
    insere_programador_habilidade('Daniel', 'Javascript')
    insere_programador_habilidade('Costa', 'Python')
    insere_programador_habilidade('Marcia', '.Net')
    insere_programador_habilidade('Luisa', 'React')
