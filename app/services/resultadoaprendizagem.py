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
                
            return  ResultadoAprendizagemModel.get_resultado_aprendizagem(), 200
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
            
            nome_rotina = dados['nome_rotina'].strip()
            FK_escola_id = dados['FK_escola_id']
            ano_letivo = dados['ano']
            momentos = dados['momentos']
            turma_compoenente = dados['turma_compoenente']
            # idRotina = ResultadoAprendizagemModel.get_resultado_aprendizagem_by_rotina_componente_id(args[0])

            
            ResultadoAprendizagemModel.update_resultado_aprendizagem(nome_rotina, FK_escola_id, ano_letivo, args[0])

            momento_id_get = ResultadoAprendizagemModel.get_momento_id_by_resultado_aprendizagem(args[0])

            for id_moment in momento_id_get:
        
                ResultadoAprendizagemModel.delete_resultado_aprendizagem_momento(id_moment)

                ResultadoAprendizagemModel.delete_momentos(id_moment)

                ResultadoAprendizagemModel.delete_relacao_momentos(id_moment)


            for i , momento in enumerate(momentos['itens']):
                momento_id = ResultadoAprendizagemModel.create_momento( momento['nome_momento'],momento['ordem'], momento['descricao'])


                ResultadoAprendizagemModel.associate_resultado_aprendizagem_momento(args[0], momento_id)

            ResultadoAprendizagemModel.delete_rotina_componente(args[0])

            for i , turma_compoenente in enumerate(turma_compoenente['itens']):
                rotina_componente = ResultadoAprendizagemModel.associate_rotina_componente_turma( args[0], turma_compoenente['tumar_profissional_componente'])
            
            return  {'id': args[0] ,'nome_rotina': nome_rotina}, 201

        except:
            return { 'error': 'verifique a requisição !' }, 400