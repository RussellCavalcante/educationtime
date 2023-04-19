from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from app.utils.defaultGet import GetModel
from uuid import uuid1, uuid4
import re
from app import conn


class FrequenciaEstudanteModel(): 
    
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
    def get_frequencia_estudante(self, *args, **kwargs):
        
             
        queryDefalt = f""" 
                            idade_serie.id AS idade_serie__id, 
                            idade_serie.resultado AS idade_serie__resultado,
                            idade_serie.meta AS idade_serie_meta,
                            estado.nome AS estado__nome, estado.uf AS estado__uf ,
                            municipio.id AS municipio__id ,municipio.nome as municipio__nome, estado.id AS estado__id, 
                            escola.nome_escola AS escola__nome_escola,
                            idade_serie.FK_turma_id AS idade_serie__FK_turma_id,
                            turma.id AS turma__id,
                            turma.ano_letivo AS turma__ano_letivo,
                            turma.nome_turma AS turma__nome_turma,
                            turno.nome AS turno__nome,
                            etapa_ensino.id AS etapa_ensino__id,
                            etapa_ensino.nome AS etapa_ensino__nome,
                            grau_etapa_ensino.id AS grau_etapa_ensino__id,
                            grau_etapa_ensino.nome_grau AS grau_etapa_ensino__nome_grau,
                                (SELECT acao_idade_serie.id AS acao_idade_serie__id, acao_idade_serie.nome_acao AS acao_idade_serie__nome_acao, acao_idade_serie.prazo AS acao_idade_serie__prazo  FROM acao_idade_serie WHERE acao_idade_serie.FK_idade_serie_id = idade_serie.id FOR JSON PATH) AS acoes
                            FROM idade_serie
                            INNER JOIN turma ON idade_serie.FK_turma_id = turma.id
                            INNER JOIN grau_etapa_ensino ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id
                            INNER JOIN etapa_ensino ON grau_etapa_ensino.FK_etapa_ensino = etapa_ensino.id
                            INNER JOIN turno ON turma.FK_turno_id = turno.id
                            INNER JOIN escola ON turma.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                        """
        
        j= GetModel.get_default(queryDefalt, **kwargs)

        return j

    @classmethod
    def associate_frequencia_estudante(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into frequencia_estudante (FK_frequencia_id, FK_estudante_id, faltas, presenca) values(?,?,?,?);",args[1], args[2], args[3], args[4])

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
    def create_frequencia(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into frequencia ( FK_componente_educador_turma_id, mes) OUTPUT INSERTED.id values(?,?);",args[1], args[2])

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