from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class EscolaModel():
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
    def get_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("SELECT * FROM escola INNER JOIN municipio ON escola.FK_municipio_id = municipio.id INNER JOIN estado ON municipio.FK_UF_id = estado.id;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome_escola','endereco', 'email_escola', 'telefone', 'cod_inep', 'FK_municipio_id', 'idMunicipio', 'codigo_ibge', 'nomemunicipio', 'FK_UF_id', 'iduf', 'nomeuf', 'uf') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_escola_by_id(*args, **kwargs):
        cursor = conn.cursor()
        
 
        cursor.execute(f"SELECT * FROM escola INNER JOIN municipio ON escola.FK_municipio_id = municipio.id INNER JOIN estado ON municipio.FK_UF_id = estado.id WHERE escola.id= {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome_escola','endereco', 'email_escola', 'telefone', 'cod_inep', 'FK_municipio_id', 'idMunicipio', 'codigo_ibge', 'nomemunicipio', 'FK_UF_id', 'iduf', 'nomeuf', 'uf') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    def get_by_muncipio_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT id, nome_escola, FK_municipio_id FROM escola WHERE FK_municipio_id = {args[0]};")
        
        result = cursor.fetchall() 
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id','nome_escola', 'FK_municipio_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_escola(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into escola ( nome_escola , endereco , email_escola, telefone, cod_inep, FK_municipio_id) values(?,?,?,?,?,?)",args[1], args[2], args[3], int(args[4]), int(args[5]), int(args[6]))
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None 
    
    @classmethod
    def update_escola(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE escola
                        SET nome_escola = ?, endereco = ?, email_escola = ?,telefone = ?,cod_inep = ?, FK_municipio_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], int(args[4]), int(args[5]), args[6], args[7])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

