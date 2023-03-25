from flask_restful import Resource, reqparse
from app.models.equipe_monitoramento import EquipeMonitoramentoModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('FK_user_id', type=int, help="campo de nome do FK_user_id")
atributos.add_argument('Fk_profile_id', type=int, help="campo de Fk_profile_id")
atributos.add_argument('Escolas', type=dict, help="email data_inicio")

class EquipeMonitoramentoServices(Resource):
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                
            return  EquipeMonitoramentoModel.get_equipe_monitoramento_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  EquipeMonitoramentoModel.get_equipe_monitoramento(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_escola_by_muncipio_id(self, *args, **kwargs):
        try:
            return  EquipeMonitoramentoModel.get_by_muncipio_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()
            
            FK_user_id = dados['FK_user_id']
            FK_escola_id = dados['FK_escola_id']
            Fk_profile_id = dados['Fk_profile_id']
            data_inicio = dados['data_inicio'].strip()
            data_fim = dados['data_fim'].strip()

            EquipeMonitoramentoModel.create_equipe_monitoramento(FK_user_id, FK_escola_id, Fk_profile_id, data_inicio, data_fim)
            
            return  {'created_equipe_monitoramento': FK_user_id}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def update(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()
            
            FK_user_id = dados['FK_user_id']
            FK_escola_id = dados['FK_escola_id']
            Fk_profile_id = dados['Fk_profile_id']
            data_inicio = dados['data_inicio'].strip()
            data_fim = dados['data_fim'].strip()
          

            EquipeMonitoramentoModel.update_equipe_monitoramento(FK_user_id, FK_escola_id, Fk_profile_id, data_inicio, data_fim ,args[0])
            return {'updated': FK_user_id }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

