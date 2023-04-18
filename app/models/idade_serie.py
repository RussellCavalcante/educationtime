from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn
import json
import pprint


class IdadeSerieModel(): 


    @classmethod
    def get(self, *args, **kwargs):
        cursor = conn.cursor()
        qtd = kwargs.get('qtd')
        if not qtd:
            qtd = None
             
        queryDefalt = f"""SELECT distinct {'TOP ' + str(qtd) if qtd else ''}
                            idade_serie.id AS idade_serie__id, 
                                idade_serie.resultado AS idade_serie__resultado,
                                idade_serie.meta AS idade_serie_meta,
                                estado.nome AS estado__nome, estado.uf AS estado__uf ,
                                municipio.id AS municipio__id ,municipio.nome as municipio__nome, estado.id AS estado__id, 
                                escola.nome_escola AS escola__nome_escola,
                                idade_serie.FK_turma_id AS idade_serie__FK_turma_id,
                                turma.id AS turma__id,
                                turma.nome_turma AS turma__nome_turma,
                                turno.nome AS turno__nome,
                                (SELECT acao_idade_serie.id AS acao_idade_serie__id, acao_idade_serie.nome_acao AS acao_idade_serie__nome_acao, acao_idade_serie.prazo AS acao_idade_serie__prazo  FROM acao_idade_serie WHERE acao_idade_serie.FK_idade_serie_id = idade_serie.id FOR JSON PATH) AS acoes
                            FROM idade_serie
                            INNER JOIN turma ON idade_serie.FK_turma_id = turma.id
                            INNER JOIN turno ON turma.FK_turno_id = turno.id
                            INNER JOIN escola ON turma.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                        """
        
        is_first_condition = True
        for column, value in kwargs.items():
            if column != 'order_by' and column != 'qtd' and value is not None:
                if is_first_condition:
                    if column != 'qtd':
                    
                        columnSplited = column.split('__')
                    
                    
                        queryDefalt += f"WHERE {columnSplited[0]}.{columnSplited[1]} = {value}"
                        is_first_condition = False
                      
                
                else:
                    columnSplited = column.split('__')
                    print(columnSplited)
                      
                    queryDefalt += f"AND {columnSplited[0]}.{columnSplited[1]} = {value}"
                
                
                
                    

        order_by = kwargs.get('order_by')
        if order_by:
            queryDefalt += f" ORDER BY {order_by}"
        
         
        
        queryDefalt += " FOR JSON PATH, ROOT('request');"

        cursor.execute(queryDefalt)
        result = cursor.fetchone()
        cursor.close()

        # print(result[0])
        # input()
        # pprint.pprint(result[0])
        # input()
        if kwargs.items():
            
            json_string = result[0]
        else:
            json_string = result[0] + ']}'
        # print(type(json_string))
        # pprint.pprint(json_string)
        # input()
        # jsonSend = json.loads(json_string)
        j = eval(json_string)
       
        # print(j)
        # input()
        # json_obj = {'plano_aula': json_string}
        # print(json_obj)
        # input()
        return j
    
    @classmethod
    def associate_acao_idade_serie(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into acao_idade_serie (FK_idade_serie_id, nome_acao, prazo) values(?,?,?);",args[1], args[2], args[3])

            # result = cursor.fetchone()
            cursor.commit()
            cursor.close()
            # return result[0]
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_idade_serie(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into idade_serie ( FK_turma_id, resultado, meta) OUTPUT INSERTED.id values(?,?,?);",args[1], args[2], args[3])

            result = cursor.fetchone()
            cursor.commit()
            cursor.close()
            return result[0]
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None


    @classmethod
    def update_notas_saeb_area_conhecimento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute('''
                        UPDATE notas_saeb_area_conhecimento
                        SET meta = ?
                        WHERE id = ?
                        ''',args[1], args[2])

            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None


    @classmethod
    def delete_rotina_componente(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()

            cursor.execute('''
                            DELETE FROM rotina_componente_turma WHERE FK_resultado_aprendizagem = ?;

                            ''', args[1])


            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def delete_momentos(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()

            cursor.execute('''
                            DELETE FROM momento WHERE id = ?;

                            ''', args[1])


            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def delete_resultado_aprendizagem_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()

            cursor.execute('''
                            DELETE FROM resultado_aprendizagem_momento WHERE FK_momento_id = ?;

                            ''', args[1])


            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def delete_relacao_momentos(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()

            cursor.execute('''
                            DELETE FROM resultado_aprendizagem_momento WHERE FK_momento_id = ?;

                            ''', args[1])


            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None