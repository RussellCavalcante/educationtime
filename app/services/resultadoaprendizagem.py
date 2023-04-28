from flask_restful import Resource, reqparse
from app.models.resultadoaprendizagem import ResultadoAprendizagemModel 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('metas', type=dict, help="campo obrigatorio ")


class ResultadoAprendizagemServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  ResultadoAprendizagemModel.get_resultado_aprendizagem(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:    
            resultado_aprendizagem = ResultadoAprendizagemModel.get_resultado_aprendizagem_by_id(args[0])
            componente = ResultadoAprendizagemModel.get_resultado_aprendizagem_componente_educador_by_id(args[0])
            
            resultado_aprendizagem['turma_compoenente'] = componente['turma_compoenente']

            return  resultado_aprendizagem, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            

            
            metas = dados['metas']
            # nota_saeb = ResultadoAprendizagemModel.create_resultado_aprendizagem(FK_escola_id, ano_letivo)
            
            for i , metas in enumerate(metas['itens']):
                ResultadoAprendizagemModel.update_notas_saeb_area_conhecimento(metas['meta'],metas['FK_notas_saeb_area_conhecimento_id'])
                for i , acoes in enumerate(metas['acoes']):
                    ResultadoAprendizagemModel.associate_resultado_aprendizagem_area_conhecimento( acoes['nome_acao'], acoes['prazo'], metas['FK_notas_saeb_area_conhecimento_id'])

            return  {'id': metas['FK_notas_saeb_area_conhecimento_id'] }, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            
            metas = dados['metas']           
                
            for i , acoes in enumerate(metas['acoes']):

                ResultadoAprendizagemModel.update_resultado_aprendizagem_acoes_status(acoes['status'], acoes['resultado_aprendizagem_acoes__id'])

            return  {'updated': 'Atualizado os status das ações solicitadas' }, 201

        except:
            return { 'error': 'verifique a requisição !' }, 400