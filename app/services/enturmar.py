from flask_restful import Resource, reqparse
from app.models.enturmar import EnturmarModel
from app.models.user import UserModel

from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('FK_turma_id', type=int, help="campo de telefone")
atributos.add_argument('Fk_estudante_id', type=dict, help="campo de perfil_id")


class EnturmarServices(Resource):

    @jwt_required()
    def post(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            FK_turma_id = dados['FK_turma_id']
            Fk_estudante_id = dados['Fk_estudante_id']
            
            
            for i , estudante in enumerate(Fk_estudante_id['estudantes']):
                EnturmarModel.create_enturmar( FK_turma_id, estudante)
            
            return  {'created': FK_turma_id}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
        

    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            FK_turma_id = dados['FK_turma_id']
            Fk_estudante_id = dados['Fk_estudante_id']
            

            enturmar = EnturmarModel.get_FK_turma_id_enturmar(FK_turma_id)

            # print(enturmar)
            # input()
            manter = []
            excluirAssociacao = []
            novos = []
            for element in enturmar:
                if element not in Fk_estudante_id['estudantes']:
                    excluirAssociacao.append(element)
                    EnturmarModel.delete_enturmar(element)
                else:
                    manter.append(element) 

            for adicionar in Fk_estudante_id['estudantes']:
    
                if adicionar not in manter:
                    novos.append(adicionar)
                    EnturmarModel.create_enturmar(FK_turma_id,adicionar)

            # print(excluirAssociacao)
            # print(manter)
            # print(novos)
            # input()
            
            return {'updated': {FK_turma_id: {'estudantes': Fk_estudante_id['estudantes']} }}, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400