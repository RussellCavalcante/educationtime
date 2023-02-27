from flask_restful import Resource, reqparse
from app.models.funcoes import FuncoesModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('bimestre_escolar', type=str, help="campo obrigatorio ")
atributos.add_argument('etapa_ensino', type=str, help="campo obrigatorio")
atributos.add_argument('ano', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_unidade_tematica_id', type=int, help="campo obrigatorio ")
atributos.add_argument('conteudo', type=str, help="campo obrigatorio ")


class GetFuncoes(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  FuncoesModel.get_funcoes(), 200
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        
        return  FuncoesModel.get_funcoes_by_id(args[0]), 200
    