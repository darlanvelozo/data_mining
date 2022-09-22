from csv import reader
from distutils import text_file
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from Processo_inicio import processo
from Processo_fim import processoFim
from cod_patente import count_pc_by
from cod_cnpj import cnpj
from funcoes import classificar_all, encontrar_correto



links = []
with open('links.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    list_of_rows.remove(list('0'))

links.append(list_of_rows)

def encontrar_nome_patente(x):
    try:
        s = str(x).find('“')
        aux = str(x)[s:]
        e = aux[1:].find('”')
        if len(aux[:e+2])<5:
            return []
        return aux[:e+2]
    except:
        return[]

def retornar_patent(x):
    if len(count_pc_by(x)) == 0:
        if len(encontrar_nome_patente(x)) != 0:
            return encontrar_nome_patente(x)
        else:
            return []
    else:
        return count_pc_by(x)


 
TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

lista_todos_registros = []
lista_registros_links = []
lista_classificacao = []
def classificar(x):
    x = str(x)
    if x.find('Contrato de Licença de Exploração de Tecnologia') != -1:
         lista_registros_links.append(['links[0][l][0]', x, 'Contrato de Licença de Exploração de Tecnologia', retornar_patent(x), cnpj(x), processoFim(x)[0]])
    else:
        lista_registros_links.append(['links[0][l][0]', x, '[]', retornar_patent(x), cnpj(x), processoFim(x)[0]])
        

lista_completa = [] 

def ler_todos_links():
    
#len(links[0])
    l=0
    while l < 1:
        print("segundos:",(len(links[0])-l)*7, "\nminutos:" ,((len(links[0])-l)*7)/60, "\nhoras: ", (((len(links[0])-l)*7)/60)/60)
        try:
            #==============|| inicalizando a busca a partir dos links gerados ||===============#
            option = Options()
            option.headless = True
            driver = webdriver.Chrome()
            driver.get(links[0][l][0])

            #==============|| buscando os dados e encerrando a consulta ||===============#
            documento = driver.find_element_by_class_name('DocumentView-content-text')
            html_documento = documento.get_attribute('outerHTML')
            soup_documento = BeautifulSoup(html_documento, 'html.parser')
            text_pag = soup_documento.get_text()
            driver.quit()
            
            #==============|| Estabelecendo o inicio ao fim do processo ||===============# 
            """start_process = text_pag[text_pag.find(processo(text_pag)[0]): ]
            end_process = start_process[len(processo(start_process)[0]):]
            result = start_process[:start_process.find(processo_fim(end_process)[0])-1]"""
            lista_completa = classificar_all(text_pag)
            lista_teste = []
            '''for i in range(len(lista_completa)):
                lista_teste.append(encontrar_correto(lista_completa[i]))'''

            
            print("uiui",lista_completa)
            print(len(lista_completa))
            
            '''print("n lista: ",len(lista_todos_registros))
            print("n processos: ",len(processo(text_pag)))
            print("l: ", l)
            print("n link: ", len(links[0]))'''
        except:
            print("erro")
            break
        l+=1



ler_todos_links()
    

df = pd.DataFrame(lista_registros_links, columns=['link','Conteudo'])

#df = pd.DataFrame(lista_registros_links, columns=['Link', 'Conteudo', 'classificacao', 'codigo', 'cnpj', 'processo'])


df.to_csv("unicamp.csv", index = False)

