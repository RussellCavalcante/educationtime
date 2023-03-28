from flask_restful import Resource, reqparse
from app.models.user import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from flask import Flask
from flask import jsonify
# from flask import request

# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import JWTManager

# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('username', type=str, required=True, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('password', type=str, help="campo de senha e obrigatorio")
atributos.add_argument('nome', type=str, help="campo obrigatorio")
atributos.add_argument('email', type=str, help="campo de email e obrigatorio")
atributos.add_argument('phone', type=str, help="campo de telefone")
atributos.add_argument('FK_perfil_id', type=int, help="campo de perfil_id")


class User(Resource):
    #/usuarios/{user_id}
        
    def get(self, user_id):
        # user = UserModel.find_user(user_id)
        
        user = user_id
        if user:
            return user.json()
        return {"message": 'Usuario nao encontrado'}, 404 # not found

    @jwt_required()
    def get_convite_by_hashconvite(self, *args, **kwargs):
        try:
            convite = UserModel.get_hash_by_hash(str(args[0]))
            if convite != False :
                    conviteId = UserModel.get_convite_by_id(convite[0]['id'])
                    return conviteId, 200
            
            elif convite == False : return  {'return':'convite invalido'}, 200


        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_all_hash_convites(self, *args, **kwargs):
        try:
            convite = UserModel.get_all_hash_convites()
            if convite != False : 
                    return convite, 200
            elif convite == False : return  {'return':'nao possui registros'}, 200


        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required
    def delete(self, user_id):
        # user = UserModel.find_user(user_id)
        try:

            user = user_id
            if user:
                try:
                    user.delete_user()   
                except:
                    return {'message': 'Desculpe foi possivel deletar'}, 500
                return {'message': 'User deleted'}
            return {'message': 'User not found.' }, 404
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

class UserRegister(Resource):
    def post(self):
        try:
            dados = atributos.parse_args()

            username = dados['username']
            password = dados['password']
            nome = dados['nome']
            email = dados['email']
            FK_perfil_id = dados['FK_perfil_id']

            if UserModel.find_by_login(dados['username']):
                return {'message': "Esse usuario '{}' ja existe.".format(dados['username'])}
            
            salt = UserModel.get_new_salt()

            encrypted_password = UserModel.password_encrypted(password, salt)
            # print(encrypted_password)

            # print(salt)

            # input()

            if not UserModel.email_validator(dados['email']):
                return {'message': "Email '{}' esta invalido.".format(dados["email"])}, 400

            UserModel.create_user(nome , email ,username ,encrypted_password, salt)
 
            id = UserModel.find_by_login(dados['username'])
           
            UserModel.associateUserProfile(id[0], FK_perfil_id) 

            return {'message':'Usuario Criado com sucesso!'}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
class ProfissionalEducacaoRegister(Resource):
    def post_profisional_educacao(self):
        try:

            dados = atributos.parse_args()

            username = dados['username']
            password = dados['password']
            nome = dados['nome']
            email = dados['email']
            roles = dados['funcao']
            
            if UserModel.find_by_login(dados['username']):
                return {'message': "Esse usuario '{}' ja existe.".format(dados['username'])}
            
            salt = UserModel.get_new_salt()

            # print(username, password)
            # input()
            

            encrypted_password = UserModel.password_encrypted(password, salt)
                    
            if not UserModel.email_validator(dados['email']):
                return {'message': "Email '{}' esta invalido.".format(dados["email"])}, 400

            # dados = {**dados, **{ 'salt': salt, 'password': encrypted_password }}

            # user = UserModel(**dados)

            UserModel.create_profissional_educacao_(nome , email ,username ,encrypted_password, salt, roles)
            # user.save_user()

            return {'message':'Usuario Criado com sucesso!'}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        

class UserLogin(Resource):


    @classmethod
    def post(cls):
        try:
            dados = atributos.parse_args()

            username = dados['username'].strip()
            password = dados['password'].strip()


            user = UserModel.find_by_login(username)
            
            salt = UserModel.find_salt_by_id(user)

            if not UserModel.assert_password(user[0], password, salt):
                return {'status': "login incorreto por favor refazer login"}, 400
        
            token_de_acesso = create_access_token(identity=1)
            
            return {'acess_token': token_de_acesso,
                    'cpf': username,
                    'id': user[0]}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400   

class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return jsonify({'message' : 'Deslogado com sucesso!'}), 200  