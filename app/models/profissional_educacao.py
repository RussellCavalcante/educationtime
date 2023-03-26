from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class ProfissionaisEducacaoModel():
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
    def get_profissionais_educacao(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("""SELECT profissonal_escola_perfil.id ,  profissonal_escola_perfil.FK_user_id, 
                        users.nome, users.email, users.telefone, users.cpf, users.accept_lgpd, users.perfil_ativo,
                        profissonal_escola_perfil.FK_perfil_id, profiles.profile_name, escola.id, escola.nome_escola ,
                        escola.FK_municipio_id, municipio.id, municipio.nome, estado.id, estado.nome, estado.uf
                        FROM profissonal_escola_perfil 
                        INNER JOIN  users ON  profissonal_escola_perfil.FK_user_id =  users.id 
                        INNER JOIN  escola ON  profissonal_escola_perfil.FK_escola_id =  escola.id 
                        INNER JOIN  municipio ON  escola.FK_municipio_id =  municipio.id 
                        INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id 
                        INNER JOIN  profiles ON  profissonal_escola_perfil.FK_perfil_id = profiles.id 
                        INNER JOIN  profissional_escola_componente ON  profissonal_escola_perfil.FK_user_id = profissional_escola_componente.FK_user_id 
                        """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'FK_user_id', 'nome', 'email', 'telefone', 'cpf', 'accept_lgpd', 'perfil_ativo',
                        'FK_perfil_id', 'profile_name', 'escola_id', 'nome_escola' ,
                        'FK_municipio_id', 'municipio_id', 'municipio_nome', 'estado_id', 'estado_nome', 'estado_uf' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_profissionais_educacao_nome(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT profissionais_educacao.FK_user_id, users.nome FROM profissionais_educacao 
        INNER JOIN users ON profissionais_educacao.FK_user_id = users.id 
        WHERE users.nome like '%{args[1]}%';""")
                                    
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_profissionais_educacao_by_FK_user_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"""SELECT profissionais_educacao.id ,  profissionais_educacao.FK_user_id, users.nome, 
                        users.email, users.telefone , users.cpf, 
                        users.accept_lgpd, users.perfil_ativo
                        FROM  profissionais_educacao 
                        INNER JOIN  profissonal_escola_perfil ON  profissionais_educacao.FK_user_id =  profissonal_escola_perfil.FK_user_id 
                        INNER JOIN  users ON  profissionais_educacao.FK_user_id =  users.id WHERE profissionais_educacao.FK_user_id = {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' ,  'FK_user_id', 'nome', 
                        'email', 'telefone' , 'cpf', 
                        'accept_lgpd', 'perfil_ativo' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False

    @classmethod
    def get_profissionais_educacao_by_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"""SELECT profissonal_escola_perfil.id ,  profissonal_escola_perfil.FK_user_id, 
                        users.nome, users.email, users.telefone, users.cpf, users.accept_lgpd, users.perfil_ativo,
                        profissonal_escola_perfil.FK_perfil_id, profiles.profile_name, escola.id, escola.nome_escola ,
                        escola.FK_municipio_id, municipio.id, municipio.nome, estado.id, estado.nome, estado.uf
                        FROM profissonal_escola_perfil 
                        INNER JOIN  users ON  profissonal_escola_perfil.FK_user_id =  users.id 
                        INNER JOIN  escola ON  profissonal_escola_perfil.FK_escola_id =  escola.id 
                        INNER JOIN  municipio ON  escola.FK_municipio_id =  municipio.id 
                        INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id 
                        INNER JOIN  profiles ON  profissonal_escola_perfil.FK_perfil_id = profiles.id 
                        INNER JOIN  profissional_escola_componente ON  profissonal_escola_perfil.FK_user_id = profissional_escola_componente.FK_user_id 
                         WHERE profissonal_escola_perfil.id = {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'FK_user_id', 'nome', 'email', 'telefone', 'cpf', 'accept_lgpd', 'perfil_ativo',
                        'FK_perfil_id', 'profile_name', 'escola_id', 'nome_escola' ,
                        'FK_municipio_id', 'municipio_id', 'municipio_nome', 'estado_id', 'estado_nome', 'estado_uf') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

        # cursor = conn.cursor()
        
        # cursor.execute(f"SELECT dirigente_municipal.id, dirigente_municipal.data_inicio, dirigente_municipal.data_fim, dirigente_municipal.FK_secretaria_municipal_id, dirigente_municipal.FK_user_id, users.nome, users.email, users.telefone, users.cpf, users.accept_lgpd, users.FK_profile_id, users.perfil_ativo, secretaria_municipal.nome, secretaria_municipal.FK_secretaria_municipio_id, municipio.nome, municipio.FK_UF_id, estado.nome, estado.uf FROM  dirigente_municipal INNER JOIN  users ON  dirigente_municipal.FK_user_id =  users.id INNER JOIN  secretaria_municipal ON  dirigente_municipal.FK_secretaria_municipal_id =  secretaria_municipal.id INNER JOIN  municipio ON  secretaria_municipal.FK_secretaria_municipio_id =  municipio.id INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id WHERE dirigente_municipal.id = {args[1]};")
        
        # result = cursor.fetchall()
        # cursor.close()

     
        # listEstadosDict = []
        # for estadoTupla in result:
            
        #     tup1 = ('id',
        #             'data_inicio',
        #             'data_fim',
        #             'FK_secretaria_municipal_id',
        #             'FK_user_id',
        #             'nome',
        #             'email',
        #             'telefone',
        #             'cpf',
        #             'accept_lgpd',
        #             'FK_profile_id',
        #             'perfil_ativo',
        #             'secretaria',
        #             'FK_secretaria_municipio_id',
        #             'municipio',
        #             'FK_UF_id',
        #             'estado',
        #             'uf') 
        #     tup2 = estadoTupla
           
        #     if len(tup1) == len(tup2): 
        #         res = dict(zip(tup1, tup2)) 
        #         # print(res)

        #         listEstadosDict.append(res)   
            
        # return listEstadosDict


    @classmethod
    def get_profissionais_educacao_escola_perfil(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("SELECT profissonal_escola_perfil.id ,  profissonal_escola_perfil.FK_user_id, users.nome, users.email, users.telefone, users.cpf, users.accept_lgpd, users.FK_profile_id, users.perfil_ativo, profiles.profile_name, escola.id, escola.nome_escola ,escola.FK_municipio_id, municipio.id, municipio.nome, estado.id, estado.nome, estado.uf FROM  profissonal_escola_perfil INNER JOIN  users ON  profissonal_escola_perfil.FK_user_id =  users.id INNER JOIN  escola ON  profissonal_escola_perfil.FK_escola_id =  escola.id INNER JOIN  municipio ON  escola.FK_municipio_id =  municipio.id INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id INNER JOIN  profiles ON  users.FK_profile_id =  profiles.id; ")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' ,  'FK_user_id', 'nome', 'email', 'telefone', 'cpf', 'accept_lgpd', 'FK_profile_id', 'perfil_ativo', 'profiles_profile_name', 'escola_id', 'nome_escola' ,'FK_municipio_id', 'municipio_id', 'municipio_nome', 'estado_id', 'estado_nome', 'uf') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_profissionais_educacao_escola_perfil_by_escola_id(*args, **kwargs):
        cursor = conn.cursor()
        # print(args)
        # input()
 
        cursor.execute(f"SELECT profissonal_escola_perfil.id ,  profissonal_escola_perfil.FK_user_id, users.nome, users.email, users.telefone, users.cpf, users.accept_lgpd, users.perfil_ativo, profissonal_escola_perfil.FK_perfil_id, profiles.profile_name, escola.id, escola.nome_escola ,escola.FK_municipio_id, municipio.id, municipio.nome, estado.id, estado.nome, estado.uf FROM  profissonal_escola_perfil INNER JOIN  users ON  profissonal_escola_perfil.FK_user_id =  users.id INNER JOIN  escola ON  profissonal_escola_perfil.FK_escola_id =  escola.id INNER JOIN  municipio ON  escola.FK_municipio_id =  municipio.id INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id INNER JOIN  profiles ON  profissonal_escola_perfil.FK_perfil_id =  profiles.id WHERE profissonal_escola_perfil.FK_escola_id = {args[1]} ")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' ,  'FK_user_id', 'nome', 'email', 'telefone', 'cpf', 'accept_lgpd', 'FK_profile_id', 'perfil_ativo', 'profiles_profile_name', 'escola_id', 'nome_escola' ,'FK_municipio_id', 'municipio_id', 'municipio_nome', 'estado_id', 'estado_nome', 'uf') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
        

    @classmethod
    def create_profissionais_educacao(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()

                # print(args)
                # input()
    
            cursor.execute("insert into profissionais_educacao ( FK_user_id) values(?);",args[1],)
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def associate_profissonal_escola_perfil(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into profissonal_escola_perfil ( FK_escola_id, FK_user_id) values(?,?);",args[1], int(args[2]))
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None 

    

    @classmethod
    def update_profissionais_educacao(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE profissionais_educacao
                        SET FK_escola_id = ?, FK_user_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], int(args[3])
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_profissionais_escola_perfil(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into profissionais_escola_perfil ( FK_user_id, FK_escola_id, FK_perfil_id) values(?,?,?);",args[1], int(args[2]), args[3])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_profissionais_educacao(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE profissonal_escola_perfil
                        SET  FK_user_id = ? , FK_escola_id = ?, FK_perfil_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], int(args[3]), int(args[3])

                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def get_profissionais_escola_componentes_by_cpf(*args, **kwargs):
        cursor = conn.cursor()
        # print(args)
        # input()
 
        cursor.execute(f"""SELECT profissionais_educacao.id ,  profissionais_educacao.FK_user_id, users.nome, 
                        users.email, users.telefone , users.cpf, 
                        users.accept_lgpd, users.perfil_ativo
                        FROM  profissionais_educacao 
                        INNER JOIN  users ON  profissionais_educacao.FK_user_id =  users.id WHERE users.cpf = {args[1]} ; """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            tup1 = ('id' ,  'FK_user_id', 'nome', 
                    'email', 'telefone', 'cpf', 
                    'accept_lgpd', 'perfil_ativo') 
            tup2 = estadoTupla
            if len(tup1) == len(tup2):
                res = dict(zip(tup1, tup2)) 

                listEstadosDict.append(res)   

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    @classmethod
    def get_componentes_by_profissional(*args, **kwargs):
        cursor = conn.cursor()
        # print(args)
        # input()
 
        cursor.execute(f"""SELECT  profissional_escola_componente.id, profissional_escola_componente.FK_user_id ,users.nome , escola.nome_escola, componente_curricular.id, componente_curricular.nome FROM profissional_escola_componente 
                            INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                            INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                            INNER JOIN escola ON profissional_escola_componente.FK_escola_id = escola.id WHERE profissional_escola_componente.FK_user_id = {args[1]} ; """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_user_id' ,'nome' , 'nome_escola', 'componente_curricular_id', 'componente_curricular_nome' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    

    @classmethod
    def get_componentes_id_by_FK_turma_id(*args, **kwargs):
        cursor = conn.cursor()
        # print(args)
        # input()
 
        cursor.execute(f"""SELECT FK_componente_id FROM profissional_escola_componente WHERE FK_escola_id = {args[1]} ; """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
    
        listEstadosDict = []
        for estadoTupla in result:

                listEstadosDict.append(estadoTupla[0])   
            
        return listEstadosDict

    @classmethod
    def delete_profissionais_escola_componentes(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            DELETE FROM profissional_escola_componente WHERE FK_componente_id = ?;
                            
                            ''', args[1])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def get_profissionais_escola_componentes(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT profissonal_escola_perfil.id ,  profissonal_escola_perfil.FK_user_id, 
                        users.nome, users.email, users.telefone, users.cpf, users.accept_lgpd, users.perfil_ativo,
                        profissonal_escola_perfil.FK_perfil_id, profiles.profile_name, escola.id, escola.nome_escola ,
                        escola.FK_municipio_id, municipio.id, municipio.nome, estado.id, estado.nome, estado.uf , 
                        profissional_escola_componente.id, profissional_escola_componente.FK_user_id , 
                        profissional_escola_componente.FK_escola_id, profissional_escola_componente.FK_componente_id , 
                        componente_curricular.nome, componente_curricular.FK_area_conhecimento_id, area_conhecimento.nome
                        FROM profissonal_escola_perfil 
                        INNER JOIN  users ON  profissonal_escola_perfil.FK_user_id =  users.id 
                        INNER JOIN  escola ON  profissonal_escola_perfil.FK_escola_id =  escola.id 
                        INNER JOIN  municipio ON  escola.FK_municipio_id =  municipio.id 
                        INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id 
                        INNER JOIN  profiles ON  profissonal_escola_perfil.FK_perfil_id = profiles.id 
                        INNER JOIN  profissional_escola_componente ON  profissonal_escola_perfil.FK_user_id = profissional_escola_componente.FK_user_id 
                        INNER JOIN  componente_curricular ON  profissional_escola_componente.FK_componente_id = componente_curricular.id 
                        INNER JOIN  area_conhecimento ON  componente_curricular.FK_area_conhecimento_id = area_conhecimento.id WHERE profissional_escola_componente.FK_componente_id = {args[1]} AND profissional_escola_componente.FK_escola_id = {args[2]}; """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' ,  'FK_user_id', 
                    'nome', 'email', 'telefone', 'cpf', 'accept_lgpd', 'perfil_ativo',
                    'FK_perfil_id', 'profile_name', 'escola_id', 'escola_nome_escola' ,
                    'escola_FK_municipio_id', 'municipio_id', 'municipio_nome', 'estado_id', 'estado_nome', 'estado_uf' , 
                    'profissional_escola_componente_id', 'profissional_escola_componente_FK_user_id' , 
                    'profissional_escola_componente_FK_escola_id', 'profissional_escola_componente_FK_componente_id' , 
                    'componente_curricular_nome', 'componente_curricular_FK_area_conhecimento_id', 'area_conhecimento_nome') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    @classmethod
    def get_componentes_by_profissional_and_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT  profissional_escola_componente.id, profissional_escola_componente.FK_user_id ,users.nome , escola.nome_escola, componente_curricular.id, componente_curricular.nome FROM profissional_escola_componente 
                            INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                            INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                            INNER JOIN escola ON profissional_escola_componente.FK_escola_id = escola.id WHERE FK_user_id = {args[1]}  AND FK_escola_id = {args[2]}; """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_user_id' ,'nome' , 'nome_escola', 'componente_curricular_id', 'componente_curricular_nome' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    @classmethod
    def get_componentes_profissional_escola(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT  profissional_escola_componente.id, profissional_escola_componente.FK_user_id ,users.nome , escola.nome_escola, componente_curricular.id, componente_curricular.nome FROM profissional_escola_componente 
                            INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                            INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                            INNER JOIN escola ON profissional_escola_componente.FK_escola_id = escola.id WHERE FK_escola_id = {args[1]}; """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_user_id' ,'nome' , 'nome_escola', 'componente_curricular_id', 'componente_curricular_nome' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    @classmethod
    def get_profisisonal_componentes(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT  profissional_escola_componente.id, profissional_escola_componente.FK_user_id ,users.nome , escola.nome_escola, componente_curricular.id, componente_curricular.nome FROM profissional_escola_componente 
                            INNER JOIN componente_curricular ON profissional_escola_componente.FK_componente_id = componente_curricular.id
                            INNER JOIN users ON profissional_escola_componente.FK_user_id = users.id
                            INNER JOIN escola ON profissional_escola_componente.FK_escola_id = escola.id; """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_user_id' ,'nome' , 'nome_escola', 'componente_curricular_id', 'componente_curricular_nome' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    
    @classmethod
    def get_area_do_conhecimento(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT id, nome FROM area_conhecimento;""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'nome' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    @classmethod
    def get_componente_by_area_do_conhecimento(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT id, nome, FK_area_conhecimento_id FROM componente_curricular WHERE FK_area_conhecimento_id =  {args[1]} ; """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id' , 'nome', 'FK_area_conhecimento_id' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
        # print(listEstadosDict)
        # input()

        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    