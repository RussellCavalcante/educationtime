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


class PlanoLeituraServices(Resource):

    @jwt_required()
    def get(self, *args, **kwargs):
        try:
                
            return  PlanoLeituraModel.get_plano_leitura(), 200
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
    def update(self, *args, **kwargs):
        try:

            dados = atributos.parse_args()
            
            nome_rotina = dados['nome_rotina'].strip()
            FK_escola_id = dados['FK_escola_id']
            ano_letivo = dados['ano']
            momentos = dados['momentos']
            turma_compoenente = dados['turma_compoenente']
            # idRotina = PlanoLeituraModel.get_rotina_aula_by_rotina_componente_id(args[0])

            
            PlanoLeituraModel.update_rotinaaula(nome_rotina, FK_escola_id, ano_letivo, args[0])

            momento_id_get = PlanoLeituraModel.get_momento_id_by_rotina_aula(args[0])

            for id_moment in momento_id_get:
        
                PlanoLeituraModel.delete_rotina_aula_momento(id_moment)

                PlanoLeituraModel.delete_momentos(id_moment)

                PlanoLeituraModel.delete_relacao_momentos(id_moment)


            for i , momento in enumerate(momentos['itens']):
                momento_id = PlanoLeituraModel.create_momento( momento['nome_momento'],momento['ordem'], momento['descricao'])


                PlanoLeituraModel.associate_rotina_aula_momento(args[0], momento_id)

            PlanoLeituraModel.delete_rotina_componente(args[0])

            for i , turma_compoenente in enumerate(turma_compoenente['itens']):
                rotina_componente = PlanoLeituraModel.associate_rotina_componente_turma( args[0], turma_compoenente['tumar_profissional_componente'])
            
            return  {'id': args[0] ,'nome_rotina': nome_rotina}, 201

        except:
            return { 'error': 'verifique a requisição !' }, 400