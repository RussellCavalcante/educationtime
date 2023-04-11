from flask_restful import Resource, reqparse
from app.models.formacaoservico import FormacaoServicosModel
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


class FormacaoServicoServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  FormacaoServicosModel.get_formacao_servico(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                
            return  FormacaoServicosModel.get_formacao_servico_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post_formacaoservico(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            FK_municipio_id = dados['FK_municipio_id'].strip()
            nome_acao = dados['nome_acao']
            data_inicio = dados['data_inicio']
            data_limite = dados['data_limite']
            escolas = dados['escolas']
            
            rotina_aula = FormacaoServicosModel.create_formacao_servico(nome_rotina, FK_escola_id, ano_letivo)
            
            for i , momento in enumerate(momentos['itens']):
                momento_id = FormacaoServicosModel.create_momento( momento['nome_momento'],momento['ordem'], momento['descricao'])
                FormacaoServicosModel.associate_rotina_aula_momento(rotina_aula, momento_id)


            
            return  {'id': rotina_componente ,'nome_rotina': nome_rotina}, 201
        
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
            idRotina = FormacaoServicosModel.get_rotina_aula_by_rotina_componente_id(args[0])

            
            FormacaoServicosModel.update_formacao_servico(nome_rotina, FK_escola_id, ano_letivo, idRotina[0])

            momento_id_get = FormacaoServicosModel.get_momento_id_by_rotina_aula(idRotina[0])

            for id_moment in momento_id_get:
        
                FormacaoServicosModel.delete_rotina_aula_momento(id_moment)

                FormacaoServicosModel.delete_momentos(id_moment)

                FormacaoServicosModel.delete_relacao_momentos(id_moment)


            for i , momento in enumerate(momentos['itens']):
                momento_id = FormacaoServicosModel.create_momento( momento['nome_momento'],momento['ordem'], momento['descricao'])


                FormacaoServicosModel.associate_rotina_aula_momento(idRotina[0], momento_id)

            FormacaoServicosModel.delete_rotina_componente(idRotina[0])

            for i , turma_compoenente in enumerate(turma_compoenente['itens']):
                rotina_componente = FormacaoServicosModel.associate_rotina_componente_turma( idRotina[0], turma_compoenente['tumar_profissional_componente'])
            
            return  {'id': rotina_componente ,'nome_rotina': nome_rotina}, 201

        except:
            return { 'error': 'verifique a requisição !' }, 400