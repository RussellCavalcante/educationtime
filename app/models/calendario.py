from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class CalendarioModel(): 
    
    @classmethod
    def get_calendario_by_id(*args, **kwargs):
        cursor = conn.cursor()
        cursor.execute(f"""SELECT conteudo_calendario.FK_calendario_id, calendario.FK_escola_id, municipio.id  ,municipio.nome, estado.id, 
                            estado.nome, estado.uf , ano, bimestre_escolar, FK_etapa_ensino , FK_turma_id, 
                            calendario.FK_componente_escola_profissional_id, unidade_tematica, conteudo, resultado, conteudo_calendario.nome, 
                            nome_escola,
                            area_conhecimento.id, area_conhecimento.nome,
                            componente_curricular.id, componente_curricular.nome
                            FROM conteudo_calendario 
                            INNER JOIN calendario ON conteudo_calendario.FK_calendario_id = calendario.id
                            INNER JOIN escola ON calendario.FK_escola_id = escola.id
                            INNER JOIN profissional_escola_componente ON  calendario.FK_componente_escola_profissional_id = profissional_escola_componente.id
                            INNER JOIN componente_curricular ON componente_curricular.id = profissional_escola_componente.FK_componente_id
                            INNER JOIN area_conhecimento ON area_conhecimento.id = componente_curricular.FK_area_conhecimento_id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            WHERE conteudo_calendario.FK_calendario_id = {args[1]};""") 
         
        result = cursor.fetchall()
        cursor.close()
        dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('conteudo_calendario_FK_calendario_id', 'FK_escola_id', 'FK_municipio_id'  ,'municipio_nome', 'FK_UF_id', 
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
    def get_tarefa_casa(self, *args, **kwargs):
        cursor = conn.cursor()
        qtd = kwargs.get('qtd')
        if not qtd:
            qtd = None
             
        queryDefalt = f"""SELECT distinct {'TOP ' + str(qtd) if qtd else ''} 
                            tarefa_casa.id AS tarefa_casa__id, 
                            tarefa_casa.nome_tarefa AS tarefa_casa__nome_tarefa,
                            tarefa_casa.data_entrega AS tarefa_casa__data_entrega,
                            estado.nome AS estado__nome, estado.uf AS estado__uf ,
                            municipio.id AS municipio__id ,municipio.nome as municipio__nome, estado.id AS estado__id, 
                            escola.nome_escola AS escola__nome_escola,
                            calendario.FK_turma_id AS calendario__FK_turma_id,
                            area_conhecimento.id AS area_conhecimento__id, area_conhecimento.nome AS area_conhecimento__nome,
                            componente_curricular.id AS componente_curricular__id, componente_curricular.nome AS componente_curricular__nome,
                            conteudo_calendario.id as conteudo_calendario__id ,conteudo_calendario.nome as conteudo_calendario__nome,
                            calendario.ano AS calendario__ano,
                            calendario.unidade_tematica AS calendario__unidade_tematica,
                            calendario.conteudo AS calendario__conteudo,
                            calendario.FK_etapa_ensino AS calendario__FK_etapa_ensino
                        FROM tarefa_casa
                        INNER JOIN conteudo_calendario ON conteudo_calendario.id = tarefa_casa.FK_conteudo_calendario_id
                        INNER JOIN calendario ON calendario.id = conteudo_calendario.FK_calendario_id
                        INNER JOIN escola ON calendario.FK_escola_id = escola.id
                        INNER JOIN profissional_escola_componente ON  calendario.FK_componente_escola_profissional_id = profissional_escola_componente.id
                        INNER JOIN componente_curricular ON componente_curricular.id = profissional_escola_componente.FK_componente_id
                        INNER JOIN area_conhecimento ON area_conhecimento.id = componente_curricular.FK_area_conhecimento_id
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
        result = cursor.fetchall()
        cursor.close()
        json_string = result[0][0]
        
        # json_obj = {'calendario': json_string}
        # print(json_obj)
        # input()
        return json_string

    @classmethod
    def associate_tarefa_casa_serie(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into tarefa_casa (FK_tarefa_casa_id, nome_acao, prazo) values(?,?,?);",args[1], args[2], args[3])

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
    def create_calendario(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into calendario_escolar ( FK_escola_id, nome, data) OUTPUT INSERTED.id values(?,?,?);",args[1], args[2], args[3])

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