from flask_restful import Resource, reqparse
from app.models.estudante import estudanteModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('cod_nacional_estudante', type=str, help="campo obrigatorio ")
atributos.add_argument('nome', type=int, help="campo obrigatorio")
atributos.add_argument('data_nascimento', type=str, help="campo obrigatorio ")
atributos.add_argument('tipo_aluno_id', type=int, help="campo obrigatorio ")
atributos.add_argument('etapa_ensino_id', type=int, help="campo obrigatorio ")
atributos.add_argument('ano', type=str, help="campo obrigatorio ano ")
atributos.add_argument('nee', type=str, help="campo obrigatorio nee ")
atributos.add_argument('nome_mae_aluno', type=str, help="campo obrigatorio nome_mae_aluno")

class GetEstudante(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  estudanteModel.get_estudante(), 200

    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        
        return  estudanteModel.get_estudante_id(args[0]), 200

    @jwt_required()
    def post_estudante(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        cod_nacional_estudante = dados['cod_nacional_estudante'].strip()
        nome = dados['nome'].strip()
        data_nascimento = dados['data_nascimento'].strip()
        tipo_aluno_id = dados['tipo_aluno_id'].strip()
        ano = dados['ano'].strip()
        nee = dados['nee']
        nome_mae_aluno = dados['nome_mae_aluno'].strip()
        
        estudanteModel.create_estudante(cod_nacional_estudante ,nome, data_nascimento, tipo_aluno_id, ano, nee, nome_mae_aluno)
        
        return  {'created': nome}, 200
    
    @jwt_required()
    def update(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        cod_nacional_estudante = dados['cod_nacional_estudante'].strip()
        nome = dados['nome'].strip()
        data_nascimento = dados['data_nascimento'].strip()
        tipo_aluno_id = dados['tipo_aluno_id'].strip()
        ano = dados['ano'].strip()
        nee = dados['nee']
        nome_mae_aluno = dados['nome_mae_aluno'].strip()

        estudanteModel.create_estudante(cod_nacional_estudante ,nome, data_nascimento, tipo_aluno_id, ano, nee, nome_mae_aluno)
        
        return {'updated': nome }, 200