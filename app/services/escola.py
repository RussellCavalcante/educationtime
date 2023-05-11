from flask_restful import Resource, reqparse
from app.models.escola import EscolaModel
from app.models.log_atividade import LogAtividadeModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from datetime import datetime
import pandas as pd
import json
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('nome_escola', type=str, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('endereco', type=str, help="campo de email e obrigatorio")
atributos.add_argument('telefone', type=int, help="campo de telefone")
atributos.add_argument('email_escola', type=str, help="email obrigatorio")
atributos.add_argument('cod_inep', type=int, help="campo de cod_inep")
atributos.add_argument('FK_municipio_id', type=int, help="campo de municipio")


class GetEscola(Resource):
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:

            return  EscolaModel.get_escola_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get(self, *args, **kwargs):
        try:

            LogAtividadeModel.create_log_atividade_vizualizacao(args[0], str(datetime.today()),'visualização', 'escola')
            return  EscolaModel.get_escola(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_escola_by_muncipio_id(self, *args, **kwargs):
        try:
            return  EscolaModel.get_by_muncipio_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()

            nome_escola = dados['nome_escola'].strip()
            endereco = dados['endereco'].strip()
            telefone = dados['telefone']
            email_escola = dados['email_escola'].strip()
            cod_inep = dados['cod_inep']
            FK_municipio_id = dados['FK_municipio_id']

             
            if EscolaModel.find_by_cod_inep(cod_inep):
                return {'error':'Já existe escola cadastrada com esse cod_inep.'}, 400

            IdEscola = EscolaModel.create_escola(nome_escola, endereco, email_escola, telefone, cod_inep, FK_municipio_id)
            LogAtividadeModel.create_log_atividade_insercao(args[0], str(datetime.today()),'criação', 'escola', f'foi adicionado escola id : {IdEscola}')
            return  {'created': nome_escola}, 201

        except:
            return { 'error': 'verifique a requisição !' }, 400


    @jwt_required()
    def post_csv(self, *args, **kwargs):
        try:

            data_csv = pd.read_csv(args[1], delimiter=';')
            
            data_json = data_csv.to_dict(orient='records')
            Escolas = 0

            EscolasExistentes = []

            EscolasJson = { 'Menssage': f'Importação de escolas concluída, Número de escolas inseridas : {Escolas}',
                            'Dados':[],
                           }

            for  dados in data_json:
                
                nome_escola = dados['nome_escola'].strip()
                endereco = dados['endereco'].strip()
                telefone = dados['telefone']
                email_escola = dados['email_escola'].strip()
                cod_inep = dados['cod_inep']
                FK_municipio_id = args[3]



                Escola = EscolaModel.find_by_cod_inep(cod_inep)
                
                if Escola:
                    if cod_inep not in EscolasExistentes:
                        EscolaJson = {'cod_inep':cod_inep,
                                      'nome_escola': nome_escola, 
                                      'mensagem': 'Código inep já cadastrado.',
                                      'status': False
                                      }
                        EscolasExistentes.append(cod_inep)
                        EscolasJson['Dados'].append(EscolaJson)
                else:
                    IdEscola = EscolaModel.create_escola(nome_escola, endereco, email_escola, telefone, cod_inep, FK_municipio_id)
                    EscolaJson = {'cod_inep':cod_inep,
                                  'nome_escola': nome_escola,
                                  'mensagem': 'Escola importada com sucesso.',
                                  'status': True
                                  }
                    EscolasJson['Dados'].append(EscolaJson)
                    LogAtividadeModel.create_log_atividade_insercao(args[0], str(datetime.today()),'criação', 'escola', f'foi adicionado escola id : {IdEscola}')
                    Escolas += 1
                    EscolasJson['Menssage'] = f'Importação de escolas concluída, Número de escolas inseridas : {Escolas}'

            if len(EscolasExistentes) > 0:
                if Escolas == 0:
                
                    return EscolasJson, 400
                else:
                    
                    return EscolasJson, 201
            else:
                
                return EscolasJson, 201
    
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def update(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()

            nome_escola = dados['nome_escola'].strip()
            endereco = dados['endereco'].strip()
            telefone = dados['telefone']
            email_escola = dados['email_escola'].strip()
            cod_inep = dados['cod_inep']
            FK_municipio_id = dados['FK_municipio_id']


            EscolaModel.update_escola(nome_escola, endereco, email_escola, telefone, cod_inep, FK_municipio_id ,args[0])
            LogAtividadeModel.create_log_atividade_atualizacao(args[1], str(datetime.today()),'atualização', 'escola', f'foi atualizado escola id : {args[0]}')
            return {'updated': nome_escola }, 200

        except:
            return { 'error': 'verifique a requisição !' }, 400

