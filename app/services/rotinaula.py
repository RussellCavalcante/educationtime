from flask_restful import Resource, reqparse
from app.models.rotinaaula import RotinaAulaModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('nome_rotina', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio")
atributos.add_argument('ano', type=str, help="campo obrigatorio ")
atributos.add_argument('momentos', type=dict, help="campo obrigatorio ")
atributos.add_argument('turma_compoenente', type=dict, help="campo obrigatorio ")


class GetrotinaAula(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  RotinaAulaModel.get_rotina_aula(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                
            return  RotinaAulaModel.get_rotinaaula_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post_rotinaoaula(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            nome_rotina = dados['nome_rotina'].strip()
            FK_escola_id = dados['FK_escola_id']
            ano_letivo = dados['ano']
            momentos = dados['momentos']
            turma_compoenente = dados['turma_compoenente']
            
            rotina_aula = RotinaAulaModel.create_rotinaaula(nome_rotina, FK_escola_id, ano_letivo)
            
            for i , momento in enumerate(momentos['itens']):
                RotinaAulaModel.create_momento( momento['nome_momento'],momento['ordem'], momento['descricao'])
            
            for i , turma_compoenente in enumerate(turma_compoenente['itens']):
                RotinaAulaModel.associate_rotina_componente_turma( rotina_aula, turma_compoenente['tumar_profissional_componente'])
            
            return  {'id': rotina_aula ,'nome_rotina': nome_rotina}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            nome = dados['nome'].strip()
            FK_turma_id = dados['FK_turma_id'].strip()
            FK_profissional_id = dados['FK_profissional_id'].strip()
            FK_momento_id = dados['FK_momento_id']
            FK_momento_id = dados['FK_componente_curricular_id'].strip()
            update_date = dados['update_date'].strip()
            current_date = dados['current_date'].strip()

            RotinaAulaModel.update_rotinaaula(nome ,FK_turma_id, FK_profissional_id, FK_momento_id, FK_momento_id, update_date, current_date, args[0])
            return {'updated': nome }, 200

        except:
            return { 'error': 'verifique a requisição !' }, 400