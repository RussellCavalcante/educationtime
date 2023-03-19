from sqlalchemy.dialects.postgresql import UUID
from app import banco
from uuid import uuid1, uuid4
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
        return None
    
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
    def create_dirigente_municipal(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into users (cpf , nome , email , telefone, FK_profile_id) values(?,?,?,?,?)",args[1], args[2], args[3], int(args[4]), args[5])
            
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

            cursor.execute("insert into users (cpf , nome , email , telefone, perfil_ativo) values(?,?,?,?,?)",args[1], args[2], args[3], int(args[4]), args[5])
            
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

            cursor.execute("insert into users (cpf , nome , email , telefone, perfil_ativo) values(?,?,?,?,?)",args[1], args[2], args[3], int(args[4]), args[5])
            
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
    def associateProfissionalEscolaPerfil(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into profissonal_escola_perfil (FK_user_id , FK_escola_id ,FK_perfil_id) values(?,?,?)",args[1], args[2], args[3])
            
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
    