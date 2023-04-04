from sqlalchemy.dialects.postgresql import UUID
# from app import banco
from uuid import uuid1, uuid4
import re
from app import conn


class planoAulaModel():
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
    def get_planoaula(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute(f"""SELECT plano_aula.id, unidade_tematica, FK_componente_escola_profissional_id, componente_curricular.nome,
                    FK_etapa_ensino,etapa_ensino.nome, ano, bimestre_escolar, resultado 
                    FROM plano_aula 
                    INNER JOIN profissional_escola_componente ON plano_aula.FK_componente_escola_profissional_id = profissional_escola_componente.id
                    INNER JOIN componente_curricular on profissional_escola_componente.FK_componente_id = componente_curricular.id
                    INNER JOIN etapa_ensino on plano_aula.FK_etapa_ensino = etapa_ensino.id
                    ; ;""")
        
        result = cursor.fetchall()
        cursor.close()

        # print(result)
        # input()
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'unidade_tematica', 'FK_componente_escola_profissional_id', 'componente_curricular_nome',
                    'FK_etapa_ensino', 'etapa_ensino_nome', 'ano', 'bimestre_escolar', 'resultado' ) 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        return listEstadosDict

    @classmethod
    def get_plano_aula_by_id(*args, **kwargs):
        cursor = conn.cursor()
        cursor.execute(f"""SELECT  agenda_diretoria.id, agenda_diretoria.FK_escola_id , agenda_diretoria.nome , 
                            agenda_diretoria.prazo, agenda_analise.resultado, agenda_analise.titulo, agenda_analise.mensagem, agenda_diretoria.recursos, agenda_equipe.nome, escola.nome_escola, estado.nome,  municipio.FK_UF_id, municipio.nome, escola.FK_municipio_id
                            FROM agenda_equipe  
                            INNER JOIN agenda_diretoria ON agenda_equipe.FK_agenda_diretoria_id = agenda_diretoria.id
                            INNER JOIN agenda_analise ON agenda_diretoria.id = agenda_analise.FK_agenda_diretoria_id
                            INNER JOIN escola ON agenda_diretoria.FK_escola_id = escola.id 
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            WHERE agenda_equipe.FK_agenda_diretoria_id =  {args[1]};""") 
        
        result = cursor.fetchall()
        cursor.close()
        dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_escola_id' , 'nome' , 
                    'prazo', 'resultado','titulo', 'mensagem', 'recursos', 'agenda_equipe_nome',  'nome_escola' ,'estado_nome', 'FK_UF_id', 'municipio_nome', 'FK_municipio_id') 
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
    def get_agenda_plano_aula_by_last_id(*args, **kwargs):
        cursor = conn.cursor()
        
 
        cursor.execute(f"SELECT TOP 1 * from plano_aula ORDER BY id DESC;")
        
        result = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('id', 'FK_escola_id', 'ano', 'bimestre_escolar', 'FK_etapa_ensino', 'FK_turma_id', 'FK_componente_escola_profissional_id', 'unidade_tematica', 'conteudo', 'resultado') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                # print(res)

                listEstadosDict.append(res)   
            
        if len(listEstadosDict) != 0:
            return listEstadosDict

        return False

    @classmethod
    def create_planoaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into plano_aula ( FK_escola_id, ano, bimestre_escolar, FK_etapa_ensino, FK_turma_id, FK_componente_escola_profissional_id, unidade_tematica, conteudo, resultado) values(?,?,?,?,?,?,?,?,?)",args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def create_conteudo_planoaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2], args[3])
            # input()
            
            cursor.execute("insert into conteudo_plano_aula ( nome, FK_plano_aula_id) values(?,?)",args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

    @classmethod
    def update_planoaula(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args)
            # input()
            
            cursor.execute('''
                        UPDATE plano_aula
                        SET bimestre_escolar = ?, etapa_ensino = ? , ano = ?, FK_unidade_tematica_id = ?, conteudo = ? 
                        WHERE id = ?
                        ''',args[1], args[2], args[3], int(args[4]), args[5], args[6])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None