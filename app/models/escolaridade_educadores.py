from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class EscolaridadeEducadoresModel():
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
    def get_escolaridade_educador(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT escolaridade_educador.id , FK_user_id, users.cpf, users.nome, FK_escola_id, 
                        escola.nome_escola, escolaridade, ano_conclusao, nome_instituicao, municipio.id , municipio.nome , estado.id, 
                        estado.nome, estado.uf  FROM escolaridade_educador
                        INNER JOIN users on escolaridade_educador.FK_user_id = users.id
                        INNER JOIN escola on escolaridade_educador.FK_escola_id = escola.id
                        INNER JOIN municipio on escola.FK_municipio_id = municipio.id
                        INNER JOIN estado on municipio.FK_UF_id = estado.id;""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'FK_user_id', 'cpf', 'nome', 'FK_escola_id', 
                       'nome_escola', 'escolaridade', 'ano_conclusao', 'nome_instituicao', 'FK_municipio_id','municipio_nome' ,'FK_UF_id', 
                        'estado_nome', 'estado_uf') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False

    @classmethod
    def get_escolaridade_educador_by_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT escolaridade_educador.id , FK_user_id, users.cpf, users.nome, FK_escola_id, 
                        escola.nome_escola, escolaridade, ano_conclusao, nome_instituicao, municipio.id , municipio.nome , estado.id, 
                        estado.nome, estado.uf  FROM escolaridade_educador
                        INNER JOIN users on escolaridade_educador.FK_user_id = users.id
                        INNER JOIN escola on escolaridade_educador.FK_escola_id = escola.id
                        INNER JOIN municipio on escola.FK_municipio_id = municipio.id
                        INNER JOIN estado on municipio.FK_UF_id = estado.id WHERE escolaridade_educador.id = {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'FK_user_id', 'cpf', 'nome', 'FK_escola_id', 
                       'nome_escola', 'escolaridade', 'ano_conclusao', 'nome_instituicao', 'FK_municipio_id','municipio_nome' ,'FK_UF_id', 
                        'estado_nome', 'estado_uf') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False

    @classmethod
    def get_escolaridade_educador_by_educadores(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT escolaridade_educador.id , FK_user_id, users.cpf, users.nome, FK_escola_id, escola.nome_escola, escolaridade, ano_conclusao, nome_instituicao, municipio.nome ,estado.nome, estado.uf  FROM escolaridade_educador
                        INNER JOIN users on escolaridade_educador.FK_user_id = users.id
                        INNER JOIN escola on escolaridade_educador.FK_escola_id = escola.id
                        INNER JOIN municipio on escola.FK_municipio_id = municipio.id
                        INNER JOIN estado on municipio.FK_UF_id = estado.id WHERE FK_user_id = {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'FK_user_id', 'cpf', 'nome', 'FK_escola_id', 
                    'nome_escola', 'escolaridade', 'ano_conclusao', 'nome_instituicao', 'municipio_nome' , 
                    'estado_nome', 'estado_uf') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    

    @classmethod
    def create_EscolaridadeEducadores(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into escolaridade_educador ( FK_user_id, FK_escola_id, escolaridade, ano_conclusao, nome_instituicao ) values(?,?,?,?,?)", args[1], args[2], args[3], args[4], args[5])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    # @classmethod
    # def delete_enturmar(*args, **kwargs):
    #     # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
    #     # try:
    #         cursor = conn.cursor()
    #             # print(args)
    #             # input()
            
    #         cursor.execute('''
    #                         DELETE FROM enturmar WHERE Fk_estudante_id = ?;
                            
    #                         ''', args[1])
                        
            
    #         conn.commit()
    #         # conn.close()
    #         # return 'created'
    #         # rows = cursor.fetchall()
    #     # except:
    #     #     print(TypeError)
    #     # #     return None

    @classmethod
    def update_escolaridade_educador(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE escolaridade_educador
                        SET FK_user_id = ?, FK_escola_id = ? , escolaridade = ?, ano_conclusao = ?, nome_instituicao = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], args[4], args[5], args[6]
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None