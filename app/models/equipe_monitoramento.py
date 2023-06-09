from sqlalchemy.dialects.postgresql import UUID
from app.utils.defaultGet import GetModel
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

        queryDefalt = f""" 
                        equipe_monitoramento.id as equipe_monitoramento__id, 
                        equipe_monitoramento.FK_user_id as equipe_monitoramento__FK_user_id ,  
                        users.nome as users__nome, 
                        equipe_monitoramento.FK_escola_id as equipe_monitoramento__FK_escola_id,
                        escola.nome_escola as escola__nome_escola, 
                        equipe_monitoramento.Fk_profile_id as equipe_monitoramento__Fk_profile_id, 
                        profiles.profile_name as profiles__profile_name, 
                        equipe_monitoramento.data_inicio as equipe_monitoramento__data_inicio, 
                        equipe_monitoramento.data_fim as equipe_monitoramento__data_fim,
                        escola.FK_municipio_id as escola__FK_municipio_id,
                        municipio.nome as municipio__nome,
                        municipio.FK_UF_id as municipio__FK_UF_id,
                        estado.nome as estado__nome,
                        estado.uf as estado__uf
                        FROM equipe_monitoramento 
                        INNER JOIN escola ON equipe_monitoramento.FK_escola_id = escola.id
                        INNER JOIN profiles ON equipe_monitoramento.Fk_profile_id = profiles.id
                        INNER JOIN users ON equipe_monitoramento.FK_user_id = users.id
                        INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                        INNER JOIN estado ON municipio.FK_UF_id = estado.id
                        """
        
        j = GetModel.get_default(queryDefalt, **kwargs)
       
        return j


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
    def get_equipe_monitoramento_FK_escola_id_and_user_id(*args, **kwargs):
        cursor = conn.cursor()

        # print(args)
        # input()

        cursor.execute(f"SELECT FK_escola_id FROM equipe_monitoramento WHERE FK_escola_id = {args[1]} AND FK_user_id = {args[2]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(  'result', result)
        # input()
        
        listEstadosDict = []
        for estadoTupla in result:

                listEstadosDict.append(estadoTupla[0])   
        
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
        


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
    def delete_equipe_monitoramento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            DELETE FROM equipe_monitoramento WHERE FK_escola_id = ?;
                            
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