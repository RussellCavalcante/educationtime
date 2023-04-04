from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class AgendaDiretoriaModel():
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
    def get_agenda_diretoria(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("""SELECT  agenda_diretoria.id, agenda_diretoria.nome , estado.uf , municipio.nome ,
                        escola.nome_escola  , agenda_diretoria.prazo, agenda_analise.resultado
                        FROM agenda_diretoria
                        INNER JOIN escola ON agenda_diretoria.FK_escola_id = escola.id
                        INNER JOIN municipio ON escola.FK_municipio_id  = municipio.id
                        INNER JOIN estado ON municipio.FK_UF_id = estado.id     
                        INNER JOIN agenda_analise ON agenda_diretoria.id = agenda_analise.FK_agenda_diretoria_id              
                    ;""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'agenda_diretoria_nome' , 'uf' , 'municipio_nome' ,
                        'nome_escola'  , 'prazo', 'resultado') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_agenda_diretoria_resultado(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("""SELECT resultado, COUNT(resultado) as 'resultado_contagem' FROM agenda_analise GROUP BY resultado;""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('resultado', 'resultado_contagem') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict
    
    @classmethod
    def get_agenda_diretoria_by_id(*args, **kwargs):
        cursor = conn.cursor()
        cursor.execute(f"""SELECT  agenda_diretoria.id, agenda_diretoria.FK_escola_id , agenda_diretoria.nome , 
                            agenda_diretoria.prazo, agenda_analise.resultado, agenda_diretoria.recursos, agenda_equipe.nome, escola.nome_escola, estado.nome,  municipio.FK_UF_id, municipio.nome, escola.FK_municipio_id
                            FROM agenda_equipe  
                            INNER JOIN agenda_diretoria ON agenda_equipe.FK_agenda_diretoria_id = agenda_diretoria.id
                            INNER JOIN agenda_analise ON agenda_diretoria.id = agenda_analise.FK_agenda_diretoria_id
                            INNER JOIN escola ON agenda_diretoria.FK_escola_id = escola.id 
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            WHERE agenda_equipe.FK_agenda_diretoria_id =   {args[1]};""") 
        
        result = cursor.fetchall()
        cursor.close()
        dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_escola_id' , 'nome' , 
                    'prazo', 'resultado', 'recursos', 'agenda_equipe_nome',  'nome_escola' ,'estado_nome', 'FK_UF_id', 'municipio_nome', 'FK_municipio_id') 
            tup2 = estadoTupla

            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)   
        

        for Dict in listEstadosDict:
        
            dictFatores = {}
            for chave in Dict:
                
                if 'equipe' not in dictFinal.keys():
                    if chave == 'agenda_equipe_nome':
                        
                        dictFinal['equipe'] = {'itens':[]}
                        dictFatores[chave] = Dict[chave]
                        
                        dictFinal['equipe']['itens'].append(dictFatores)
                       
                else:
                    if chave == 'agenda_equipe_nome':
                        
                        dictFatores[chave] = Dict[chave]
                   
                        dictFinal['equipe']['itens'].append(dictFatores)
                        
                if chave in dictFinal.keys():
                    continue

                    
                
                if chave != 'agenda_equipe_nome':
                    dictFinal[chave] = Dict[chave] 
        
        return dictFinal
    
    @classmethod
    def get_agenda_diretoria_fatores_by_last_id(*args, **kwargs):
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

    def get_by_agenda_diretoria_id(*args, **kwargs):
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT id, nome_escola, FK_municipio_id FROM escola WHERE FK_municipio_id = {args[0]};")
        
        result = cursor.fetchall() 
        cursor.close()

     
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id','nome_escola', 'FK_municipio_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def associate_agenda_diretorias_equipe(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
    
            cursor.execute("insert into agenda_equipe ( nome, FK_agenda_diretoria_id) values(?,?);",args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None 

    @classmethod
    def create_agenda_diretoria(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into agenda_diretoria ( FK_escola_id , nome , prazo, recursos) values(?,?,?,?)",args[1], args[2], args[3], args[4])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None 
    
    @classmethod
    def create_first_agenda_diretoria_analise(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into agenda_analise ( FK_agenda_diretoria_id , resultado ) values(?,?)",args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None 

    @classmethod
    def update_agenda_analise(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE agenda_analise
                        SET resultado = ?, titulo = ?, mensagem = ?
                        WHERE FK_agenda_diretoria_id = ?
                        ''',args[1], args[2], args[3], args[4])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None
    
    @classmethod
    def update_agenda_diretoria(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                        UPDATE agenda_diretoria
                        SET FK_escola_id = ?, nome = ?, prazo = ?,recursos = ?
                        WHERE id = ?
                        ''',args[1], args[2], args[3], args[4], int(args[5]))
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def delete_agenda_equipe(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
                # print(args)
                # input()
            
            cursor.execute('''
                            DELETE FROM agenda_equipe WHERE FK_agenda_diretoria_id = ?;
                            
                            ''', args[1])
                        
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None