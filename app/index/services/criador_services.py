from ..models import CustomUser


def listar_criador():
    criadores = CustomUser.objects.all()
    return criadores


def listar_criador_id(id):
    criador = CustomUser.objects.get(id=id)
    return criador


def remover_criador(criador):
    criador.delete()


def cadastrar_criador(criador):
    CustomUser.objects.create(username=criador.username, email_organizacao=criador.email_organizacao, organizacao=criador.organizacao, data_nascimento=criador.data_nascimento,
                            cargo=criador.cargo)


def editar_criador(criador, criador_novo):
    criador.username = criador_novo.username
    criador.email_organizacao = criador_novo.email_organizacao
    criador.data_nascimento = criador_novo.data_nascimento
    criador.organizacao = criador_novo.organizacao
    criador.cargo = criador_novo.cargo
    criador.save(force_update=True)  # FORÇA A ATUALIZAÇÃO DOS DADOS
