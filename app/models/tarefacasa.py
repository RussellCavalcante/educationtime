from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from app.utils.defaultGet import GetModel
from uuid import uuid1, uuid4
import re
from app import conn


class TarefaCasaModel(): 
    
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
    def get_tarefa_casa(self, *args, **kwargs):
        
        queryDefalt = f""" 
                            tarefa_casa.id AS tarefa_casa__id, 
                            tarefa_casa.nome_tarefa AS tarefa_casa__nome_tarefa,
                            tarefa_casa.data_entrega AS tarefa_casa__data_entrega,
                            estado.nome AS estado__nome, estado.uf AS estado__uf ,
                            municipio.id AS municipio__id ,municipio.nome as municipio__nome, estado.id AS estado__id, 
                            escola.nome_escola AS escola__nome_escola,
                            plano_aula.FK_turma_id AS plano_aula__FK_turma_id,
                            area_conhecimento.id AS area_conhecimento__id, area_conhecimento.nome AS area_conhecimento__nome,
                            componente_curricular.id AS componente_curricular__id, componente_curricular.nome AS componente_curricular__nome,
                            conteudo_plano_aula.id as conteudo_plano_aula__id ,conteudo_plano_aula.nome as conteudo_plano_aula__nome,
                            plano_aula.ano AS plano_aula__ano,
                            plano_aula.unidade_tematica AS plano_aula__unidade_tematica,
                            plano_aula.conteudo AS plano_aula__conteudo,
                            plano_aula.FK_etapa_ensino AS plano_aula__FK_etapa_ensino,
                            grau_etapa_ensino.nome_grau AS grau_etapa_ensino__nome_grau
                        FROM tarefa_casa
                        INNER JOIN conteudo_plano_aula ON conteudo_plano_aula.id = tarefa_casa.FK_conteudo_plano_aula_id
                        INNER JOIN plano_aula ON plano_aula.id = conteudo_plano_aula.FK_plano_aula_id
                        INNER JOIN grau_etapa_ensino ON grau_etapa_ensino.id = plano_aula.FK_etapa_ensino
                        INNER JOIN escola ON plano_aula.FK_escola_id = escola.id
                        INNER JOIN profissional_escola_componente ON  plano_aula.FK_componente_escola_profissional_id = profissional_escola_componente.id
                        INNER JOIN componente_curricular ON componente_curricular.id = profissional_escola_componente.FK_componente_id
                        INNER JOIN area_conhecimento ON area_conhecimento.id = componente_curricular.FK_area_conhecimento_id
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
    def create_tarefa_casa(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into tarefa_casa ( FK_conteudo_plano_aula_id, nome_tarefa, data_entrega) OUTPUT INSERTED.id values(?,?,?);",args[1], args[2], args[3])

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
    def delete_tarefa_casa(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()

            cursor.execute('''
                            DELETE FROM tarefa_casa WHERE FK_conteudo_plano_aula_id = ?;

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