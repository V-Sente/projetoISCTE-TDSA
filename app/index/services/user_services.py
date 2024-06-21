from ..models import CustomUser


def listar_user():
    usuarios = CustomUser.objects.all()
    return usuarios


def listar_user_id(id):
    usuario = CustomUser.objects.get(id=id)
    return usuario


def remover_user(usuario):
    usuario.delete()


def cadastrar_user(usuario):
    CustomUser.objects.create(username=usuario.username, sexo=usuario.sexo, data_nascimento=usuario.data_nascimento,
                           email=usuario.email, n_telemovel=usuario.n_telemovel)


def editar_user(usuario, usuario_novo):
    usuario.username = usuario_novo.username
    usuario.sexo = usuario_novo.sexo
    usuario.data_nascimento = usuario_novo.data_nascimento
    usuario.email = usuario_novo.email
    usuario.n_telemovel = usuario_novo.n_telemovel
    usuario.save(force_update=True)  # FORÇA A ATUALIZAÇÃO DOS DADOS
