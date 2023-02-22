from flask_restful import Resource, reqparse
from app.models.planoaula import planoAulaModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('bimestre_escolar', type=str, help="campo obrigatorio ")
atributos.add_argument('etapa_ensino', type=str, help="campo obrigatorio")
atributos.add_argument('ano', type=str, help="campo obrigatorio ")
atributos.add_argument('FK_unidade_tematica_id', type=int, help="campo obrigatorio ")
atributos.add_argument('conteudo', type=str, help="campo obrigatorio ")


class GetPlanoAula(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  planoAulaModel.get_planoaula(), 200

    @jwt_required()
    def post_planoaula(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        bimestre_escolar = dados['bimestre_escolar'].strip()
        etapa_ensino = dados['etapa_ensino'].strip()
        ano = dados['ano'].strip()
        FK_unidade_tematica_id = dados['FK_unidade_tematica_id']
        conteudo = dados['conteudo'].strip()
        
        planoAulaModel.create_planoaula(bimestre_escolar ,etapa_ensino, ano, FK_unidade_tematica_id, conteudo)
        
        return  {'created': bimestre_escolar}, 201
    