from flask_restful import Resource, reqparse
from app.models.frequencia_estudante import FrequenciaEstudanteModel 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_componente_educador_turma_id', type=int, help="campo obrigatorio ")
atributos.add_argument('mes', type=str, help="campo obrigatorio ")
atributos.add_argument('estudantes', type=dict, help="campo obrigatorio ")


class FrequenciaEstudanteServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  FrequenciaEstudanteModel.get_frequencia_estudante(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        

    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_componente_educador_turma_id = dados['FK_componente_educador_turma_id']
            mes = dados['mes']
            estudantes = dados['estudantes']
            

            
            idFrequencia= FrequenciaEstudanteModel.create_frequencia(FK_componente_educador_turma_id, mes)
            
            for i , estudante in enumerate(estudantes['itens']):
                FrequenciaEstudanteModel.associate_frequencia_estudante(idFrequencia, estudante['FK_estudante_id'], estudante['faltas'], estudante['presenca'])

            return  {'id': idFrequencia }, 201
        
        except:

            return { 'error': 'verifique a requisição !' }, 400
    
   