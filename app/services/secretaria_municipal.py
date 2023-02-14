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

class GetSecretariamunicipal(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  SecretariaMunicipalModel.get_secretaria_municipal(), 200

    @jwt_required()
    def post(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        nome = dados['nome'].strip()
        cnpj = dados['cnpj']
        endereco = dados['endereco'].strip()
        telefone = dados['telefone']
        email = dados['email'].strip()
        SecretariaMunicipalModel.create_secretaria_municipal(nome, cnpj, endereco, telefone, email)
        
        return  {'created': nome}, 201

    

