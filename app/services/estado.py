from flask_restful import Resource, reqparse
from app.models.estado import EstadoModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
# atributos.add_argument('username', type=str, required=True, help="campo de nome do usuario e obrigatorio")
# atributos.add_argument('password', type=str, required=True, help="campo de senha e obrigatorio")
# atributos.add_argument('email', type=str, help="campo de email e obrigatorio")
# atributos.add_argument('phone', type=str, help="campo de telefone")

class GetEstado(Resource):

    @jwt_required()
    def get(self):
        return EstadoModel.get_estados(), 200
