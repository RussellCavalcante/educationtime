from flask_restful import Resource, reqparse
from app.models.secretaria_municipal import SecretariaMunicipalModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('cnpj', type=int, help="campo de senha e obrigatorio")
atributos.add_argument('endereco', type=str, help="campo de email e obrigatorio")
atributos.add_argument('telefone', type=int, help="campo de telefone")
atributos.add_argument('email', type=str, help="email obrigatorio")
atributos.add_argument('FK_secretaria_UF_id', type=int, help="campo de telefone")
atributos.add_argument('FK_secretaria_municipio_id', type=int, help="email obrigatorio")

class GetSecretariamunicipal(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return  SecretariaMunicipalModel.get_secretaria_municipal(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
            return  SecretariaMunicipalModel.get_secretaria_municipal_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            nome = dados['nome'].strip()
            cnpj = dados['cnpj']
            endereco = dados['endereco'].strip()
            telefone = dados['telefone']
            email = dados['email'].strip()
            FK_secretaria_UF_id = dados['FK_secretaria_UF_id']
            FK_secretaria_municipio_id = dados['FK_secretaria_municipio_id']
            SecretariaMunicipalModel.create_secretaria_municipal(nome, cnpj, endereco, telefone, email, FK_secretaria_UF_id, FK_secretaria_municipio_id)
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
        return  {'created': nome}, 201

    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            nome = dados['nome'].strip()
            cnpj = dados['cnpj']
            endereco = dados['endereco'].strip()
            telefone = dados['telefone']
            email = dados['email'].strip()
            FK_secretaria_UF_id = dados['FK_secretaria_UF_id']
            FK_secretaria_municipio_id = dados['FK_secretaria_municipio_id']

            SecretariaMunicipalModel.update_secretaria_municipal(nome, cnpj, endereco, telefone, email, FK_secretaria_UF_id, FK_secretaria_municipio_id, args[0])
            return {'updated': nome }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400