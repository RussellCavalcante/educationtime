from flask_restful import Resource, reqparse
from app.models.planoaula import planoAulaModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio ")
atributos.add_argument('ano', type=str, help="campo obrigatorio")
atributos.add_argument('bimestre_escolar', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_etapa_ensino', type=int, help="campo obrigatorio ")
atributos.add_argument('FK_turma_id', type=int, help="campo obrigatorio ")
atributos.add_argument('FK_componente_escola_profissional', type=int, help="campo obrigatorio ")
atributos.add_argument('unidade_tematica', type=str, help="campo obrigatorio ")
atributos.add_argument('conteudo', type=str, help="campo obrigatorio ")
atributos.add_argument('resultado', type=str, help="campo obrigatorio ")
atributos.add_argument('sub_conteudo', type=dict, help="campo obrigatorio ")


class GetPlanoAula(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
        
            return  planoAulaModel.get_planoaula(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                
            return  planoAulaModel.get_planoaula_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def post_planoaula(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            FK_escola_id = dados['FK_escola_id']
            ano = dados['ano'].strip()
            bimestre_escolar = dados['bimestre_escolar'].strip()
            FK_etapa_ensino = dados['FK_etapa_ensino']
            FK_turma_id = dados['FK_turma_id']
            FK_componente_escola_profissional = dados['FK_componente_escola_profissional']
            unidade_tematica = dados['unidade_tematica'].strip()
            conteudo = dados['conteudo'].strip()
            resultado = dados['resultado']
            sub_conteudo = dados['sub_conteudo']
            
            planoAulaModel.create_planoaula(FK_escola_id ,ano, bimestre_escolar, FK_etapa_ensino, FK_turma_id, FK_componente_escola_profissional, unidade_tematica, conteudo, resultado)
            
            planoaula = planoAulaModel.get_agenda_plano_aula_by_last_id(FK_escola_id)

            for i , sub_conteudo in enumerate(sub_conteudo['itens']):
                    planoAulaModel.create_conteudo_planoaula(sub_conteudo['nome'], planoaula[0]['id'])

            return  {'created_plano_aula': bimestre_escolar}, 201
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            FK_escola_id = dados['FK_escola_id']
            ano = dados['ano'].strip()
            bimestre_escolar = dados['bimestre_escolar'].strip()
            FK_etapa_ensino = dados['FK_etapa_ensino']
            FK_turma_id = dados['FK_turma_id']
            FK_componente_escola_profissional = dados['FK_componente_escola_profissional']
            unidade_tematica = dados['unidade_tematica'].strip()
            conteudo = dados['conteudo'].strip()
            resultado = dados['resultado']
            sub_conteudo = dados['sub_conteudo']
            
            planoAulaModel.update_planoaula(FK_escola_id ,ano, bimestre_escolar, FK_etapa_ensino, FK_turma_id, FK_componente_escola_profissional, unidade_tematica, conteudo, resultado, args[0])
            return {'updated': bimestre_escolar }, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
