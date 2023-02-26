from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class RotinaAulaModel():
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
    def get_rotina_aula(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("select * from rotina_aula;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome','FK_turma_id', 'FK_profissional_id', 'FK_momento_id', 'FK_componente_curricular_id', 'update_date', 'current_date') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_rotinaaula_by_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from rotina_aula where id = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome','FK_turma_id', 'FK_profissional_id', 'FK_momento_id', 'FK_componente_curricular_id', 'update_date', 'current_date') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_rotinaaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            print(args)
            input()
            
            cursor.execute("insert into rotina_aula ( nome, FK_turma_id, FK_profissional_id, FK_componente_curricular_id, update_date, date_now ) values(?,?,?,?,?,?);",args[1], int(args[2]), int(args[3]), int(args[5]), args[6], args[7])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_rotinaaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE rotina_aula
                        SET nome = ?, FK_turma_id = ? , FK_profissional_id = ?, FK_momento_id = ?, FK_componente_curricular_id = ? , update_date = ?, current_date = ?
                        WHERE id = ?
                        ''',args[1], int(args[2]), int(args[3]), int(args[4]), int(args[5]), args[6], args[7], args[8])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None