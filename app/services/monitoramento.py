from flask_restful import Resource, reqparse
from app.models.monitoramento import MonitoramentoModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('FK_escola_id', type=int, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('FK_user_id', type=int, help="campo de email e obrigatorio")
atributos.add_argument('ano', type=str, help="campo de telefone")
atributos.add_argument('data', type=str, help="email obrigatorio")
atributos.add_argument('tipo', type=int, help="campo de cod_inep")
atributos.add_argument('Itens', type=dict, help="campo de cod_inep")



class MonitoramentoServices(Resource):
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        # try:
            return  MonitoramentoModel.get_monitoramento_by_id(args[0]), 200
        # except:
        #     return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  MonitoramentoModel.get_monitoramento(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400


    @jwt_required()
    def post(self, *args, **kwargs):
        # try:
            dados = atributos.parse_args()
            
            FK_escola_id = dados['FK_escola_id']
            FK_user_id = dados['FK_user_id']
            ano = dados['ano']
            data = dados['data'].strip()
            tipo = dados['tipo']
            Itens = dados['Itens']

            MonitoramentoModel.create_monitoramento(FK_user_id, FK_escola_id, ano, data, tipo)
            
            monitorar = MonitoramentoModel.get_monitoramento_fatores_by_last_id(FK_escola_id)
            
            for i , monitoramento in enumerate(Itens['itens']):
                MonitoramentoModel.associate_monitoramentos_fatores(monitorar[0]['id'], monitoramento['FK_fatores_id'], monitoramento['score'])
            

            return  {'created_monitoramento': FK_escola_id}, 201
        
        # except:
        #     return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def update(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()
            
            FK_escola_id = dados['FK_escola_id']
            FK_user_id = dados['FK_user_id']
            ano = dados['ano']
            data = dados['data'].strip()
            tipo = dados['tipo']
            Itens = dados['Itens']

            MonitoramentoModel.update_monitoramento(FK_user_id, FK_escola_id, ano, data ,args[0])

            # manter = []
            # excluirAssociacao = []
            # novos = []
            # for element in monitorar:
            #     if element not in Itens['itens']:
            #         excluirAssociacao.append(element)
            #         MonitoramentoModel.delete_monitoramento_fatores(element)
            #     else:
            #         manter.append(element) 

            # for adicionar in Itens['itens']:
                
            #     print(adicionar)
            #     input()

            #     if adicionar not in manter:

                    
            #         novos.append(adicionar)
            #         # if MonitoramentoModel.get_profissionais_escola_componentes(adicionar, FK_escola_id) != False:
            #         #         return {'error':f'componente curricular com id{adicionar} ja existe a esta escola '}
            #         MonitoramentoModel.associate_monitoramentos_fatores(adicionar['FK_monitoramento'], adicionar['FK_fatores'], adicionar)
            return {'updated': FK_escola_id }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

