import re
'''
            '([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})',
            '([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})'''
def cnpj(text):
    try:  
        list_rgx1 = [
          '\d\d.\d\d\d.\d\d\d/\d\d\d\d-\d\d'
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

