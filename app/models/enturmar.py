from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class EnturmarModel():
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
    def get_enturmar(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("SELECT enturmar.FK_estudante_id, estudante.cod_nacional_estudante, estudante.nome FROM  turma INNER JOIN  enturmar ON  turma.id =  enturmar.FK_turma_id INNER JOIN  estudante ON  estudante.id =  enturmar.FK_estudante_id ;")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id',
                    'FK_estudante_id',
                    'nome') 

            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    @classmethod
    def get_enturmar_by_turma(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT enturmar.FK_estudante_id, estudante.cod_nacional_estudante, estudante.nome FROM  turma INNER JOIN  enturmar ON  turma.id =  enturmar.FK_turma_id INNER JOIN  estudante ON  estudante.id =  enturmar.FK_estudante_id WHERE  turma.id = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id',
                    'FK_estudante_id',
                    'nome') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_enturmar_by_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT enturmar.FK_estudante_id, estudante.cod_nacional_estudante, estudante.nome FROM  turma INNER JOIN  enturmar ON  turma.id =  enturmar.FK_turma_id INNER JOIN  estudante ON  estudante.id =  enturmar.FK_estudante_id WHERE  enturmar.id = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id',
                    'FK_estudante_id',
                    'nome') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_enturmar(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into enturmar ( FK_turma_id, Fk_estudante_id) values(?,?)", args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def update_enturmar(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE enturmar
                        SET FK_turma_id = ?, Fk_estudante_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], int(args[3])
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None