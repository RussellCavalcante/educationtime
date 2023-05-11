from flask_restful import Resource, reqparse
from app.models.estudante import estudanteModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import pandas as pd
# from app.config import conn
from datetime import date
from datetime import datetime

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('cod_nacional_estudante', type=int, help="campo obrigatorio")
atributos.add_argument('nome', type=str, help="campo obrigatorio")
atributos.add_argument('data_nascimento', type=str, help="campo obrigatorio ")
atributos.add_argument('tipo_aluno', type=str, help="campo obrigatorio ")
atributos.add_argument('nee', type=int, help="campo obrigatorio nee ")
atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio int ")


class GetEstudante(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
            return  estudanteModel.get_estudante(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_cod(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_cod(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_cod_and_escola(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_cod_escola(args[0], args[1]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_estudante_by_turma_by_escola_id(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_by_turma_by_escola_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_nome(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_nome(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_by_nome_and_escola(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_nome(args[0], args[1]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get_estudante_turma_id(self, *args, **kwargs):
        try:
                    
            return  estudanteModel.get_estudante_turma_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def post_estudante(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            cod_nacional_estudante = dados['cod_nacional_estudante']
            nome = dados['nome'].strip()
            data_nascimento = dados['data_nascimento'].strip()
            tipo_aluno = dados['tipo_aluno'].strip()
            nee = dados['nee']
            FK_escola_id = dados['FK_escola_id']

            if estudanteModel.find_by_cod_nacional_estudante(cod_nacional_estudante):
                return {'error':'existe estudante com mesmo codigo nacional'}
            
            data_envio = data_nascimento.split('-')
            today = str(date.today()).split('-')
            
            data1 = datetime(int(data_envio[0]), int(data_envio[1]), int(data_envio[2]))
            data2 = datetime(int(today[0]), int(today[1]), int(today[2]))
   
            difdata = data2 - data1

            if int(str(difdata).split(':')[0].split('days')[0])  <= 0:
                
                return {'error':'Data de nascimento superior a data informada.'}

            estudanteModel.create_estudante(cod_nacional_estudante ,nome, data_nascimento, tipo_aluno, nee, FK_escola_id)
            
            return  {'created': nome}, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def post_csv(self, *args, **kwargs):
        try:

            data_csv = pd.read_csv(args[0], delimiter=';')
            
            data_json = data_csv.to_dict(orient='records')
            Estudantes = 0

            EstudantesExistentes = []

            EstudantesJson = { 'Menssage': f'Importação de estudantes concluída, Número de estudantes inseridos : {Estudantes}',
                            'Dados':[],
                           }

            for  dados in data_json:
                
                cod_nacional_estudante = dados['cod_nacional_estudante']
                nome = dados['nome'].strip()
                data_nascimento = dados['data_nascimento'].strip()
                tipo_aluno = dados['tipo_aluno'].strip()
                nee = dados['nee']
                FK_escola_id = args[2]



                estudante = estudanteModel.find_by_cod_nacional_estudante(cod_nacional_estudante)
                
                if estudante:
                    if cod_nacional_estudante not in EstudantesExistentes:
                        estudanteJson = {'cod_nacional_estudante':cod_nacional_estudante,
                                      'nome': nome,
                                      'Mensagem': 'Código Nacional do Estudante já cadastrado.',
                                      'status': False}
                        EstudantesExistentes.append(cod_nacional_estudante)
                        EstudantesJson['Dados'].append(estudanteJson)
                else:
                    Idestudante = estudanteModel.create_estudante(cod_nacional_estudante, nome , data_nascimento, tipo_aluno, nee, FK_escola_id)
                    estudanteJson = {'cod_nacional_estudante':cod_nacional_estudante,
                                  'nome': nome,
                                  'Mensagem': 'Estudante importado com sucesso.',
                                  'status': True
                                  }
                    EstudantesJson['Dados'].append(estudanteJson)
                    # LogAtividadeModel.create_log_atividade_insercao(args[0], str(datetime.today()),'criação', 'escola', f'foi adicionado escola id : {IdEscola}')
                    Estudantes += 1
                    EstudantesJson['Menssage'] = f'Importação de estudantes concluída, Número de estudantes inseridos : {Estudantes}'

            if len(EstudantesExistentes) > 0:
                if Estudantes == 0:
                
                    return EstudantesJson, 400
                else:
                    
                    return EstudantesJson, 201
            else:
                
                return EstudantesJson, 201
    
        except:
            return { 'error': 'verifique a requisição !' }, 400


    @jwt_required()
    def update(self, *args, **kwargs):
        try:
                
            dados = atributos.parse_args()
            
            cod_nacional_estudante = dados['cod_nacional_estudante']
            nome = dados['nome'].strip()
            data_nascimento = dados['data_nascimento'].strip()
            tipo_aluno = dados['tipo_aluno']
            nee = dados['nee']
            FK_escola_id = dados['FK_escola_id']

            estudanteModel.update_estudante(cod_nacional_estudante ,nome, data_nascimento, tipo_aluno, nee, FK_escola_id, args[0])
            
            return {'updated': nome }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400