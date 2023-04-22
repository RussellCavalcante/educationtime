from sqlalchemy.dialects.postgresql import UUID
from app import banco
from uuid import uuid1, uuid4
import json
import re
from app import conn



class UserModel():
    # __tablename__ = 'users'
    

    # id = banco.Column(banco.String(36),default=lambda x:str(uuid1()), primary_key=True)
    # username = banco.Column(banco.String(255), nullable=False)
    # password = banco.Column(banco.String(64), nullable=False)
    # email = banco.Column(banco.String(255), nullable=False)
    # phone = banco.Column(banco.Integer(), nullable=False)
    # salt = banco.Column(banco.String(36),default=lambda x:str(uuid4()))


    def __init__(self, username, password, email, phone, salt):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.salt = salt


    def json(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'salt': self.salt
        }

    def assert_password(*args, **kwargs) -> bool:
        from hashlib import md5

        password_with_md5 = args[1] + args[2]
        password_with_md5 = md5(str(password_with_md5).encode('utf-8')).hexdigest()

        cursor = conn.cursor()
 
        cursor.execute(f"select password from users where id={args[0]};")

        password = cursor.fetchall()
        cursor.close()

        return password_with_md5 == password[0][0]
    
    @classmethod
    def email_validator(cls, email):    
        regex =  r"^[A-Za-z0-9](([_.-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([.-]?[a-zA-Z0-9]+)*)([.][A-Za-z]{2,4})$"
        if(re.search(regex,email)): 
            return email
        return None


    @classmethod
    def find_user(cls, id):
        user = cls.query.filter_by(id=id).first()  #select * from hoteis where hotel_id = $hotel_id
        if user:
            return user
        return None

    @classmethod
    def find_salt_by_id(cls, id):
        # user = cls.query.filter_by(id=id).first()  #select * from hoteis where hotel_id = $hotel_id
        cursor = conn.cursor()
 
        user = cursor.execute(f"select * from users where id={id[0]};")

        rows = cursor.fetchall()

        if len(rows) != 0:
            return rows[0][7]
        return None
    
    @classmethod
    def find_by_login(cls, username):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        cursor = conn.cursor()
 
        cursor.execute("select * from users where cpf = ?;", username)

        row = cursor.fetchall()

        cursor.commit()
        
        # print('Rows --->>',row, type(row) )
        # input()
        if len(row) != 0:
            return row[0]
        return False
    
    @classmethod
    def find_profissional_by_FK_user_id(*args, **kwargs):

        cursor = conn.cursor()
        qtd = kwargs.get('qtd')
        if not qtd:
            qtd = None
             
        queryDefalt = f"""SELECT CAST( (SELECT distinct {'TOP ' + str(qtd) if qtd else ''} profissonal_escola_perfil.id AS profissonal_escola_perfil__id, 
                            profissonal_escola_perfil.FK_escola_id AS profissonal_escola_perfil__FK_escola_id, 
                            escola.nome_escola AS escola__nome_escola,  
                            profissonal_escola_perfil.FK_perfil_id AS profissonal_escola_perfil__FK_perfil_id, 
                            profiles.profile_name AS profiles__profile_name, 
                            municipio.FK_UF_id AS  municipio__FK_UF_id, 
                            estado.nome AS estado__nome, 
                            escola.FK_municipio_id AS escola__FK_municipio_id, 
                            municipio.nome AS municipio__nome
                            FROM profissonal_escola_perfil
                            INNER JOIN escola ON profissonal_escola_perfil.FK_escola_id = escola.id 
                            INNER JOIN profiles ON profissonal_escola_perfil.FK_perfil_id = profiles.id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            WHERE profissonal_escola_perfil.FK_user_id = {args[1]} """
        
        
        is_first_condition = True
        for column, value in kwargs.items():
            if column != 'order_by' and column != 'qtd' and column != 'IdLog' and value is not None:
                if is_first_condition:
                    if column != 'qtd':
                    
                        columnSplited = column.split('__')
                    
                    
                        queryDefalt += f"WHERE {columnSplited[0]}.{columnSplited[1]} = {value}"
                        is_first_condition = False
                      
                
                else:
                    columnSplited = column.split('__')
                      
                    queryDefalt += f"AND {columnSplited[0]}.{columnSplited[1]} = {value}"
                
                
                
                    

        order_by = kwargs.get('order_by')
        if order_by:
            queryDefalt += f" ORDER BY {order_by}"
        
         
        
        queryDefalt += " FOR JSON PATH, ROOT('request')) AS VARCHAR(MAX));"

        cursor.execute(queryDefalt)
        result = cursor.fetchall()

        if result[0][0] != None:
            s = str(result)

            
            strip1 = s.lstrip("[('")
            strip2 = strip1.rstrip("', )]")
            
            j = json.loads(strip2)

            return j
        return False

    @classmethod
    def find_dirigente_by_FK_user_id(*args, **kwargs):

        cursor = conn.cursor()
        qtd = kwargs.get('qtd')
        if not qtd:
            qtd = None
             
        queryDefalt = f"""SELECT CAST( (SELECT distinct {'TOP ' + str(qtd) if qtd else ''} dirigente_municipal.id AS dirigente_municipal__id, 
                            dirigente_municipal.data_inicio AS dirigente_municipal__data_inicio,
                            dirigente_municipal.data_fim AS dirigente_municipal__data_fim, 
                            dirigente_municipal.FK_secretaria_municipal_id AS dirigente_municipal__FK_secretaria_municipal_id,
                            dirigente_municipal.FK_user_id AS dirigente_municipal__FK_user_id,
                            users.nome AS users__nome,
                            users.email AS users__email, 
                            users.telefone AS users__telefone,
                            users.cpf AS  users__cpf, 
                            users.accept_lgpd AS users__accept_lgpd,
                            users.perfil_ativo AS users__perfil_ativo, 
                            secretaria_municipal.nome AS secretaria_municipal__nome, 
                            secretaria_municipal.FK_secretaria_municipio_id AS secretaria_municipal__FK_secretaria_municipio_id,
                            municipio.nome AS municipio__nome,
                            municipio.FK_UF_id AS municipio__FK_UF_id,
                            estado.nome AS estado__nome, 
                            estado.uf AS estado__ud
                             FROM  dirigente_municipal 
                            INNER JOIN  users ON  dirigente_municipal.FK_user_id =  users.id 
                            INNER JOIN  secretaria_municipal ON  dirigente_municipal.FK_secretaria_municipal_id =  secretaria_municipal.id 
                            INNER JOIN  municipio ON  secretaria_municipal.FK_secretaria_municipio_id =  municipio.id 
                            INNER JOIN  estado ON  municipio.FK_UF_id =  estado.id
                            WHERE dirigente_municipal.FK_user_id = {args[1]} """
        
        
        is_first_condition = True
        for column, value in kwargs.items():
            if column != 'order_by' and column != 'qtd' and column != 'IdLog' and value is not None:
                if is_first_condition:
                    if column != 'qtd':
                    
                        columnSplited = column.split('__')
                    
                    
                        queryDefalt += f"WHERE {columnSplited[0]}.{columnSplited[1]} = {value}"
                        is_first_condition = False
                      
                
                else:
                    columnSplited = column.split('__')
                      
                    queryDefalt += f"AND {columnSplited[0]}.{columnSplited[1]} = {value}"
                
                
                
                    

        order_by = kwargs.get('order_by')
        if order_by:
            queryDefalt += f" ORDER BY {order_by}"
        
         
        
        queryDefalt += " FOR JSON PATH, ROOT('request')) AS VARCHAR(MAX));"

        cursor.execute(queryDefalt)
        result = cursor.fetchall()

        if result[0][0] != None:
            s = str(result)

            
            strip1 = s.lstrip("[('")
            strip2 = strip1.rstrip("', )]")
            
            j = json.loads(strip2)

            return j
        return False

    @classmethod
    def find_by_FK_secretaria_municipio_id(cls, FK_secretaria_municipio_id):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        cursor = conn.cursor()
 
        cursor.execute("select id, FK_user_id from dirigente_municipal where FK_secretaria_municipal_id = ? ;", FK_secretaria_municipio_id)

        rows = cursor.fetchall()

        cursor.commit()
        
        if len(rows) != 0:

            for row in rows:
                
                cursor.execute("select id, perfil_ativo from users where id = ? ;", row[1])

                data = cursor.fetchall()

                if data[0][1] == True:
                    return True
            
        return False
    
    @classmethod
    def find_by_email(cls, email):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        cursor = conn.cursor()
 
        cursor.execute("select * from users where email = ?;", email)

        row = cursor.fetchall()

        cursor.commit()
        
        # print('Rows --->>',row, type(row) )
        # input()
        if len(row) != 0:
            return row[0]
        return False
    
    @classmethod
    def find_by_roles(cls, username):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        cursor = conn.cursor()
 
        cursor.execute("select * from users where funcoes = ?;", username)

        row = cursor.fetchall()

        cursor.commit()
        
        # print('Rows --->>',row, type(row) )
        # input()
        if len(row) != 0:
            return row[0]
        return None

    @classmethod
    def create_user(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into users (nome , email, cpf, password, salt) values(?,?,?,?,?)",args[1], args[2], args[3], args[4], args[5])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_user(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE users
                        SET cpf = ?, nome = ?, email = ?, telefone = ? , password = ?, salt = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], args[4], args[5], args[6], args[7])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_dirigente_municipal(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into users (cpf , nome , email , telefone, perfil_ativo) values(?,?,?,?,?)",args[1], args[2], args[3], int(args[4]), args[5])
            
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
                        UPDATE users
                        SET cpf = ?, nome = ?, email = ?, telefone = ? , FK_profile_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], args[4], args[5], int(args[6])
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_profissionais_editora(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into users (cpf , nome , email , telefone, perfil_ativo, convite) values(?,?,?,?,?,?)",args[1], args[2], args[3], int(args[4]), args[5], args[6])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_convite_acesso(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into convite_acesso (FK_user_id , data_envio , link, salt) values(?,?,?,?)",args[1], args[2], args[3], args[4])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    

    @classmethod
    def update_profissionais_editora(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE users
                        SET cpf = ?, nome = ?, email = ?, telefone = ? , perfil_ativo = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], args[4], args[5], int(args[6])
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None


    @classmethod
    def create_profissionais_educacao(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into users (cpf , nome , email , telefone, perfil_ativo, convite) values(?,?,?,?,?,?)",args[1], args[2], args[3], args[4], args[5], args[6])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_log_login(*args, **kwargs):
   
            cursor = conn.cursor()
            

            conn.autocommit = True

            cursor.execute("insert into log_autenticacao (FK_user_id , date , navegador , ip ) OUTPUT INSERTED.id values(?,?,?,?)",args[1], args[2], args[3],args[4])
            
            # conn.commit()
            result = cursor.fetchone()
            cursor.commit()
            cursor.close()
            return result[0]
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def get_log_autenticacao_by_last_id(*args, **kwargs):
        cursor = conn.cursor()
        
 
        cursor.execute(f"SELECT TOP 1 * from log_autenticacao WHERE FK_user_id = {args[1]} ORDER BY id DESC ;")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_user_id', 'date', 'navegador', 'ip', 'date_logout') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False


    @classmethod
    def update_log_login(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE log_autenticacao
                        SET date_logout = ?
                        WHERE id = ?
                        ''', args[1], args[2]
                        )
            
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
                        UPDATE users
                        SET cpf = ?, nome = ?, email = ?, telefone = ? ,  perfil_ativo = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], args[4], args[5], int(args[6])
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def get_new_salt(cls, *args, **kwargs):
        return str(uuid4())


    @classmethod
    def password_encrypted(cls, password, salt, *args, **kwargs):
        from hashlib import md5

        return md5(str(password + salt).encode('utf-8')).hexdigest()


    # def save_user(self):
    #     banco.session.add(self)
    #     banco.session.commit()
    
    
    # def delete_user(self):
    #     banco.session.delete(self)
    #     banco.session.commit()

    @classmethod
    def associateUserProfile(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()

            conn.autocommit = True

            cursor.execute("insert into user_profiles (FK_user_id , FK_profile_id) values(?,?)",args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def associateUserProfile(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into user_profiles (FK_user_id , FK_profile_id) values(?,?)",args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_associateUserProfile(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE user_profiles
                        SET FK_user_id = ?, FK_profile_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], 
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def get_user_profiles_by_user_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT id, FK_user_id, FK_profile_id FROM user_profiles WHERE FK_user_id = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_user_id', 'FK_profile_id' ) 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False

    @classmethod
    def get_hash_by_hash(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"SELECT id , data_envio, data_aceito, link, salt, status FROM convite_acesso WHERE link = '{args[1]}';")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            tup1 = ('id' , 'data_envio', 'data_aceito', 'link', 'salt', 'status') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    @classmethod
    def update_convite_acesso(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE convite_acesso
                        SET data_aceito = ?, status = ?
                        WHERE FK_user_id = ?
                        ''',args[1], args[2], args[3])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_status_convite_acesso(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE convite_acesso
                        SET status = ?
                        WHERE id = ?
                        ''',args[1], args[2])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None


    @classmethod
    def get_all_hash_convites(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT convite_acesso.id , convite_acesso.FK_user_id, users.nome , 
                        profiles.profile_name , convite_acesso.data_envio, 
                        convite_acesso.data_aceito, convite_acesso.status
                        FROM convite_acesso 
                        INNER JOIN users ON convite_acesso.FK_user_id = users.id
                        INNER JOIN user_profiles ON convite_acesso.FK_user_id = user_profiles.FK_user_id
                        INNER JOIN profiles ON user_profiles.FK_profile_id = profiles.id """)
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            tup1 = ('id' , 'FK_user_id', 'nome' , 
                        'profile_name' , 'data_envio', 
                        'data_aceito', 'status') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False
    
    @classmethod
    def get_convite_by_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT convite_acesso.id , convite_acesso.FK_user_id, users.nome , profiles.profile_name ,
                        users.telefone, users.email, cpf
                        FROM convite_acesso 
                        INNER JOIN users ON convite_acesso.FK_user_id = users.id
                        INNER JOIN user_profiles ON convite_acesso.FK_user_id = user_profiles.FK_user_id
                        INNER JOIN profiles ON user_profiles.FK_profile_id = profiles.id
                        WHERE convite_acesso.id ='{args[1]}';""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            tup1 = ('id' , 'FK_user_id', 'nome' , 'profile_name' ,
                        'telefone', 'email', 'cpf') 
            
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False




    @classmethod
    def associateProfissionalEscolaPerfil(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into profissonal_escola_perfil (FK_user_id , data_inicio, data_fim ,FK_escola_id ,FK_perfil_id) values(?,?,?,?,?)",args[1], args[2], args[3], args[4], args[5])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def associateProfissionalEscolaComponentes(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into profissional_escola_componente (FK_user_id , FK_escola_id ,FK_componente_id) values(?,?,?)",args[1], args[2], args[3])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def update_profissionais_educacao_componentes(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE profissional_escola_componente
                        SET FK_user_id = ?, FK_escola_id = ?, FK_componente_id = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], int(args[4])
                        )
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    