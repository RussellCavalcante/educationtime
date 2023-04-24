from sqlalchemy.dialects.postgresql import UUID
from app.utils.defaultGet import GetModel
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class NotasSaebModel():
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
    def get_notas_saeb_by_rotina_componente_id(*args, **kwargs):
        cursor = conn.cursor()

        cursor.execute(f"""SELECT FK_notas_saeb
                            FROM rotina_componente_turma
                            WHERE id = {args[1]}
                            """)

        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:

            # tup1 = ('id')

            # tup2 = estadoTupla

            # if len(tup1) == len(tup2):
            #     res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(estadoTupla[0])
        # print(listEstadosDict)
        # input()

        return listEstadosDict

    @classmethod
    def get_momento_id_by_notas_saeb(*args, **kwargs):
        cursor = conn.cursor()

        cursor.execute(f"""SELECT FK_momento_id
                            FROM notas_saeb_momento
                            WHERE FK_notas_saeb_id = {args[1]}

                            """)

        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:

            # tup1 = ('id')

            # tup2 = estadoTupla

            # if len(tup1) == len(tup2):
            #     res = dict(zip(tup1, tup2))
            #     # print(res)

                listEstadosDict.append(estadoTupla[0])

        return listEstadosDict


    @classmethod
    def get_notas_saeb(*args, **kwargs):
        queryDefalt = f""" 

                            notas_saeb.id AS notas_saeb__id,
                            notas_saeb.ano AS notas_saeb__ano,
                            escola.id AS escola__id,
                            escola.nome_escola AS escola__nome_escola,
                            municipio.id AS municipio__id,
                            municipio.nome AS municipio__nome, 
                            estado.id AS estado__id, 
                            estado.uf AS estado__uf,
                            estado.nome AS estado__nome, 
                            (SELECT 
                            notas_saeb_area_conhecimento.id AS notas_saeb_area_conhecimento__id,
                            notas_saeb_area_conhecimento.nota AS notas_saeb_area_conhecimento__nota, 
                            area_conhecimento.nome AS area_conhecimento__nome,
                            area_conhecimento.id AS area_conhecimento__id
                            FROM notas_saeb_area_conhecimento 
                            INNER JOIN area_conhecimento ON notas_saeb_area_conhecimento.FK_area_conhecimento_id = area_conhecimento.id
                            WHERE notas_saeb_area_conhecimento.FK_notas_saeb_id = notas_saeb.id FOR JSON PATH) AS notas

                            FROM notas_saeb
                            
                            INNER JOIN escola ON notas_saeb.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id 
                        """
        
        j = GetModel.get_default(queryDefalt, **kwargs)
       
        return j

    @classmethod
    def get_notas_saeb_by_id(*args, **kwargs):
        cursor = conn.cursor()


        # cursor.execute(f"""SELECT rotina_componente_turma.id, estado.id ,estado.uf , municipio.id, municipio.nome ,
        #                     notas_saeb.FK_escola_id, escola.nome_escola , notas_saeb.nome,
        #                     momento.ordem, momento.nome_momento, momento.descricao, turma.id, users.nome,
        #                     turma.FK_etapa_ensino_id , etapa_ensino.nome, grau_etapa_ensino.id, grau_etapa_ensino.nome_grau, componente_curricular.nome,
        #                     notas_saeb.ano_letivo, turma.nome_turma, turno.nome
        #                     FROM rotina_componente_turma
        #                     INNER JOIN notas_saeb ON rotina_componente_turma.FK_notas_saeb = notas_saeb.id
        #                     INNER JOIN notas_saeb_momento ON notas_saeb.id = notas_saeb_momento.FK_notas_saeb_id
        #                     INNER JOIN momento ON notas_saeb_momento.FK_momento_id = momento.id
        #                     INNER JOIN turma_componente_educador ON rotina_componente_turma.FK_turma_componente_educador_id = turma_componente_educador.id
        #                     INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
        #                     INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
        #                     INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
        #                     INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
        #                     INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id
        #                     INNER JOIN escola ON notas_saeb.FK_escola_id = escola.id
        #                     INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
        #                     INNER JOIN estado ON municipio.FK_UF_id = estado.id
        #                     INNER JOIN turno ON turma.FK_turno_id = turno.id
        #                     INNER JOIN grau_etapa_ensino ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id
        #                     WHERE rotina_componente_turma.id = {args[1]};""")
        cursor.execute(f"""SELECT notas_saeb.id, municipio.FK_UF_id, estado.uf, 
                            estado.nome, escola.FK_municipio_id, municipio.nome, notas_saeb.FK_escola_id, escola.nome_escola,
                            notas_saeb.nome, notas_saeb.ano_letivo,
                            momento.ordem, momento.nome_momento, momento.descricao
                            FROM notas_saeb_momento
                            INNER JOIN notas_saeb ON notas_saeb_momento.FK_notas_saeb_id = notas_saeb.id
                            INNER JOIN momento ON notas_saeb_momento.FK_momento_id = momento.id
                            INNER JOIN escola ON notas_saeb.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            WHERE notas_saeb.id = {args[1]};""")

        result = cursor.fetchall()
        cursor.close()
        dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:

            # tup1 = ('id', 'FK_UF_id' ,'nome_uf' , 'FK_municipio_id', 'municipio_nome' , 'FK_escola_id', 'nome_escola' , 'nome_rotina','ordem', 'nome_momento', 'descricao', 'FK_turma_id', 'educador_nome',
            #             'FK_etapa_ensino_id' , 'etapa_ensino_nome', 'FK_grau_etapa_ensino_id', 'nome_grau', 'componente_curricular_nome', 'ano', 'nome_turma', 'turno_nome')
            tup1 = ('id', 'FK_UF_id', 'uf', 
                    'estado_nome', 'FK_municipio_id', 'municipio_nome', 'FK_escola_id', 'nome_escola',
                    'nome_rotina', 'ano',
                    'ordem', 'nome_momento', 'descricao')

            tup2 = estadoTupla

            if len(tup1) == len(tup2):
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)

        # AceptKeysListTurmaCompoenente = {'FK_turma_id':int, 'educador_nome':str,
        #                 'FK_etapa_ensino_id':int , 'etapa_ensino_nome':str,  'FK_grau_etapa_ensino_id':int , 'nome_grau':str, 'componente_curricular_nome':str, 'nome_turma':str, 'turno_nome':str}

        NotAceptKeyForStart = {'ordem':str, 'nome_momento':str,'descricao':str}

        for Dict in listEstadosDict:

            dictMmentos = {}
            # turma_compoenenteDict = {}

            for chave in Dict:

                if 'momentos' not in dictFinal.keys():
                    if chave == 'ordem':

                        dictFinal['momentos'] = {'itens':[]}
                        dictMmentos[chave] = Dict[chave]

                else:
                    if chave == 'ordem' or chave == 'nome_momento' or chave == 'descricao':

                        dictMmentos[chave] = Dict[chave]

                    if chave == 'descricao':
                        dictFinal['momentos']['itens'].append(dictMmentos)

                # if 'turma_compoenente' not in dictFinal.keys():
                #     if chave == 'FK_turma_id':

                #         dictFinal['turma_compoenente'] = {'itens':[]}
                #         turma_compoenenteDict[chave] = Dict[chave]

                # else:
                    # if chave in AceptKeysListTurmaCompoenente.keys() :

                    #     turma_compoenenteDict[chave] = Dict[chave]

                    # if chave == 'turno_nome':
                    #     dictFinal['turma_compoenente']['itens'].append(turma_compoenenteDict)

                if chave in dictFinal.keys():
                    continue


                if chave not in NotAceptKeyForStart.keys():

                        dictFinal[chave] = Dict[chave]

        # print(dictFinal)
        # input()
        return dictFinal
    
    @classmethod
    def get_notas_saeb_by_FK_escola_id_and_ano(*args, **kwargs):
        cursor = conn.cursor()

        cursor.execute(f"""SELECT notas_saeb_area_conhecimento.id, notas_saeb.FK_escola_id, escola.nome_escola, escola.FK_municipio_id,
                        municipio.nome, municipio.FK_UF_id, estado.uf, estado.nome, notas_saeb.ano, 
                        notas_saeb_area_conhecimento.id, notas_saeb_area_conhecimento.FK_area_conhecimento_id,
                        area_conhecimento.nome, notas_saeb_area_conhecimento.nota
                        FROM notas_saeb_area_conhecimento 
                        INNER JOIN area_conhecimento ON notas_saeb_area_conhecimento.FK_area_conhecimento_id = area_conhecimento.id
                        INNER JOIN notas_saeb ON notas_saeb_area_conhecimento.FK_notas_saeb_id = notas_saeb.id
                        INNER JOIN escola ON notas_saeb.FK_escola_id = escola.id
                        INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                        INNER JOIN estado ON municipio.FK_UF_id = estado.id
                        WHERE notas_saeb.FK_escola_id = {args[1]} AND notas_saeb.ano = '{args[2]}'""")

        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        dictAll = []
        dictFinal = {}
        
        listEstadosDict = []
        for estadoTupla in result:

            # tup1 = ('id', 'FK_UF_id' ,'nome_uf' , 'FK_municipio_id', 'municipio_nome' , 'FK_escola_id', 'nome_escola' , 'nome_rotina','ordem', 'nome_momento', 'descricao', 'FK_turma_id', 'educador_nome',
            #             'FK_etapa_ensino_id' , 'etapa_ensino_nome', 'FK_grau_etapa_ensino_id', 'nome_grau', 'componente_curricular_nome', 'ano', 'nome_turma', 'turno_nome')
            tup1 = ('id', 'FK_escola_id', 'nome_escola', 'FK_municipio_id',
                        'municipio_nome', 'FK_UF_id', 'estado_uf', 'estado_nome', 'ano', 
                        'notas_saeb_area_conhecimento_id', 'FK_area_conhecimento_id',
                        'area_conhecimento_nome', 'nota')

            tup2 = estadoTupla

            if len(tup1) == len(tup2):
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)

        AceptKeysListTurmaCompoenente = { 'notas_saeb_area_conhecimento_id':str, 'FK_area_conhecimento_id':str, 'area_conhecimento_nome':str, 'nota':str}

        NotAceptKeyForStart = {'notas_saeb_area_conhecimento_id':str, 'FK_area_conhecimento_id':str, 'area_conhecimento_nome':str, 'nota':int}

        # print(listEstadosDict)
        # input()

        for Dict in listEstadosDict:

            # print(dictAll)
            # input()
            
            # dictMmentos = {}
            notasDict = {}

            for chave in Dict:

                if 'notas' not in dictFinal.keys():
                    if chave == 'notas_saeb_area_conhecimento_id':

                        dictFinal['notas'] = {'itens':[]}
                        notasDict[chave] = Dict[chave]

                else:
                    if chave in AceptKeysListTurmaCompoenente.keys() :

                        notasDict[chave] = Dict[chave]

                    if chave == 'nota':
                        dictFinal['notas']['itens'].append(notasDict)

                        dictAll.append(dictFinal)
                        dictFinal = {}
                        
                if chave in dictFinal.keys():
                    continue

                
                if chave not in NotAceptKeyForStart.keys():
                        
                        dictFinal[chave] = Dict[chave]


        return dictAll

    @classmethod
    def get_notas_saeb_by_last_id(*args, **kwargs):
        cursor = conn.cursor()


        cursor.execute(f"SELECT TOP 1 * from agenda_diretoria ORDER BY id DESC;")

        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:

            tup1 = ('id', 'FK_escola_id', 'nome', 'prazo', 'recursos')
            tup2 = estadoTupla

            if len(tup1) == len(tup2):
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False


    @classmethod
    def find_by_notassaeb_by_escola_and_ano(cls, email):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        cursor = conn.cursor()
 
        cursor.execute("select * from notas_saeb where FK_escola_id = ?;", email)

        row = cursor.fetchall()

        cursor.commit()
        
        # print('Rows --->>',row, type(row) )
        # input()
        if len(row) != 0:
            return row[0]
        return False
    
    @classmethod
    def create_notas_saeb(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("""insert into notas_saeb ( FK_escola_id, ano) OUTPUT INSERTED.id values(?,?);
                           """,args[1], args[2])



            result = cursor.fetchone()
            cursor.commit()
            cursor.close()
            return result[0]
            # print(result[0])
            # input()
            # conn.commit()
            # cursor.close()

            # listEstadosDict = []
            # for estadoTupla in result:

            #     tup1 = ('id', 'nome', 'FK_escola_id', 'ano_letivo')
            #     tup2 = estadoTupla

            #     if len(tup1) == len(tup2):
            #         res = dict(zip(tup1, tup2))
            #         # print(res)

            #         listEstadosDict.append(res)

            # if len(listEstadosDict) != 0:
            #     return listEstadosDict

            # return False
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    @classmethod
    def associate_notas_saeb_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into notas_saeb_momento ( FK_notas_saeb_id, FK_momento_id) values(?,?);",args[1], args[2])

            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def associate_notas_saeb_area_conhecimento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into notas_saeb_area_conhecimento ( FK_area_conhecimento_id, FK_notas_saeb_id, nota) values(?,?,?);",args[1], args[2], args[3])

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
    def create_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into momento ( nome_momento, ordem, descricao) OUTPUT INSERTED.id values(?,?,?);",args[1], args[2], args[3])

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
    def associate_notas_saeb_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into notas_saeb_momento ( FK_notas_saeb_id, FK_momento_id) OUTPUT INSERTED.id values(?,?);",args[1], args[2])

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
    def update_notas_saeb(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute('''
                        UPDATE notas_saeb
                        SET nome = ?, FK_escola_id = ? , ano_letivo = ?
                        WHERE id = ?
                        ''',args[1],args[2], args[3], int(args[4]))

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
                            DELETE FROM rotina_componente_turma WHERE FK_notas_saeb = ?;

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
    def delete_notas_saeb_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()

            cursor.execute('''
                            DELETE FROM notas_saeb_momento WHERE FK_momento_id = ?;

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
                            DELETE FROM notas_saeb_momento WHERE FK_momento_id = ?;

                            ''', args[1])


            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None