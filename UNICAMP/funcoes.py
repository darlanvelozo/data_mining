# coding=utf8
from cgi import print_arguments
from gettext import find
from Processo_inicio import processo, processoFim
def classificar_all(x):
    lista_processada = []
    for i in range(len(processo(x))):
        try:
            start_process = x[str(x).find(processo(x)[i]): ]
            end_process = start_process[len(processo(start_process)[0]):]
            result = start_process[:str(start_process).find(processoFim(end_process)[0])-1]
            lista_processada.append(result)
        except:
            if i != len(processo(x)):
                try:
                    start_process = x[str(x).find(processo(x)[i]): ]
                    end_process = start_process[len(processo(start_process)[0]):]
                    lista_processada.append(start_process)
                    return lista_processada
                except:
                   return lista_processada

            else:
                return lista_processada 

#x = '1-P-10998/2020 - Inova - Carta Acordo - Partes: Unicamp e Linköping University - Suécia - Data de Assinatura: 27.08.20 - Vigência: indeterminada - Resumo do  Objeto: Compromisso, perante à Fapesp, em respeitar e executar as respectivas Políticas Institucionais de Propriedade Intelectual, Confidencialidade e Publicação em relação ao projeto “Developing Novel Double Perovskite Materials for Solar Cells”. 1-P-15905/2020 - Inova - Contrato de Reconhecimento de Cotitularidade, Direitos e Deveres sobre Tecnologia - Partes: Unicamp, Universidade Federal de Uberlândia - UFU, e Fundação de Amparo à Pesquisa do Estado de Minas Gerais - FAPEMIG - Data de Assinatura: 08.10.21 - Vigência: até o término de vigência da última patente ou do arquivamento definitivo do pedido de patente - Resumo do Objeto: Regularização da titularidade e o reconhecimento mútuo dos direitos e obrigações sobre a tecnologia “Formulações nanohíbridas para encapsulamento de fármacos”, depositada junto ao INPI em 29.05.20. 1-P-15942/2020 - Inova - Contrato de Ajuste de Propriedade Intelectual - Partes: Unicamp e Universidade Estadual Paulista “Julio De Mesquita Filho” - Unesp - Data de Assinatura: 03.12.20 - Vigência: pelo período de vigência da patente - Resumo do Objeto: Estabelecer as condições de Propriedade Intelectual entre a Unicamp e a Unesp da tecnologia “Formulação Farmacêutica e usos da mesma”, depositada junto ao INPI em 01.04.19, bem como de todos os resultados, metodologias, inovações técnicas, produtos, processos e “know-how”, privilegiáveis ou não, obtidos em virtude da tecnologia. 1-P-16935/2020 - Inova - Contrato de Propriedade Intelectual - Partes: Unicamp e Universidade Federal de Santa Catarina - Data de Assinatura: 14.12.20 - Vigência: pelo período de vigência da patente ou 10 anos em caso de indeferimento - Resumo do Objeto: Estabelecer as condições de Propriedade Intelectual entre a Unicamp e a UFSC da tecnologia “Sequência genética otimizada que codifica a proteína maebl de plas '
'''print(processo(x))
print(processoFim(x))
print(len(classificar_all(x)))'''

'''                 end_process = start_process[len(processo(start_process)[0]):]
                    result = start_process[:str(start_process).find(processoFim(end_process)[0])-1]
                    if len(processoFim(end_process)) > 0:
                        lista_processada.append(result)
                        return lista_processada
                    else:
                        lista_processada.append(start_process)
                        return lista_processada'''

x = '1-P-32397/2021 - Inova - Contrato de Licença de Exploração Não Exclusiva de Tecnologia - Partes: Unicamp/ Funcamp e RHK Technology, Inc - Data de Assinatura: 14.12.21  - Vigência: pelo período de vigência da patente - Resumo do  Objeto: Formalização da licença para exploração de patente e seu know how em caráter não exclusivo, da licenciante para a licenciada, da tecnologia “Sistema de detecção de luz para microscópios de varredura de sonda”, depositado junto ao INPI em 28.07.20, para fins de desenvolvimento, produção e comercialização, conforme descrito no documento de patente, em área geográfica irrestrita.'
a = []
#print(processo(x))
def encontrar_correto(x):
    lista = []
    for i in range(len(processo(x))):
        try:
            s = x[x.find(processo(x)[i]):x.find(processoFim(x)[i+1])]
            lista.append(s)
        except:
            break
    return lista

def agora_vai(x): 
    lista_results = []
    try:
        i=0
        while True :
            try: 
                start_process = x[x.find(processo(x)[i]): ]
                end_process = start_process[len(processo(start_process)[0]):]
                result = start_process[:start_process.find(processoFim(end_process)[0])-1]
                lista_results.append(result)
                i+=1
            except:
                if i != len(processo(x)):
                    try:
                        start_process = x[str(x).find(processo(x)[i]): ]
                        end_process = start_process[len(processo(start_process)[0]):]
                        
                        lista_results.append(result)
                        return lista_results
                    except:
                        return lista_results
                return lista_results    
                
    except:
        return lista_results                

"""print(agora_vai(x)[0])"""
def classificar_processo(x): 
    categoria = agora_vai(x)[0]
    categoria_final = categoria[len(processo(categoria)[0])+2:]
    print(categoria_final[: str(categoria_final).find('-')])



g = '1-P-28253/2013 - Inova - Termo de Rescisão ao Contrato de Licenciamento de Tecnologia - Partes: Unicamp/Funcamp e Ouro Fino Saúde Animal LTDA. - Resumo do Objeto: Rescisão do Contrato que objetivou a formalização do licenciamento exclusivo, da Unicamp para a Ouro Fino, da tecnologia “Micropartículas de óleos essenciais e seus usos para prevenção de doenças entéricas”.'
def categoria(g):
    anelise = g[len(processo(g)[0])+3:]
    classificar_menor = anelise[:str(anelise).find('-')]
    classificar_maior = anelise[:str(anelise).find('–')]
    if len(classificar_menor) > 100:
        return classificar_maior
    else:
        return classificar_menor

def pegar_processo(x):
    return processoFim(x)

def retornar_lista_unica(x):
    try:
        for k in range(len(x)):
            for l in range(len(x)):
                if x[l]==x[k]:
                    x.remove(x[l])
    except:
        return x
''''''