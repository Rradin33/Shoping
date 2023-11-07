# ( shop_cart ) haman sabade kharid dakhele site ast k ma inja esmash ra shop_cart gozashtim
# in file ra misazim chon dakhele sabade kharid mikhahim karhai anjam bedim mesl ( ezafe kardan, hazf kardan, update kardan, edit kardan va ... ) k inja anjam midahim
# chon model nadaran va b models.py ham kari nadaran haminja hameye codhashon ro minevisim

# baraye sabade kharid bayad az ( session ) estefade konim, session ha dadeha ro dakhele campioter moshtari negahdari mikonand ra zamani k ma behesh begim va kelid in dadeha ro dakhele Database ghesmate session negah dari mikonad

#----------------------------------------------------------------

from apps.products.models import Product          # in ketabkhane marbot b def ( __iter__ ) ast

# ba in code yek sabade kala misazim
class ShopCart:
   def __init__(self, request):
      self.session = request.session              # ba in code session ra seda mizanim k azash estefade konim k rajebe session bala tozih dadam
      temp = self.session.get('shop_cart')   # inja migim boro baraye man get kon yani baraye man biyar sessioni k esmesh hast shop_cart va berizesh dakhele zarf ( temp ) k sakhtimeesh
      if not temp:                           # yani agar session khali ast va shop_cart chizi tosh nist ( yani moshtari kalai ro entekhab nakarde )
         temp = self.session['shop_cart']={}     # yani session shop.cart ro khali por kon, chon moshtari chizi b sabade kharid ezafe nakarde dg
      self.shop_cart = temp                     # inja migim tamame amaliyate bala ra k dakhele zarf temp ast ro dakhele( shop_cart ) negahdari kon
      self.count = len(self.shop_cart.keys())    # ( count ) tedad kalahaye daron sabademon ro moshmare, ( len(self.shop_cart.keys()) ) len yani beshmar tedad ( keys ) yani tedad kilidhaye dakhele shop_cart dar kol yaki tamame kalahai k dakhele sabade kharid hastand ro beshmar va bego hata agar kalai ham nabod bego ( 0 )
      
#----------------------------------------------------------------

# in def baraye in ast k dar marhale akhare add kardan, delete kardan, update kardan codha ra save konim ba in code ( self.save() )
def save(self):
   self.session.modified = True
   
#----------------------------------------------------------------

# in def baraye ezafe kardan kala b sabade kharid ast  
   def add_to_shop_cart(self, product, qty):      # in def baraye zamani ast k mikhahim yek kala b sabade kharid ezafe konim va behesh migim chandta azash mikhaim ezafe konim, ( product ) haman kala ast va ( qty ) b vasile qty chandta az oun kala mitavanim ezafe konim, pas harmoghe def ( add_to_shop_cart ) ro seda zadim yani mikhaim kalai ezafe konim ya yeki az oun kala ya chandta az oun kala
      product_id = str(product.id)                # in ro minevisim k har product yek id dashte bashe masalan product shomare 2 ya product shomare 23; ( str ) k neveshtim baraye in ast k id kala ra b sorate reshtei neshan dahad
      if product_id not in self.shop_cart:         # vaghti mikhaim yek kala ra ezafe konim b sabade kharid bayad baresi konim k in kala ghablan ezafe shode b sabade kharid ya na, in code mige negah kon bebin agar in kala nabod dakhele shop_cart ya hamon sabade kharid, ( shop_cart ) haman sabade kharid ast k esmash ra shop_cart gozashtim
         self.shop_cart[product_id] = {"qty": 0, "price": product.price, "final_price":product.get_price_by_discount()}      # ba in code dakhele sabade kharid yeki az oun kalai k moshtari ezafe karde sakhte mishe va ( qty ) yani tedad oun kala ra 0 mizarim va ( price ) ro barabar ba product.price mizarim k ha ghaimati k dakhele panel admin sabt kardim ounja zaher bashe, ( "final_price":product.get_price_by_discount ) yani dakhele sabade kharid har bar k mikhai ghaimat ro neshon bedi agar oun kala takhfif dasht ghaimate nahai ba takhfifesh ro neshon bede, ( get_price_by_discount ) in yek def ast k baraye takhfifhaye kalaha neveshtim daron folder products va file models.py, k bad ma inja esm in def ro get_price_by_discount minevisism k daron sabade kharid ghaimate kalaha ba takhfif hesab shavand
      self.shop_cart[product_id]["qty"]+=int(qty)       # dar code bala ma tedad kala ya qty ro 0 gozashtim vali ba in code migim moshtari har chandta k khast az oun kala mitone sefaresh bede 1 ta 10 ta 
      self.count = len(self.shop_cart.keys())      #  ( count ) tedad kalahaye daron sabademon ro moshmare, ( len(self.shop_cart.keys()) ) len yani beshmar tedad ( keys ) yani tedad kilidhaye dakhele shop_cart dar kol yaki tamame kalahai k dakhele sabade kharid hastand ro beshmar va bego hata agar kalai ham nabod bego ( 0 ), va bad ba in code tedad kala ra k moshtari vared karde ast ra hesab mikonad va dakhele sabade kharid neshan midahad
      self.save()                                # varaye save kardan dar marhale akhar aval yek def save minevisim va inja oun def save ra seda mizanim, man bala yek def save neveshtam
      
#----------------------------------------------------------------
   
# in def baraye pak kardan yek kala az sabade kharid ast
   def delete_from_shop_cart(self, product):       # ba in def kalai ra k mikhahim az sabade kharid hazf mikonim ( product ) oun kala ast
      product_id = str(product.id)                 # bad in oun product ro k mikhahim pak konim mikeshim biron
      del self.shop_cart[product_id]          # va bad az dakhele shop_cart yani haman sabade kharid oun product_id k entekhab shode ast ra kalash hazf shavad
      self.save()                            # varaye save kardan dar marhale akhar aval yek def save minevisim va inja oun def save ra seda mizanim, man bala yek def save neveshtam
   
#---------------------------------------------------------------
   
# in def baraye dokme be roz rasani ya Update daron safhe sabade kharid ast k hamrah ba in code bayad ajax va URL in view ham benvisim 
def update(self, product_id_list, qty_list):
   i = 0                                   # ( i ) shomarande ast yani beshmar
   for product_id in product_id_list:
      self.shop_cart[product_id]['qty'] = int(qty_list[i])
      i+=1
      self.save()         # varaye save kardan dar marhale akhar aval yek def save minevisim va inja oun def save ra seda mizanim, man bala yek def save neveshtam
      
#---------------------------------------------------------------

# in def ra minevisim k in class ( ShopCart ) ra tabdil konad b yek class iterabele k ba for beshe rosh kar kard
   def __iter__(self):
      list_id = self.shop_cart.keys()              # aval ba in ccode behesh migim tamam kilidhaye shop_cart ro bekesh biron, ( keys ) haman id kalaha hastand, dar kol yani behesh migim tamame kalahai k daron sabade kala moshtari ast ra id hashon ro bekesh biron va berizeshon dakhele zarfi b name ( list_id )
      products = Product.objects.filter(id__in = list_id)     # ( Product.objects.filter )ba in code mire dakhele Product va tamame kalahash ro negah mikone va ba in code ( (id__in = list_id) ) paida mikone kalahai k id ouna ba id kalahaye dakhele list id yeki hastan va mirize dakhele zarfi b name ( products ), baraye inke b ( Product ) vasl beshim ketabkhone oun ro bala safhe bayad benvisim
      temp = self.shop_cart.copy()                            # ( self.shop_cart ) ro k dar def haye balai neveshtim ra miyarim inja behesh migim yek copy azash begir va bad oun copy ro beriz dakhele zarfi b name temp
      
      for product in products:          # yani baraye har product dakhele products
         temp[str(product.id)]["product"]=product         # ba in code yek feild jadid dar ghesmate values sakhte mishe b nam ( product ), bad migim az oun temp boro id productesho biyar va ( ["product"] ) feide product ro behesh ezafe kon va ( ["product"]=product ) va oun product morede nazar ro ba tamame etela'atesh beriz dakhele feide product k jadid sakhti, tamame telela'at yani ba tozihatesho gheimato ina, masalan mesl kala ( mirahan motorsavari )
         
      for item in temp.values():          # yani baraye har item dakheme values haye temp, ( values ) haman qty va price va product hastand, k product ro dar code bala zafe kardim
         item["total_price"]=int(item["final_price"])*item["qty"]     # ba in code yek feild jadid dar ghesmate values sakhte mishe b nam ( total_price ), ba in code dar ghesmate sabade kharid ( qty ) yani tedad kala va ( price ) gheimate kala ra ba ham ( * ) zarb mikonad va gheimate total ro ounja minevise  
         yield item                     # ( yield ) haman return ast, yani vaghti karhaye bala ra anjam dadi item ro baraye man bargardon

#----------------------------------------------------------------
         
# def pain baraye mohasebe kole kalaha dar sabade kharid ast k gheimate nahai ra b moshtari neshan midahad
   def calc_total_price(self):
      sum = 0
      for item in self.shop_cart.values():
         sum+=int(item['final_price'])*item['qty']       # ( final_price ) ro bala daron def add_to_shop_cart neveshtim va bad miyarimesh inja k jelosh tozih dadam baraye ch kari ast, ghaimate nahai kala ro neshon mishe va agar kala takhfif dashte bashe ghaimate nahai ro ba takhfifi hesab mikone va neshon mide, 
      return sum
      




# bad az inke in codha ra dar in file neveshtim mirim ghesmate view va codehaye ounja ro minevisim
