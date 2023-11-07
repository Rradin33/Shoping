# ( comper.py ) in file baraye moghayese kalaha ba yekdigar ast, masalan moshtari daron site yek kala ra search mikonad va tamame kalahai k oun modeli hastand vasash b namayesh dar miyan va moshtari behtarinesho entekhab mikone va mikhare

#----------------------------------------------------------------

class CompareProduct:                # Compare yani moghayese kardan 
   def __init__(self, request):        
      self.session = request.session      # aval yek session ra seda mizanim va misazim, ( session ) baes mishe etela'at dakhele Database k beheshon ehtiyaj darim baraye modati dakhele hafeze compioter save shavand
      compare_product = self.session.get('compare_product')     # ( compare_product ) esm session hast k mikhahim oun ra begirim va berizim dakhele zarf compare_product
      if not compare_product:                                   # yani agar compare_product khali ast, ( not ) yani khali, yani agar etela'ati dakhele session vojod nadarad va khali hast
         compare_product = self.session['compare_product']=[]   # bad migim yek session khali besaz va yek list khali behesh nesbat bede 
      self.compare_product = compare_product                    # ( self.compare_product ) in fazaye zakhire sazi ma hast k oun ro dorost mikonim darvaghe self.compare_product list ma ast yani in [      ] , k barabar ast ba compare_product
      self.count = len(self.compare_product)                    # ( self.count ) in yani tedad product haye daron oun list ra b dast miyare yani masalan [ 43,3,12 ] in alan 3ta count hast, ba ( len ) tedad onsorhaye list b dast miyad 
# dar kol ba in code mikhahim yek list besazim k code ya id kalahaye search shode tavasote moshtari daron oun list save shavad, injori [ 12,34,67 ]


   
   
# in def baraye add kardane kala dakhele list sessin ast
   def add_to_compare_product(self,productId):       # inja migim har bar k add_to_compare_product ro seda zadam yek productId yani code kala vasat mifrestam ta betone amaliyat pain ro anjam bede
      productId = int(productId)                     # oun productId eshte ast ba in code int(productId) migim b sorate adad sahih bashe yani 3 6 78 19 kon 
      if productId not in self.compare_product:      # va agar oun productId daron in session nabod, ( self.compare_product ) in hamon fazaye zakhire sazi ma hast k dar class bala neveshtim, in if ro minevisim chon nemikhahim kalaye tekrari dakhele compare_product bashe pas migim agar nabod bad dar code pain migim oun ro ezafe kon 
         self.compare_product.append(productId)      # productId ro b in session append kon yani ezafe kon
      self.count = len(self.compare_product)         # ( self.count ) in yani tedad product haye daron oun list ra b dast miyare yani masalan [ 43,3,12 ] in alan 3ta count hast, ba ( len ) tedad onsorhaye list b dast miyad 
      self.session.modified = True                   # va dar akhar edit session ro True mikonim
# bad bayad baraye in def view benvisim
   
   
   
   
# in def baraye pak kardan kala az list sessin hast
   def delete_from_compare_product(self, productId):        # harmoghe in def ra seda zadim yek productId yani code kala behesh midim ta betone amaliyat pain ro anjam bede 
      self.compare_product.remove(int(productId))           # ba in code oun vaghti def bala ro seda zadim oun kala az list ma hazf mishavad; ( int ) yani code kala b sorate adad sahih ast va ashari nist injori [ 2, 34, 12, 20 ]
      self.session.modified = True                          # # va dar akhar edit session ro True mikonim
# bad bayad baraye in def view benvisim
   
   
   

# in baraye zamani ast k ma kolan mikhahim kole session ra pak konim
   def clear_compare_product(self):
      del self.session['compare_product']  
      self.session.modified = True
      
      

# bad az in codha bayad berim dakhele views.py va safhe moghayese kalaha daron site ra besazim


