from flask_restful import Resource, reqparse
from app.models.dirigente_municipal import DirigenteMunicipalModel
from app.models.user import UserModel

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


class DirigenteMunicipalServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        # try:
            return  DirigenteMunicipalModel.get_dirigente_municipal(), 200
        # except:
        #     return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
            return  DirigenteMunicipalModel.get_dirigente_municipal_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            cpf = dados['cpf']
            nome = dados['nome'].strip()
            telefone = dados['telefone']
            email = dados['email'].strip()
            FK_perfil_id = dados['FK_perfil_id']

            data_inicio = dados['data_inicio']
            data_fim = dados['data_fim']
            FK_secretaria_municipio_id = dados['FK_secretaria_municipio_id']

            UserModel.create_dirigente_municipal(cpf, nome, email, int(telefone), FK_perfil_id)

            user = UserModel.find_by_login(cpf)
            
            DirigenteMunicipalModel.create_dirigente_municipal(data_inicio, data_fim, FK_secretaria_municipio_id, user[0])
            
            return  {'created': nome}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
        

    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            cpf = dados['cpf']
            nome = dados['nome'].strip()
            telefone = dados['telefone']
            email = dados['email'].strip()
            FK_perfil_id = dados['FK_perfil_id']

            data_inicio = dados['data_inicio']
            data_fim = dados['data_fim']
            FK_secretaria_municipio_id = dados['FK_secretaria_municipio_id']

            user = UserModel.find_by_login(cpf)
            UserModel.update_dirigente_municipal(cpf, nome, email, int(telefone), FK_perfil_id, user[0])
            user = UserModel.find_by_login(cpf)
            DirigenteMunicipalModel.update_dirigente_municipal(data_inicio, data_fim, FK_secretaria_municipio_id, user[0] , args[0])
            
            return {'updated': nome }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400