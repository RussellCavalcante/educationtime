from flask_restful import Resource, reqparse
from app.models.profissional_educacao import ProfissionaisEducacaoModel
from app.models.user import UserModel

from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('cpf', type=str, required=True, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('nome', type=str, help="campo obrigatorio")
atributos.add_argument('email', type=str, help="campo de email e obrigatorio")
atributos.add_argument('telefone', type=int, help="campo de telefone")
atributos.add_argument('FK_perfil_id', type=int, help="campo de perfil_id")
# atributos.add_argument('FK_user_id', type=str, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('FK_escola_id', type=int, help="campo de email e obrigatorio")
atributos.add_argument('perfil_ativo', type=str, help="perfil_ativo")
# atributos.add_argument('FK_user_id', type=int, help="campo de user")


class ProfissionaisEducacaoServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return  ProfissionaisEducacaoModel.get_profissionais_educacao(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
            return  ProfissionaisEducacaoModel.get_profissionais_educacao_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    # @jwt_required()
    # def get_by_muncipio_id(self, *args, **kwargs):
    #     try:
    #         return  ProfissionaisEditoraModel.get_dirigente_municipal_by_secretaria_id(args[0]), 200
    #     except:
    #         return { 'error': 'verifique a requisição !' }, 400


    @jwt_required()
    def post(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            cpf = dados['cpf']
            nome = dados['nome'].strip()
            telefone = dados['telefone']
            email = dados['email'].strip()
            FK_perfil_id = dados['FK_perfil_id']
            FK_escola_id = dados['FK_escola_id']
            perfil_ativo = dados['perfil_ativo']
            
            if UserModel.find_by_login(cpf):
                return {'error': 'Profissional de educação ja existente'}, 400
            
            UserModel.create_profissionais_educacao(cpf, nome, email, int(telefone), FK_perfil_id, perfil_ativo)

            user = UserModel.find_by_login(cpf)
            
            ProfissionaisEducacaoModel.create_profissionais_educacao(FK_escola_id, user[0])
            
            return  {'created': nome}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
        

    
    @jwt_required()
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            cpf = dados['cpf']
            nome = dados['nome'].strip()
            telefone = dados['telefone']
            email = dados['email'].strip()
            FK_perfil_id = dados['FK_perfil_id']
            FK_escola_id = dados['FK_escola_id']
            perfil_ativo = dados['perfil_ativo']
            
            profissionaleducacao = ProfissionaisEducacaoModel.get_profissionais_educacao_by_id(args[0])

            UserModel.update_profissionais_educacao(cpf, nome, email, int(telefone), FK_perfil_id, perfil_ativo, profissionaleducacao[0]['user_id'])
            user = UserModel.find_by_login(cpf)
            ProfissionaisEducacaoModel.update_profissionais_educacao(FK_escola_id, user[0] , args[0])
            
            return {'updated': nome }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400