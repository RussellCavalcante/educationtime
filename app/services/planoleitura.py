from flask_restful import Resource, reqparse
from app.models.planoleitura import PlanoLeituraModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from app.config import conn

# from werkzeug.security import safe_str_cmp
from app.blacklist import BLACKLIST

atributos = reqparse.RequestParser()

atributos.add_argument('FK_escola_id', type=int, help="campo obrigatorio ")
atributos.add_argument('ano', type=int, help="campo obrigatorio")
atributos.add_argument('qtd_livros', type=int, help="campo obrigatorio ")
atributos.add_argument('prazo', type=int, help="campo obrigatorio ")
atributos.add_argument('turma_compoenente', type=dict, help="campo obrigatorio ")
atributos.add_argument('livros', type=dict, help="campo obrigatorio ")

class PlanoLeituraServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  PlanoLeituraModel.get_plano_leitura(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
        
    @jwt_required()
    def get_livros(self, *args, **kwargs):
        try:
                
            return  PlanoLeituraModel.get_plano_leitura_livros(**kwargs), 200
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def get_by_id(self, *args, **kwargs):
        try:    
            rotinaaula = PlanoLeituraModel.get_rotinaaula_by_id(args[0])
            componente = PlanoLeituraModel.get_rotinaaula_componente_educador_by_id(args[0])
            
            rotinaaula['turma_compoenente'] = componente['turma_compoenente']

            return  rotinaaula, 200
        except:
            return { 'error': 'verifique a requisição !' }, 400

    @jwt_required()
    def post(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            qtd_livros = dados['qtd_livros']
            FK_escola_id = dados['FK_escola_id']
            ano = dados['ano']
            prazo = dados['prazo']
            turma_compoenente = dados['turma_compoenente']
            
            plano_leitura = PlanoLeituraModel.create_plano_leitura(FK_escola_id, ano, qtd_livros, prazo)

            for i , turma_compoenente in enumerate(turma_compoenente['itens']):
                PlanoLeituraModel.associate_plano_leitura_componente_turma( plano_leitura, turma_compoenente['tumar_profissional_componente'])
            
            return  {'id_plano_leitura': plano_leitura ,}, 201
        
        except:
            return { 'error': 'verifique a requisição !' }, 400
    
    @jwt_required()
    def update_livro(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            livros = dados['livros']
            getleituralivros = PlanoLeituraModel.find_livros_by_FK_plano_componente_turma_id(args)
            if getleituralivros != False:
                PlanoLeituraModel.delete_estudantes_livros_status(getleituralivros[0])
                PlanoLeituraModel.delete_livros(getleituralivros[0])
   
            for i , livro in enumerate(livros['itens']):
                
                
            
                PlanoLeituralivros = PlanoLeituraModel.associate_plano_leitura_livros(livro['titulo'], livro['autoria'], args[0])

                for i , estudante in enumerate(livro['estudantes']):
                    PlanoLeituraModel.associate_plano_leitura_estudante( estudante['FK_estudante_id'], PlanoLeituralivros, estudante['status'])
        
            return  {'plano_leitura': args[0]}, 200

        except:  'verifique a requisição !' , 400