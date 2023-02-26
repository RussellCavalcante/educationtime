from flask_restful import Resource, reqparse
from app.models.etapa_ensino import EtapaEnsinoModel
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


class GetEtapaEnsino(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  EtapaEnsinoModel.get_etapa_ensino(), 200
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        
        return  EtapaEnsinoModel.get_etapa_ensino_by_id(args[0]), 200
    
    @jwt_required()
    def get_grau_etapa_ensino(self, *args, **kwargs):
        
        return  EtapaEnsinoModel.get_grau_etapa_ensino(), 200

    @jwt_required()
    def get_grau_etapa_ensino_by_id(self, *args, **kwargs):
        
        return  EtapaEnsinoModel.get_etapa_ensino_by_id(args[0]), 200
    
    @jwt_required()
    def get_grau_etapa_ensino_by_FK_etapa_ensino(self, *args, **kwargs):
        
        return  EtapaEnsinoModel.get_grau_etapa_ensino_by_FK_etapa_ensino(args[0]), 200
    