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

@avaliable_route.route('/municipio/<int:id>', methods=['GET'])

def get_municipio(id):    
    from app.services.municipio import GetMunicipio
    
    _Get_services = GetMunicipio()
    
    return _Get_services.get(id)

@avaliable_route.route('/SecretariaMunicipal', methods=['GET'])

def get_secretaria_municipal():    
    from app.services.secretaria_municipal import GetSecretariamunicipal
    
    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.get()

@avaliable_route.route('/SecretariaMunicipal/Inserir', methods=['POST'])

def post_secretaria_municipal():    
    from app.services.secretaria_municipal import GetSecretariamunicipal
    
    _Get_services = GetSecretariamunicipal()
    
    return _Get_services.post()

@avaliable_route.route('/Escolas', methods=['GET'])

def get_escola():    
    from app.services.escola import GetEscola
    
    _Get_services = GetEscola()
    
    return _Get_services.get()

@avaliable_route.route('/Escolas/Inserir', methods=['POST'])

def post_escola():    
    from app.services.escola import GetEscola
    
    _Get_services = GetEscola()
    
    return _Get_services.post()