# dar inja model mahsolat va brand ha ra minevisim

#----------------------------------------------------------------

from django.db import models
from utils import FileUpload          # ( FileUpload ) esm classi ast k daron file ( utils ) neveshtim va baraye uplode kardan axsha estefade mishe
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField        # in code in ejaze ra b ma midahad ta betavanim dar ghestame tozihat site yek seri emkanat b vojod biyarim ta betavanim neveshte ha ra khoshkeltar konim ya vasate neveshteha axs upload konim, in ketabkhane marbot b class Product va ( description ) ast
from django.urls import reverse
from datetime import datetime
from django.db.models import Sum, Avg
from middlewares.middlewares import RequestMiddleware

#----------------------------------------------------------------

# in class baraye esm brand neveshte mishaavad

class Brand(models.Model):
   brand_title = models.CharField(max_length=100, verbose_name='نام برند')
   
   # in 2 code pain marbot b upload kardan axs dar site hastand, baraye in kar aval miravim code asli ra dakhele file ( utils ) minevisim va bad address oun classi k daron file utils neveshtim ra inja minevisim, vali ghablesh bayad bala benvisim ( from utils import FileUpload )
   file_upload = FileUpload('images' , 'brand')                               # ( FileUpload ) esm classi ast k daron file ( utils ) neveshtim va baraye uplode kardan axsha estefade mishe, ( images ) poshe aval ast, ( brand ) poshe dovom ast
   image_name = models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر برند کالا')       # in code ham marbot b code bala ast baraye uplode kardane axs
   
   slug = models.SlugField(max_length=200, null=True)        # ( slug ) b yek ghesmat az address site k dar balaye site dar ghesmare URL neveshte mishe slug migan, behtar ast hamishe dar ghesmate models yek ( slug ) neveshte shavad, masalan agar esm brand ma PEPSI bod dakhele panel admin k mikhahim slug oun ra benvisim dakhele cadr slug minevisim ( pepsi ), injori kalame pepsi yek toke az URL mi mishavad va hatman slug ro bayad ba horof kochack benvisim
    
    
    
   def __str__(self):
      return self.brand_title
   
   class Meta:
      verbose_name = 'برند'
      verbose_name_plural = 'برندها'        # dar vaghe in baraye panel admin ast k dar ghesmate title b sorate jam neveshte mishavad, baraye sitehaye engilisi zaban ehtiyaji nist benvisim chon khode panel ye ( s ) b akharesh ezafe mikone vali baraye sitehaye farsi minevisim 
      
#----------------------------------------------------------------

# alan mikhaim model tamame mahsolati k mifroshim ra benvisim

class ProductsGroup(models.Model):
   group_title = models.CharField(max_length=100, verbose_name='عنوان گروه کالا')
   
   # in 2 code pain marbot b upload kardan axs dar site hastand, baraye in kar aval miravim code asli ra dakhele file ( utils ) minevisim va bad address oun classi k daron file utils neveshtim ra inja minevisim, vali ghablesh bayad bala benvisim ( from utils import FileUpload )
   file_upload = FileUpload('images' , 'products_group')                               # ( FileUpload ) esm classi ast k daron file ( utils ) neveshtim va baraye uplode kardan axsha estefade mishe, ( images ) poshe aval ast, ( products_group ) poshe dovom ast
   image_name = models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر برند کالا')    # in code ham marbot b code bala ast baraye uplode kardane axs
   
   description = models.TextField(blank=True, null=True, verbose_name='توضیحات گروه کالا')            # ( blank ) harmoghe True bashad yani moshtari majbor nist dar hengame sabt etela'at in ra por konad, ( null ) zamani k True bashad Database feilde hai ra k vasashon chizi neveshte nashode ra b sorate pishfarz null gharar mide
   is_active = models.BooleanField(default=True, blank=True, verbose_name='وضعیت فعال / غیر فعال')   # ( default=True ) yani hame moshtariha az haman aval True bashand yani active bashand, ( blank ) harmoghe True bashad yani moshtari majbor nist dar hengame sabt etela'at in ra por konad
   group_parent = models.ForeignKey('ProductsGroup', on_delete=models.CASCADE, blank=True, null=True, verbose_name='والد گروه کالا', related_name='groups')           # ( group_parent = models.ForeignKey('ProductGroup' ) yani in kala valede asli ast va sargoroh baghiye kalaha ast, harmoghe az ( ForeignKey ) estefade mikonim hatman akharesh bayad yek ( related_name ) benvisim, ( on_delete=models.CASCADE ) b in mani ast k az anjai k in yek kalaye valed ast va sar goroh baghiye kalaha in code ba'es mishavad k agar in kala ra pak kardim tamame farzandan in kala(yani kalahaye zir majmoe in kala) ham hazf shavand, baraye mesal ma yek navisande darim va yek ketab , har nevisande mitavanad sahebe chandin ketab bashad va bad vaghti ma dar class book ( author = models.ForeignKey(Author, on_delete=models.CASCADE) ) in code ra minevisim bad vaghti yek nevisande ra pak mikonim tamame ketabhai k marbot b an nevisande hastand va an nevisande neveshte pak mishavad
   register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
   published_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')      # baraye timezon bayad bala benvisim ( from django.utils import timezone )
   update_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ اخرین به روز رسانی')
   slug = models.SlugField(max_length=200, null=True)         # ( slug ) b yek ghesmat az address site k dar balaye site dar ghesmare URL neveshte mishe slug migan, behtar ast hamishe dar ghesmate models yek ( slug ) neveshte shavad
   
   
   def __str__(self):
      return self.group_title
   
   class Meta:
      verbose_name = 'گروه کالا'
      verbose_name_plural = 'گروه های کالا'      # dar vaghe in baraye panel admin ast k dar ghesmate title b sorate jam neveshte mishavad, baraye sitehaye engilisi zaban ehtiyaji nist benvisim chon khode panel ye ( s ) b akharesh ezafe mikone vali baraye sitehaye farsi minevisim
      
#---------------------------------------------------------------- 

# ba in model mikhahim vijegi mahsolat ra benvisim yani ( rang, jens, tarh, andaze, vazn, tarikh tolid, tarikh engheza )

class Feature(models.Model):
   feature_name = models.CharField(max_length=100, verbose_name='نام ویژگی')     # ( feature name ) yani nam vijegi k manzor haman  ( rang, jens, tarh, andaze, vazn, RAM, tarikh tolid, tarikh engheza ) 
   Product_Group = models.ManyToManyField(ProductsGroup, verbose_name='گروه کالا', related_name='features_of_groups')     # ( ManyToManyField ) in yek modeli ast k rabete chand b chand darad k neveshtim ba ( ProductsGroup ) k bala neveshtim rabete chand b chand dashte bashad, yani baraye in ast k vijegi mahsolat ra k bala neveshtim merbot b ko2m goroh kala bashe, yani masalan yeki az vijegiha RAM ast k faghat marbot b goroh kalahaye mobaili va compioteri mishe, ( related_name='features_of_groups' ) yani ma b class ( ProductsGroup ) k bala neveshtim yek feilde b esm ( features_of_groups ) ezafe mikonim k b in kar ManyToManyField migan yani rabete chand b chand
   
   
   def __str__(self):
      return self.feature_name
   
   class Meta:
      verbose_name = 'ویژگی'
      verbose_name_plural = 'ویژگیها'
      

#-----------------------------------------------------------------

# in model baraye mahsolat ast

class Product(models.Model):
   product_name = models.CharField(max_length=500, verbose_name='نام کالا')
   description = RichTextUploadingField(config_name= 'default', blank= True, verbose_name='توضیحات کالا')       # ( description ) marbot b ketabkhane ( from ckeditor_uploader.fields import RichTextUploadingField ) ast k bala neveshti, baraye ghesmate tozihat bayad yek seri codha dar ghesmate Settings va urls.py asli benvisim k dar folder ( Guide ) tozih dadam, 

# in 2 code pain marbot b upload kardan axs dar site hastand, baraye in kar aval miravim code asli ra dakhele file ( utils ) minevisim va bad address oun classi k daron file utils neveshtim ra inja minevisim, vali ghablesh bayad bala benvisim ( from utils import FileUpload )
   file_upload = FileUpload('images' , 'product')                               # ( FileUpload ) esm classi ast k daron file ( utils ) neveshtim va baraye uplode kardan axsha estefade mishe, ( images ) poshe aval ast, ( products_group ) poshe dovom ast
   image_name = models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر کالا')    # in code ham marbot b code bala ast baraye uplode kardane axs
   
   product_group = models.ManyToManyField(ProductsGroup, verbose_name='گروه کالا', related_name='products_of_groups')         # baraye in ast k shayad bekhahim yek mahsol ra dar chandin goroh dashte bashim, neveshti rabete chand b chand ba ProductsGrous dashte bashe, ( related_name='products_of_groups' ) yani ma b class ( ProductsGroup ) k bala neveshtim yek feilde b esm ( products_of_groups ) ezafe mikonim k b in kar ManyToManyField migan yani rabete chand b chand
   price = models.PositiveIntegerField(default=0, verbose_name='قیمت کالا')                                                 # ( default=0 ) yani ghaimate kalaha az ebteda 0 bashad
   brand = models.ForeignKey(Brand, verbose_name='برند کالا', on_delete=models.CASCADE, null=True, related_name='brands')   # ( on_delete=models.CASCADE ) yani agar yek mahsol az in brand ra pak kardim baghiye zir majmoe in brand ham pak shavand      
   is_active = models.BooleanField(default=True, blank=True, verbose_name='وضعیت فعال / غیر فعال')
   register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
   published_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')      # baraye timezon bayad bala benvisim ( from django.utils import timezone )
   update_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ اخرین به روز رسانی')
   features = models.ManyToManyField(Feature, through='ProductFeature')     # baraye model ( product ) in ra minevisim ta kalaha betavanand daron site b vizhegihashon(feature) dastresi dashte bashand, ( through ) baes mishe k ma betavanim az tarigh product b tamam vizhegihaye kalaha vasl beshim va yek esm baraye an entekhab mikonim ( through='ProductFeature )
   slug = models.SlugField(max_length=200, null=True)
   
   
   def __str__(self):
      return self.product_name
   
   
   
# in def marbot b ( slug ) ast, baraye in ast dakhele site roye yek kala k click mikonim safhe marbot b oun kala baz mishavad va slug oun kala k dar panel admin vasash neveshtim dar URL site neveshte mishavad va moshtari joziyat oun kala ra k ma dakhele panel admin neveshtim ra mitavanad bebinad, masal rang, vazn, size va ..., baraye in kar aval dar ghesmate views.py yek class neveshtim b name ( class ProductDetailView ) k marbot b in def ast bad url ( class ProductDetailView ) in class ra minevisim va bad va in def ra ham inja zite ( class Product ) minevisim va bad dakhele folder ( product_box.html ) jelo tamame ( href ) ha bayad esm in def ra benvisim ( {{product.get_absolute_url}} ), product haman zarfi ast k dar class ( class ProductDetailView ) sakhtim va slug ha ra rikhtim dakhelesh va get_absolute_url in ham esm in def ast
   def get_absolute_url(self):  
       return reverse("products:product_details", kwargs={"slug": self.slug})   # baraye reverse bayad in ketabkhane bala ezafe shavad ( from django.urls import reverse ), in code ya baraye ma reverse kon yani baraye ma bargardon ( products:product_details ), products esm url ast va product_details esm url class ProductDetailView, ( kwargs={"slug": self.slug} ) in ham yani slug har kala ra bala dar ghesmate url site neshan bede 
             
  
  
# inja yek def zire ( Product ) yani kalaha minevisim k marbot b ( discount ) ast yani takhfif, ma codhaye takhfifhaye kalaha ra daron folder discounts va daron models.py neveshtim
# in def baes mishavad har kalai k daron site takhfif khorde bod oun takhfif zire axs oun kala daron sate neshan dade shavad
# har kalai bar asas in tabe mizan takhfife khodesh ro bar asas ghaimatesh bayad dashte bashe
   def get_price_by_discount(self):
      list1=[]                                                      # aval yek list khali dorost mikonim k takhfife kalaha ro berize tosh
      for dbd in self.discount_basket_details2.all():               # ( discount_basket_details2 ) in haman "related_name='discount_basket_details2" ast k daron folder discounts file models.py zire class DiscountBasketDetails jeloye product neveshtim, ( all ) yani hame takhfifasho neshon bede, ( dbd ) yani DiscountBasketDetails
         if (dbd.discount_basket.is_active==True and                # ( discount_basket ) in haman ( discount_basket ) ast k daron folder discounts file models.py zire class DiscountBasketDetails neveshtim va chon jelo discount_basket dakhele parantez neveshtim ( DiscountBasket ) b hamin elat b class ( DiscountBasket ) k balaye oun neveshtim vast shode ast bekhatere hamin minevisim ( dbd.discount_basket.is_active==True ) chon is_active yeki az gozinehaye ( DiscountBasket ) ast, dar kol in code yani agar ( discount_basket ) is_activesh mosavi ba True bashe.
            dbd.discount_basket.start_date <= datetime.now() and    # ( discount_basket ) in haman ( discount_basket ) ast k daron folder discounts file models.py zire class DiscountBasketDetails neveshtim va chon jelo discount_basket dakhele parantez neveshtim ( DiscountBasket ) b hamin elat b class ( DiscountBasket ) k balaye oun neveshtim vast shode ast bekhatere hamin minevisim ( dbd.discount_basket.start_date <= datetime.now ) chon start_date yeki az gozinehaye ( DiscountBasket ) ast, dar kol in code yani tarikhe shoroe takhfif gozashtan kamtar ya mosavi ba tarikh o sa'at alan bashe 
            datetime.now() <= dbd.discount_basket.end_date):        # in baraye ( end_time ) ast, yani tarikhe payani takhfif gozashtan kamtar ya mosavi ba tarikh o sa'at alan bashe
            list1.append(dbd.discount_basket.discount)              # inja migim b list1 k bala neveshtim ( append ) yani ezafe kon ( dincount ) ro, discount ham yek gozine dakhele discount_basket hast mesl start_date va end_date
      
      descount=0                   # inja y zarf dorost mikonim baraye discount nahai yani akharin takhfifi k emal mishe ghabl az kharid k aval oun ro 0 mizarim, yek zaman yek kala hast k 2ta takhfif rosh emal shode yani ham 25% takhfif dare ham 50%, az in code b bad baraye injor kalahai neveshtim
      if(len(list1)>0):            # yani agar kalai k bala daron zarf list1 darim yek takhfif rosh emal shode ast
         discount = max(list1)     # maximum takhfif oun kala ro hesab kon va bad mirizim dakhele zarf discount
         return self.price-(self.price*discount/100)       # va dar akhar ba in formol darsad ro az gheimate vaghei kala kam mikonim
# agar oun kala dakhele hichkodom az sabadha ( list1 va discount ) nabashe discountesh 0 hast yani takhfifi nadare vali agar dakhele yaki az zarfha bashe takhfifesh hesab mishe
# va dar akhar baraye inke takhfifha zire axs dakhele site neshan dade beshan mirim dakhele ( template, partials, product, product_box.html ) esm in get ro b gheimat ezafe mikonim ( <div class="product-card__prices">{{ product.get_price_by_discount|intcomma }} تومان</div> )
   
   
   
   # in code baraye tedad mojodi kala daron anbar ast
   def get_number_in_warehouse(self):
      sum1 = self.warehouse_products.filter(warehouse_type_id=1).aggregate(sum('qty'))       # ( warehouse_products ) haman esmi ast k daron folder warehouses dakhele models.py zire class Warehouse jelo product va ba jelo related_name neveshtim, vaghti ma baraye yek model foreignkey minevisim va bad vasash related_name minevisim b in mani ast k bayad esmi k jelo related_name yani ( 'warehouse_products' ) neveshtim ra b modele folder Products ezafe shavad, va bed behesh migim ( .filter(warehouse_type_id=1) ) yani boro dakhele Database va oun kalahai k warehouse_type_id ouna 1 hastand ro filter kon va joda kon( id=1 kalahai hastand k kharidari shodand tavasote modir va id=2 kalahai hastand k forosh raftand ), va dar akhar ( .aggregate(sum('qty')) ) miyad (sum) yani jam mikone (qty) yani tedadeshon ro yani tamame ounai k id=1 darand ro tedad kalashon ro jam mikone yani tamame kalahai k kharidari shodand ro jam mikon, yani masalan az yek kala 50 ta kharidim az yek kalaye dg 100 ta bad in code miyad 100 ro jam mikone ba 5 k mishe 150, baraye inke betavanim az sum estefade konim bayad ketabkhane sum ra bala benvisim ( from django.db.models import Sum )
      sum2 = self.warehouse_products.filter(warehouse_type_id=2).aggregate(sum('qty'))       # in code tamame kalahaye forosh rafte ra jam mikonad chon ( id=2 ) ast va dakhele Database id=2 yani kalahaye forokhte shode vali code bala tamame kalahaye kharidari shode ra jam mikonad, pas harchi kharidari shode tu zarf ( sum1 ) rikhte shode va harchi forokhte shode tu zarf ( sum2 ) rikhte shode
      
      input = 0                     # inja yek zarf khali b nam input dorost mikonim
      if sum1['qty__sum']!=None:          # bazi kalaha momkene daron anbar sabt shode bashand vali hanoz na kharidari shodand na forosh raftand pas ouna None hastand, pas in code mige agar kalahai k daron sum1 hast va kharidari shodand ( !=None ) yani agar None nabod berizesh dakhele input 
         input = sum1['qty__sum']
         
      output = 0
      if sum2['qty__sum']!=None:          # in ham mesl code bala ast vali baraye kalahaye forosh rafte ast, yani agar kalahaye forosh rafte None nabodand berizeshon dakhele yek zarf b nam output
         output = sum2['qty__sum'] 
         
      return input-output         # va dar akhar in code yani ( input ) har chandta kala k kharidam menhaye ( output ) har chandta kala k forokhtam mikonim, inha ra menhaye ham mikonim va tedad kalahai k daron anbar monde b dast miyad
   
   
   
   
# in def neshan midahad kodam moshtari ch emtiyazi b in kala dade ast
   def get_user_scor(self):
      request = RequestMiddleware(get_response=None)      # ( RequestMiddleware ) in baraye zamani ast k ma ehtiyaj darim dakhele folderhaye models.py request dashte bashim mesl ( request.user ) ta betavanad userha ra paida konad, baraye inke betavanim az ( RequestMiddleware ) estefade konim yek folder joda b nam middlwares sakhtim va daronash yek class b nam RequestMiddlware neveshtim va bad harmoghe khastim dakhele modeli az request estefade konim esm oun class yani ( RequestMiddleware ) ra dakhele oun models.py minevisim, in ketabkhane ro bayad bala benvisim ( from middlewares.middlewares import RequestMiddleware )
      request = request.thread_local.current_request      # in 2 code ba ham hastand
      
      score = 0    # az in code b pain baraye mohasebe emtiaze moshtariyan ast
      user_score = self.scoring_product.filter(scoring_user=request.user)
      if user_score.count() > 0:
         score = user_score[0].score 
      return score              
# bad az in baraye inke 5ta setare dar site zaher beshe ta betonim emtiyaz bedim bayad berim frontend va js oun ro benvisim
   

   

# in def baraye miyangin emtiyaz yek kala ast, yani yek kala k chandin moshtari ouno kharidan ta alan miyangin emtiyazatesh cheghadr ast, masalan 3 setare 5 setare ... in code baraye in ast vaghti moshtari vared site mishe zire kalai k mikhad bekhare neshon dade beshe oun kala ch emtiyazi darad ya chandta setare darad
   def get_average_score(self):     # ( get_average_score ) yani gereftan miyangin emtiyaz, ( self ) yani kala, yani gereftan miyangin emtiyaz in self ya kala 
      avgScore = self.scoring_product.all().aggregate(Avg('score'))['score__avg']      # ( self.scoring_product.all() ) self yani kala, in code mige az in kala boro ( scoring_product esho ) biyar va all yani hamasho biyar, ( scoring_product ) hamoni hast k dakhele folder comment_scoring_favorites bad dakhele models.py zire kelas scoring jelo product neveshtim ( related_name='scoring_product' ), ( (Avg('score') ) in yani miyangin emtiyazash ra hesab kon, masalan 2 nafar yek kala mikharan yekisho behesh 4 setare mide yekishon 2 setar mide bad zire oun kala minevise 3 setare chon miyangin 4 va 2 ro miyare 
      if avgScore == None:    # yani agar natonesti miyangin etiyazat ro b dast biyari
         avgScore = 0         # avgScore ya miyangin emtiyaz ro bezar 0, in baraye zamani hast k masalan b yek kala hich emtiyazi dade nashode va 0 neshan midahad
      return avgScore
   
   
   
   
# in def marbot b class Favorite dakhele folder ( comment_scoring_favorite ) va dakhele models.py ast, in def neshan midahad k aya in kala baraye moshtari joze alaghemandihash ast ya na yani aya moshtari oun tike ghalbe pain kala ra mizane ya na   
   def get_user_favorite(self):
      request = RequestMiddleware(get_response=None)      # ( RequestMiddleware ) in baraye zamani ast k ma ehtiyaj darim dakhele folderhaye models.py request dashte bashim mesl ( request.user ) ta betavanad userha ra paida konad, baraye inke betavanim az ( RequestMiddleware ) estefade konim yek folder joda b nam middlwares sakhtim va daronash yek class b nam RequestMiddlware neveshtim va bad harmoghe khastim dakhele modeli az request estefade konim esm oun class yani ( RequestMiddleware ) ra dakhele oun models.py minevisim, in ketabkhane ro bayad bala benvisim ( from middlewares.middlewares import RequestMiddleware )
      request = request.thread_local.current_request      # in 2 code ba ham hastand
      flag = self.favorite_product.filter(favorite_user=request.user).exists()      # ( favorite_product ) yani boro dakhele Database boro soraghe jadvale favorite_product va ( filter ) yani filter kon yani check kon bebin ( favorite_user=request.user ) k aya request_user yani moshtari k dakhele site ast ( favorite_user ) b chizi alaghemand bode? chizi ro like karde ? ( exists ) chon filter neveshtim inja exists minevisim yani neshan bede yani True ya False kon k aya moshtari b kala alaghemand ast ya na, albate moshtari hatman bayad login bashad
      return flag
      
   
   
   class Meta:
      verbose_name = 'کالا'
      verbose_name_plural = 'کالاها'

#-----------------------------------------------------------

# in model baraye vizhegi kalaha ast ( az rabete chand b chand model kala va model vizhegi b vojod miyad )
# masalan ma yek code kala darim k az jadval ya model product miyad va yek code vizhegi darim k az jadval ya model features miyad
# darvaghe ma ba in code model ( product ) va model ( feature ) ra b ham vasl mikonim va yek ( value ) b anha ezafe mikonim

class ProductFeature(models.Model):          # in model gharare ta jadval ya model bala ra b ham vasl konad yani ( product va feature )
   product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا', related_name='product_features')        # in code vasl mishe b model ( product ) va bad ( related_name='product_features' ) vaghti in ra minevisim yani tamame productha shamel feature ya vizhegi mishavand va beas mishe k befahmim har kala ch vizhegihai darand
   feature = models.ForeignKey(Feature, on_delete=models.CASCADE, verbose_name='ویژگی')              # in code vasl mishe b model ( feature )              
   value = models.CharField(max_length=100, verbose_name='مقدار ویژگی کالا')           # ( value ) yani inke baraye mahsol mobail vizhegi RAM oun bashe 2GIG, dar inja mobail dar jadval ( product ) ast, RAM dar jadval ( feature ) ast, 2GIG dar jadval ( value ) ast, ka hami inha b ham vasl mishavand, ya masalan kala pirahan vizhegi rangesh bashe ghermez k ghermez value ast
   
   
   
   def __str__(self):
      return f"{self.product} - {self.feature} : {self.value}"

   class Meta:
      verbose_name = 'ویژگی محصول'
      verbose_name_plural = 'ویژگی های محصولات'
      
#----------------------------------------------------------------

# in model baraye in ast k har kalai betone axs dashte bashe

class ProductGallery(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا', related_name='gallery_images')     # in code ra b sorate ( ForeignKey ) yani rabete chand b chand minevisim va vaslash mikonim b model ( product ) asli, ( related_name='gallery_images' ) kare related_name in ast k vast mishavad b safhe html yani behesh yek esm midim mesl ( gallery_images ) bad in esm ra raftam daron safhe ( product_detail.html ) daron yek halghe ( for ) neveshtam
   
   # in 2 code pain marbot b upload kardan axs dar site hastand, baraye in kar aval miravim code asli ra dakhele file ( utils ) minevisim va bad address oun classi k daron file utils neveshtim ra inja minevisim, vali ghablesh bayad bala benvisim ( from utils import FileUpload )
   file_upload = FileUpload('images' , 'product_gallery')                               # ( FileUpload ) esm classi ast k daron file ( utils ) neveshtim va baraye uplode kardan axsha estefade mishe, ( images ) poshe aval ast, ( products_group ) poshe dovom ast
   image_name = models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر کالا')    # in code ham marbot b code bala ast baraye uplode kardane axs
   
   
   
class Meta:
   verbose_name = 'تصویر'
   verbose_name_plural = 'تصاویر'
   
