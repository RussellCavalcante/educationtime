from flask_restful import Resource, reqparse
from app.models.momento import MomentoModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('nome_momento', type=str, help="campo obrigatorio ")
atributos.add_argument('prioridade', type=int, help="campo obrigatorio")
atributos.add_argument('descricao', type=str, help="campo obrigatorio ")



class GetMomento(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        
        return  MomentoModel.get_momento(), 200
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        
        return  MomentoModel.get_momento_by_id(args[0]), 200

    @jwt_required()
    def post_momemnto(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        nome_momento = dados['nome_momento'].strip()
        prioridade = dados['prioridade']
        descricao = dados['descricao']
        id = MomentoModel.get_momento_by_nome_momemto(nome_momento)
        
        MomentoModel.create_momento(nome_momento ,int(prioridade), descricao)
        

        return  {'created': nome_momento,
                 'id': id}, 201
    
    @jwt_required()
    def update(self, *args, **kwargs):
        dados = atributos.parse_args()
        
        nome_momento = dados['nome_momento'].strip()
        priodidade = dados['priodidade']
        descricao = dados['descricao'].strip()
        

        MomentoModel.update_momento(nome_momento ,priodidade, descricao, args[0])
        return {'updated': nome_momento }, 200
