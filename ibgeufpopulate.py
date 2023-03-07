import requests 
import pyodbc
import pprint

conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:sql-poncetech.database.windows.net,1433;Database=editora-aprender-homolog-2023-2-16-16-50;Uid=poncetech-admin;Pwd=12@editora@12!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

def get_estados_by_nome(*args, **kwargs):
        cursor = conn.cursor()
 
        cursor.execute("select * from estado where nome = ?", args[0])
        
        estados = cursor.fetchall()
        
        cursor.close()
        
        listEstadosDict = []
        for estadoTupla in estados:
            
            tup1 = ('id', 'nome', 'uf') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                listEstadosDict.append(res)   
            
        return listEstadosDict

def create_estado(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2])
            # input()
            
            cursor.execute("insert into estado (nome, uf) values(?,?)",args[0], args[1])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None

def get_municipios_by_nome(*args, **kwargs):
        cursor = conn.cursor()
        # print(args[0])
        # input()
 
        cursor.execute("select * from municipio where nome = ?", args[0])
        
        estados = cursor.fetchall()
        cursor.close()

        listEstadosDict = []
        for estadoTupla in estados:
            
            tup1 = ('id', 'codigo_ibge', 'nome', 'FK_UF_id') 
            tup2 = estadoTupla
           
            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2)) 
                listEstadosDict.append(res)   
            
        return listEstadosDict

def create_municipio(*args, **kwargs):
        # user = cls.query.filter_by(username=username).first()  #select * from hoteis where hotel_id = $hotel_id
        # try:
            cursor = conn.cursor()
            # print(args[1], args[2])
            # input()
            
            cursor.execute("insert into municipio (codigo_ibge, nome, FK_UF_id) values(?,?,?)",args[0], args[1], args[2])
            
            conn.commit()
            # conn.close()
            # return 'created'
            # rows = cursor.fetchall()
        # except:
        #     print(TypeError)
        # #     return None


def main ():
       
    x = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/distritos')
    # print(x.status_code)
    # print(x.json())
    data = x.json()

    for d, i in enumerate(data):
        # pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(i)
        print(d, len(data))
        # print(i)
        # input()
        municipioDict = i['municipio']

        regiaoimediata = municipioDict['regiao-imediata']
        
        regiaointermediaria = regiaoimediata['regiao-intermediaria']
        
        # print('regiaointermediaria -----<<<',regiaointermediaria.keys())

        # input()
        estadoNome = regiaointermediaria['UF']['nome']
        
        estadoUF = regiaointermediaria['UF']['sigla']

        estado  = get_estados_by_nome(estadoNome)

        # print(estadoNome, estadoUF)


        # print('estado --->>>', estado, len(estado))

        if len(estado) == 0:
            # print('entrou')
            create_estado(estadoNome, estadoUF)

        estadoafter  = get_estados_by_nome(estadoNome)
        idUF = estadoafter[0]['id']

        
        # print(idUF)
        # # input()

        # print('municipioDict -----<<<',municipioDict.keys())
        nomeMunicipio = municipioDict['nome']

        cod_ibge = municipioDict['id']

        # print(nomeMunicipio, cod_ibge)


        # input()

        municipio = get_municipios_by_nome(nomeMunicipio)

        if len(municipio) == 0:
            # print('entrou')
            create_municipio(cod_ibge, nomeMunicipio, idUF)

        # print(municipio)
        ### primeiro verificar se o uf existe 


        ### se existe pega id pelo nome e cadastra municipio
         
    
        ### se nao existe cria o uf e pega o id do uf pelo nome cria municipio associado a o uf 

        # print(len(data), data[0])
        # print(data[0].keys())
        # print(data[0]['municipio'])
        

main()