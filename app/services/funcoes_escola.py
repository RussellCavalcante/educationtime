from flask_restful import Resource, reqparse
from app.models.funcoes_escola import FuncoesEscolaModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('nome', type=str, help="campo obrigatorio")
atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio int ")
atributos.add_argument('FK_profile_id', type=int, help="campo obrigatorio nee ")


class FuncoesEscolaServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return  FuncoesEscolaModel.get_Funcoes_escola(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                    
            return  FuncoesEscolaModel.get_Funcoes_escola_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_Funcoes_escola_by_FK_escola_id(self, *args, **kwargs):
        try:
                    
            return  FuncoesEscolaModel.get_Funcoes_escola_by_FK_escola_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            nome = dados['nome'].strip()
            FK_profile_id = dados['FK_profile_id']
            FK_escola_id = dados['FK_escola_id']

            FuncoesEscolaModel.create_funcao_escola(nome,  FK_escola_id, FK_profile_id,)
            
            return  {'created': nome}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            
            nome = dados['nome'].strip()
            FK_profile_id = dados['FK_profile_id']
            FK_escola_id = dados['FK_escola_id']


            FuncoesEscolaModel.update_funcao_escola(nome, FK_escola_id,  FK_profile_id, args[0])
            
            return {'updated': nome }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400