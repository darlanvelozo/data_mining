import re
'''
            '([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})',
            '([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})'''


def processoFim(text):
    try:  
        list_rgx1 = [
          '\d\d-[A-Z]-\d{4}/\d{4}',
          '\d-[A-Z]-\d{5}/\d{4}/g',
          '\d-[A-Z]-\d{4}/\d{4}',
          '\d\d-[A-Z]-\d{5}/\d{4}',
          ''

          
          

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

