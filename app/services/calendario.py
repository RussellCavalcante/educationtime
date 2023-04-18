from flask_restful import Resource, reqparse
from app.models.calendario import CalendarioModel 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio ")
atributos.add_argument('nome', type=str, help="campo obrigatorio ")
atributos.add_argument('data', type=str, help="campo obrigatorio ")


class CalendarioServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  CalendarioModel.get_tarefa_casa(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        

    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_escola_id = dados['FK_escola_id']
            nome = dados['nome']
            data = dados['data']

            
            calendarioId = CalendarioModel.create_calendario(FK_escola_id, nome, data)
            

            return  {'id': calendarioId }, 201
        
        except:

            return { 'error': 'verifique a requisição !' }, 400
    
   