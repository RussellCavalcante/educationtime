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
atributos.add_argument('password', type=str, required=True, help="campo de senha e obrigatorio")
atributos.add_argument('nome', type=str, help="campo obrigatorio")
atributos.add_argument('email', type=str, help="campo de email e obrigatorio")
atributos.add_argument('phone', type=str, help="campo de telefone")
atributos.add_argument('roles', type=str, help="campo de roles")


class User(Resource):
    #/usuarios/{user_id}
        
    def get(self, user_id):
        # user = UserModel.find_user(user_id)
        
        user = user_id
        if user:
            return user.json()
        return {"message": 'Usuario nao encontrado'}, 404 # not found


    @jwt_required
    def delete(self, user_id):
        # user = UserModel.find_user(user_id)
        user = user_id
        if user:
            try:
                user.delete_user()   
            except:
                 return {'message': 'Desculpe foi possivel deletar'}, 500
            return {'message': 'User deleted'}
        return {'message': 'User not found.' }, 404

class UserRegister(Resource):
    def post(self):
        dados = atributos.parse_args()

        username = dados['username']
        password = dados['password']
        nome = dados['nome']
        email = dados['email']
        roles = dados['roles']
        
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

        UserModel.create_user(nome , email ,username ,encrypted_password, salt, roles)
        # user.save_user()

        return {'message':'Usuario Criado com sucesso!'}, 201


        

class UserLogin(Resource):


    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        username = dados['username'].strip()
        password = dados['password'].strip()


        user = UserModel.find_by_login(username)
        
        salt = UserModel.find_salt_by_id(user)

        if not UserModel.assert_password(user[0], password, salt,):
            return {'status': False}, 400
    
        token_de_acesso = create_access_token(identity=1)
        
        return {'acess_token': token_de_acesso,
                'cpf': username,
                'id': user[0]}, 200
            

class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return jsonify({'message' : 'Deslogado com sucesso!'}), 200  