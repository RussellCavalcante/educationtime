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

@avaliable_route.route('/uf/inserir', methods=['POST'])

def post_uf():    
    from app.services.estado import GetEstado

    _Get_services = GetEstado()
    
    return _Get_services.post()

@avaliable_route.route('/municipio/<int:id>', methods=['GET'])

def get_municipio_by(id):    
    from app.services.municipio import GetMunicipio
    
    _Get_services = GetMunicipio()
    
    return _Get_services.get(id)

@avaliable_route.route('/municipio', methods=['GET'])

def get_municipio():    
    from app.services.municipio import GetMunicipio
    
    _Get_services = GetMunicipio()
    
    return _Get_services.get_all()

@avaliable_route.route('/municipio/inserir/<int:id>', methods=['POST'])

def post_municipio_by_uf(id):    
    from app.services.municipio import GetMunicipio
    
    _Get_services = GetMunicipio()
    
    return _Get_services.post(id)


@avaliable_route.route('/secretariamunicipal', methods=['GET'])

def get_secretaria_municipal():    
    from app.services.secretaria_municipal import GetSecretariamunicipal
    
    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.get()

@avaliable_route.route('/secretariamunicipal/inserir', methods=['POST'])

def post_secretaria_municipal():    
    from app.services.secretaria_municipal import GetSecretariamunicipal
    
    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.post()

@avaliable_route.route('/escolas', methods=['GET'])

def get_escola():    
    from app.services.escola import GetEscola
    
    _Get_services = GetEscola()
    
    return _Get_services.get()

@avaliable_route.route('/escolas/inserir', methods=['POST'])

def post_escola():    
    from app.services.escola import GetEscola
    
    _Get_services = GetEscola()
    
    return _Get_services.post()

@avaliable_route.route('/turmas', methods=['GET'])

def get_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get()

@avaliable_route.route('/turmas/inserir', methods=['POST'])

def post_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.post_turma()

@avaliable_route.route('/turmas/turno', methods=['GET'])

def get_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_turno()

@avaliable_route.route('/turmas/turno/inserir', methods=['POST'])

def post_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.post_turno()

@avaliable_route.route('/turmas/modalidade', methods=['GET'])

def get_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_modalidade()

@avaliable_route.route('/turmas/modalidade/inserir', methods=['POST'])

def post_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.post_modalidade()

@avaliable_route.route('/turmas/etapaEnsino', methods=['GET'])

def get_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.get_etapa_ensino()

@avaliable_route.route('/turmas/etapaEnsino/inserir', methods=['POST'])

def post_turma():    
    from app.services.turma import GetTurma
    
    _Get_services = GetTurma()
    
    return _Get_services.post_etapa_ensino()