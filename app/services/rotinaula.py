from flask_restful import Resource, reqparse
from app.models.rotinaaula import RotinaAulaModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('nome', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_turma_id', type=int, help="campo obrigatorio")
atributos.add_argument('FK_profissional_id', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_momento_id', type=int, help="campo obrigatorio ")
atributos.add_argument('FK_componente_curricular_id', type=str, help="campo obrigatorio ")
atributos.add_argument('update_date', type=str, help="campo obrigatorio ")
atributos.add_argument('current_date', type=str, help="campo obrigatorio ")


class GetrotinaAula(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  RotinaAulaModel.get_rotina_aula(), 200
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        
        return  RotinaAulaModel.get_rotinaaula_by_id(args[0]), 200

    @jwt_required()
    def post_rotinaoaula(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        nome = dados['nome'].strip()
        FK_turma_id = dados['FK_turma_id']
        FK_profissional_id = dados['FK_profissional_id']
        FK_momento_id = dados['FK_momento_id']
        FK_componente_curricular_id = dados['FK_componente_curricular_id']
        update_date = dados['update_date'].strip()
        current_date = dados['current_date'].strip()
        
        RotinaAulaModel.create_rotinaaula(nome ,int(FK_turma_id), int(FK_profissional_id),  int(FK_momento_id), int(FK_componente_curricular_id), str(update_date), str(current_date))
        
        return  {'created': nome}, 201
    
    @jwt_required()
    def update(self, *args, **kwargs):
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
