from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class SecretariaMunicipalModel():
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
    def get_secretaria_municipal(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("select * from secretaria_municipal")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome', 'cnpj', 'endereco', 'telefone', 'email', 'FK_secretaria_UF_id', 'FK_secretaria_municipio_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_secretaria_municipal_by_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from secretaria_municipal where id = {args[1]}")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome', 'cnpj', 'endereco', 'telefone', 'email', 'FK_secretaria_UF_id', 'FK_secretaria_municipio_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_secretaria_municipal(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into secretaria_municipal ( nome, cnpj, endereco, telefone, email, FK_secretaria_UF_id, FK_secretaria_municipio_id) values(?,?,?,?,?,?,?)",args[1], int(args[2]), args[3], int(args[4]), args[5], int(args[6]), int(args[7]))
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def update_secretaria_municipal(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE secretaria_municipal
                        SET nome = ?, cnpj = ?, endereco = ?,telefone = ?,email = ?,FK_secretaria_UF_id = ?, FK_secretaria_municipio_id=?
                        WHERE id = ?
                        ''',args[1], int(args[2]), args[3], int(args[4]), args[5], int(args[6]), int(args[7], args[8])
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None