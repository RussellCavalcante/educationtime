from sqlalchemy.dialects.postgresql import UUID
from app.utils.defaultGet import GetModel
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class estudanteModel():
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
    def get_estudante(*args, **kwargs):
        queryDefalt = f""" 
                            estudante.id AS estudante__id, 
                            estudante.nome AS estudante__nome, 
                            estudante.cod_nacional_estudante AS estudante__cod_nacional_estudante, 
                            estudante.data_nascimento AS estudante__data_nascimento, 
                            estudante.tipo_aluno AS estudante__tipo_aluno, 
                            estudante.nee AS estudante__nee, 
                            estudante.FK_escola_id AS estudante__FK_escola_id, 
                            escola.nome_escola AS escola__nome_escola, 
                            municipio.id AS municipio__id, 
                            municipio.nome AS municipio__nome, 
                            estado.id AS estado__id,
                            estado.nome AS estado__nome, 
                            estado.uf AS estado__uf 
                            FROM  estudante 
                            INNER JOIN  escola ON  estudante.FK_escola_id =  escola.id 
                            INNER JOIN  municipio ON  escola.FK_municipio_id =  municipio.id 
                            INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id
                        """
        
        j = GetModel.get_default(queryDefalt, **kwargs)
       
        return j


    @classmethod
    def get_estudante_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"SELECT estudante.id, estudante.nome, estudante.cod_nacional_estudante, estudante.data_nascimento, estudante.tipo_aluno, estudante.nee, estudante.FK_escola_id, escola.nome_escola, municipio.id, municipio.nome, estado.id, estado.nome, estado.uf FROM  estudante INNER JOIN  escola ON  estudante.FK_escola_id =  escola.id INNER JOIN  municipio ON  escola.FK_municipio_id =  municipio.id INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id WHERE estudante.id= {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome','cod_nacional_estudante', 'data_nascimento', 'tipo_aluno', 'nee', 'FK_escola_id', 'nome_escola', 'FK_municipio_id', 'municipio_nome', 'FK_UF_id', 'estado_nome', 'uf') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def find_by_cod_nacional_estudante(cls, cod_nacional_estudante):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        cursor = conn.cursor()
 
        cursor.execute("select * from estudante where cod_nacional_estudante = ?;", cod_nacional_estudante)

        row = cursor.fetchall()

        cursor.commit()
        
        # print('Rows --->>',row, type(row) )
        # input()
        if len(row) != 0:
            return row[0]
        return False
    

    @classmethod
    def get_estudante_cod(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"SELECT id, nome, cod_nacional_estudante FROM estudante WHERE cod_nacional_estudante= {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'estudant_nome','cod_nacional_estudante') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_estudante_cod_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"SELECT id, nome, cod_nacional_estudante FROM estudante WHERE cod_nacional_estudante = {args[1]} AND FK_escola_id = {args[2]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'estudant_nome','cod_nacional_estudante') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_estudante_by_turma_by_escola_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT
                                enturmar.FK_turma_id,
                                turma.nome_turma,
                                COUNT(enturmar.FK_turma_id) as "num_estudantes"
                                FROM enturmar
                                INNER JOIN turma ON
                                enturmar.FK_turma_id = turma.id
                                WHERE turma.FK_escola_id = {args[1]}
                                GROUP BY enturmar.FK_turma_id, turma.nome_turma ;""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('FK_turma_id', 'nome_turma', 'num_estudantes') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_estudante_nome(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"SELECT id, nome, cod_nacional_estudante FROM estudante WHERE nome like '%{args[1]}%';")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'estudant_nome','cod_nacional_estudante') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_estudante_nome_and_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"SELECT id, nome, cod_nacional_estudante FROM estudante WHERE nome like '%{args[1]}%' and FK_escola_id = {args[2]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'estudant_nome','cod_nacional_estudante') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_estudante_turma_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select enturmar.FK_estudante_id, estudante.cod_nacional_estudante, estudante.nome from turma  inner join enturmar on turma.id = enturmar.FK_turma_id inner join estudante on  estudante.id =  enturmar.FK_estudante_id where turma.id = {args[1]};")
        
         
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('FK_estudante_id',
             'cod_nacional_estudante',
             'nome') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict


    @classmethod
    def create_estudante(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute("insert into estudante ( cod_nacional_estudante, nome , data_nascimento, tipo_aluno, nee, FK_escola_id) values(?,?,?,?,?,?)",int(args[1]), args[2], args[3], args[4], args[5], int(args[6]))
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_estudante(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE estudante
                        SET cod_nacional_estudante = ?, nome = ?, data_nascimento = ?, tipo_aluno = ? , nee = ?, FK_escola_id = ? 
                        WHERE id = ?
                        ''',int(args[1]), args[2], args[3], args[4], args[5], int(args[6]), int(args[7]))

            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    