from sqlalchemy.dialects.postgresql import UUID
# from app import banco
import json

from uuid import uuid1, uuid4
import re
from app import conn


class planoAulaModel():
    # __tablename__ = 'estado'
    

    # id = banco.Column(banco.String(36),default=lambda x:str(uuid1()), primary_key=True)
    # username = banco.Column(banco.String(255), nullable=False)
    # password = banco.Column(banco.String(64), nullable=False)
    # email = banco.Column(banco.String(255), nullable=False)
    # phone = banco.Column(banco.Integer(), nullable=False)
    # salt = banco.Column(banco.String(36),default=lambda x:str(uuid4()))


    # def __init__(self, username, password, email, phone, salt):
    #     self.username = username
    #     self.password = password
    #     self.email = email
    #     self.phone = phone
    #     self.salt = salt


    @classmethod
    def get_planoaula(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT plano_aula.id, unidade_tematica, FK_componente_escola_profissional_id, componente_curricular.nome,
                    FK_etapa_ensino,etapa_ensino.nome, ano, bimestre_escolar, resultado 
                    FROM plano_aula 
                    INNER JOIN profissional_escola_componente ON plano_aula.FK_componente_escola_profissional_id = profissional_escola_componente.id
                    INNER JOIN componente_curricular on profissional_escola_componente.FK_componente_id = componente_curricular.id
                    INNER JOIN etapa_ensino on plano_aula.FK_etapa_ensino = etapa_ensino.id
                    ; ;""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'unidade_tematica', 'FK_componente_escola_profissional_id', 'componente_curricular_nome',
                    'FK_etapa_ensino', 'etapa_ensino_nome', 'ano', 'bimestre_escolar', 'resultado' ) 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_plano_aula_by_id(*args, **kwargs):
        cursor = conn.cursor()
        cursor.execute(f"""SELECT conteudo_plano_aula.FK_plano_aula_id, plano_aula.FK_escola_id, municipio.id  ,municipio.nome, estado.id, 
                            estado.nome, estado.uf , ano, bimestre_escolar, FK_etapa_ensino , FK_turma_id, 
                            plano_aula.FK_componente_escola_profissional_id, unidade_tematica, conteudo, resultado, conteudo_plano_aula.nome, 
                            nome_escola,
                            area_conhecimento.id, area_conhecimento.nome,
                            componente_curricular.id, componente_curricular.nome
                            FROM conteudo_plano_aula 
                            INNER JOIN plano_aula ON conteudo_plano_aula.FK_plano_aula_id = plano_aula.id
                            INNER JOIN escola ON plano_aula.FK_escola_id = escola.id
                            INNER JOIN profissional_escola_componente ON  plano_aula.FK_componente_escola_profissional_id = profissional_escola_componente.id
                            INNER JOIN componente_curricular ON componente_curricular.id = profissional_escola_componente.FK_componente_id
                            INNER JOIN area_conhecimento ON area_conhecimento.id = componente_curricular.FK_area_conhecimento_id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            WHERE conteudo_plano_aula.FK_plano_aula_id = {args[1]};""") 
         
        result = cursor.fetchall()
        cursor.close()
        dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('conteudo_plano_aula_FK_plano_aula_id', 'FK_escola_id', 'FK_municipio_id'  ,'municipio_nome', 'FK_UF_id', 
                            'estado_nome', 'estado_uf' , 'ano', 'bimestre_escolar', 'FK_etapa_ensino' , 'FK_turma_id', 
                            'FK_componente_escola_profissional', 'unidade_tematica', 'conteudo', 'resultado', 'nome', 'nome_escola', 'area_conhecimento_id', 'area_conhecimento_nome',
                            'componente_curricular_id', 'componente_curricular_nome')
            tup2 = estadoTupla

            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)   
        

        for Dict in listEstadosDict:
        
            dictFatores = {}
            for chave in Dict:
                
                if 'sub_conteudo' not in dictFinal.keys():
                    if chave == 'nome':
                        
                        dictFinal['sub_conteudo'] = {'itens':[]}
                        dictFatores[chave] = Dict[chave]
                        
                        dictFinal['sub_conteudo']['itens'].append(dictFatores)
                       
                else:
                    if chave == 'nome':
                        
                        dictFatores[chave] = Dict[chave]
                   
                        dictFinal['sub_conteudo']['itens'].append(dictFatores)
                        
                if chave in dictFinal.keys():
                    continue

                    
                
                if chave != 'nome':
                    dictFinal[chave] = Dict[chave] 
        
        return dictFinal
    
    @classmethod
    def get_plano_aula_by_turma_id(self, *args, **kwargs):
        cursor = conn.cursor()
        query = f"""SELECT 
                            distinct plano_aula.id, 
                            plano_aula.FK_escola_id,
                            municipio.id AS municipio_id ,municipio.nome as municipio_nome, estado.id AS estado_id, 
                            estado.nome AS estado_nome, estado.uf ,
                            plano_aula.FK_componente_escola_profissional_id,resultado, 
                            area_conhecimento.id AS area_conhecimento_id, area_conhecimento.nome AS area_conhecimento_nome,
                            componente_curricular.id AS componente_curricular_id, componente_curricular.nome AS componente_curricular_nome,
                            plano_aula.ano,
                            plano_aula.unidade_tematica,
                            plano_aula.conteudo,
                            plano_aula.FK_etapa_ensino,
                            plano_aula.FK_turma_id,
                            escola.nome_escola,
                            (SELECT nome FROM conteudo_plano_aula WHERE FK_plano_aula_id = plano_aula.id FOR JSON PATH) AS sub_conteudo
                        FROM plano_aula
                        INNER JOIN conteudo_plano_aula ON conteudo_plano_aula.FK_plano_aula_id = plano_aula.id
                        INNER JOIN escola ON plano_aula.FK_escola_id = escola.id
                        INNER JOIN profissional_escola_componente ON  plano_aula.FK_componente_escola_profissional_id = profissional_escola_componente.id
                        INNER JOIN componente_curricular ON componente_curricular.id = profissional_escola_componente.FK_componente_id
                        INNER JOIN area_conhecimento ON area_conhecimento.id = componente_curricular.FK_area_conhecimento_id
                        INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                        INNER JOIN estado ON municipio.FK_UF_id = estado.id
                        """
        
        is_first_condition = True
        for column, value in kwargs.items():
            if column != 'order_by' and value is not None:
                if is_first_condition:
                    query += f"WHERE {column} = '{value}'"
                else:
                    query += f"AND {column} = '{value}'"

        order_by = kwargs.get('order_by')
        if order_by:
            query += f" ORDER BY {order_by}"
        
        query += " FOR JSON PATH, ROOT('plano_aula');"
    
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        json_string = result[0][0]
        print(json_string)
        json_obj = {'plano_aula': json_string}
        print(json_obj)
        input()
        return json_obj
                        
    @classmethod
    def get_agenda_plano_aula_by_last_id(*args, **kwargs):
        cursor = conn.cursor()
        
 
        cursor.execute(f"SELECT TOP 1 * from plano_aula ORDER BY id DESC;")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_escola_id', 'ano', 'bimestre_escolar', 'FK_etapa_ensino', 'FK_turma_id', 'FK_componente_escola_profissional_id', 'unidade_tematica', 'conteudo', 'resultado') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False

    @classmethod
    def create_planoaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into plano_aula ( FK_escola_id, ano, bimestre_escolar, FK_etapa_ensino, FK_turma_id, FK_componente_escola_profissional_id, unidade_tematica, conteudo, resultado) values(?,?,?,?,?,?,?,?,?)",args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_conteudo_planoaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into conteudo_plano_aula ( nome, FK_plano_aula_id) values(?,?)",args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_planoaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE plano_aula
                        SET FK_escola_id = ?, ano = ? , bimestre_escolar = ?, FK_etapa_ensino = ?, FK_turma_id = ?, 
                        FK_componente_escola_profissional_id = ?, unidade_tematica = ?, conteudo = ?, resultado = ?
                        WHERE id = ?

                        ''',args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9], args[10])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def delete_conteudo_plano_aula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            DELETE FROM conteudo_plano_aula WHERE FK_plano_aula_id = ?;
                            
                            ''', args[1])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None