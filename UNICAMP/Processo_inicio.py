import re
'''
            '([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})',
            '([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})'''

def processo(text):
    try:  
        list_rgx1 = [
          '(\d{1,2}-[A-Z]-\d{4,5}/\d{4}.{1,10}nova)',
          '\d-[A-Z]-\d{5}/\d{4} - [A-Z]nova -',
          '\d-[A-Z]-\d{5}/\d{4} -[A-Z]nova -',
          '\d-[A-Z]-\d{5}/\d{4} - [A-Z]nova-',
          '\d-[A-Z]-\d{5}/\d{4} -[A-Z]nova-',
          '\d-[A-Z]-\d{5}/\d{4}-[A-Z]nova-',

          '\d-[A-Z]-\d{4}/\d{4} - [A-Z]nova -',
          '\d-[A-Z]-\d{4}/\d{4} -[A-Z]nova -',
          '\d-[A-Z]-\d{4}/\d{4} - [A-Z]nova-',
          '\d-[A-Z]-\d{4}/\d{4} -[A-Z]nova-',
          '\d-[A-Z]-\d{4}/\d{4}-[A-Z]nova-',

          '\d-[A-Z]-\d{5}/\d{4} – [A-Z]nova –',
          '\d-[A-Z]-\d{5}/\d{4} –[A-Z]nova –',
          '\d-[A-Z]-\d{5}/\d{4} – [A-Z]nova–',
          '\d-[A-Z]-\d{5}/\d{4} –[A-Z]nova–',
          '\d-[A-Z]-\d{5}/\d{4}–[A-Z]nova–',
          
          '\d-[A-Z]-\d{5}/\d{4} – [A-Z]nova -',
          '\d\d-[A-Z]-\d{5}/\d{4} – [A-Z]nova -',
          '\d\d-[A-Z]-\d{4}/\d{4} – [A-Z]nova -',
          
          '\d-[A-Z]-\d{4}/\d{4} – [A-Z]nova -',
          '\d-[A-Z]-\d{4}/\d{4} –[A-Z]nova -',
          '\d-[A-Z]-\d{5}/\d{4} –[A-Z]nova -',
          '\d\d-[A-Z]-\d{5}/\d{4} –[A-Z]nova -',
          '\d\d-[A-Z]-\d{4}/\d{4} – [A-Z]nova -',
          
          '\d\d-[A-Z]-\d{5}/\d{4} –[A-Z]nova –',
          '\d\d-[A-Z]-\d{5}/\d{4} - [A-Z]nova -',
          '\d\d-[A-Z]-\d{4}/\d{4} – [A-Z]nova –'


          
                    ]
        list_rgx2 = [
                     ]

        pcs = []

        for rgx in (list_rgx1):
          result = re.findall(rgx, text)

          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED1+ ")
              pcs.append(r)

         # procurando regex - LISTA 2
        '''for rgx in (list_rgx2):
          result = re.findall(rgx, text)

          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED2+ ")
              pcs.append(r)
        '''
    
        # print("PATENT CITATION's Puras ==============")
        # print("Total -> ", len(pcs))
        # for p in pcs:
        #   print(" ===> ", p)
        # print("PATENT CITATION's Puras==============")
        
        return pcs
    except Exception as e:
        return 'No answer' + str(e)

def processoFim(text):
    try:  
        list_rgx1 = [
          '\d\d-[A-Z]-\d{4}/\d{4}',
          '\d-[A-Z]-\d{5}/\d{4}',
          '\d-[A-Z]-\d{4}/\d{4}',
          '\d\d-[A-Z]-\d{5}/\d{4}'


                    ]
        list_rgx2 = [
                     ]

        pcss = []

        for rgx in (list_rgx1):
          result = re.findall(rgx, text)

          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED1+ ")
              pcss.append(r)

         # procurando regex - LISTA 2
        '''for rgx in (list_rgx2):
          result = re.findall(rgx, text)

          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED2+ ")
              pcs.append(r)
        '''
    
        # print("PATENT CITATION's Puras ==============")
        # print("Total -> ", len(pcs))
        # for p in pcs:
        #   print(" ===> ", p)
        # print("PATENT CITATION's Puras==============")
        
        return pcss
    except Exception as e:
        return 'No answer' + str(e)

def encotrar_inicio_fim(text):
    try:  
        list_rgx1 = [
          '(\d{1,2}-[A-Z]-\d{4,5}/\d{4}.{1,10}nova).{1,900}?((\d\d-[A-Z]-\d{4}/\d{4})|(\d-[A-Z]-\d{5}/\d{4})|(\d-[A-Z]-\d{4}/\d{4})|(\d\d-[A-Z]-\d{5}/\d{4}))'

                    ]

        pcss = []

        for rgx in (list_rgx1):
          result = re.findall(rgx, text)
          print(result)
          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED1+ ")
              pcss.append(r)

         # procurando regex - LISTA 2
        '''for rgx in (list_rgx2):
          result = re.findall(rgx, text)

          #as regex encontradas serão eliminadas para evitar repetição
          for r in result:
            if len(r) > 5:
              text = str(text).replace(r, " +DELETED2+ ")
              pcs.append(r)
        '''
    
        # print("PATENT CITATION's Puras ==============")
        # print("Total -> ", len(pcs))
        # for p in pcs:
        #   print(" ===> ", p)
        # print("PATENT CITATION's Puras==============")
        
        return pcss
    except Exception as e:
        return 'No answer' + str(e)

def encontrar_processo(text):
  return re.findall('(\d{1,2}-[A-Z]-\d{4,5}\/\d{4}.{1,10}nova).{1,600}?((\d\d-[A-Z]-\d{4}\/\d{4})|(\d-[A-Z]-\d{5}\/\d{4})|(\d-[A-Z]-\d{4}\/\d{4})|(\d\d-[A-Z]-\d{5}\/\d{4}))', text)
  