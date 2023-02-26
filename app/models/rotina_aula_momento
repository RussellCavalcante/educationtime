from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class MomentoModel():
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
    def get_rotina_aula_momento(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("select * from rotina_aula_momento;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_rotina_aula_id','FK_momento_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_rotina_aula_momento_by_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from rotina_aula_momento where id = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_rotina_aula_id','FK_momento_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_rotina_aula_momento_by_FK_rotina_aula_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from momento where FK_rotina_aula_id = '{args[1]}';")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_rotina_aula_id','FK_momento_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict


    @classmethod
    def create_rotina_aula_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute("insert into rotina_aula_momento ( FK_rotina_aula_id, FK_momento_id ) values(?,?);",int(args[1]), int(args[2]))
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_rotina_aula_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE rotina_aula_momento
                        SET FK_rotina_aula_id = ?, FK_momento_id = ? 
                        WHERE id = ?
                        ''',int(args[1]), int(args[2]))
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None