from flask_restful import Resource, reqparse
from app.models.agenda_diretoria import AgendaDiretoriaModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('FK_escola_id', type=int, help="campo de nome do usuario e obrigatorio")
atributos.add_argument('nome', type=str, help="campo de telefone")
atributos.add_argument('prazo', type=str, help="email obrigatorio")
atributos.add_argument('recursos', type=str, help="campo de cod_inep")
atributos.add_argument('equipe', type=dict, help="campo de cod_inep")
atributos.add_argument('resultado', type=int, help="campo de telefone")
atributos.add_argument('titulo', type=str, help="campo email obrigatorio")
atributos.add_argument('mensagem', type=str, help="campo email obrigatorio")




class AgendaDiretoriaServices(Resource):
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:
            return  AgendaDiretoriaModel.get_agenda_diretoria_by_id(args[0]), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  AgendaDiretoriaModel.get_agenda_diretoria(), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400


    @jwt_required()
    def post(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()
            
            FK_escola_id = dados['FK_escola_id']
            nome = dados['nome']
            prazo = dados['prazo']
            recursos = dados['recursos'].strip()
            equipe = dados['equipe']

            AgendaDiretoriaModel.create_agenda_diretoria(FK_escola_id, nome, prazo, recursos)
            
            agenda = AgendaDiretoriaModel.get_agenda_diretoria_fatores_by_last_id(FK_escola_id)
            
            for i , agenda_diretoria in enumerate(equipe['itens']):
                AgendaDiretoriaModel.associate_agenda_diretorias_equipe(agenda_diretoria['Nome'], agenda[0]['id'])
            
            AgendaDiretoriaModel.create_first_agenda_diretoria_analise(agenda[0]['id'], 0)

            return  {'created_agenda_diretoria': FK_escola_id}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def update(self, *args, **kwargs):
        try:
            dados = atributos.parse_args()
            
            FK_escola_id = dados['FK_escola_id']
            nome = dados['nome']
            prazo = dados['prazo']
            recursos = dados['recursos'].strip()
            equipe = dados['equipe']
            resultado = dados['resultado']
            titulo = dados['titulo'].strip()
            mensagem = dados['mensagem'].strip()


            AgendaDiretoriaModel.update_agenda_diretoria(FK_escola_id, nome, prazo, recursos,args[0])

            AgendaDiretoriaModel.delete_agenda_equipe(args[0])
            for i , agenda_diretoria in enumerate(equipe['itens']):
                AgendaDiretoriaModel.associate_agenda_diretorias_equipe(agenda_diretoria['Nome'], args[0])

            AgendaDiretoriaModel.update_agenda_analise(resultado, titulo, mensagem, args[0])

            return {'updated': args[0] }, 200
        
        except:
            return { 'error': 'verifique a requisição !' }, 400

