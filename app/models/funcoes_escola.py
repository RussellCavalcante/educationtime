from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class FuncoesEscolaModel():
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
    def get_Funcoes_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("""SELECT funcoes_escola.id, funcoes_escola.nome, funcoes_escola.FK_escola_id, escola.nome_escola , 
                        funcoes_escola.FK_profile_id , profiles.profile_name  
                        FROM funcoes_escola 
                        INNER JOIN escola ON funcoes_escola.FK_escola_id = escola.id 
                        INNER JOIN profiles ON funcoes_escola.FK_profile_id = profiles.id ;""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome', 'FK_escola_id', 'nome_escola' , 
                        'FK_profile_id' , 'profile_name'  ) 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict


    @classmethod
    def get_Funcoes_escola_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT funcoes_escola.id, funcoes_escola.nome, funcoes_escola.FK_escola_id, escola.nome_escola , 
                        funcoes_escola.FK_profile_id , profiles.profile_name , escola.nome_escola, municipio.FK_UF_id, municipio.nome, escola.FK_municipio_id
                        FROM funcoes_escola 
                        INNER JOIN escola ON funcoes_escola.FK_escola_id = escola.id 
                        INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                        INNER JOIN estado ON municipio.FK_UF_id = estado.id
                        INNER JOIN profiles ON funcoes_escola.FK_profile_id = profiles.id WHERE funcoes_escola.id= {args[1]};""")
         
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome', 'FK_escola_id', 'nome_escola' , 
                        'FK_profile_id' , 'profile_name', 'nome_escola' ,'estado_nome', 'FK_UF_id', 'municipio_nome', 'FK_municipio_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_Funcoes_escola_by_FK_escola_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT funcoes_escola.id, funcoes_escola.nome, funcoes_escola.FK_escola_id, escola.nome_escola , 
                        funcoes_escola.FK_profile_id , profiles.profile_name  
                        FROM funcoes_escola 
                        INNER JOIN escola ON funcoes_escola.FK_escola_id = escola.id 
                        INNER JOIN profiles ON funcoes_escola.FK_profile_id = profiles.id WHERE funcoes_escola.FK_escola_id= {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome', 'FK_escola_id', 'nome_escola' , 
                        'FK_profile_id' , 'profile_name') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    

    @classmethod
    def create_funcao_escola(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute("insert into funcoes_escola ( nome, FK_escola_id , FK_profile_id) values(?,?,?)",args[1], args[2], args[3])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_funcao_escola(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE funcoes_escola
                        SET nome = ?, FK_escola_id = ?, FK_profile_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], args[4])

            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    