from flask_restful import Resource, reqparse
from app.models.equipe_monitoramento import EquipeMonitoramentoModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('FK_user_id', type=int, help="campo de nome do FK_user_id")
atributos.add_argument('Fk_profile_id', type=int, help="campo de Fk_profile_id")
atributos.add_argument('Escolas', type=dict, help="email data_inicio")

class EquipeMonitoramentoServices(Resource):
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:

            return  EquipeMonitoramentoModel.get_equipe_monitoramento_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get(self, *args, **kwargs):
        try:

            return  EquipeMonitoramentoModel.get_equipe_monitoramento(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_escola_by_muncipio_id(self, *args, **kwargs):
        try:
            return  EquipeMonitoramentoModel.get_by_muncipio_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()

            FK_user_id = dados['FK_user_id']
            Escolas = dados['Escolas']
            Fk_profile_id = dados['Fk_profile_id']


            for i , monitoramento in enumerate(Escolas['escolas']):

                EquipeMonitoramentoModel.create_equipe_monitoramento(FK_user_id, monitoramento['FK_escola_id'], Fk_profile_id, monitoramento['data_inicio'], monitoramento['data_fim'])

            return  {'created_equipe_monitoramento': FK_user_id}, 201

        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def update(self, *args, **kwargs):
        # try:
            dados = atributos.parse_args()


            FK_user_id = dados['FK_user_id']
            Escolas = dados['Escolas']
            Fk_profile_id = dados['Fk_profile_id']
            monitorar = []
            manter = []
            excluirAssociacao = []
            novos = []

            for i , monitoramento in enumerate(Escolas['escolas']):

                # print()
                
                equipe =  EquipeMonitoramentoModel.get_equipe_monitoramento_FK_escola_id_and_user_id(monitoramento['FK_escola_id'], FK_user_id)
                # print('equipe',equipe[0])
                # input()
                if equipe != False:
                    monitorar.append(equipe[0])

            print('monitorar',monitorar)
            input()


            for monitoramento in Escolas['escolas']:
                for element in monitorar:
                    

                        if element not in monitoramento['FK_escola_id']:
                            excluirAssociacao.append(element)
                            EquipeMonitoramentoModel.delete_equipe_monitoramento(element)
                        else:
                            manter.append(element)

                for adicionar in monitoramento['FK_escola_id']:


                    if adicionar not in manter:
                        novos.append(adicionar)
                        EquipeMonitoramentoModel.create_equipe_monitoramento(FK_user_id, monitoramento['FK_escola_id'], Fk_profile_id, monitoramento['data_inicio'], monitoramento['data_fim'])

            # EquipeMonitoramentoModel.update_equipe_monitoramento(FK_user_id, FK_escola_id, Fk_profile_id, data_inicio, data_fim ,args[0])
            return {'updated': FK_user_id }, 200

        # except:
        #     return { 'error': 'verifique a requisição !' }, 400

