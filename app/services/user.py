from flask_restful import Resource, reqparse
from app.models.user import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from datetime import date
from datetime import datetime
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
atributos.add_argument('cpf', type=str, required=True, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('password', type=str, help="campo de senha e obrigatorio")
atributos.add_argument('nome', type=str, help="campo obrigatorio")
atributos.add_argument('email', type=str, help="campo de email e obrigatorio")
atributos.add_argument('telefone', type=str, help="campo de telefone")
atributos.add_argument('FK_perfil_id', type=int, help="campo de perfil_id")
# atributos.add_argument('date', type=str, help="campo obrigatorio")
atributos.add_argument('navegador', type=str, help="campo de email e obrigatorio")
atributos.add_argument('ip', type=str, help="campo de telefone")
atributos.add_argument('date_logout', type=str, help="campo de email e obrigatorio")


class User(Resource):
    #/usuarios/{user_id}
        
    def get(self, user_id):
        # user = UserModel.find_user(user_id)
        
        user = user_id
        if user:
            return user.json()
        return {"message": 'Usuario nao encontrado'}, 404 # not found

    def get_convite_by_hashconvite(self, *args, **kwargs):
        # try:
            convite = UserModel.get_hash_by_hash(str(args[0]))
            if convite != False :
                    if convite[0]['status'] == 'expirado':
                        return {"error":"convite expirado"}, 400
                    
                    data_envio = convite[0]['data_envio'].split('-')
                    today = str(date.today()).split('-')
                    
                    data1 = datetime(int(data_envio[0]), int(data_envio[1]), int(data_envio[2]))
                    data2 = datetime(int(today[0]), int(today[1]), int(today[2]))

                    difdata = data2 - data1
                
                    if int(str(difdata).split(':')[0]) > 30:
                        UserModel.update_status_convite_acesso('expirado',convite[0]['id'])
                        return{'error':'convite expirado'}

                    if convite[0]['status'] == 'aceito':
                        return {"error":"convite ja aceito"}, 400

                    
                    conviteId = UserModel.get_convite_by_id(convite[0]['id'])
                    return conviteId, 200
            
            elif convite == False : return  {'error':'convite invalido'}, 400


        # except:
        #     return { 'error': 'verifique a requisição !' }, 400
        
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

            cpf = dados['cpf']
            password = dados['password']
            nome = dados['nome']
            email = dados['email']
            FK_perfil_id = dados['FK_perfil_id']

            if UserModel.find_by_login(dados['cpf']):
                return {'message': "Esse usuario '{}' ja existe.".format(dados['cpf'])}
            
            salt = UserModel.get_new_salt()

            encrypted_password = UserModel.password_encrypted(password, salt)
            # print(encrypted_password)

            # print(salt)

            # input()

            if not UserModel.email_validator(dados['email']):
                return {'message': "Email '{}' esta invalido.".format(dados["email"])}, 400

            UserModel.create_user(nome , email ,cpf ,encrypted_password, salt)
 
            id = UserModel.find_by_login(dados['cpf'])
           
            UserModel.associateUserProfile(id[0], FK_perfil_id) 

            return {'message':'Usuario Criado com sucesso!'}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
class ProfissionalEducacaoRegister(Resource):
    def post_profisional_educacao(self):
        try:

            dados = atributos.parse_args()

            cpf = dados['cpf']
            password = dados['password']
            nome = dados['nome']
            email = dados['email']
            roles = dados['funcao']
            
            if UserModel.find_by_login(dados['cpf']):
                return {'message': "Esse usuario '{}' ja existe.".format(dados['cpf'])}
            
            salt = UserModel.get_new_salt()

            # print(cpf, password)
            # input()
            

            encrypted_password = UserModel.password_encrypted(password, salt)
                    
            if not UserModel.email_validator(dados['email']):
                return {'message': "Email '{}' esta invalido.".format(dados["email"])}, 400

            # dados = {**dados, **{ 'salt': salt, 'password': encrypted_password }}

            # user = UserModel(**dados)

            UserModel.create_profissional_educacao_(nome , email ,cpf ,encrypted_password, salt, roles)
            # user.save_user()

            return {'message':'Usuario Criado com sucesso!'}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
        

class UserLogin(Resource):


    @classmethod
    def post(cls):
        try:
        
            dados = atributos.parse_args()

            cpf = dados['cpf'].strip()
            password = dados['password']
            navegador = dados['navegador']
            ip = dados['ip']

            if not UserModel.find_by_login(cpf):
                return {'status': "Por favor, verifique suas credenciais de acesso."}, 400
            
            user = UserModel.find_by_login(cpf)
            
            salt = UserModel.find_salt_by_id(user)

            if not UserModel.assert_password(user[0], password, salt):
                return {'status': "Por favor, verifique suas credenciais de acesso."}, 400
        
            token_de_acesso = create_access_token(identity=1)

            dateNow = datetime.today()

            IdLog = UserModel.create_log_login(user[0], dateNow, navegador, ip)


            return {'acess_token': token_de_acesso,
                    'cpf': cpf,
                    'IdLog':IdLog,
                    'id': user[0]}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400   

class UserLogout(Resource):
    
    
    @jwt_required()
    def post(self,*args, **kwargs):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        dateNow = datetime.today()
        logId = UserModel.get_log_autenticacao_by_last_id(args[0])
        UserModel.update_log_login( dateNow, logId[0]['id'] )
        return jsonify({'message' : 'Deslogado com sucesso!'}), 200  
    
class UserEdit(Resource):


    @classmethod
    def update(cls, *args, **kwargs):
        try:
            dados = atributos.parse_args()

            cpf = dados['cpf']
            password = dados['password']
            nome = dados['nome']
            email = dados['email']
            telefone = dados['telefone']
            # FK_perfil_id = dados['FK_perfil_id']

            # if UserModel.find_by_login(dados['cpf']):
            #     return {'message': "Esse usuario '{}' ja existe.".format(dados['cpf'])}
            
            salt = UserModel.get_new_salt()

            encrypted_password = UserModel.password_encrypted(password, salt)

            if not UserModel.email_validator(dados['email']):
                return {'message': "Email '{}' esta invalido.".format(dados["email"])}, 400

            UserModel.update_user(cpf, nome , email ,telefone ,encrypted_password, salt, args[0])
 
            # id = UserModel.find_by_login(dados['cpf'])
           
            # UserModel.associateUserProfile(id[0], FK_perfil_id) 
            today = date.today()

            UserModel.update_convite_acesso(str(today), 'aceito', args[0])

            return {'message':f'Usuario {nome} atualizado com sucesso!'}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400