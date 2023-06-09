from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from app.utils.defaultGet import GetModel
from uuid import uuid1, uuid4
import re
from app import conn


class TurmaModel():
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
    def get_turma(*args, **kwargs):
        queryDefalt = f""" 
                            turma.id AS turma__id, 
                            turma.nome_turma AS turma__nome_turma, 
                            turma.ano_letivo AS turma__ano_letivo, 
                            turma.FK_modalidade_id AS turma__FK_modalidade_id, 
                            modalidade.nome AS modalidade__nome, 
                            turma.FK_grau_etapa_ensino_id AS turma__FK_grau_etapa_ensino_id, 
                            grau_etapa_ensino.nome_grau AS grau_etapa_ensino__nome_grau, 
                            turma.FK_etapa_ensino_id AS turma__FK_etapa_ensino_id, 
                            etapa_ensino.nome AS etapa_ensino__nome, 
                            turma.FK_turno_id AS turma__FK_turno_id, 
                            turno.nome AS turno__nome, 
                            turma.FK_escola_id AS turma__FK_escola_id, 
                            escola.nome_escola AS escola__nome_escola, 
                            escola.FK_municipio_id AS escola__FK_municipio_id, 
                            municipio.nome AS municipio__nome, 
                            municipio.FK_UF_id municipio__FK_UF_id, 
                            estado.uf AS estado__uf, 
                            estado.nome AS estado__nome
                            FROM turma 
                            INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id 
                            INNER JOIN grau_etapa_ensino  ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id 
                            INNER JOIN  turno ON  turma.FK_turno_id =  turno.id 
                            INNER JOIN  modalidade ON turma.FK_modalidade_id = modalidade.id 
                            INNER JOIN  escola  ON turma.FK_escola_id =  escola.id 
                            INNER JOIN  municipio ON  escola.FK_municipio_id = municipio.id 
                            INNER JOIN estado  ON municipio.FK_UF_id =  estado.id
                        """
        
        j = GetModel.get_default(queryDefalt, **kwargs)
       
        return j

    @classmethod
    def get_turma_by_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select turma.id, turma.nome_turma, turma.ano_letivo, turma.FK_modalidade_id, modalidade.nome, turma.FK_grau_etapa_ensino_id, grau_etapa_ensino.nome_grau, turma.FK_etapa_ensino_id, etapa_ensino.nome, turma.FK_turno_id, turno.nome, turma.FK_escola_id, escola.nome_escola, escola.FK_municipio_id, municipio.nome, municipio.FK_UF_id, estado.uf, estado.nome FROM turma INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id INNER JOIN grau_etapa_ensino  ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id INNER JOIN  turno ON  turma.FK_turno_id =  turno.id INNER JOIN  modalidade ON turma.FK_modalidade_id = modalidade.id INNER JOIN  escola  ON turma.FK_escola_id =  escola.id INNER JOIN  municipio ON  escola.FK_municipio_id = municipio.id INNER JOIN estado  ON municipio.FK_UF_id =  estado.id WHERE turma.id = {args[1]};")
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 
                    'nome_turma',
                    'ano_letivo', 
                    'FK_modalidade_id',
                    'modalidade_nome',
                    'FK_grau_etapa_ensino_id',
                    'nome_grau',
                    'FK_etapa_ensino_id',
                    'etapa_ensino_nome',
                    'FK_turno_id',
                    'turno_nome',
                    'FK_escola_id',
                    'nome_escola',
                    'FK_municipio_id',
                    'nome_municipio',
                    'FK_UF_id',
                    'uf',
                    'nome_uf'
                ) 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_turma_by_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select turma.id, turma.nome_turma, turma.ano_letivo, turma.FK_modalidade_id, modalidade.nome, turma.FK_grau_etapa_ensino_id, grau_etapa_ensino.nome_grau, turma.FK_etapa_ensino_id, etapa_ensino.nome, turma.FK_turno_id, turno.nome, turma.FK_escola_id, escola.nome_escola, escola.FK_municipio_id, municipio.nome, municipio.FK_UF_id, estado.uf, estado.nome FROM turma INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id INNER JOIN grau_etapa_ensino  ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id INNER JOIN  turno ON  turma.FK_turno_id =  turno.id INNER JOIN  modalidade ON turma.FK_modalidade_id = modalidade.id INNER JOIN  escola  ON turma.FK_escola_id =  escola.id INNER JOIN  municipio ON  escola.FK_municipio_id = municipio.id INNER JOIN estado  ON municipio.FK_UF_id =  estado.id WHERE turma.FK_escola_id = {args[1]};")
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 
                    'nome_turma',
                    'ano_letivo', 
                    'FK_modalidade_id',
                    'modalidade_nome',
                    'FK_grau_etapa_ensino_id',
                    'nome_grau',
                    'FK_etapa_ensino_id',
                    'etapa_ensino_nome',
                    'FK_turno_id',
                    'turno_nome',
                    'FK_escola_id',
                    'nome_escola',
                    'FK_municipio_id',
                    'nome_municipio',
                    'FK_UF_id',
                    'uf',
                    'nome_uf'
                ) 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_turma_id_by_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""select id
                        FROM turma 
                        WHERE FK_escola_id = {args[1]} AND nome_turma = '{str(args[2])}';""")
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
        

                listEstadosDict.append(estadoTupla[0])   
            
        return listEstadosDict

    @classmethod
    def create_turma(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into turma ( nome_turma , FK_etapa_ensino_id , ano_letivo, FK_modalidade_id, FK_turno_id, FK_grau_etapa_ensino_id, FK_escola_id) values(?,?,?,?,?,?,?)",args[1], args[2], args[3], int(args[4]), int(args[5]), int(args[6]), int(args[7]))
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    @classmethod
    def update_turma(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            UPDATE turma
                            SET nome_turma = ?, FK_etapa_ensino_id = ?, ano_letivo = ?,FK_modalidade_id = ?,FK_turno_id = ? , FK_grau_etapa_ensino_id = ?, FK_escola_id = ?
                            WHERE id = ?
                        ''',args[1], int(args[2]), args[3], int(args[4]), int(args[5]), int(args[6]), args[7], args[8])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None


    @classmethod
    def get_modalidade(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("select * from modalidade;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_modalidade(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into modalidade ( nome ) values(?)",args[1])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def get_turno(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("select * from turno;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_turno(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into turno ( nome ) values(?)",args[1])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def get_etapa_ensino(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("select * from etapa_ensino;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_etapa_ensino(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into etapa_ensino ( nome ) values(?)",args[1])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None