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



@avaliable_route.route('/Logout', methods=['POST'])
def Logout():
    from app.services.user import UserLogout

    _logout_service = UserLogout()

    return _logout_service.post()    

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
    
    _Get_services = GetEscola()
    
    return _Get_services.get()

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
    
    return _Get_services.post()

@avaliable_route.route('/escolas/update/<int:id>', methods=['PUT'])

def update_escola(id):    
    from app.services.escola import GetEscola

    _Get_services = GetEscola()
    
    return _Get_services.update(id)


@avaliable_route.route('/turmas', methods=['GET'])

def get_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get()

@avaliable_route.route('/turmas/<int:id>', methods=['GET'])

def get_turma_by_id(id):    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_by_id(id)

@avaliable_route.route('/turmas/inserir', methods=['POST'])

def post_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.post_turma()

@avaliable_route.route('/Estudante', methods=['GET'])

def get_estudante():    
    from app.services.estudante import GetEstudante
    
    _Get_services = GetEstudante()
    
    return _Get_services.get()


@avaliable_route.route('/estudante/inserir', methods=['POST'])

def post_estudante():    
    from app.services.estudante import GetEstudante
    
    _Get_services = GetEstudante()
    
    return _Get_services.post_estudante()

@avaliable_route.route('/estudante/update/<int:id>', methods=['PUT'])

def update_estudante(id):    
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


@avaliable_route.route('/planoaula/inserir', methods=['POST'])

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


@avaliable_route.route('/rotinaaula/inserir', methods=['POST'])

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

@avaliable_route.route('/Enturmar/Update/<int:id>', methods=['PUT'])

def update_enturmar(id):    
    from app.services.enturmar import EnturmarServices

    _Get_services = EnturmarServices()
    
    return _Get_services.update(id)

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

