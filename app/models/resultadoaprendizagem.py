from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class ResultadoAprendizagemModel():
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
    def get_resultado_aprendizagem_by_rotina_componente_id(*args, **kwargs):
        cursor = conn.cursor()

        cursor.execute(f"""SELECT FK_resultado_aprendizagem
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
    def get_momento_id_by_resultado_aprendizagem(*args, **kwargs):
        cursor = conn.cursor()

        cursor.execute(f"""SELECT FK_momento_id
                            FROM resultado_aprendizagem_momento
                            WHERE FK_resultado_aprendizagem_id = {args[1]}

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
    def get_resultado_aprendizagem(*args, **kwargs):
        cursor = conn.cursor()

        cursor.execute("""SELECT resultado_aprendizagem_acoes.id, nome_escola, escola.FK_municipio_id,
                            municipio.nome, estado.uf, estado.nome, notas_saeb.ano
                            FROM resultado_aprendizagem_acoes 
                            INNER JOIN notas_saeb_area_conhecimento ON resultado_aprendizagem_acoes.FK_notas_saeb_area_conhecimento_id = notas_saeb_area_conhecimento.id
                            INNER JOIN notas_saeb ON notas_saeb_area_conhecimento.FK_notas_saeb_id = notas_saeb.id
                            INNER JOIN escola ON notas_saeb.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id""")

        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        # dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:

            # tup1 = ('id', 'FK_UF_id' ,'nome_uf' , 'FK_municipio_id', 'municipio_nome' , 'FK_escola_id', 'nome_escola' , 'nome_rotina','ordem', 'nome_momento', 'descricao', 'FK_turma_id', 'educador_nome',
            #             'FK_etapa_ensino_id' , 'etapa_ensino_nome', 'FK_grau_etapa_ensino_id', 'nome_grau', 'componente_curricular_nome', 'ano', 'nome_turma', 'turno_nome')
            tup1 = ("id", 'nome_escola', "FK_municipio_id",
                            "municipio_nome", "estado_uf", "estado_nome", "ano")

            tup2 = estadoTupla

            if len(tup1) == len(tup2):
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)


        return listEstadosDict

    @classmethod
    def get_resultado_aprendizagem_by_id(*args, **kwargs):
        cursor = conn.cursor()


        # cursor.execute(f"""SELECT rotina_componente_turma.id, estado.id ,estado.uf , municipio.id, municipio.nome ,
        #                     resultado_aprendizagem.FK_escola_id, escola.nome_escola , resultado_aprendizagem.nome,
        #                     momento.ordem, momento.nome_momento, momento.descricao, turma.id, users.nome,
        #                     turma.FK_etapa_ensino_id , etapa_ensino.nome, grau_etapa_ensino.id, grau_etapa_ensino.nome_grau, componente_curricular.nome,
        #                     resultado_aprendizagem.ano_letivo, turma.nome_turma, turno.nome
        #                     FROM rotina_componente_turma
        #                     INNER JOIN resultado_aprendizagem ON rotina_componente_turma.FK_resultado_aprendizagem = resultado_aprendizagem.id
        #                     INNER JOIN resultado_aprendizagem_momento ON resultado_aprendizagem.id = resultado_aprendizagem_momento.FK_resultado_aprendizagem_id
        #                     INNER JOIN momento ON resultado_aprendizagem_momento.FK_momento_id = momento.id
        #                     INNER JOIN turma_componente_educador ON rotina_componente_turma.FK_turma_componente_educador_id = turma_componente_educador.id
        #                     INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
        #                     INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
        #                     INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
        #                     INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
        #                     INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id
        #                     INNER JOIN escola ON resultado_aprendizagem.FK_escola_id = escola.id
        #                     INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
        #                     INNER JOIN estado ON municipio.FK_UF_id = estado.id
        #                     INNER JOIN turno ON turma.FK_turno_id = turno.id
        #                     INNER JOIN grau_etapa_ensino ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id
        #                     WHERE rotina_componente_turma.id = {args[1]};""")
        cursor.execute(f"""SELECT resultado_aprendizagem.id, municipio.FK_UF_id, estado.uf, 
                            estado.nome, escola.FK_municipio_id, municipio.nome, resultado_aprendizagem.FK_escola_id, escola.nome_escola,
                            resultado_aprendizagem.nome, resultado_aprendizagem.ano_letivo,
                            momento.ordem, momento.nome_momento, momento.descricao
                            FROM resultado_aprendizagem_momento
                            INNER JOIN resultado_aprendizagem ON resultado_aprendizagem_momento.FK_resultado_aprendizagem_id = resultado_aprendizagem.id
                            INNER JOIN momento ON resultado_aprendizagem_momento.FK_momento_id = momento.id
                            INNER JOIN escola ON resultado_aprendizagem.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            WHERE resultado_aprendizagem.id = {args[1]};""")

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
    def get_resultado_aprendizagem_componente_educador_by_id(*args, **kwargs):
        cursor = conn.cursor()


        # cursor.execute(f"""SELECT rotina_componente_turma.id, estado.id ,estado.uf , municipio.id, municipio.nome ,
        #                     resultado_aprendizagem.FK_escola_id, escola.nome_escola , resultado_aprendizagem.nome,
        #                     momento.ordem, momento.nome_momento, momento.descricao, turma.id, users.nome,
        #                     turma.FK_etapa_ensino_id , etapa_ensino.nome, grau_etapa_ensino.id, grau_etapa_ensino.nome_grau, componente_curricular.nome,
        #                     resultado_aprendizagem.ano_letivo, turma.nome_turma, turno.nome
        #                     FROM rotina_componente_turma
        #                     INNER JOIN resultado_aprendizagem ON rotina_componente_turma.FK_resultado_aprendizagem = resultado_aprendizagem.id
        #                     INNER JOIN resultado_aprendizagem_momento ON resultado_aprendizagem.id = resultado_aprendizagem_momento.FK_resultado_aprendizagem_id
        #                     INNER JOIN momento ON resultado_aprendizagem_momento.FK_momento_id = momento.id
        #                     INNER JOIN turma_componente_educador ON rotina_componente_turma.FK_turma_componente_educador_id = turma_componente_educador.id
        #                     INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
        #                     INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
        #                     INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
        #                     INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
        #                     INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id
        #                     INNER JOIN escola ON resultado_aprendizagem.FK_escola_id = escola.id
        #                     INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
        #                     INNER JOIN estado ON municipio.FK_UF_id = estado.id
        #                     INNER JOIN turno ON turma.FK_turno_id = turno.id
        #                     INNER JOIN grau_etapa_ensino ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id
        #                     WHERE rotina_componente_turma.id = {args[1]};""")
        cursor.execute(f"""SELECT rotina_componente_turma.id , turma.id, users.nome, turma.FK_etapa_ensino_id, etapa_ensino.nome, 
                        turma.FK_grau_etapa_ensino_id, grau_etapa_ensino.nome_grau, turma.nome_turma, turno.nome,
                        profissional_escola_componente.FK_componente_id , componente_curricular.nome
                        FROM rotina_componente_turma 
                        INNER JOIN resultado_aprendizagem ON rotina_componente_turma.FK_resultado_aprendizagem = resultado_aprendizagem.id
                        INNER JOIN turma_componente_educador ON rotina_componente_turma.FK_turma_componente_educador_id = turma_componente_educador.id
                        INNER JOIN profissional_escola_componente ON  turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
                        INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                        INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                        INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
                        INNER JOIN turno ON turma.FK_turno_id = turno.id
                        INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id
                        INNER JOIN grau_etapa_ensino ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id

                        WHERE resultado_aprendizagem.id  = {args[1]};""")

        result = cursor.fetchall()
        cursor.close()
        dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:

            # tup1 = ('id', 'FK_UF_id' ,'nome_uf' , 'FK_municipio_id', 'municipio_nome' , 'FK_escola_id', 'nome_escola' , 'nome_rotina','ordem', 'nome_momento', 'descricao', 'FK_turma_id', 'educador_nome',
            #             'FK_etapa_ensino_id' , 'etapa_ensino_nome', 'FK_grau_etapa_ensino_id', 'nome_grau', 'componente_curricular_nome', 'ano', 'nome_turma', 'turno_nome')
            tup1 = ('id' , 'turma_id', 'educador_nome', 'FK_etapa_ensino_id', 'etapa_ensino_nome', 
                            'FK_grau_etapa_ensino_id', 'nome_grau', 'nome_turma', 'turno_nome','FK_componente_id' , 'componente_curricular_nome')

            tup2 = estadoTupla

            if len(tup1) == len(tup2):
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)

        AceptKeysListTurmaCompoenente = {'id':str, 'turma_id':str,'educador_nome':str,'FK_etapa_ensino_id':str, 'etapa_ensino_nome':str, 'FK_grau_etapa_ensino_id':str,'nome_grau':str, 'nome_turma':str,'turno_nome':str, 'FK_componente_id':str,'componente_curricular_nome':str}

        # NotAceptKeyForStart = {'id':str, 'turma_id':str,'educador_nome':str,'FK_etapa_ensino_id':str, 'etapa_ensino_nome':str, 'FK_grau_etapa_ensino_id':str,'nome_grau':str, 'nome_turma':str,'turno_nome':str}

        # print(listEstadosDict)
        # input()

        for Dict in listEstadosDict:

            # print(Dict)
            # input()

            # dictMmentos = {}
            turma_compoenenteDict = {}

            for chave in Dict:

                # if 'momentos' not in dictFinal.keys():
                #     if chave == 'ordem':

                #         dictFinal['momentos'] = {'itens':[]}
                #         dictMmentos[chave] = Dict[chave]

                # else:
                    # if chave == 'ordem' or chave == 'nome_momento' or chave == 'descricao':

                    #     dictMmentos[chave] = Dict[chave]

                    # if chave == 'descricao':
                    #     dictFinal['momentos']['itens'].append(dictMmentos)
                # print(chave)
                # input()

                if 'turma_compoenente' not in dictFinal.keys():
                    if chave == 'id':

                        dictFinal['turma_compoenente'] = {'itens':[]}
                        turma_compoenenteDict[chave] = Dict[chave]

                else:
                    if chave in AceptKeysListTurmaCompoenente.keys() :

                        turma_compoenenteDict[chave] = Dict[chave]

                    if chave == 'componente_curricular_nome':
                        dictFinal['turma_compoenente']['itens'].append(turma_compoenenteDict)

                if chave in dictFinal.keys():
                    continue


                # if chave not in NotAceptKeyForStart.keys():
                        
                #         dictFinal[chave] = Dict[chave]


        return dictFinal

    @classmethod
    def get_resultado_aprendizagem_by_last_id(*args, **kwargs):
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
    def create_resultado_aprendizagem(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("""insert into resultado_aprendizagem ( FK_escola_id, ano) OUTPUT INSERTED.id values(?,?);
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
    def associate_resultado_aprendizagem_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into resultado_aprendizagem_momento ( FK_resultado_aprendizagem_id, FK_momento_id) values(?,?);",args[1], args[2])

            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def associate_resultado_aprendizagem_area_conhecimento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into resultado_aprendizagem_acoes ( nome_acao, prazo, FK_notas_saeb_area_conhecimento_id) values(?,?,?);",args[1], args[2], args[3])

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
    def associate_resultado_aprendizagem_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into resultado_aprendizagem_momento ( FK_resultado_aprendizagem_id, FK_momento_id) OUTPUT INSERTED.id values(?,?);",args[1], args[2])

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