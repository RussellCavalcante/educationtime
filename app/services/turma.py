from flask_restful import Resource, reqparse
from app.models.turma import TurmaModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('cod_turma', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_etapa_ensino_id', type=int, help="campo obrigatorio")
atributos.add_argument('ano_letivo', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_modalidade_id', type=int, help="campo obrigatorio ")
atributos.add_argument('FK_turno_id', type=int, help="campo obrigatorio ")
atributos.add_argument('FK_grau_etapa_ensino_id', type=int, help="campo obrigatorio nome ")

class GetTurma(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            
            return  TurmaModel.get_turma(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                
            return  TurmaModel.get_turma_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post_turma(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            
            # print(dados)
            # input()
            cod_turma = dados['cod_turma'].strip()
            FK_etapa_ensino_id = dados['FK_etapa_ensino_id']
            ano_letivo = dados['ano_letivo'].strip()
            FK_modalidade_id = dados['FK_modalidade_id']
            FK_turno_id = dados['FK_turno_id']
            FK_grau_etapa_ensino_id = dados['FK_grau_etapa_ensino_id']

            TurmaModel.create_turma(cod_turma, FK_etapa_ensino_id, ano_letivo, FK_modalidade_id, FK_turno_id, FK_grau_etapa_ensino_id)
            
            return  {'created': cod_turma}, 201
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_turno(self, *args, **kwargs):
        try:
                
            return  TurmaModel.get_turno(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post_turno(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()
            
            nome = dados['nome'].strip()
            
            TurmaModel.create_turno(nome)
            
            return  {'created': nome}, 201
        
        except:
                return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_modalidade(self, *args, **kwargs):
        try:

            return  TurmaModel.get_modalidade(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def post_modalidade(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            nome = dados['nome'].strip()
            
            TurmaModel.create_modalidade(nome)
            
            return  {'created': nome}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_etapa_ensino(self, *args, **kwargs):
        try:
                
            return  TurmaModel.get_etapa_ensino(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()

            cod_turma = dados['cod_turma'].strip()
            FK_etapa_ensino_id = dados['FK_etapa_ensino_id']
            ano_letivo = dados['ano_letivo'].strip()
            FK_modalidade_id = dados['FK_modalidade_id']
            FK_turno_id = dados['FK_turno_id']
            FK_grau_etapa_ensino_id = dados['FK_grau_etapa_ensino_id']

            TurmaModel.update_turma(cod_turma, FK_etapa_ensino_id, ano_letivo, FK_modalidade_id, FK_turno_id, FK_grau_etapa_ensino_id, args[0])
            return {'updated': cod_turma }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
