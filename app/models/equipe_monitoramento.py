from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class EquipeMonitoramentoModel():
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
    def get_equipe_monitoramento(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("""SELECT equipe_monitoramento.id, FK_user_id, users.nome , FK_escola_id, escola.nome_escola, Fk_profile_id, 
                                profiles.profile_name , data_inicio, data_fim 
                            FROM equipe_monitoramento 
                            INNER JOIN escola ON equipe_monitoramento.FK_escola_id = escola.id
                            INNER JOIN profiles ON equipe_monitoramento.Fk_profile_id = profiles.id
                            INNER JOIN users ON equipe_monitoramento.FK_user_id = users.id""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_user_id' ,  'users_nome'  , 'FK_escola_id', 'nome_escola', 
                    'Fk_profile_id', 'profile_name' , 'data_inicio', 'data_fim') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_equipe_monitoramento_by_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"""SELECT equipe_monitoramento.id, FK_user_id, users.nome , FK_escola_id, escola.nome_escola, Fk_profile_id, 
                                profiles.profile_name , data_inicio, data_fim 
                            FROM equipe_monitoramento 
                            INNER JOIN escola ON equipe_monitoramento.FK_escola_id = escola.id
                            INNER JOIN profiles ON equipe_monitoramento.Fk_profile_id = profiles.id
                            INNER JOIN users ON equipe_monitoramento.FK_user_id = users.id
                              WHERE equipe_monitoramento.id = {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_user_id' ,  'users_nome'  , 'FK_escola_id', 'nome_escola', 
                    'Fk_profile_id', 'profile_name' , 'data_inicio', 'data_fim') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_equipe_monitoramento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into equipe_monitoramento ( FK_user_id , FK_escola_id, Fk_profile_id, data_inicio, data_fim) values(?,?,?,?,?)", args[1], args[2], args[3], args[4], args[5])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def delete_create_equipe_monitoramento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            DELETE FROM create_equipe_monitoramento WHERE Fk_estudante_id = ?;
                            
                            ''', args[1])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_equipe_monitoramento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE equipe_monitoramento
                        SET FK_user_id = ?, FK_escola_id = ?, Fk_profile_id = ? , data_inicio = ?, data_fim = ?
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