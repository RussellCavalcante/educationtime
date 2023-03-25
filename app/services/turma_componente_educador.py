from flask_restful import Resource, reqparse
from app.models.turma_componente_educador import TurmaComponenteEducadorModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('FK_profissionais_componentes_id', type=dict, help="campo de nome do FK_profissional_componente")
atributos.add_argument('FK_turma_id', type=int, help="campo de FK_turma_id e obrigatorio")



class TurmaComponentesEducadoresServices(Resource):
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                
            return  TurmaComponenteEducadorModel.get_turma_componente_educador_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  TurmaComponenteEducadorModel.get_turma_componente_educador(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_by_turma_id(self, *args, **kwargs):
        try:
                
            return  TurmaComponenteEducadorModel.get_turma_componente_educador_by_turma_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()

            FK_turma_id = dados['FK_turma_id']
            FK_profissionais_componentes_id = dados['FK_profissionais_componentes_id']
            # print(FK_profissionais_componentes_id)
            # input()
           
            for i , profissional in enumerate(FK_profissionais_componentes_id['profissionais_componentes_id']):
                TurmaComponenteEducadorModel.create_turma_componente_educador(profissional, FK_turma_id)
            
            return  {'created_TurmaComponenteEducador': FK_profissionais_componentes_id['profissionais_componentes_id']}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def update(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()
            
            FK_profissionais_componentes_id = dados['FK_profissionais_componentes_id']
            FK_turma_id = dados['FK_turma_id']

            enturmar = TurmaComponenteEducadorModel.get_componente_educador_FK_turma_id_(FK_turma_id)
            manter = []
            excluirAssociacao = []
            novos = []
            for element in enturmar:
                if element not in FK_profissionais_componentes_id['profissionais_componentes_id']:
                    excluirAssociacao.append(element)
                    TurmaComponenteEducadorModel.delete_turma_componente_educador(element)
                else:
                    manter.append(element) 

            for adicionar in FK_profissionais_componentes_id['profissionais_componentes_id']:
                

                if adicionar not in manter:
                    novos.append(adicionar)
                    TurmaComponenteEducadorModel.create_turma_componente_educador(adicionar, FK_turma_id)


            # TurmaComponenteEducadorModel.update_turma_componente_educador(FK_profissional_componente_id, FK_turma_id, args[0])
            return {'updated': FK_profissionais_componentes_id }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

