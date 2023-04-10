from flask_restful import Resource, reqparse
from app.models.perfil import PerfilModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('profile_name', type=str, required=True, help="campo obrigatorio")
atributos.add_argument('FK_roles_id', type=dict, required=True, help="campo obrigatorio")



class PerfilServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return  PerfilModel.get_perfil(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:

            return  PerfilModel.get_perfil_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    @jwt_required()
    def get_by_user_id(self, *args, **kwargs):
        try:

            return  PerfilModel.get_perfil_by_user_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_perfilRolesby_perfil_id(self, *args, **kwargs):
        try:

            return  PerfilModel.get_perfilRoles_by_perfil_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_perfilRoles(self, *args, **kwargs):
        try:

            return  PerfilModel.get_perfilRoles(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_Roles(self, *args, **kwargs):
        try:

            return  PerfilModel.get_Roles(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
class PerfilRegister(Resource):
    def post(self):
        try:
            dados = atributos.parse_args()

            profile_name = dados['profile_name']
            
            FK_roles_id = dados['FK_roles_id']

            if PerfilModel.find_by_profile_name(profile_name):
                return {'message': "Esse perfil '{}' ja existe.".format(profile_name)}
            
            PerfilModel.create_perfil(profile_name)
           
            id = PerfilModel.find_by_profile_name(profile_name)

            for i , role in enumerate(FK_roles_id['roles']):

                PerfilModel.associateProfileRoles(id[0], role['role_id'], role['valor']) 

            return {'message':'Perfil Criado com sucesso!'}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()

            profile_name = dados['profile_name']
            
            FK_roles_id = dados['FK_roles_id']
            # id = PerfilModel.find_by_FK_profile_id(args[0])

            # print(id)
            # input()
            if not PerfilModel.find_by_profile_id(args[0]):
                return {'message': "Esse perfil '{}' nao foi encontrado.".format(profile_name)}, 400    

            PerfilModel.delete_profile_roles(args[0])

            PerfilModel.update_profile(profile_name, args[0])


            for i , role in enumerate(FK_roles_id['roles']):
                
                PerfilModel.associateProfileRoles(args[0], role['role_id'], role['valor'])

            return {'message':'Perfil atualizado com sucesso!'}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400