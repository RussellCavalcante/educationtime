from flask_restful import Resource, reqparse
from app.models.municipio import MunicipioModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('codigo_ibge', type=str, help="campo de nome de uf e obrigatorio")
atributos.add_argument('nome', type=str, help="campo de uf")
atributos.add_argument('FK_UF_id', type=int, help="campo de FK_UF_id")

class GetMunicipio(Resource):

    @jwt_required()
    def get_by_uf_id(self, *args, **kwargs):
        
        return  MunicipioModel.get_municipios_by_uf(args[0]), 200

    @jwt_required()
    def get_all(self, *args, **kwargs):
        
        return  MunicipioModel.get_municipios_by(), 200

    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        
        return  MunicipioModel.get_municipios_by_id(args[0]), 200

    @jwt_required()
    def post(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        codigo_ibge = dados['codigo_ibge'].strip()
        nome = dados['nome'].strip()
        FK_UF_id = dados['FK_UF_id']
        # ibge = dados['ibge']
        # pais = dados['pais']
        # ddd = dados['ddd']
        
        MunicipioModel.create_municipio(codigo_ibge, nome, FK_UF_id)
        return {'created': nome }, 200

    @jwt_required()
    def update(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        codigo_ibge = dados['codigo_ibge'].strip()
        nome = dados['nome'].strip()
        FK_UF_id = dados['FK_UF_id']

        MunicipioModel.update_municipio(codigo_ibge, nome, FK_UF_id, args[0])
        return {'updated': nome }, 200
