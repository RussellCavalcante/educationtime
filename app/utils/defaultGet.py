from sqlalchemy.dialects.postgresql import UUID
# from app import banco
import json
from uuid import uuid1, uuid4
import re
from app import conn
import pprint

import json
import re

class LazyDecoder(json.JSONDecoder):
    def decode(self, s, **kwargs):
        regex_replacements = [
            (re.compile(r'([^\\])\\([^\\])'), r'\1\\\\\2'),
            (re.compile(r',(\s*])'), r'\1'),
        ]
        for regex, replacement in regex_replacements:
            s = regex.sub(replacement, s)
        return super().decode(s, **kwargs)
    

class GetModel(): 
    
    @classmethod
    def get_plano_aula_by_id(*args, **kwargs):
        cursor = conn.cursor()
        cursor.execute(f"""SELECT conteudo_plano_aula.FK_plano_aula_id, plano_aula.FK_escola_id, municipio.id  ,municipio.nome, estado.id, 
                            estado.nome, estado.uf , ano, bimestre_escolar, FK_etapa_ensino , FK_turma_id, 
                            plano_aula.FK_componente_escola_profissional_id, unidade_tematica, conteudo, resultado, conteudo_plano_aula.nome, 
                            nome_escola,
                            area_conhecimento.id, area_conhecimento.nome,
                            componente_curricular.id, componente_curricular.nome
                            FROM conteudo_plano_aula 
                            INNER JOIN plano_aula ON conteudo_plano_aula.FK_plano_aula_id = plano_aula.id
                            INNER JOIN escola ON plano_aula.FK_escola_id = escola.id
                            INNER JOIN profissional_escola_componente ON  plano_aula.FK_componente_escola_profissional_id = profissional_escola_componente.id
                            INNER JOIN componente_curricular ON componente_curricular.id = profissional_escola_componente.FK_componente_id
                            INNER JOIN area_conhecimento ON area_conhecimento.id = componente_curricular.FK_area_conhecimento_id
                            INNER JOIN municipio ON escola.FK_municipio_id = municipio.id
                            INNER JOIN estado ON municipio.FK_UF_id = estado.id
                            WHERE conteudo_plano_aula.FK_plano_aula_id = {args[1]};""") 
         
        result = cursor.fetchall()
        cursor.close()
        dictFinal = {}
        listEstadosDict = []
        for estadoTupla in result:
            
            tup1 = ('conteudo_plano_aula_FK_plano_aula_id', 'FK_escola_id', 'FK_municipio_id'  ,'municipio_nome', 'FK_UF_id', 
                            'estado_nome', 'estado_uf' , 'ano', 'bimestre_escolar', 'FK_etapa_ensino' , 'FK_turma_id', 
                            'FK_componente_escola_profissional', 'unidade_tematica', 'conteudo', 'resultado', 'nome', 'nome_escola', 'area_conhecimento_id', 'area_conhecimento_nome',
                            'componente_curricular_id', 'componente_curricular_nome')
            tup2 = estadoTupla

            if len(tup1) == len(tup2): 
                res = dict(zip(tup1, tup2))
                listEstadosDict.append(res)   
        

        for Dict in listEstadosDict:
        
            dictFatores = {}
            for chave in Dict:
                
                if 'sub_conteudo' not in dictFinal.keys():
                    if chave == 'nome':
                        
                        dictFinal['sub_conteudo'] = {'itens':[]}
                        dictFatores[chave] = Dict[chave]
                        
                        dictFinal['sub_conteudo']['itens'].append(dictFatores)
                       
                else:
                    if chave == 'nome':
                        
                        dictFatores[chave] = Dict[chave]
                   
                        dictFinal['sub_conteudo']['itens'].append(dictFatores)
                        
                if chave in dictFinal.keys():
                    continue

                    
                
                if chave != 'nome':
                    dictFinal[chave] = Dict[chave] 
        
        return dictFinal
    
    @classmethod
    def get_default(self, *args, **kwargs):

        cursor = conn.cursor()
        qtd = kwargs.get('qtd')
        if not qtd:
            qtd = None
             
        queryDefalt = f"""SELECT CAST( (SELECT distinct {'TOP ' + str(qtd) if qtd else ''} {args[0]} """
        
        
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
        

        s = str(result)

        strip1 = s.lstrip("[('")
        strip2 = strip1.rstrip("', )]")
        
        j = json.loads(strip2, cls=LazyDecoder)
        
        return j

   