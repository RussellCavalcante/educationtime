from flask_restful import Resource, reqparse
from app.models.frequencia_estudante import FrequenciaEstudanteModel 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_conteudo_plano_aula_id', type=int, help="campo obrigatorio ")
atributos.add_argument('nome_tarefa', type=str, help="campo obrigatorio ")
atributos.add_argument('data_entrega', type=str, help="campo obrigatorio ")


class FrequenciaEstudanteServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  FrequenciaEstudanteModel.get_tarefa_casa(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        

    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_conteudo_plano_aula_id = dados['FK_conteudo_plano_aula_id']
            nome_tarefa = dados['nome_tarefa']
            data_entrega = dados['data_entrega']

            
            idIdadeSerie = FrequenciaEstudanteModel.create_tarefa_casa(FK_conteudo_plano_aula_id, nome_tarefa, data_entrega)
            

            return  {'id': idIdadeSerie }, 201
        
        except:

            return { 'error': 'verifique a requisição !' }, 400
    
   