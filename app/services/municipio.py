from flask_restful import Resource, reqparse
from app.models.municipio import MunicipioModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('codigo_ibge', type=str, help="campo de nome de uf e obrigatorio")
atributos.add_argument('nome', type=str, help="campo de uf")

class GetMunicipio(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  MunicipioModel.get_municipios_by_uf(args[0]), 200

    @jwt_required()
    def get_all(self, *args, **kwargs):
        
        return  MunicipioModel.get_municipios_by(), 200

    @jwt_required()
    def post(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        codigo_ibge = dados['codigo_ibge'].strip()
        nome = dados['nome'].strip()
        # ibge = dados['ibge']
        # pais = dados['pais']
        # ddd = dados['ddd']
        
        MunicipioModel.create_municipio(codigo_ibge, nome, args[0])
        return {'created': nome }, 200