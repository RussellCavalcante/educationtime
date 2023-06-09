from sqlalchemy.dialects.postgresql import UUID
from app.utils.defaultGet import GetModel
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class DirigenteMunicipalModel():
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
    def find_by_secretaria(cls, id):
        cursor = conn.cursor()
 
        cursor.execute("select * from secretaria_municipal where id = ?;", id)

        row = cursor.fetchall()

        cursor.commit()
        
        # print('Rows --->>',row, type(row) )
        # input()
        if len(row) != 0:
            return row[0]
        return False

    @classmethod
    def get_dirigente_municipal(*args, **kwargs):
        
        queryDefalt = f""" 
                            dirigente_municipal.id AS dirigente_municipal__id, 
                            dirigente_municipal.data_inicio AS dirigente_municipal__data_inicio, 
                            dirigente_municipal.data_fim AS dirigente_municipal__data_fim, 
                            secretaria_municipal.id AS secretaria_municipal__id,
                            users.id AS users__id, 
                            users.nome AS users__nome, 
                            users.email AS users__email, 
                            users.telefone AS users__telefone, 
                            users.cpf AS users__cpf, 
                            users.accept_lgpd AS users__accept_lgpd, 
                            users.perfil_ativo AS users__perfil_ativo, 
                            secretaria_municipal.nome,
                            municipio.id AS municipio__id,
                            municipio.nome AS municipio__nome, 
                            estado.id AS estado__id, 
                            estado.uf AS estado__uf,
                            estado.nome AS estado__nome
                            FROM  dirigente_municipal 
                            INNER JOIN  users ON  dirigente_municipal.FK_user_id =  users.id 
                            INNER JOIN  secretaria_municipal ON  dirigente_municipal.FK_secretaria_municipal_id =  secretaria_municipal.id 
                            INNER JOIN  municipio ON  secretaria_municipal.FK_secretaria_municipio_id =  municipio.id 
                            INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id
                        """
        
        j = GetModel.get_default(queryDefalt, **kwargs)
       
        return j
    
    @classmethod
    def get_dirigente_municipal_by_secretaria_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT dirigente_municipal.id, users.nome FROM dirigente_municipal INNER JOIN users ON dirigente_municipal.FK_user_id =  users.id INNER JOIN  secretaria_municipal ON  dirigente_municipal.FK_secretaria_municipal_id = secretaria_municipal.id INNER JOIN municipio ON secretaria_municipal.FK_secretaria_municipio_id = municipio.id WHERE municipio.id ={args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id','nome') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_dirigente_municipal_by_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT dirigente_municipal.id, dirigente_municipal.data_inicio, dirigente_municipal.data_fim, dirigente_municipal.FK_secretaria_municipal_id, dirigente_municipal.FK_user_id, users.nome, users.email, users.telefone, users.cpf, users.accept_lgpd, users.perfil_ativo, secretaria_municipal.nome, secretaria_municipal.FK_secretaria_municipio_id, municipio.nome, municipio.FK_UF_id, estado.nome, estado.uf FROM  dirigente_municipal INNER JOIN  users ON  dirigente_municipal.FK_user_id =  users.id INNER JOIN  secretaria_municipal ON  dirigente_municipal.FK_secretaria_municipal_id =  secretaria_municipal.id INNER JOIN  municipio ON  secretaria_municipal.FK_secretaria_municipio_id =  municipio.id INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id WHERE dirigente_municipal.id = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id',
                    'data_inicio',
                    'data_fim',
                    'FK_secretaria_municipal_id',
                    'FK_user_id',
                    'nome',
                    'email',
                    'telefone',
                    'cpf',
                    'accept_lgpd',
                    'perfil_ativo',
                    'secretaria',
                    'FK_secretaria_municipio_id',
                    'municipio',
                    'FK_UF_id',
                    'estado',
                    'uf') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_dirigente_municipal(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into dirigente_municipal ( data_inicio, data_fim, FK_secretaria_municipal_id, FK_user_id) values(?,?,?,?)",args[1], args[2], int(args[3]), int(args[4]))
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def update_dirigente_municipal(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE dirigente_municipal
                        SET data_inicio = ?, data_fim = ?, FK_secretaria_municipal_id = ?, FK_user_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], int(args[3]), int(args[4]), int(args[5])
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None