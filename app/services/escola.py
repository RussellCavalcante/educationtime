from flask_restful import Resource, reqparse
from app.models.escola import EscolaModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('nome_escola', type=str, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('endereco', type=str, help="campo de email e obrigatorio")
atributos.add_argument('telefone', type=int, help="campo de telefone")
atributos.add_argument('email_escola', type=str, help="email obrigatorio")
atributos.add_argument('cod_inep', type=int, help="campo de cod_inep")

class GetEscola(Resource):
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        
        return  EscolaModel.get_escola_by_id(args[0]), 200

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  EscolaModel.get_escola(), 200

    @jwt_required()
    def post(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        nome_escola = dados['nome_escola'].strip()
        endereco = dados['endereco'].strip()
        telefone = dados['telefone']
        email_escola = dados['email_escola'].strip()
        cod_inep = dados['cod_inep']
        EscolaModel.create_escola(nome_escola, endereco, email_escola, telefone, cod_inep)
        
        return  {'created': nome_escola}, 201

    @jwt_required()
    def update(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        nome_escola = dados['nome_escola'].strip()
        endereco = dados['endereco'].strip()
        telefone = dados['telefone']
        email_escola = dados['email_escola'].strip()
        cod_inep = dados['cod_inep']
        
        EscolaModel.update_escola(nome_escola, endereco, email_escola, telefone, cod_inep, args[0])
        return {'updated': nome_escola }, 200

