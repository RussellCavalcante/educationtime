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
 
        cursor.execute("""SELECT rotina_componente_turma.id, rotina_aula.nome, users.nome, componente_curricular.nome,
                         etapa_ensino.nome, rotina_aula.ano_letivo FROM rotina_componente_turma
                        INNER JOIN rotina_aula ON rotina_componente_turma.FK_rotina_aula = rotina_aula.id
                        INNER JOIN turma_componente_educador ON rotina_componente_turma.FK_turma_componente_educador_id = turma_componente_educador.id
                        INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
                        INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                        INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                        INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
                        INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'rotina_aula_nome', 'educador_nome', 'componente_curricular_nome',
                    'etapa_ensino_nome', 'ano' )
             
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
    def get_rotina_aula_by_last_id(*args, **kwargs):
        cursor = conn.cursor()
        
 
        cursor.execute(f"SELECT TOP 1 * from agenda_diretoria ORDER BY id DESC;")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_escola_id', 'nome', 'prazo', 'recursos') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False

    @classmethod
    def create_rotinaaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input() 
            
            cursor.execute("""insert into rotina_aula ( nome, FK_escola_id, ano_letivo) OUTPUT INSERTED.id values(?,?,?);        
                           """,args[1], args[2], args[3])
            
            

            result = cursor.fetchone()
            cursor.commit()
            cursor.close()
            return result[0]
            # print(result[0])
            # input()
            # conn.commit()
            # cursor.close()

            # listEstadosDict = []
            # for estadoTupla in result:
                
            #     tup1 = ('id', 'nome', 'FK_escola_id', 'ano_letivo') 
            #     tup2 = estadoTupla
            
            #     if len(tup1) == len(tup2): 
            #         res = dict(zip(tup1, tup2))
            #         # print(res)

            #         listEstadosDict.append(res)   
                
            # if len(listEstadosDict) != 0:
            #     return listEstadosDict

            # return False
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def associate_rotina_componente_turma(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute("insert into rotina_componente_turma ( FK_rotina_aula, FK_turma_componente_educador_id) values(?,?);",args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute("insert into momento ( nome_momento, ordem, descricao) values(?,?,?);",args[1], args[2], args[3])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    
    @classmethod
    def associate_rotina_aula_momento(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            print(args)
            input()
            
            cursor.execute("insert into rotina_aula_momento ( FK_rotina_aula_id, FK_momento_id) values(?,?);",args[1], args[2])
            
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