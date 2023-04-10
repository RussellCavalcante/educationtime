from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class TurmaComponenteEducadorModel():
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
    def get_turma_componente_educador(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("""SELECT turma_componente_educador.id , turma_componente_educador.FK_profissional_componente_id, users.nome,
                            turma_componente_educador.FK_turma_id , turma.nome_turma,
                            profissional_escola_componente.FK_componente_id , componente_curricular.nome,
                            profissional_escola_componente.FK_escola_id, escola.nome_escola
                            FROM turma_componente_educador 
                            INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
                            INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                            INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
                            INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                            INNER JOIN escola ON profissional_escola_componente.FK_escola_id = escola.id""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'FK_profissional_componente_id', 'nome',
                            'FK_turma_id' , 'nome_turma',
                            'FK_componente_id' , 'componente_curricular_nome',
                            'FK_escola_id', 'nome_escola') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_turma_componente_educador_by_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"""SELECT turma_componente_educador.id , turma_componente_educador.FK_profissional_componente_id, users.nome,
                            turma_componente_educador.FK_turma_id , turma.nome_turma,
                            profissional_escola_componente.FK_componente_id , componente_curricular.nome,
                            profissional_escola_componente.FK_escola_id, escola.nome_escola
                            FROM turma_componente_educador 
                            INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
                            INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                            INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
                            INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                            INNER JOIN escola ON profissional_escola_componente.FK_escola_id = escola.id WHERE turma_componente_educador.id ={args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'FK_profissional_componente_id', 'nome',
                            'FK_turma_id' , 'nome_turma',
                            'FK_componente_id' , 'componente_curricular_nome',
                            'FK_escola_id', 'nome_escola') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_componente_educador_FK_turma_id_(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"SELECT FK_profissional_componente_id FROM turma_componente_educador WHERE FK_turma_id = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:

                listEstadosDict.append(estadoTupla[0])   
            
        return listEstadosDict


    @classmethod
    def get_turma_componente_educador_by_turma_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"""SELECT turma_componente_educador.id , turma_componente_educador.FK_profissional_componente_id, users.nome,
                            turma_componente_educador.FK_turma_id , turma.nome_turma,
                            profissional_escola_componente.FK_componente_id , componente_curricular.nome,
                            profissional_escola_componente.FK_escola_id, escola.nome_escola
                            FROM turma_componente_educador 
                            INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
                            INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                            INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
                            INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                            INNER JOIN escola ON profissional_escola_componente.FK_escola_id = escola.id WHERE turma.id ={args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'FK_profissional_componente_id', 'nome',
                            'FK_turma_id' , 'nome_turma',
                            'FK_componente_id' , 'componente_curricular_nome',
                            'FK_escola_id', 'nome_escola') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_turma_componentes_profissional_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT turma_componente_educador.id , turma_componente_educador.FK_profissional_componente_id, users.nome,
                    turma_componente_educador.FK_turma_id , turma.nome_turma,
                    profissional_escola_componente.FK_componente_id , componente_curricular.nome,
                    profissional_escola_componente.FK_escola_id, escola.nome_escola, turma.ano_letivo,
                    etapa_ensino.id, etapa_ensino.nome, grau_etapa_ensino.id, grau_etapa_ensino.nome_grau,
                    turno.id, turno.nome
                    
                    FROM turma_componente_educador 
                    INNER JOIN profissional_escola_componente ON turma_componente_educador.FK_profissional_componente_id = profissional_escola_componente.id
                    INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                    INNER JOIN turma ON turma_componente_educador.FK_turma_id = turma.id
                    INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                    INNER JOIN escola ON profissional_escola_componente.FK_escola_id = escola.id
                    INNER JOIN etapa_ensino ON turma.FK_etapa_ensino_id = etapa_ensino.id
                    INNER JOIN grau_etapa_ensino ON turma.FK_grau_etapa_ensino_id = grau_etapa_ensino.id
                    INNER JOIN turno ON turma.FK_turno_id = turno.id
                    WHERE escola.id = {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' ,'FK_profissional_componente_id', 'educador_nome',
                    'FK_turma_id' , 'nome_turma',
                    'FK_componente_id' , 'componente_curricular_nome',
                    'FK_escola_id', 'nome_escola', 'ano', 'etapa_ensino_id', 'etapa_ensino_nome', 'FK_grau_etapa_ensino_id', 'nome_grau',
                    'turno_id', 'turno_nome') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_turma_componente_educador(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into turma_componente_educador ( FK_profissional_componente_id , FK_turma_id) values(?,?)", args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def delete_turma_componente_educador(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            DELETE FROM turma_componente_educador WHERE FK_profissional_componente_id = ?;
                            
                            ''', args[1])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_turma_componente_educador(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE turma_componente_educador
                        SET FK_profissional_componente_id = ?, FK_turma_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3]
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None