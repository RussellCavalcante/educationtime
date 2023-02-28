from flask_restful import Resource, reqparse
from app.models.estado import EstadoModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, required=True,help="campo de nome de uf e obrigatorio")
atributos.add_argument('uf', type=str,  required=True, help="campo de uf")


class GetEstado(Resource):

    @jwt_required()
    def get_by_id(self,*args, **kwargs):
        try:
            return EstadoModel.get_estados_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' },400
    @jwt_required()
    def get(self):
        try:
            return EstadoModel.get_estados(), 200
        except:
            return { 'error': 'verifique a requisição !' },400
        
    @jwt_required()
    def post(self):
        try:

            dados = atributos.parse_args()
            
            nome = dados['nome'].strip()
            uf = dados['uf'].strip()
            # ibge = dados['ibge']
            # pais = dados['pais']
            # ddd = dados['ddd']
            
            EstadoModel.create_estado(nome, uf)
            return {'created': nome }, 200
        except:
            return { 'error': 'verifique a requisição !' },400

    def update(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()
            
            nome = dados['nome'].strip()
            uf = dados['uf'].strip()

            EstadoModel.update_estado(nome, uf, args[0])
            return {'updated': nome }, 200
        except:
            return { 'error': 'verifique a requisição !' },400