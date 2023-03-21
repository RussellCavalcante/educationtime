from flask_restful import Resource, reqparse
from app.models.escolaridade_educadores import EscolaridadeEducadoresModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_user_id', type=int, help="campo obrigatorio fk_user_id ")
atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio escola ")
atributos.add_argument('escolaridade', type=str, help="campo obrigatorio")
atributos.add_argument('ano_conclusao', type=str, help="campo obrigatorio")
atributos.add_argument('nome_instituicao', type=str, help="campo obrigatorio")


class EscolaridadeEducadoresaServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return  EscolaridadeEducadoresModel.get_escolaridade_educador(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    # @jwt_required()
    # def get_escolaridade_educador_by_id(self, *args, **kwargs):
    #     try:
                    
    #         return  EscolaridadeEducadoresModel.get_escolaridade_educador_by_educadores(args[0]), 200
    #     except:
    #         return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_escolaridade_educador_by_educador(self, *args, **kwargs):
        # try:
                    
            return  EscolaridadeEducadoresModel.get_escolaridade_educador_by_educadores(args[0]), 200
        # except:
        #     return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def post(self, *args, **kwargs):
        # try:

            dados = atributos.parse_args()
            
            FK_user_id = dados['FK_user_id']
            FK_escola_id = dados['FK_escola_id']
            escolaridade = dados['escolaridade'].strip()
            ano_conclusao = dados['ano_conclusao'].strip()
            nome_instituicao = dados['nome_instituicao'].strip()

            EscolaridadeEducadoresModel.create_EscolaridadeEducadores(FK_user_id,  FK_escola_id, escolaridade, ano_conclusao, nome_instituicao)
            
            return  {'created_escolaridade': escolaridade}, 200
        # except:
        #     return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            
            FK_user_id = dados['FK_user_id']
            FK_escola_id = dados['FK_escola_id']
            escolaridade = dados['escolaridade'].strip()
            ano_conclusao = dados['ano_conclusao'].strip()
            nome_instituicao = dados['nome_instituicao'].strip()


            EscolaridadeEducadoresModel.update_escolaridade_educador(FK_user_id, FK_escola_id,  escolaridade, ano_conclusao, nome_instituicao ,args[0])
            
            return {'updated_escolaridade_educador': FK_user_id }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400