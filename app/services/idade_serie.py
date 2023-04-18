from flask_restful import Resource, reqparse
from app.models.idade_serie import IdadeSerieModel 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio ")
atributos.add_argument('resultado', type=float, help="campo obrigatorio ")
atributos.add_argument('meta', type=float, help="campo obrigatorio ")
atributos.add_argument('acoes', type=dict, help="campo obrigatorio ")

class IdadeSerieServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:

            return  IdadeSerieModel.get(**kwargs), 200
        
        except:
           return { 'error': 'verifique a requisição !' }, 400
        

    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_escola_id = dados['FK_escola_id']
            resultado = dados['resultado']
            meta = dados['meta']
            acoes = dados['acoes']
            
            idIdadeSerie = IdadeSerieModel.create_idade_serie(FK_escola_id, resultado, meta)
            
            for i , acoes in enumerate(acoes['itens']):
                IdadeSerieModel.associate_acao_idade_serie(idIdadeSerie, acoes['nome_acao'], acoes['prazo'])

            return  {'id': idIdadeSerie }, 201
        
        except:

            return { 'error': 'verifique a requisição !' }, 400
    
   