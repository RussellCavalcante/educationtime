from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class   PerfilModel():
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
    def get_perfil(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("select * from profiles;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'profile_name') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_perfil_by_id(*args, **kwargs):
        cursor = conn.cursor()
        
 
        cursor.execute(f"""SELECT profiles.id, profile_name, FK_roles_id, profile_roles.valor FROM profile_roles
                            INNER JOIN profiles ON profile_roles.FK_profile_id = profiles.id
                            WHERE profiles.id = {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close() 
        dictFinal = {}
        listEstadosDict = [] 
        for estadoTupla in result:
            
            tup1 = ('id', 'profile_name', 'FK_roles_id', 'valor') 
            tup2 = estadoTupla

            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)   
            

        for Dict in listEstadosDict:
        
            dictFatores = {}
            for chave in Dict:
                
                if 'Itens' not in dictFinal.keys():
                    if chave == 'FK_roles_id':
                        
                        dictFinal['Itens'] = {'itens':[]}
                        dictFatores[chave] = Dict[chave]
                       
                else:
                    if chave == 'FK_roles_id' or chave == 'valor':
                      
                        dictFatores[chave] = Dict[chave]
                   
                    if chave == 'valor':
                        dictFinal['Itens']['itens'].append(dictFatores)
                        
                if chave in dictFinal.keys():
                    continue

                    
                if chave != 'FK_roles_id':
                    if chave != 'valor':
                        dictFinal[chave] = Dict[chave] 

                
        return dictFinal

    @classmethod
    def get_perfil_by_user_id(*args, **kwargs):
        cursor = conn.cursor()
        
 
        cursor.execute(f"""SELECT profiles.id, profile_name, FK_roles_id, profile_roles.valor FROM profile_roles
                            INNER JOIN profiles ON profile_roles.FK_profile_id = profiles.id
                            INNER JOIN user_profiles ON profiles.id = user_profiles.FK_profile_id
                            INNER JOIN users ON user_profiles.FK_user_id = users.id
                            WHERE users.id = {args[1]};""")
        
        result = cursor.fetchall()
        cursor.close() 
        dictFinal = {}
        listEstadosDict = [] 
        for estadoTupla in result:
            
            tup1 = ('id', 'profile_name', 'FK_roles_id', 'valor') 
            tup2 = estadoTupla

            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)   
            

        for Dict in listEstadosDict:
        
            dictFatores = {}
            for chave in Dict:
                
                if 'Itens' not in dictFinal.keys():
                    if chave == 'FK_roles_id':
                        
                        dictFinal['Itens'] = {'itens':[]}
                        dictFatores[chave] = Dict[chave]
                       
                else:
                    if chave == 'FK_roles_id' or chave == 'valor':
                      
                        dictFatores[chave] = Dict[chave]
                   
                    if chave == 'valor':
                        dictFinal['Itens']['itens'].append(dictFatores)
                        
                if chave in dictFinal.keys():
                    continue

                    
                if chave != 'FK_roles_id':
                    if chave != 'valor':
                        dictFinal[chave] = Dict[chave] 

                
        return dictFinal

    @classmethod
    def get_perfilRoles_by_perfil_id(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from profile_roles where FK_profiles_id = {args[1]};")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_profiles_id', 'FK_roles_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_perfilRoles(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from profile_roles ;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_profiles_id', 'FK_roles_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_Roles(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"select * from roles ;")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'role_name') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def create_perfil(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()

            conn.autocommit = True

            cursor.execute("insert into profiles ( profile_name ) values(?)",args[1])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def find_by_profile_name(*args, **kwargs):
        try:
            # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
            cursor = conn.cursor()

            cursor.execute("select * from profiles where profile_name = ?;", args[1])

            row = cursor.fetchall()

            cursor.commit()
            
            # print('Rows --->>',row, type(row) )
            # input()
            if len(row) != 0:
                return row[0]
            return None
        except:
           return { 'error': 'nao foi possivel achar esse perfil !' }, 400
    
    @classmethod
    def find_by_profile_id(*args, **kwargs):
        try:
            # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
            cursor = conn.cursor()

            cursor.execute("""select id FROM profiles
                            WHERE id = ?;""", args[1])

            row = cursor.fetchall()

            cursor.commit()
            
            # print('Rows --->>',row, type(row) )
            # input()
            if len(row) != 0:
                return row
            return False
        except:
           return { 'error': 'nao foi possivel achar esse perfil !' }, 400
    @classmethod
    def associateProfileRoles(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        try:
            cursor = conn.cursor()

            conn.autocommit = True

            cursor.execute("insert into profile_roles ( FK_profile_id, FK_roles_id, valor ) values(?,?,?)",args[1], args[2], args[3])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        except:
           return { 'error': 'verifique se existe as roles ou perfis inseridas na requisição!' }, 400
        #     return None

    @classmethod
    def update_profile(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            UPDATE profiles
                            SET profile_name = ?
                            WHERE id = ?
                        ''', args[1], args[2])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        except:
           return { 'error': ' nao foi possivel fazer a atualização do perfil verifique a requisição  !' }, 400


    @classmethod
    def update_profile_roles(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            UPDATE profile_roles
                            SET FK_roles_id = ?, FK_profile_id = ?
                            WHERE FK_profile_id = ?
                        ''', args[1], args[2], args[3])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def delete_profile(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            DELETE FROM profiles WHERE id = ?;
                            
                            ''', args[1])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def delete_profile_roles(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1])
            # input()
            
            cursor.execute('''
                            DELETE FROM profile_roles WHERE FK_profile_id = ?;
                            
                            ''', args[1])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None