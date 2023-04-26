from flask_restful import Resource, reqparse
from app.models.indicadores import IndicadoresModel
from app.models.user import UserModel
from app.utils.contrucotorEmail import constructorEmail
from app.utils.sendEmail import sendEmailModel
from datetime import date

from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('cpf', type=str, required=True, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('nome', type=str, help="campo obrigatorio")
atributos.add_argument('email', type=str, help="campo de email e obrigatorio")
atributos.add_argument('telefone', type=int, help="campo de telefone")
atributos.add_argument('FK_perfil_id', type=int, help="campo de perfil_id")
atributos.add_argument('data_inicio', type=str, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('data_fim', type=str, help="campo de email e obrigatorio")
atributos.add_argument('FK_secretaria_municipio_id', type=int, help="FK_secretaria_municipal")
atributos.add_argument('FK_user_id', type=int, help="campo de user")
atributos.add_argument('perfil_ativo', type=int, help="campo de user")


class IndicadoresServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            estudante = IndicadoresModel.get(**kwargs), 200
            if estudante[0] == False:
                return {'error':'Nao existe registro para essa solicitação.'}, 400
            else : return estudante
            
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_escolaridade_educadores(self, *args, **kwargs):
        try:
            escolaridade = IndicadoresModel.get_escolaridade_educadores(**kwargs), 200
            if escolaridade[0] == False:
                return {'error':'Nao existe registro para essa solicitação.'}, 400
            else : return escolaridade
        except:
            return {'error': 'verifique a requisição !'}, 400
        
        
    @jwt_required()
    def get_acoes_agenda_diretoria(self, *args, **kwargs):
        try:
            escolaridade = IndicadoresModel.get_acoes_agenda_diretoria(**kwargs), 200
            if escolaridade[0] == False:
                return {'error':'Nao existe registro para essa solicitação.'}, 400
            else : return escolaridade
        except:
            return {'error': 'verifique a requisição !'}, 400
        
    @jwt_required()
    def get_satisfacao(self, *args, **kwargs):
        try:
            escolaridade = IndicadoresModel.get_satisfacao(**kwargs), 200
            if escolaridade[0] == False:
                return {'error':'Nao existe registro para essa solicitação.'}, 400
            else : return escolaridade
        except:
            return {'error': 'verifique a requisição !'}, 400

