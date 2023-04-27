from flask_restful import Resource, reqparse
from app.models.notassaeb import NotasSaebModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_escola_id', type=str, help="campo obrigatorio ")
atributos.add_argument('ano', type=int, help="campo obrigatorio")
atributos.add_argument('notas', type=dict, help="campo obrigatorio ")


class NotasSaebServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  NotasSaebModel.get_notas_saeb(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:    
            notas_saeb = NotasSaebModel.get_notas_saeb_by_id(args[0])
            componente = NotasSaebModel.get_notas_saeb_componente_educador_by_id(args[0])
            
            notas_saeb['turma_compoenente'] = componente['turma_compoenente']

            return  notas_saeb, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_notas_saeb_by_FK_escola_id_and_ano(self, *args, **kwargs):
        try:    
            # notas_saeb = NotasSaebModel.get_notas_saeb_by_id(args[0])
            componente = NotasSaebModel.get_notas_saeb_by_FK_escola_id_and_ano(args[0], args[1])
            
            return  componente, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
      
            FK_escola_id = dados['FK_escola_id']
            ano_letivo = dados['ano']
            
            notas = dados['notas']

            if NotasSaebModel.find_by_notassaeb_by_escola_and_ano(FK_escola_id , ano_letivo):
                return {'error':'notas ja cadastradas a escola e ano letivo informados.'}, 400
            
            nota_saeb = NotasSaebModel.create_notas_saeb(FK_escola_id, ano_letivo)
            
            for i , notas in enumerate(notas['itens']):
                NotasSaebModel.associate_notas_saeb_area_conhecimento( notas['FK_area_conehcimento_id'], nota_saeb, notas['nota'])
            
            return  {'id': nota_saeb }, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update(self, *args, **kwargs):
        # try:

            dados = atributos.parse_args()
            
      
            FK_escola_id = dados['FK_escola_id']
            ano_letivo = dados['ano']
            
            notas = dados['notas']

            if NotasSaebModel.find_by_notassaeb(args[0]) == False:
                return {'error':'Nota saeb inexistente verifique se existe.'}, 400
            
            NotasSaebModel.update_notas_saeb(FK_escola_id, ano_letivo, args[0])
            
            # NotasSaebModel.delete_notas_saeb_area_conhecimento(args[0])


            for i , notas in enumerate(notas['itens']):
                if NotasSaebModel.find_by_notassaeb__area_conhecimento(notas['FK_area_conehcimento_id'], args[0]):
                    NotasSaebModel.update_notas_saeb_area_conhecimento( notas['nota'], args[0], notas['FK_area_conehcimento_id'], args[0])
                else:
                    NotasSaebModel.associate_notas_saeb_area_conhecimento( notas['FK_area_conehcimento_id'], args[0], notas['nota'])
            return  {'updated': args[0] }, 201

        # except:
        #     return { 'error': 'verifique a requisição !' }, 400