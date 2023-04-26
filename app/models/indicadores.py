from sqlalchemy.dialects.postgresql import UUID
from app.utils.defaultGet import GetModel
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn
import json


class IndicadoresModel():

    @classmethod
    def get(self, *args, **kwargs):
        cursor = conn.cursor()

        estado = kwargs.get('FK_estado_id')

        grupo = 'estado.nome AS grupo'
        group_by = 'GROUP BY estado.nome'

        if estado:
            grupo = 'municipio.nome AS grupo'

            group_by = 'GROUP BY municipio.nome'
        else:
            False
            
        municipio = kwargs.get('FK_municipio_id')

        if municipio:
            grupo = 'escola.nome_escola AS grupo'
            group_by = 'GROUP BY escola.nome_escola'
        else:
            False
        escola = kwargs.get('FK_escola_id')

        if escola:
            grupo = 'turma.nome_turma AS grupo'
            group_by = 'GROUP BY turma.nome_turma'
        else:
            False
             
        queryDefalt = f"""SELECT CAST( (SELECT distinct COUNT(enturmar.FK_turma_id) as "num_estudantes",
                            COUNT(DISTINCT enturmar.FK_turma_id) AS "num_turmas",
                            CAST(COUNT(enturmar.FK_turma_id) AS decimal) / COUNT(DISTINCT enturmar.FK_turma_id) AS media_estudantes_por_turma,

                            
                            { grupo }
                            
                            FROM enturmar
                            INNER JOIN turma ON enturmar.FK_turma_id = turma.id
                            INNER JOIN escola ON turma.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id

                            { 'WHERE estado.id = '+ str(estado) if estado else ''}
                            { 'WHERE municipio.id = '+ str(municipio) if municipio else ''}
                            { 'WHERE escola.id = '+ str(escola) if escola else ''}


                            { group_by }
                            
                            """
        
        
        
         
        
        queryDefalt += " FOR JSON PATH, ROOT('request')) AS VARCHAR(MAX));"

        cursor.execute(queryDefalt)
        result = cursor.fetchall()
        
        if result[0][0] == None:
            return False
        
        s = str(result)

        strip1 = s.lstrip("[('")
        strip2 = strip1.rstrip("', )]")
        
        j = json.loads(strip2)
        
        return j
    

    @classmethod
    def get_escolaridade_educadores(self, *args, **kwargs):
        cursor = conn.cursor()

        estado = kwargs.get('FK_estado_id')

        
        group_by = 'GROUP BY escolaridade_educador.escolaridade'

        # if estado:
        #     grupo = 'municipio.nome AS grupo'

        #     group_by = 'GROUP BY municipio.nome'
        # else:
        #     False
            
        municipio = kwargs.get('FK_municipio_id')

        # if municipio:
        #     grupo = 'escola.nome_escola AS grupo'
        #     group_by = 'GROUP BY escola.nome_escola'
        # else:
        #     False
        escola = kwargs.get('FK_escola_id')

        # if escola:
        #     grupo = 'turma.nome_turma AS grupo'
        #     group_by = 'GROUP BY turma.nome_turma'
        # else:
        #     False
             
        queryDefalt = f"""SELECT CAST( (SELECT distinct CASE escolaridade_educador.escolaridade
                                    WHEN 1 THEN 'Ensino médio'
                                    WHEN 2 THEN 'Graduação'
                                    WHEN 3 THEN 'Pós-graduação'
                                    WHEN 4 THEN 'Mestrado'
                                    WHEN 5 THEN 'Doutorado'
                                END AS escolaridade,
                                COUNT(DISTINCT escolaridade_educador.FK_user_id) AS quantidade
                            FROM escolaridade_educador
                            INNER JOIN escola ON escolaridade_educador.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            

                            { 'WHERE estado.id = '+ str(estado) if estado else ''}
                            { 'WHERE municipio.id = '+ str(municipio) if municipio else ''}
                            { 'WHERE escola.id = '+ str(escola) if escola else ''}

                            {group_by}

                            
                            """
        
        
        
         
        
        queryDefalt += " FOR JSON PATH, ROOT('request')) AS VARCHAR(MAX));"


        cursor.execute(queryDefalt)


        result = cursor.fetchall()
        
        if result[0][0] == None:
            return False

        s = str(result)

        strip1 = s.lstrip("[('")
        strip2 = strip1.rstrip("', )]")
        
        j = json.loads(strip2)
        
        return j
    
    @classmethod
    def get_acoes_agenda_diretoria(self, *args, **kwargs):
        cursor = conn.cursor()

        estado = kwargs.get('FK_estado_id')

        grupo = 'estado.nome AS grupo'

        group_by = 'GROUP BY estado.nome'

        where = 'WHERE agenda_analise.resultado > 1'

        if estado:
            grupo = 'municipio.nome AS grupo'

            group_by = 'GROUP BY municipio.nome'

            where += f'AND estado.id = {str(estado)}'
        else:
            False
            
        municipio = kwargs.get('FK_municipio_id')

        if municipio:
            grupo = 'escola.nome_escola AS grupo'
            group_by = 'GROUP BY escola.nome_escola'
            where += f'AND municipio.id = {str(municipio)}'
        else:
            False
        escola = kwargs.get('FK_escola_id')

        if escola:
            grupo = 'turma.nome_turma AS grupo'
            group_by = 'GROUP BY turma.nome_turma'
            where += f'AND escola.id = {str(escola)}'
        else:
            False
             
        queryDefalt = f"""SELECT CAST( (SELECT distinct 
                            COUNT(CASE WHEN agenda_analise.resultado > 2 THEN agenda_analise.resultado END) as "num_analises_realizadas",
                            COUNT(agenda_analise.resultado) as "num_analises_total",


                            { grupo }

                            FROM agenda_analise
                            INNER JOIN agenda_diretoria ON agenda_analise.FK_agenda_diretoria_id = agenda_diretoria.id
                            INNER JOIN escola ON agenda_diretoria.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id

                            {where}

                            {group_by}

                            
                            """
        
        
        
         
        
        queryDefalt += " FOR JSON PATH, ROOT('request')) AS VARCHAR(MAX));"

        cursor.execute(queryDefalt)


        result = cursor.fetchall()
        
        if result[0][0] == None:
            return False

        s = str(result)

        strip1 = s.lstrip("[('")
        strip2 = strip1.rstrip("', )]")
        
        j = json.loads(strip2)
        
        return j
    

    @classmethod
    def get_satisfacao(self, *args, **kwargs):
        cursor = conn.cursor()

        estado = kwargs.get('FK_estado_id')

        grupo = 'estado.nome AS grupo'
        group_by = 'GROUP BY estado.nome'

        if estado:
            grupo = 'municipio.nome AS grupo'

            group_by = 'GROUP BY municipio.nome'
        else:
            False
            
        municipio = kwargs.get('FK_municipio_id')

        if municipio:
            grupo = 'escola.nome_escola AS grupo'
            group_by = 'GROUP BY escola.nome_escola'
        else:
            False
        escola = kwargs.get('FK_escola_id')

        if escola:
            grupo = 'turma.nome_turma AS grupo'
            group_by = 'GROUP BY turma.nome_turma'
        else:
            False
             
        queryDefalt = f"""SELECT CAST( (SELECT distinct COUNT(CASE WHEN agenda_analise.resultado = 2 THEN agenda_analise.resultado END) as "insatisfatorio",
                            COUNT(CASE WHEN agenda_analise.resultado = 3 THEN agenda_analise.resultado END) as "parcialm_satisfatorio",
                            COUNT(CASE WHEN agenda_analise.resultado = 4 THEN agenda_analise.resultado END) as "satisfatorio",
                            COUNT(agenda_analise.resultado) as "num_analises_total",

                            {grupo}

                            FROM agenda_analise
                            INNER JOIN agenda_diretoria ON agenda_analise.FK_agenda_diretoria_id = agenda_diretoria.id
                            INNER JOIN escola ON agenda_diretoria.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id

                            { 'WHERE estado.id = '+ str(estado) if estado else ''}
                            { 'WHERE municipio.id = '+ str(municipio) if municipio else ''}
                            { 'WHERE escola.id = '+ str(escola) if escola else ''}


                            { group_by }
                            
                            """
        
        
        
         
        
        queryDefalt += " FOR JSON PATH, ROOT('request')) AS VARCHAR(MAX));"

        cursor.execute(queryDefalt)
        result = cursor.fetchall()
        
        if result[0][0] == None:
            return False

        s = str(result)

        strip1 = s.lstrip("[('")
        strip2 = strip1.rstrip("', )]")
        
        j = json.loads(strip2)
        
        return j
