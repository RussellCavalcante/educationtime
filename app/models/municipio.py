from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class MunicipioModel():
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
    def get_municipios_by_uf(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from municipio where FK_UF_id={args[1]}")
        
        estados = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in estados:
            
            tup1 = ('id', 'codigo_ibge', 'nome', 'FK_UF_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_municipios_by_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from municipio where id={args[1]}")
        
        estados = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in estados:
            
            tup1 = ('id', 'codigo_ibge', 'nome', 'FK_UF_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                listEstadosDict.append(res)   
            
        return listEstadosDict


    @classmethod
    def get_municipios_by(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from municipio;")
        
        estados = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in estados:
            
            tup1 = ('id', 'codigo_ibge', 'nome', 'FK_UF_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                listEstadosDict.append(res)   
            
        return listEstadosDict


    @classmethod
    def create_municipio(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2])
            # input()
            
            cursor.execute("insert into municipio (codigo_ibge, nome, FK_UF_id) values(?,?,?)",args[1], args[2], args[3])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None


    @classmethod
    def update_municipio(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE municipio
                        SET codigo_ibge = ?, nome = ? , FK_UF_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], args[4])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None