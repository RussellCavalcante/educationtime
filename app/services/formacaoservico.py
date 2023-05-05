from flask_restful import Resource, reqparse
from app.models.formacaoservico import FormacaoServicosModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('nome', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_municipio_id', type=int, help="campo obrigatorio")
atributos.add_argument('ano', type=str, help="campo obrigatorio ")
atributos.add_argument('responsavel', type=str, help="campo obrigatorio ")
atributos.add_argument('data_inicio', type=str, help="campo obrigatorio ")
atributos.add_argument('data_limite', type=str, help="campo obrigatorio ")
atributos.add_argument('escolas', type=dict, help="campo obrigatorio ")
atributos.add_argument('profissionais', type=dict, help="campo obrigatorio ")


class FormacaoServicoServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  FormacaoServicosModel.get_formacao_servico(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        

    @jwt_required()
    def get_formacao_servico_profissionais(self, *args, **kwargs):
        try:
                
            return  FormacaoServicosModel.get_formacao_servico_profissional(**kwargs), 200
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
            
            FK_municipio_id = dados['FK_municipio_id']
            nome = dados['nome']
            ano = dados['ano']
            responsavel = dados['responsavel']
            data_inicio = dados['data_inicio']
            data_limite = dados['data_limite']
            escolas = dados['escolas']
            
            formacaoServico = FormacaoServicosModel.create_formacao_servico(FK_municipio_id, ano ,nome, responsavel, data_inicio, data_limite)
            
            for i , escola in enumerate(escolas['itens']):
                FormacaoServicosModel.associate_formacao_servico_escola(formacaoServico, escola['FK_escola_id'])


            
            return  {'created': formacaoServico }, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def post_formacaoservico_escola_profissional(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            FK_profissional_escola_componente_id = dados['profissionais']
            
            for i , profissional in enumerate(FK_profissional_escola_componente_id['itens']):
                FormacaoServicosModel.associate_formacao_servico_escola_profissional(args[0],profissional['FK_profissional_escola_componente_id'])
            
            return  {'created': args[0] }, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_profissional_escola_componente_id = dados['profissionais']
            
            for i , profissional in enumerate(FK_profissional_escola_componente_id['itens']):
                FormacaoServicosModel.update_formacao_servico_educador_componente_escola(profissional['status'],args[0])
            
            return  {'updated': args[0] }, 201
        

        except:
            return { 'error': 'verifique a requisição !' }, 400