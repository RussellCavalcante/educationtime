from flask_restful import Resource, reqparse
from app.models.profissionais_editora import ProfissionaisEditoraModel
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
atributos.add_argument('endereco', type=str, help="endereco")
# atributos.add_argument('FK_user_id', type=int, help="campo de user")


class ProfissionaisEditoraServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return  ProfissionaisEditoraModel.get_profissionais_editora(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
            return  ProfissionaisEditoraModel.get_profissionais_editora_by_id(args[0]), 200
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
            endereco = dados['endereco']
            
            if UserModel.find_by_login(cpf):
                return {'error': 'Profissional da editora ja existente'}, 400
            
            UserModel.create_profissionais_editora(cpf, nome, email, int(telefone), FK_perfil_id)

            user = UserModel.find_by_login(cpf)
            
            ProfissionaisEditoraModel.create_profissionais_editora(FK_escola_id, endereco, user[0])
            
            return  {'created': nome}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
        

    
    @jwt_required()
    def update(self, *args, **kwargs):
        # try:

            dados = atributos.parse_args()
            cpf = dados['cpf']
            nome = dados['nome'].strip()
            telefone = dados['telefone']
            email = dados['email'].strip()
            FK_perfil_id = dados['FK_perfil_id']

            # FK_user_id = dados['FK_user_id']
            FK_escola_id = dados['FK_escola_id']
            endereco = dados['endereco']
            
            profissionaleditora = ProfissionaisEditoraModel.get_profissionais_editora_by_id(args[0])
            print(profissionaleditora)
            input()
            
            UserModel.update_profissionais_editora(cpf, nome, email, int(telefone), FK_perfil_id, profissionaleditora[0]['FK_user_id'])
            user = UserModel.find_by_login(cpf)
            ProfissionaisEditoraModel.update_profissionais_editora(FK_escola_id, endereco, user[0] , args[0])
            
            return {'updated': nome }, 200
        
        # except:
        #     return { 'error': 'verifique a requisição !' }, 400