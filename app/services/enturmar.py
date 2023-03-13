from flask_restful import Resource, reqparse
from app.models.enturmar import EnturmarModel
from app.models.user import UserModel

from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('FK_turma_id', type=int, help="campo de telefone")
atributos.add_argument('Fk_estudante_id', type=int, help="campo de perfil_id")


class EnturmarServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return EnturmarModel.get_enturmar(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
            return EnturmarModel.get_enturmar_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_turma_id(self, *args, **kwargs):
        try:
            return EnturmarModel.get_enturmar_by_turma(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400


    @jwt_required()
    def post(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            FK_turma_id = dados['FK_turma_id']
            Fk_estudante_id = dados['Fk_estudante_id']
            
            
            
            EnturmarModel.create_enturmar( FK_turma_id, Fk_estudante_id)
            
            return  {'created': FK_turma_id}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
        

    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_turma_id = dados['FK_turma_id']
            Fk_estudante_id = dados['Fk_estudante_id']
            
            
            EnturmarModel.update_enturmar(FK_turma_id, Fk_estudante_id , args[0])
            
            return {'updated': FK_turma_id }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400