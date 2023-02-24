from flask_restful import Resource, reqparse
from app.models.estado import EstadoModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, help="campo de nome de uf e obrigatorio")
atributos.add_argument('uf', type=str, help="campo de uf")


class GetEstado(Resource):

    @jwt_required()
    def get(self):
        return EstadoModel.get_estados(), 200

    @jwt_required()
    def post(self):
        dados = atributos.parse_args()
        
        nome = dados['nome'].strip()
        uf = dados['uf'].strip()
        # ibge = dados['ibge']
        # pais = dados['pais']
        # ddd = dados['ddd']
        
        EstadoModel.create_estado(nome, uf)
        return {'created': nome }, 200

    def update(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        nome = dados['nome'].strip()
        # uf = dados['uf'].strip()
        # ibge = dados['ibge']
        # pais = dados['pais']
        # ddd = dados['ddd']
        print(nome, args)
        input()

        EstadoModel.update_estado(nome, args)
        return {'updated': nome }, 200
