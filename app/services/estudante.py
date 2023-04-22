from flask_restful import Resource, reqparse
from app.models.estudante import estudanteModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('cod_nacional_estudante', type=int, help="campo obrigatorio")
atributos.add_argument('nome', type=str, help="campo obrigatorio")
atributos.add_argument('data_nascimento', type=str, help="campo obrigatorio ")
atributos.add_argument('tipo_aluno', type=str, help="campo obrigatorio ")
atributos.add_argument('nee', type=int, help="campo obrigatorio nee ")
atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio int ")


class GetEstudante(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return  estudanteModel.get_estudante(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_cod(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_cod(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_estudante_by_turma_by_escola_id(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_by_turma_by_escola_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_nome(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_nome(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_estudante_turma_id(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_turma_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def post_estudante(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            cod_nacional_estudante = dados['cod_nacional_estudante']
            nome = dados['nome'].strip()
            data_nascimento = dados['data_nascimento'].strip()
            tipo_aluno = dados['tipo_aluno'].strip()
            nee = dados['nee']
            FK_escola_id = dados['FK_escola_id']

            estudanteModel.create_estudante(cod_nacional_estudante ,nome, data_nascimento, tipo_aluno, nee, FK_escola_id)
            
            return  {'created': nome}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            
            cod_nacional_estudante = dados['cod_nacional_estudante']
            nome = dados['nome'].strip()
            data_nascimento = dados['data_nascimento'].strip()
            tipo_aluno = dados['tipo_aluno']
            nee = dados['nee']
            FK_escola_id = dados['FK_escola_id']

            estudanteModel.update_estudante(cod_nacional_estudante ,nome, data_nascimento, tipo_aluno, nee, FK_escola_id, args[0])
            
            return {'updated': nome }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400