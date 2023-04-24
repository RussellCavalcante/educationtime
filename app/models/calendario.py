from sqlalchemy.dialects.postgresql import UUID
from app.utils.defaultGet import GetModel
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
    def get_calendario_casa(self, *args, **kwargs):
    
        queryDefalt = f""" 
                            calendario_escolar.id AS calendario_escolar__id,
                            calendario_escolar.nome AS calendario_escolar__nome,
                            calendario_escolar.data AS calendario_escolar__data,
                            escola.id AS escola__id,
                            escola.nome_escola AS escola__nome_escola,
                            municipio.id AS municipio__id,
                            municipio.nome AS municipio__nome, 
                            estado.id AS estado__id, 
                            estado.uf AS estado__uf,
                            estado.nome AS estado__nome
                            FROM calendario_escolar
                            
                            INNER JOIN escola ON calendario_escolar.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                        """
        
        j = GetModel.get_default(queryDefalt, **kwargs)
       
        return j


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