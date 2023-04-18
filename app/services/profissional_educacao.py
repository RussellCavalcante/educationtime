from flask_restful import Resource, reqparse
from app.models.profissional_educacao import ProfissionaisEducacaoModel
from app.models.user import UserModel
from app.utils.contrucotorEmail import constructorEmail
from app.utils.sendEmail import sendEmailModel
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
atributos.add_argument('perfil_ativo', type=str, help="perfil_ativo")
atributos.add_argument('componentes_curriculares', type=dict, help="componentes_curriculares")

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
        

    @jwt_required()
    def get_profissional_educador_by_cpf(self, *args, **kwargs):
        try:
            profissional = ProfissionaisEducacaoModel.get_profissionais_escola_componentes_by_cpf(str(args[0]))
            if profissional != False :
                  return profissional, 200
            else : return  {'return':'nao ha registro para esse cpf'}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_componentes_by_profissional_escola(self, *args, **kwargs):
        try:
            profissional = ProfissionaisEducacaoModel.get_componentes_profissional_escola(args[0])
            if profissional != False :
                  return profissional, 200
            else : return  {'return':'nao ha componentes para esse usuario'}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_componentes_by_profissional(self, *args, **kwargs):
        try:
            profissional = ProfissionaisEducacaoModel.get_componentes_by_profissional(args[0])
            if profissional != False :
                  return profissional, 200
            else : return  {'return':'nao ha componentes para esse usuario'}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_componentes_by_profissional_and_escola(self, *args, **kwargs):
        try:
            profissional = ProfissionaisEducacaoModel.get_componentes_profissional_escola(args[0])
            if profissional != False :
                  return profissional, 200
            else : return  {'return':'nao ha componentes para esse usuario'}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_profisisonal_componentes(self, *args, **kwargs):
        try:
            profissional = ProfissionaisEducacaoModel.get_profisisonal_componentes()
            if profissional != False :
                  return profissional, 200
            else : return  {'return':'nao ha componentes para esse usuario'}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    

    @jwt_required()
    def get_area_do_conhecimento(self, *args, **kwargs):
        try:
            return  ProfissionaisEducacaoModel.get_area_do_conhecimento(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_componente(self, *args, **kwargs):
        try:
            return  ProfissionaisEducacaoModel.get_componente(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_componente_by_area_do_conhecimento(self, *args, **kwargs):
        try:
            profissional = ProfissionaisEducacaoModel.get_componente_by_area_do_conhecimento(str(args[0]))
            if profissional != False :
                  return profissional, 200
            else : return  {'return':'nao ha registro para esse cpf'}, 400
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_profissional_educador_by_nome(self, *args, **kwargs):
        try:
            profissional = ProfissionaisEducacaoModel.get_profissionais_educacao_nome(str(args[0]))
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
            FK_escola_id = dados['FK_escola_id']
            perfil_ativo = dados['perfil_ativo']
            componentes_curriculares = dados['componentes_curriculares']
            
            if UserModel.find_by_login(cpf):
                     
                if ProfissionaisEducacaoModel.get_profissionais_educacao_escola_perfil_by_escola_id(FK_escola_id) == False:
                    # print('entrou')
                    # input()
                    user = UserModel.find_by_login(cpf)
                    
                    if ProfissionaisEducacaoModel.get_profissionais_educacao_by_FK_user_id(user[0]) == False:
                        ProfissionaisEducacaoModel.create_profissionais_educacao( user[0])

                    UserModel.associateProfissionalEscolaPerfil(user[0], FK_escola_id, FK_perfil_id)

                    componentizar = ProfissionaisEducacaoModel.get_componentes_id_by_FK_turma_id(FK_escola_id)

                    # print(componentizar)
                    # input()
                    manter = []
                    excluirAssociacao = []
                    novos = []
                    # UserModel.associateUserProfile(user[0], FK_perfil_id)
                    for element in componentizar:
                        if element not in componentes_curriculares['componentes']:
                            excluirAssociacao.append(element)
                            ProfissionaisEducacaoModel.delete_profissionais_escola_componentes(element)
                        else:
                            manter.append(element) 

                    for adicionar in componentes_curriculares['componentes']:
            
                        if adicionar not in manter:
                            novos.append(adicionar)
                            if ProfissionaisEducacaoModel.get_profissionais_escola_componentes(adicionar, FK_escola_id) != False:
                                    return {'error':f'componente curricular com id{adicionar} ja existe a esta escola '}
                            UserModel.associateProfissionalEscolaComponentes(user[0], FK_escola_id, adicionar)
                    # for i , componentes in enumerate(componentes_curriculares['componentes']):
                    #     # print(componentes, ProfissionaisEducacaoModel.get_profissionais_escola_componentes(componentes, FK_escola_id))
                    #     # input()
                    #     if ProfissionaisEducacaoModel.get_profissionais_escola_componentes(componentes, FK_escola_id) != False:
                    #          return {'error':f'componente curricular com id {componentes} ja existe a esta escola '}, 400
                        
                    #     UserModel.associateProfissionalEscolaComponentes(user[0], FK_escola_id, componentes)

                    return  {'created': nome}, 201
                
                elif ProfissionaisEducacaoModel.get_profissionais_educacao_escola_perfil_by_escola_id(FK_escola_id):   
                    return {'error': 'escola ja associada a perfil'}, 400
            
         

            UserModel.create_profissionais_educacao(cpf, nome, email, int(telefone), perfil_ativo)

            user = UserModel.find_by_login(cpf)

            salt = UserModel.get_new_salt()

            today = date.today()

            hashconvite = UserModel.password_encrypted(cpf, salt)

            body = sendEmailModel.conviteAcesso(hashconvite)

            constructorEmail(email, body)

            UserModel.create_convite_acesso(user[0], str(today), hashconvite, salt)
            
            UserModel.associateProfissionalEscolaPerfil(user[0], FK_escola_id, FK_perfil_id)

            UserModel.associateUserProfile(user[0], FK_perfil_id)
            
            ProfissionaisEducacaoModel.create_profissionais_educacao( user[0])

            componentizar = ProfissionaisEducacaoModel.get_componentes_id_by_FK_turma_id(FK_escola_id)

            # print(componentizar)
            # input()
            manter = []
            excluirAssociacao = []
            novos = []
            for element in componentizar:
                if element not in componentes_curriculares['componentes']:
                    excluirAssociacao.append(element)
                    ProfissionaisEducacaoModel.delete_profissionais_escola_componentes(element)
                else:
                    manter.append(element) 

            for adicionar in componentes_curriculares['componentes']:
    
                if adicionar not in manter:
                    novos.append(adicionar)
                    if ProfissionaisEducacaoModel.get_profissionais_escola_componentes(adicionar, FK_escola_id) != False:
                            return {'error':f'componente curricular com id{adicionar} ja existe a esta escola '}
                    UserModel.associateProfissionalEscolaComponentes(user[0], FK_escola_id, adicionar)

            # for i , componentes in enumerate(componentes_curriculares['componentes']):
            #             if ProfissionaisEducacaoModel.get_profissionais_escola_componentes(componentes, FK_escola_id) != False:
            #                  return {'error':f'componente curricular com id{componentes} ja existe a esta escola '}
            #             UserModel.associateProfissionalEscolaComponentes(user[0], FK_escola_id, componentes)

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
            # FK_perfil_id = dados['FK_perfil_id']
            FK_escola_id = dados['FK_escola_id']
            perfil_ativo = dados['perfil_ativo']
            componentes_curriculares = dados['componentes_curriculares']
            
            profissionaleducacao = ProfissionaisEducacaoModel.get_profissionais_educacao_by_id(args[0])

            UserModel.update_profissionais_educacao(cpf, nome, email, int(telefone), perfil_ativo, profissionaleducacao[0]['FK_user_id'])
            user = UserModel.find_by_login(cpf)
            # print(args[0])
            # input()

            ProfissionaisEducacaoModel.update_profissionais_educacao(FK_escola_id, user[0] , args[0])
            
            componentizar = ProfissionaisEducacaoModel.get_componentes_id_by_FK_turma_id(FK_escola_id)

            manter = []
            excluirAssociacao = []
            novos = []
            for element in componentizar:
                if element not in componentes_curriculares['componentes']:
                    excluirAssociacao.append(element)
                    ProfissionaisEducacaoModel.delete_profissionais_escola_componentes(element)
                else:
                    manter.append(element) 

            for adicionar in componentes_curriculares['componentes']:
    
                if adicionar not in manter:
                    novos.append(adicionar)
                    UserModel.associateProfissionalEscolaComponentes(user[0], FK_escola_id, adicionar)

            # for i , componentes in enumerate(componentes_curriculares['componentes']):
            #             componenteId = ProfissionaisEducacaoModel.get_componentes_by_profissional(user[0], componentes, FK_escola_id) 
            #             # print(componenteId)
            #             # input()
            #                 # != False:
            #                 #  return {'error':f'componente curricular com id {componentes} nao foi encontrado'}
            #             UserModel.update_profissionais_educacao_componentes(user[0], FK_escola_id, componentes, componenteId[0]['id'])

            return {'updated': nome }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400