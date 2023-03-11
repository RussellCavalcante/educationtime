from sqlalchemy.dialects.postgresql import UUID
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
        cursor = conn.cursor()
 
        cursor.execute("select * from estudante;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'cod_nacional_estudante','nome', 'data_nascimento', 'tipo_aluno', 'nee') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict


    @classmethod
    def get_estudante_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from estudante where = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'cod_nacional_estudante','nome', 'data_nascimento', 'tipo_aluno', 'nee') 
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
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into estudante ( cod_nacional_estudante, nome , data_nascimento, tipo_aluno, nee, FK_escola_id) values(?,?,?,?,?,?)",int(args[1]), args[2], args[3], args[4], int(args[5]), int(args[6]))
            
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
                        ''',int(args[1]), args[2], args[3], args[4], int(args[5]), int(args[6]), int(args[7]))

            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    