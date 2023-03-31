from flask_restful import Resource, reqparse
from app.models.profissionais_editora import ProfissionaisEditoraModel
from app.models.user import UserModel
from app.utils.sendEmail import sendEmail
from datetime import date
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
atributos.add_argument('perfil_ativo', type=str, help="perfil_ativo")
atributos.add_argument('convite', type=int, help="campo de user")


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
        
    @jwt_required()
    def get_by_cpf(self, *args, **kwargs):
        try:
            return  ProfissionaisEditoraModel.get_profissionais_editora_by_cpf(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_profissional_editora_by_nome(self, *args, **kwargs):
        try:
            profissional = ProfissionaisEditoraModel.get_profissionais_editora_nome(str(args[0]))
            if profissional != False :
                  return profissional, 200
            else : return  {'return':'nao ha registro para esse cpf'}, 400
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            cpf = dados['cpf']
            nome = dados['nome'].strip()
            telefone = dados['telefone']
            email = dados['email'].strip()
            FK_perfil_id = dados['FK_perfil_id']
            perfil_ativo = dados['perfil_ativo']
            endereco = dados['endereco']
            convite = dados['convite']
            
            if UserModel.find_by_login(cpf):
                return {'error': 'Profissional da editora ja existente'}, 400
            
            UserModel.create_profissionais_editora(cpf, nome, email, int(telefone), perfil_ativo, convite)

            user = UserModel.find_by_login(cpf)

            salt = UserModel.get_new_salt()

            today = date.today()

            hashconvite = UserModel.password_encrypted(cpf, salt)

            sendEmail(hashconvite, email)

            UserModel.create_convite_acesso(user[0], str(today), hashconvite, salt)

            if UserModel.get_user_profiles_by_user_id(user[0]):
                return {'error':'Usuario ja associado a perfil selecianado'}, 400

            UserModel.associateUserProfile(user[0], FK_perfil_id)
            
            ProfissionaisEditoraModel.create_profissionais_editora(endereco, user[0])
            
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
            perfil_ativo = dados['perfil_ativo']
            endereco = dados['endereco']
            if ProfissionaisEditoraModel.get_profissionais_editora_by_id(args[0]) == False:
                return {'error':'profissional não existente'}, 400
            
            profissionaleditora = ProfissionaisEditoraModel.get_profissionais_editora_by_id(args[0])
            

            UserModel.update_profissionais_editora(cpf, nome, email, int(telefone), perfil_ativo , profissionaleditora[0]['FK_user_id'])
            
            user = UserModel.find_by_login(cpf)

           
            if UserModel.get_user_profiles_by_user_id(user[0]) == False:
                return {'error':'nao existe perfil associado ao usuario cadastrado'}, 400
            
            userProfile = UserModel.get_user_profiles_by_user_id(user[0])


            UserModel.update_associateUserProfile(user[0], FK_perfil_id, userProfile[0]['id'])
            ProfissionaisEditoraModel.update_profissionais_editora(endereco, user[0] , args[0])

            
            return {'updated': nome }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400