# codhai k mikhahim dar jahaye mokhtalef azashon estefade konim dar file ( utils.py) minevisim va bad addreseshon ro dar views.py minevisim

#----------------------------------------------------------------

# in def marbot b ( active_code ) ast k baraye moshtari b sorate random yek shomare ferestade beshe va check beshe ta hesabesh sakhte beshe

def create_random_code(count):              # in code karesh ine k y adad masalan 5 raghami b sorate random begire va hamon adad 5 raghami baraye man bargardone    
   import random
   count-=1
   return random.randint(10**count, 10**(count+1)-1)  
   
# ma masalan yek adad mikhahim bein 10000 ta 99999, baraye hamin code bala ra minevisim ta in adad sakhte shavand

#----------------------------------------------------------------

# in def marbot b ersal sms baraye moshtari ast masalan baraye tablighat ya tabrike tavalod va bad addresesh ro dar views.py minevisim
# baraye ersal sms aval vared google mishavim sherkathaye ziyadi hastand k in kar ra baraye ma anjam midahand
# bad dar yeki az sitehai k ersal sms ra anjam midahand sabtenam mikonim va bad khodeshon dakhele siteshon tozih dadan k bayad chikar konim
# bad dakhele siteshon yek seri code gozashtan k ma bayad biyarin inja benvisim


from kavenegar import *              # ( kavenegar ) esm yek sherkat ast k ma dar sitash sabtenam kardim va oun baraye ma ersal smsha ra anjam midahad, vali ghablesh bayad benvisil ( pip install kavenegar )

def send_sms(mobile_number, message):               # baraye in def yek shomare mobail mikhahim va yek message
   try:
      api = KavenegarAPI('K3GK53GK45HG3K4HG5KH3G4K5H5GK3H454KH3G')       # in code API ast k khode sherkat kavenegar behemon midahad va faghat baraye ma ast va ba har bar estefade in code taghir mikonad
      params = { 'sender':'', 'receptor':mobile_number, 'message':message }
      response = api.sms_send(params)
      return response
   except APIException as error:
      print(f'error1:{error}')
   except HTTPException as error:
      print (f'error2:{error}')

# in codha ra dakhele khode site kavenegar neveshte ma bayad copy konim inja ta ejra shavand

#----------------------------------------------------------------

# in code marbot b upload kardan axsha va tasavirha dar siteman ast
# in code ra inja minevisim va bad harmoghe khastim azash estefade konim address in code ra midahim b anjai k mikhahim axs upload konim

import os
from uuid import uuid4           # in ketabkhane mitone ta binahayad baraye esm axsha esmhaye hash shode ghair tekrari tolid kone

class FileUpload:
   def __init__(self, dir, prefix):           # ( dir ) manzor hamon image ast, ( prefix ) esm oun classi ast k dar an mikhahim az image estefade konim va axs upload konim, in class ha dar folder ( products ) va daron file ( models.py ) hastand, baraye mesal class Brand va ProductGroup
      self.dir = dir
      self.prefix = prefix
      
   
   def upload_to(self, instance, filename):                  # ( filename ) yani haman esm mokhafaf axsha k akhar axha neveshte mishe masalan ( a.apg )
      filename, ext = os.path.splitext(filename)             # in code marbot b esm axha hast va esm axsha ra 2 ghesmat mikonad, ( filename ) esm asli axs ast, ( ext ) esm pasvand axs ast 
      return f'{self.dir}/{self.prefix}/{uuid4()}{ext}'      # ( {uuid4()}{ext} ) (uuid4) esm axs ra misazad k esmhaye gheir tekrari dorost mikonad va (ext) ham esm pasvand axs hast masalan apg, dar kol in kode yani dakhele in ( {self.dir} ) poshe bad dakhele in ( {self.prefix} ) zir poshe yek esm gheir tekrari ( {uuid4()} ) tplod kon va behesh yek pasvand ( {ext} ) bede
   
   