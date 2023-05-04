from sqlalchemy.dialects.postgresql import UUID
from app.utils.defaultGet import GetModel
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class FormacaoServicosModel():
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
    def get_formacao_servico_by_rotina_componente_id(*args, **kwargs):
        cursor = conn.cursor()

        cursor.execute(f"""SELECT FK_formacao_servico
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
    def get_momento_id_by_formacao_servico(*args, **kwargs):
        cursor = conn.cursor()

        cursor.execute(f"""SELECT FK_momento_id
                            FROM formacao_servico_momento
                            WHERE FK_formacao_servico_id = {args[1]}

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
    def get_formacao_servico(*args, **kwargs):
        queryDefalt = f""" 
                            formacao_servico_escola.id AS formacao_servico_escola__id, 
                            formacao_servico.id AS formacao_servico__id, 
                            formacao_servico.FK_municipio AS formacao_servico__FK_municipio,
                            formacao_servico.nome AS formacao_servico__nome, 
                            formacao_servico.responsavel AS formacao_servico__responsavel, 
                            formacao_servico.ano_letivo AS formacao_servico__ano_letivo, 
                            formacao_servico.data_inicio AS  formacao_servico__data_inicio, 
                            formacao_servico.data_limite AS formacao_servico__data_limite, 
                            escola.id AS escola__id,
                            escola.nome_escola AS escola__nome_escola 
                            FROM formacao_servico_escola 
                            INNER JOIN formacao_servico ON formacao_servico_escola.FK_formacao_servico_id = formacao_servico.id
                            INNER JOIN escola ON formacao_servico_escola.FK_escola_id = escola.id
                        """
        
        j = GetModel.get_default(queryDefalt, **kwargs)
       
        return j

    @classmethod
    def get_formacao_servico_by_id(*args, **kwargs):
        cursor = conn.cursor()


        cursor.execute(f"""SELECT rotina_componente_turma.id, estado.id ,estado.uf , municipio.id, municipio.nome ,
                            formacao_servico.FK_escola_id, escola.nome_escola , formacao_servico.nome,
                            momento.ordem, momento.nome_momento, momento.descricao, turma.id, users.nome,
                            turma.FK_etapa_ensino_id , etapa_ensino.nome, componente_curricular.nome,
                            formacao_servico.ano_letivo, turma.nome_turma, turno.nome
                            FROM rotina_componente_turma
                            INNER JOIN formacao_servico ON rotina_componente_turma.FK_formacao_servico = formacao_servico.id
                            INNER JOIN formacao_servico_momento ON formacao_servico.id = formacao_servico_momento.FK_formacao_servico_id
                            INNER JOIN momento ON formacao_servico_momento.FK_momento_id = momento.id
                            INNER JOIN turma_componente_educador ON rotina_componente_turma.FK_turma_componente_educador_id = turma_componente_educador.id
                            INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
                            INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                            INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                            INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
                            INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id
                            INNER JOIN escola ON formacao_servico.FK_escola_id = escola.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            INNER JOIN turno ON turma.FK_turno_id = turno.id
                            WHERE rotina_componente_turma.id = {args[1]};""")

        result = cursor.fetchall()
        cursor.close()
        dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:

            tup1 = ('id', 'FK_uf_id' ,'uf' , 'FK_municipio_id', 'municipio_nome' , 'FK_escola_id', 'nome_escola' , 'nome_rotina','ordem', 'nome_momento', 'descricao', 'FK_turma_id', 'educador_nome',
                        'FK_etapa_ensino_id' , 'etapa_ensino_nome', 'componente_curricular_nome', 'ano', 'nome_turma', 'turno_nome')
            tup2 = estadoTupla

            if len(tup1) == len(tup2):
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)

        AceptKeysListTurmaCompoenente = {'FK_turma_id':int, 'educador_nome':str,
                        'FK_etapa_ensino_id':int , 'etapa_ensino_nome':str, 'componente_curricular_nome':str, 'ano':str, 'nome_turma':str, 'turno_nome':str}

        NotAceptKeyForStart = {'ordem':str, 'nome_momento':str,'descricao':str,'FK_turma_id':int, 'educador_nome':str, 'FK_etapa_ensino_id':int , 'etapa_ensino_nome':str,
                               'componente_curricular_nome':str, 'ano':str, 'nome_turma':str, 'turno_nome':str}

        for Dict in listEstadosDict:

            dictMmentos = {}
            turma_compoenenteDict = {}

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

                if 'turma_compoenente' not in dictFinal.keys():
                    if chave == 'FK_turma_id':

                        dictFinal['turma_compoenente'] = {'itens':[]}
                        turma_compoenenteDict[chave] = Dict[chave]

                else:
                    if chave in AceptKeysListTurmaCompoenente.keys() :

                        turma_compoenenteDict[chave] = Dict[chave]

                    if chave == 'turno_nome':
                        dictFinal['turma_compoenente']['itens'].append(turma_compoenenteDict)

                if chave in dictFinal.keys():
                    continue


                if chave not in NotAceptKeyForStart.keys():

                            dictFinal[chave] = Dict[chave]


        return dictFinal

    @classmethod
    def get_formacao_servico_by_last_id(*args, **kwargs):
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
    def create_formacao_servico(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("""insert into formacao_servico ( FK_municipio, ano_letivo, nome, responsavel ,data_inicio, data_limite) OUTPUT INSERTED.id values(?,?,?,?,?,?);
                           """,args[1], args[2], args[3], args[4], args[5], args[6]) 



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
    def associate_formacao_servico_escola(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into formacao_servico_escola ( FK_formacao_servico_id , FK_escola_id) values(?,?);",args[1], args[2])

            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def associate_formacao_servico_escola_profissional(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into formacao_servico_educador_componente_escola ( FK_formacao_servico_escola_id , FK_profissional_escola_componente_id) values(?,?);",args[1], args[2])

            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def associate_rotina_componente_turma(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into rotina_componente_turma ( FK_formacao_servico, FK_turma_componente_educador_id) OUTPUT INSERTED.id values(?,?);",args[1], args[2])

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
    def associate_formacao_servico_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute("insert into formacao_servico_momento ( FK_formacao_servico_id, FK_momento_id) OUTPUT INSERTED.id values(?,?);",args[1], args[2])

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
    def update_formacao_servico(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            cursor.execute('''
                        UPDATE formacao_servico
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
                            DELETE FROM rotina_componente_turma WHERE FK_formacao_servico = ?;

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
    def delete_formacao_servico_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()

            cursor.execute('''
                            DELETE FROM formacao_servico_momento WHERE FK_momento_id = ?;

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
                            DELETE FROM formacao_servico_momento WHERE FK_momento_id = ?;

                            ''', args[1])


            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None