from flask import Flask, jsonify, Blueprint, request

from app.services.user import *
from app import server, banco, config

avaliable_route = Blueprint('avaliable_route', __name__)

@avaliable_route.route('/', methods=['GET'])
def started():    
    
    return {'build!':'run aplication success'}, 200


@avaliable_route.route('/Login', methods=['POST'])
def Login():    
    from app.services.user import UserLogin

    _login_services = UserLogin()
    
    return _login_services.post()



@avaliable_route.route('/Logout/<int:id>', methods=['POST'])
def Logout(id):
    from app.services.user import UserLogout

    _logout_service = UserLogout()

    return _logout_service.post(id)    

@avaliable_route.route('/Login/Cadastro', methods=['POST'])
def register():
    from app.services.user import UserRegister

    _register_service = UserRegister()

    return _register_service.post()    

@avaliable_route.route('/uf', methods=['GET'])

def get_uf():    
    from app.services.estado import GetEstado

    _Get_services = GetEstado()
    
    return _Get_services.get()

@avaliable_route.route('/uf/<int:id>', methods=['GET'])

def get_uf_by(id):    
    from app.services.estado import GetEstado

    _Get_services = GetEstado()
    
    return _Get_services.get_by_id(id)


@avaliable_route.route('/uf/inserir', methods=['POST'])

def post_uf():    
    from app.services.estado import GetEstado

    _Get_services = GetEstado()
    
    return _Get_services.post()

@avaliable_route.route('/uf/update/<int:id>', methods=['PUT'])

def update_uf(id):    
    from app.services.estado import GetEstado

    _Get_services = GetEstado()
    
    return _Get_services.update(id)

@avaliable_route.route('/municipio/uf/<int:id>', methods=['GET'])

def get_municipio_by_uf(id):    
    from app.services.municipio import GetMunicipio
    
    _Get_services = GetMunicipio()
    
    return _Get_services.get_by_uf_id(id)

@avaliable_route.route('/municipio/<int:id>', methods=['GET'])

def get_municipio_by(id):    
    from app.services.municipio import GetMunicipio
    
    _Get_services = GetMunicipio()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/municipio', methods=['GET'])

def get_municipio():    
    from app.services.municipio import GetMunicipio
    
    _Get_services = GetMunicipio()
    
    return _Get_services.get_all()

@avaliable_route.route('/municipio/inserir', methods=['POST'])

def post_municipio_by_uf():    
    from app.services.municipio import GetMunicipio
    
    _Get_services = GetMunicipio()
    
    return _Get_services.post()

@avaliable_route.route('/municipio/update/<int:id>', methods=['PUT'])

def update_municipio(id):    
    from app.services.municipio import GetMunicipio

    _Get_services = GetMunicipio()
    
    return _Get_services.update(id)

@avaliable_route.route('/secretariamunicipal', methods=['GET'])

def get_secretaria_municipal():    
    from app.services.secretaria_municipal import GetSecretariamunicipal
    
    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.get()

@avaliable_route.route('/secretariamunicipal/<int:id>', methods=['GET'])

def get_secretaria_municipal_by_id(id):    
    from app.services.secretaria_municipal import GetSecretariamunicipal
    
    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/secretariamunicipal/municipio/<int:id>', methods=['GET'])

def get_secretaria_municipal_by_municipio_id(id):    
    from app.services.secretaria_municipal import GetSecretariamunicipal
    
    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.get_by_municipio_id(id)

@avaliable_route.route('/secretariamunicipal/inserir', methods=['POST'])

def post_secretaria_municipal():    
    from app.services.secretaria_municipal import GetSecretariamunicipal
    
    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.post()

@avaliable_route.route('/secretariamunicipal/update/<int:id>', methods=['PUT'])

def update_secretaria_municipal(id):    
    from app.services.secretaria_municipal import GetSecretariamunicipal

    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.update(id)

@avaliable_route.route('/escolas', methods=['GET'])

def get_escola():    
    from app.services.escola import GetEscola
    kwargs = request.args.to_dict()
    _Get_services = GetEscola()

    return _Get_services.get(request.args.get('IdLog'), **kwargs)

@avaliable_route.route('/escolas/<int:id>', methods=['GET'])

def get_escola_by(id):    
    from app.services.escola import GetEscola
    
    _Get_services = GetEscola()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/escolas/municipio/<int:id>', methods=['GET'])

def get_by_muncipio_id(id):    
    from app.services.escola import GetEscola
    
    _Get_services = GetEscola()
    
    return _Get_services.get_escola_by_muncipio_id(id)

@avaliable_route.route('/escolas/inserir', methods=['POST'])

def post_escola():    
    from app.services.escola import GetEscola
    
    _Get_services = GetEscola()        

    return _Get_services.post(request.args.get('IdLog'))

@avaliable_route.route('/escolas/update/<int:id>', methods=['PUT'])

def update_escola(id):    
    from app.services.escola import GetEscola

    _Get_services = GetEscola()
    
    return _Get_services.update(id, request.args.get('IdLog'))


@avaliable_route.route('/turmas', methods=['GET'])

def get_turma():    
    from app.services.turma import GetTurma
    kwargs = request.args.to_dict()
    _Get_services = GetTurma()
    
    return _Get_services.get(**kwargs)

@avaliable_route.route('/turmas/<int:id>', methods=['GET'])

def get_turma_by_id(id):    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/turmas/escola/<int:id>', methods=['GET'])

def get_turma_by_escola(id):    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_by_escola(id)

@avaliable_route.route('/turmas/inserir', methods=['POST'])

def post_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.post_turma()

@avaliable_route.route('/Estudante', methods=['GET'])

def get_estudante():    
    from app.services.estudante import GetEstudante
    kwargs = request.args.to_dict()
    _Get_services = GetEstudante()
    
    return _Get_services.get(**kwargs)


@avaliable_route.route('/Estudante/Cadastro', methods=['POST'])

def post_estudante_cadastro():    
    from app.services.estudante import GetEstudante
    
    _Get_services = GetEstudante()
    
    return _Get_services.post_estudante()

@avaliable_route.route('/Estudante/Update/<int:id>', methods=['PUT'])

def update_estudante_cadastro(id):    
    from app.services.estudante import GetEstudante
    
    _Get_services = GetEstudante()
    
    return _Get_services.update(id)



@avaliable_route.route('/turno', methods=['GET'])

def get_turno():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_turno()

@avaliable_route.route('/modalidade', methods=['GET'])

def get_modalidade():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_modalidade()


@avaliable_route.route('/etapaEnsino', methods=['GET'])

def get_turma_etapa_ensino():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_etapa_ensino()

@avaliable_route.route('/turmas/update/<int:id>', methods=['PUT'])

def update_turma(id):    
    from app.services.turma import GetTurma

    _Get_services = GetTurma()
    
    return _Get_services.update(id)


@avaliable_route.route('/planoaula', methods=['GET'])

def get_planoaula():    
    from app.services.planoaula import GetPlanoAula
    
    _Get_services = GetPlanoAula()
    
    return _Get_services.get()

@avaliable_route.route('/planoaula/<int:id>', methods=['GET'])

def get_planoaula_by(id):    
    from app.services.planoaula import GetPlanoAula
    
    _Get_services = GetPlanoAula()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/planoaula/turma', methods=['GET'])

def get_planoaula_by_turma():    
    from app.services.planoaula import GetPlanoAula
    kwargs = request.args.to_dict()
    _Get_services = GetPlanoAula()
    
    return _Get_services.get_by_turma_id(**kwargs)


@avaliable_route.route('/PlanoaAula/Cadastro', methods=['POST'])

def post_plano_aula():    
    from app.services.planoaula import GetPlanoAula
    
    _Get_services = GetPlanoAula()
    
    return _Get_services.post_planoaula()

@avaliable_route.route('/planoaula/update/<int:id>', methods=['PUT'])

def update_plano_aula(id):    
    from app.services.planoaula import GetPlanoAula

    _Get_services = GetPlanoAula()
    
    return _Get_services.update(id)

@avaliable_route.route('/rotinaaula', methods=['GET'])

def get_rotinaula():    
    from app.services.rotinaula import GetrotinaAula
    
    _Get_services = GetrotinaAula()
    
    return _Get_services.get()

@avaliable_route.route('/rotinaaula/<int:id>', methods=['GET'])

def get_rotinaula_by(id):    
    from app.services.rotinaula import GetrotinaAula
    
    _Get_services = GetrotinaAula()
    
    return _Get_services.get_by_id(id)


@avaliable_route.route('/RotinaAula/Cadastro', methods=['POST'])

def post_rotin_aula():    
    from app.services.rotinaula import GetrotinaAula
    
    _Get_services = GetrotinaAula()
    
    return _Get_services.post_rotinaoaula()

@avaliable_route.route('/rotinaaula/update/<int:id>', methods=['PUT'])

def update_rotin_aula(id):    
    from app.services.rotinaula import GetrotinaAula

    _Get_services = GetrotinaAula()
    
    return _Get_services.update(id)

@avaliable_route.route('/rotinaaula/momento', methods=['GET'])

def get_momento():    
    from app.services.momento import GetMomento
    
    _Get_services = GetMomento()
    
    return _Get_services.get()

@avaliable_route.route('/rotinaaula/momento/<int:id>', methods=['GET'])

def get_momento_by(id):    
    from app.services.momento import GetMomento
    
    _Get_services = GetMomento()
    
    return _Get_services.get_by_id(id)


@avaliable_route.route('/rotinaaula/momento/inserir', methods=['POST'])

def post_momento():    
    from app.services.momento import GetMomento
    
    _Get_services = GetMomento()
    
    return _Get_services.post_momemnto()

@avaliable_route.route('/rotinaaula/momento/update/<int:id>', methods=['PUT'])

def update_momento(id):    
    from app.services.momento import GetMomento

    _Get_services = GetMomento()
    
    return _Get_services.update(id)

@avaliable_route.route('/rotina_aula_momento', methods=['GET'])

def get_rotina_aula_momento():    
    from app.services.rotina_aula_momento import GetRotinaAulaMomento
    
    _Get_services = GetRotinaAulaMomento()
    
    return _Get_services.get()

@avaliable_route.route('/rotina_aula_momento/<int:id>', methods=['GET'])

def get_rotina_aula_momento_by(id):    
    from app.services.rotina_aula_momento import GetRotinaAulaMomento
    
    _Get_services = GetRotinaAulaMomento()
    
    return _Get_services.get_by_id(id)


@avaliable_route.route('/rotina_aula_momento/inserir', methods=['POST'])

def post_rotina_aula_momento():    
    from app.services.rotina_aula_momento import GetRotinaAulaMomento
    
    _Get_services = GetRotinaAulaMomento()
    
    return _Get_services.post_momemnto()

@avaliable_route.route('/rotina_aula_momento/update/<int:id>', methods=['PUT'])

def update_rotina_aula_momento(id):    
    from app.services.rotina_aula_momento import GetRotinaAulaMomento

    _Get_services = GetRotinaAulaMomento()
    
    return _Get_services.update(id)

@avaliable_route.route('/etapa_ensino', methods=['GET'])

def get_etapa_ensino():    
    from app.services.etapa_ensino import GetEtapaEnsino
    
    _Get_services = GetEtapaEnsino()
    
    return _Get_services.get()

@avaliable_route.route('/etapa_ensino/<int:id>', methods=['GET'])

def get_etapa_ensino_by(id):    
    from app.services.etapa_ensino import GetEtapaEnsino
    
    _Get_services = GetEtapaEnsino()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/grau_etapa_ensino', methods=['GET'])

def get_grau_etapa_ensino():    
    from app.services.etapa_ensino import GetEtapaEnsino
    
    _Get_services = GetEtapaEnsino()
    
    return _Get_services.get_grau_etapa_ensino()

@avaliable_route.route('/grau_etapa_ensino/<int:id>', methods=['GET'])

def get_grau_etapa_ensino_by(id):    
    from app.services.etapa_ensino import GetEtapaEnsino
    
    _Get_services = GetEtapaEnsino()
    
    return _Get_services.get_grau_etapa_ensino_by_id(id)

@avaliable_route.route('/grau_etapa_ensino/fk_etapa_ensino/<int:id>', methods=['GET'])

def get_grau_etapa_ensino_by_fk_etapa_ensino(id):    
    from app.services.etapa_ensino import GetEtapaEnsino
    
    _Get_services = GetEtapaEnsino()
    
    return _Get_services.get_grau_etapa_ensino_by_FK_etapa_ensino(id)

@avaliable_route.route('/perfil', methods=['GET'])

def get_perfil():    
    from app.services.perfil import PerfilServices
    
    _Get_services = PerfilServices()
    
    return _Get_services.get()

@avaliable_route.route('/perfil/<int:id>', methods=['GET'])

def get_perfil_by(id):    
    from app.services.perfil import PerfilServices
    
    _Get_services = PerfilServices()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/perfil/user/<int:id>', methods=['GET'])

def get_perfil_by_user_id(id):    
    from app.services.perfil import PerfilServices
    
    _Get_services = PerfilServices()
    
    return _Get_services.get_by_user_id(id)

@avaliable_route.route('/perfil/Cadastro', methods=['POST'])

def post_perfil():    
    from app.services.perfil import PerfilRegister
    
    _Get_services = PerfilRegister()
    
    return _Get_services.post()

@avaliable_route.route('/perfil/Cadastro/<int:id>', methods=['PUT'])

def update_perfil_register(id):    
    from app.services.perfil import PerfilRegister
    
    _Get_services = PerfilRegister()
    
    return _Get_services.update(id)

@avaliable_route.route('/perfil/perfilRoles/<int:id>', methods=['GET'])

def get_perfilRoles_by_perfil_id(id):    
    from app.services.perfil import PerfilServices
    
    _Get_services = PerfilServices()
    
    return _Get_services.get_perfilRolesby_perfil_id(id)

@avaliable_route.route('/perfil/perfilRoles', methods=['GET'])

def get_perfilRoles():    
    from app.services.perfil import PerfilServices
    
    _Get_services = PerfilServices()
    
    return _Get_services.get_perfilRoles()

@avaliable_route.route('/perfil/Roles', methods=['GET'])

def get_Roles():    
    from app.services.perfil import PerfilServices
    
    _Get_services = PerfilServices()
    
    return _Get_services.get_Roles()


@avaliable_route.route('/profissionalEducacao/inserir', methods=['POST'])


def post_profissional_educacao():    
    from app.services.user import ProfissionalEducacaoRegister
    
    _Get_services = ProfissionalEducacaoRegister()
    
    return _Get_services.post_profisional_educacao()

@avaliable_route.route('/Dirigente', methods=['GET'])

def get_Dirigente():    
    from app.services.dirigente_municipal import DirigenteMunicipalServices
    
    _Get_services = DirigenteMunicipalServices()
    
    return _Get_services.get()

@avaliable_route.route('/Dirigente/<int:id>', methods=['GET'])

def get_Dirigente_by(id):    
    from app.services.dirigente_municipal import DirigenteMunicipalServices
    
    _Get_services = DirigenteMunicipalServices()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/dirigente/municipio/<int:id>', methods=['GET'])
def get_Dirigente_by_municipio_id(id):    
    from app.services.dirigente_municipal import DirigenteMunicipalServices
    
    _Get_services = DirigenteMunicipalServices()
    
    return _Get_services.get_by_muncipio_id(id)


@avaliable_route.route('/Dirigente/Cadastro', methods=['POST'])

def post_dirigente():    
    from app.services.dirigente_municipal import DirigenteMunicipalServices
    
    _Get_services = DirigenteMunicipalServices()
    
    return _Get_services.post()

@avaliable_route.route('/Dirigente/Update/<int:id>', methods=['PUT'])

def update_dirigente(id):    
    from app.services.dirigente_municipal import DirigenteMunicipalServices

    _Get_services = DirigenteMunicipalServices()
    
    return _Get_services.update(id)

@avaliable_route.route('/Enturmar/Cadastro', methods=['POST'])

def post_enturmar():    
    from app.services.enturmar import EnturmarServices
    
    _Get_services = EnturmarServices()
    
    return _Get_services.post()

@avaliable_route.route('/Enturmar/Update', methods=['PUT'])

def update_enturmar():    
    from app.services.enturmar import EnturmarServices

    _Get_services = EnturmarServices()
    
    return _Get_services.update()

@avaliable_route.route('/estudante/turma/<int:id>', methods=['GET'])

def get_estudante_turma_id(id):
    from app.services.estudante import GetEstudante

    _Get_services = GetEstudante()

    return _Get_services.get_estudante_turma_id(id)

@avaliable_route.route('/Estudante/<int:id>', methods=['GET'])

def get_estudante_by(id):    
    from app.services.estudante import GetEstudante
    
    _Get_services = GetEstudante()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/Estudante/Cod/<int:id>', methods=['GET'])

def get_estudante_cod(id):    
    from app.services.estudante import GetEstudante
    
    _Get_services = GetEstudante()
    
    return _Get_services.get_by_cod(id)

@avaliable_route.route('/Estudante/Turma/Escola/<int:id>', methods=['GET'])

def get_estudante_by_turma_by_escola_id(id):    
    from app.services.estudante import GetEstudante
    
    _Get_services = GetEstudante()
    
    return _Get_services.get_estudante_by_turma_by_escola_id(id)

@avaliable_route.route('/ProfissionaisEditora', methods=['GET'])

def get_ProfissionaisEditora():    
    from app.services.profissionais_editora import ProfissionaisEditoraServices
    
    _Get_services = ProfissionaisEditoraServices()
    
    return _Get_services.get()

@avaliable_route.route('/ProfissionaisEditora/<int:id>', methods=['GET'])

def get_ProfissionaisEditora_by(id):    
    from app.services.profissionais_editora import ProfissionaisEditoraServices
    
    _Get_services = ProfissionaisEditoraServices()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/ProfissionaisEditora/<string:cpf>', methods=['GET'])

def get_ProfissionaisEditora_by_cpf(cpf):    
    from app.services.profissionais_editora import ProfissionaisEditoraServices
    
    _Get_services = ProfissionaisEditoraServices()
    
    return _Get_services.get_by_cpf(cpf)


@avaliable_route.route('/ProfissionaisEditora/nome/<string:nome>', methods=['GET'])

def get_ProfissionaisEditora_by_nome(nome):    
    from app.services.profissionais_editora import ProfissionaisEditoraServices
    
    _Get_services = ProfissionaisEditoraServices()
    
    return _Get_services.get_profissional_editora_by_nome(nome)

@avaliable_route.route('/ProfissionaisEditora/Cadastro', methods=['POST'])

def post_ProfissionaisEditora():    
    from app.services.profissionais_editora import ProfissionaisEditoraServices
    
    _Get_services = ProfissionaisEditoraServices()
    
    return _Get_services.post()


@avaliable_route.route('/ProfissionaisEditora/Update/<int:id>', methods=['PUT'])

def update_ProfissionaisEditora(id):    
    from app.services.profissionais_editora import ProfissionaisEditoraServices

    _Get_services = ProfissionaisEditoraServices()
    
    return _Get_services.update(id)
@avaliable_route.route('/Estudante/Nome/<nome>', methods=['GET'])

def get_estudante_nome(nome):    
    from app.services.estudante import GetEstudante
    
    _Get_services = GetEstudante()
    
    return _Get_services.get_by_nome(nome)

@avaliable_route.route('/ProfissionaisEducacao', methods=['GET'])
def get_ProfissionaisEducacao():    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    kwargs = request.args.to_dict()
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.get(**kwargs)


@avaliable_route.route('/ProfissionaisEducacao/<int:id>', methods=['GET'])

def get_ProfissionaisEducacao_by(id):    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/ProfissionaisEducacao/Componentes/Profissional/<int:id>', methods=['GET'])

def get_componentes_by_profissional(id):    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
   
    if request.args.get('FK_escola_id'):
        return _Get_services.get_componentes_by_profissional_and_escola(id, request.args.get('FK_escola_id'))


    return _Get_services.get_componentes_by_profissional(id)

@avaliable_route.route('/ProfissionaisEducacao/Componentes/Profissional', methods=['GET'])

def get_componentes_by_profissional_escola():    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
   
    if request.args.get('FK_escola_id'):
        return _Get_services.get_componentes_by_profissional_and_escola(request.args.get('FK_escola_id'))


    return _Get_services.get_profisisonal_componentes()

@avaliable_route.route('/ProfissionaisEducacao/<string:cpf>', methods=['GET'])

def get_ProfissionaisEducacao_by_cpf(cpf):    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.get_profissional_educador_by_cpf(cpf)

@avaliable_route.route('/ProfissionaisEducacao/nome/<string:nome>', methods=['GET'])

def get_ProfissionaisEducacao_by_nome(nome):    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.get_profissional_educador_by_nome(nome)


@avaliable_route.route('/ProfissionaisEducacao/Cadastro', methods=['POST'])

def post_ProfissionaisEducacao():    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.post()

@avaliable_route.route('/ProfissionaisEducacao/Update/<int:id>', methods=['PUT'])

def update_ProfissionaisEducacao(id):    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.update(id)

@avaliable_route.route('/AreaDoConhecimento', methods=['GET'])
def get_AreaDoConhecimento():    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.get_area_do_conhecimento()

@avaliable_route.route('/Componente', methods=['GET'])
def get_Componente():    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.get_componente()

@avaliable_route.route('/Componente/AreaDoConhecimento/<int:id>', methods=['GET'])
def get_ComponenteAreaDoConhecimento(id):    
    from app.services.profissional_educacao import ProfissionaisEducacaoServices
    
    _Get_services = ProfissionaisEducacaoServices()
    
    return _Get_services.get_componente_by_area_do_conhecimento(id)

@avaliable_route.route('/FuncoesEscola', methods=['GET'])
def get_FuncoesEscola():    
    from app.services.funcoes_escola import FuncoesEscolaServices
    # print(request.args.get('email'))
    # input()
    _Get_services = FuncoesEscolaServices()
    
    return _Get_services.get()

@avaliable_route.route('/FuncoesEscola/<int:id>', methods=['GET'])

def get_FuncoesEscola_by(id):    
    from app.services.funcoes_escola import FuncoesEscolaServices
    
    _Get_services = FuncoesEscolaServices()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/FuncoesEscola/escola/<int:id>', methods=['GET'])

def get_FuncoesEscola_by_cpf(id):    
    from app.services.funcoes_escola import FuncoesEscolaServices
    
    _Get_services = FuncoesEscolaServices()
    
    return _Get_services.get_Funcoes_escola_by_FK_escola_id(id)


@avaliable_route.route('/FuncoesEscola/Cadastro', methods=['POST'])

def post_FuncoesEscola():    
    from app.services.funcoes_escola import FuncoesEscolaServices
    
    _Get_services = FuncoesEscolaServices()
    
    return _Get_services.post()

@avaliable_route.route('/FuncoesEscola/Update/<int:id>', methods=['PUT'])

def update_FuncoesEscola(id):    
    from app.services.funcoes_escola import FuncoesEscolaServices
    _Get_services = FuncoesEscolaServices()
    
    return _Get_services.update(id)

@avaliable_route.route('/EscolaridadeEducador', methods=['GET'])
def get_EscolaridadeEducador():    
    from app.services.escolaridade_educadores import EscolaridadeEducadoresaServices
    kwargs = request.args.to_dict()
    _Get_services = EscolaridadeEducadoresaServices()
    
    return _Get_services.get(**kwargs)

@avaliable_route.route('/EscolaridadeEducador/educador/<int:id>', methods=['GET'])

def get_EscolaridadeEducador_by_cpf(id):    
    from app.services.escolaridade_educadores import EscolaridadeEducadoresaServices
    
    _Get_services = EscolaridadeEducadoresaServices()
    
    return _Get_services.get_escolaridade_educador_by_educador(id)

@avaliable_route.route('/EscolaridadeEducadores/escola/<int:id>', methods=['GET'])

def get_escolaridade_educadores(id):    
    from app.services.escolaridade_educadores import EscolaridadeEducadoresaServices
    
    _Get_services = EscolaridadeEducadoresaServices()
    
    return _Get_services.get_escolaridade_educadores(id)

@avaliable_route.route('/EscolaridadeEducador/<int:id>', methods=['GET'])

def get_EscolaridadeEducador_by_id(id):    
    from app.services.escolaridade_educadores import EscolaridadeEducadoresaServices
    
    _Get_services = EscolaridadeEducadoresaServices()
    
    return _Get_services.get_escolaridade_educador_by_id(id)

@avaliable_route.route('/EscolaridadeEducador/image/<int:id>', methods=['GET'])

def get_EscolaridadeEducador_image_by_id(id):    
    from app.services.escolaridade_educadores import EscolaridadeEducadoresaServices
    
    _Get_services = EscolaridadeEducadoresaServices()
    
    return _Get_services.get_image_escolaridade_educador_by_id(id)


@avaliable_route.route('/EscolaridadeEducador/Cadastro', methods=['POST'])

def post_EscolaridadeEducador():    
    from app.services.escolaridade_educadores import EscolaridadeEducadoresaServices
    
    _Get_services = EscolaridadeEducadoresaServices()
    
    return _Get_services.post()

@avaliable_route.route('/EscolaridadeEducador/image/Cadastro', methods=['POST'])

def post_image_escolaridade_educador():
    if 'file' not in request.files:
        return jsonify({"message":"Arquivo obrigatório!"}), 500
    file = request.files['file']
    
    if file and config.allowed_file(file.filename) and request.args.get('idEscolaridade'):
        
        from app.services.escolaridade_educadores import EscolaridadeEducadoresaServices
    
        _Get_services = EscolaridadeEducadoresaServices()
        
        return _Get_services.post_image(file.stream.read(), request.args.get('idEscolaridade'), file.filename.rsplit('.', 1)[1].lower())
        

@avaliable_route.route('/EscolaridadeEducador/Update/<int:id>', methods=['PUT'])

def update_EscolaridadeEducador(id):    
    from app.services.escolaridade_educadores import EscolaridadeEducadoresaServices
    _Get_services = EscolaridadeEducadoresaServices()
    
    return _Get_services.update(id)

@avaliable_route.route('/EquipeMonitoramento', methods=['GET'])

def get_EquipeMonitoramento():    
    from app.services.equipe_monitoramento import EquipeMonitoramentoServices
    
    _Get_services = EquipeMonitoramentoServices()
    
    return _Get_services.get()

@avaliable_route.route('/EquipeMonitoramento/<int:id>', methods=['GET'])

def get_EquipeMonitoramento_by_id(id):    
    from app.services.equipe_monitoramento import EquipeMonitoramentoServices
    
    _Get_services = EquipeMonitoramentoServices()
    
    return _Get_services.get_by_id(id)


@avaliable_route.route('/EquipeMonitoramento/Cadastro', methods=['POST'])

def post_EquipeMonitoramento():    
    from app.services.equipe_monitoramento import EquipeMonitoramentoServices
    
    _Get_services = EquipeMonitoramentoServices()
    
    return _Get_services.post()

@avaliable_route.route('/EquipeMonitoramento/Update/<int:id>', methods=['PUT'])

def update_EquipeMonitoramento(id):    
    from app.services.equipe_monitoramento import EquipeMonitoramentoServices
    _Get_services = EquipeMonitoramentoServices()
    
    return _Get_services.update(id)

@avaliable_route.route('/TurmaComponenteEducador', methods=['GET'])

def get_TurmaComponenteEducador():    
    from app.services.turma_componente_educador import TurmaComponentesEducadoresServices
    

    _Get_services = TurmaComponentesEducadoresServices()
    
    if request.args.get('FK_escola_id'):
        return _Get_services.get_componentes_by_profissional_and_escola(request.args.get('FK_escola_id'))

    return _Get_services.get()

@avaliable_route.route('/TurmaComponenteEducador/<int:id>', methods=['GET'])

def get_TurmaComponenteEducador_by_id(id):    
    from app.services.turma_componente_educador import TurmaComponentesEducadoresServices
    
    _Get_services = TurmaComponentesEducadoresServices()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/TurmaComponenteEducador/Turma/<int:id>', methods=['GET'])

def get_TurmaComponenteEducador_by_turma_id(id):    
    from app.services.turma_componente_educador import TurmaComponentesEducadoresServices
    
    _Get_services = TurmaComponentesEducadoresServices()
    
    return _Get_services.get_by_turma_id(id)


@avaliable_route.route('/TurmaComponenteEducador/Cadastro', methods=['POST'])

def post_TurmaComponenteEducador():    
    from app.services.turma_componente_educador import TurmaComponentesEducadoresServices
    
    _Get_services = TurmaComponentesEducadoresServices()
    
    return _Get_services.post()

@avaliable_route.route('/TurmaComponenteEducador/Update/<int:id>', methods=['PUT'])

def update_TurmaComponenteEducador(id):    
    from app.services.turma_componente_educador import TurmaComponentesEducadoresServices
    _Get_services = TurmaComponentesEducadoresServices()
    
    return _Get_services.update(id)

@avaliable_route.route('/convite/<string:convite>', methods=['GET'])

def get_convite_by_hashconvite(convite):    
    from app.services.user import User
    
    _Get_services = User()
    
    return _Get_services.get_convite_by_hashconvite(convite)

@avaliable_route.route('/convites', methods=['GET'])

def get_all_hash_convites():    
    from app.services.user import User
    
    _Get_services = User()
    
    return _Get_services.get_all_hash_convites()

@avaliable_route.route('/convites/UserEdit/<int:id>', methods=['PUT'])

def user_update_by(id):    
    from app.services.user import UserEdit
    _Get_services = UserEdit()
    
    return _Get_services.update(id)

@avaliable_route.route('/Monitoramento', methods=['GET'])

def get_Monitoramento():    
    from app.services.monitoramento import MonitoramentoServices
    
    _Get_services = MonitoramentoServices()
    
    return _Get_services.get()

@avaliable_route.route('/Monitoramento/<int:id>', methods=['GET'])

def get_Monitoramento_by_id(id):    
    from app.services.monitoramento import MonitoramentoServices
    
    _Get_services = MonitoramentoServices()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/Monitoramento/Cadastro', methods=['POST'])

def post_Monitoramento():    
    from app.services.monitoramento import MonitoramentoServices
    
    _Get_services = MonitoramentoServices()
    
    return _Get_services.post()

@avaliable_route.route('/Monitoramento/Update/<int:id>', methods=['PUT'])

def update_Monitoramento(id):    
    from app.services.monitoramento import MonitoramentoServices
    _Get_services = MonitoramentoServices()
    
    return _Get_services.update(id)

@avaliable_route.route('/AgendaDiretoria', methods=['GET'])

def get_AgendaDiretoria():    
    from app.services.agenda_diretoria import AgendaDiretoriaServices
    kwargs = request.args.to_dict()
    _Get_services = AgendaDiretoriaServices()
    
    return _Get_services.get(**kwargs)

@avaliable_route.route('/AgendaDiretoria/<int:id>', methods=['GET'])

def get_AgendaDiretoria_by_id(id):    
    from app.services.agenda_diretoria import AgendaDiretoriaServices
    
    _Get_services = AgendaDiretoriaServices()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/AgendaDiretoria/resultado', methods=['GET'])

def get_AgendaDiretoria_resultado():    
    from app.services.agenda_diretoria import AgendaDiretoriaServices
    
    _Get_services = AgendaDiretoriaServices()
    
    return _Get_services.get_contar_resultado()

@avaliable_route.route('/AgendaDiretoria/Cadastro', methods=['POST'])

def post_AgendaDiretoria():    
    from app.services.agenda_diretoria import AgendaDiretoriaServices
    
    _Get_services = AgendaDiretoriaServices()
    
    return _Get_services.post()

@avaliable_route.route('/AgendaDiretoria/Update/<int:id>', methods=['PUT'])

def update_AgendaDiretoria(id):    
    from app.services.agenda_diretoria import AgendaDiretoriaServices
    _Get_services = AgendaDiretoriaServices()
    
    return _Get_services.update(id)

@avaliable_route.route('/FormacaoServico/Cadastro', methods=['POST'])

def post_FormacaoServico():    
    from app.services.formacaoservico import FormacaoServicoServices
    
    _Get_services = FormacaoServicoServices()
    
    return _Get_services.post_formacaoservico()

@avaliable_route.route('/FormacaoServico', methods=['GET'])

def get_FormacaoServico():    
    from app.services.formacaoservico import FormacaoServicoServices
    kwargs = request.args.to_dict()
    _Get_services = FormacaoServicoServices()
    
    return _Get_services.get(**kwargs)

@avaliable_route.route('/PlanoLeitura/Cadastro', methods=['POST'])

def post_PlanoLeitura():    
    from app.services.planoleitura import PlanoLeituraServices
    
    _Get_services = PlanoLeituraServices()
    
    return _Get_services.post()

@avaliable_route.route('/PlanoLeitura', methods=['GET'])

def get_planoleitura():    
    from app.services.planoleitura import PlanoLeituraServices
    
    _Get_services = PlanoLeituraServices()
    
    return _Get_services.get()

@avaliable_route.route('/NotasSaeb/Cadastro', methods=['POST'])

def post_NotasSaeb():    
    from app.services.notassaeb import NotasSaebServices
    
    _Get_services = NotasSaebServices()
    
    return _Get_services.post()

@avaliable_route.route('/NotasSaeb', methods=['GET'])

def get_post_NotasSaeb():    
    from app.services.notassaeb import NotasSaebServices
    
    _Get_services = NotasSaebServices()

    if request.args.get('FK_escola_id') and request.args.get('ano'):
        return _Get_services.get_notas_saeb_by_FK_escola_id_and_ano(request.args.get('FK_escola_id'), request.args.get('ano'))

    return _Get_services.get()

@avaliable_route.route('/ResultadoAprendizagem/Cadastro', methods=['POST'])

def post_ResultadoAprendizagem():    
    from app.services.resultadoaprendizagem import ResultadoAprendizagemServices
    
    _Get_services = ResultadoAprendizagemServices()
    
    return _Get_services.post()

@avaliable_route.route('/ResultadoAprendizagem', methods=['GET'])

def get_post_ResultadoAprendizagem():    
    from app.services.resultadoaprendizagem import ResultadoAprendizagemServices
    
    _Get_services = ResultadoAprendizagemServices()

    return _Get_services.get()

@avaliable_route.route('/idadeserie/Cadastro', methods=['POST'])

def post_IdadeSerie(): 

        from app.services.idade_serie import IdadeSerieServices

        _Get_services = IdadeSerieServices()

        return _Get_services.post()

@avaliable_route.route('/idadeserie', methods=['GET'])

def get_idadeserie():    
    from app.services.idade_serie import IdadeSerieServices
    kwargs = request.args.to_dict()
    _Get_services = IdadeSerieServices()
    
    return _Get_services.get(**kwargs)

@avaliable_route.route('/TarefaCasa/Cadastro', methods=['POST'])

def post_tarefacasa():    
    from app.services.tarefacasa import TarefaCasaServices
    
    _Get_services = TarefaCasaServices()
    
    return _Get_services.post()

@avaliable_route.route('/TarefaCasa', methods=['GET'])

def get_tarefacasa():    
    from app.services.tarefacasa import TarefaCasaServices
    kwargs = request.args.to_dict()
    _Get_services = TarefaCasaServices()
    
    return _Get_services.get(**kwargs)

@avaliable_route.route('/Calendario/Cadastro', methods=['POST'])

def post_calendario():    
    from app.services.calendario import CalendarioServices
    
    _Get_services = CalendarioServices()
    
    return _Get_services.post()

@avaliable_route.route('/FrequenciaEstudante/Cadastro', methods=['POST'])

def post_frequencia_estudante():    
    from app.services.frequencia_estudante import FrequenciaEstudanteServices
    
    _Get_services = FrequenciaEstudanteServices()
    
    return _Get_services.post()

@avaliable_route.route('/FrequenciaEstudante', methods=['GET'])

def get_frequencia_estudante():    
    from app.services.frequencia_estudante import FrequenciaEstudanteServices
    
    _Get_services = FrequenciaEstudanteServices()
    
    return _Get_services.get()

