from flask_restful import Resource, reqparse
from app.models.tarefacasa import TarefaCasaModel 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_conteudo_plano_aula_id', type=int, help="campo obrigatorio ")
atributos.add_argument('tarefas', type=dict, help="campo obrigatorio ")


class TarefaCasaServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  TarefaCasaModel.get_tarefa_casa(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        

    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_conteudo_plano_aula_id = dados['FK_conteudo_plano_aula_id']

            tarefas = dados['tarefas']
           
            for i , tarefa in enumerate(tarefas['itens']):
                TarefaCasaModel.create_tarefa_casa(FK_conteudo_plano_aula_id, tarefa['nome_tarefa'], tarefa['data_entrega'])
                        

            return  {'status': f'tarefas criadas para o FK_conteudo_plano_aula_id : {FK_conteudo_plano_aula_id}' }, 201
        
        except:

            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_conteudo_plano_aula_id = dados['FK_conteudo_plano_aula_id']

            tarefas = dados['tarefas']
           
            TarefaCasaModel.delete_tarefa_casa(FK_conteudo_plano_aula_id)

            for i , tarefa in enumerate(tarefas['itens']):
                TarefaCasaModel.create_tarefa_casa(FK_conteudo_plano_aula_id, tarefa['nome_tarefa'], tarefa['data_entrega'])
                        
            return  {'updated': f'tarefas atualizadas para o FK_conteudo_plano_aula_id : {FK_conteudo_plano_aula_id}' }, 200

        except:
            return { 'error': 'verifique a requisição !' }, 400