from flask_restful import Resource, reqparse
from app.models.municipio import MunicipioModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
# atributos.add_argument('username', type=str, required=True, help="campo de nome do usuario e obrigatorio")
# atributos.add_argument('password', type=str, required=True, help="campo de senha e obrigatorio")
# atributos.add_argument('email', type=str, help="campo de email e obrigatorio")
# atributos.add_argument('phone', type=str, help="campo de telefone")

class GetMunicipio(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  MunicipioModel.get_municipios_by_uf(args[0]), 200
