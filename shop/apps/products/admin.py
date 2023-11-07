# inja marbot b panel admin ast k ba codhai k inja minevisim mitavanim panel admin ra modiriyat konim yani btonim kalai ezafe konim ya hazf konim ya gheimate kalaharo kam o ziyad konim va ...
# aval bayad tamaame modelhai k neveshtim ra yeki yeki inja biyavarim va codhaye marbit b panel admin anha ra benvisim

#----------------------------------------------------------------

from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Brand, ProductsGroup, Product, ProductFeature, Feature, ProductGallery
from django.db.models.aggregates import Count                    # in ketabkhane marbot b 2 def k dar class ( ProductsGroupAdmin ) neveshtim ast k tozihatesh ro jelo haman def neveshtam
from admin_decorators import short_description, order_field      # in ketabkhane marbot b 2 code ast k balaye ( def count_product_of_group ) neveshtim va baraye in ast k ma betavanim esmhaye enelisi dakhele panel karbari ra b farsi tabdil konim, va baraye in k in ketabkhane fa'al shavad bayad decorators ro nasb konim ba in code ( pip install django-admin-decorators )

#----------------------------------------------------------------

# in baraye model Brand ast

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
   list_display = ('brand_title', 'slug')             # ( list_display ) haman cadrhai ast k daron panel admin sakhte mishavad va ma minevisim ch chizhai az model Brand ra mikhahim dakhele oun cadrha bebinim
   list_filter = ('brand_title',)              # yani yek dokme filter sakhte mishe k bar asas brand_title mitonim brand ha ra paida konim, ( , ) in alamati k akharesh mizarim b in mani ast k chon faghat y done gozine neveshtim bayad akharesh ( , ) bezarim ta tapel bodanesh moshakhas beshe, ( tapel ) yani haman parantez k dakhelesh neveshtim
   search_fields = ('brand_title',)            # yek dokme search sakhte mishe k bar asas brand_title mitonim brand ha ra search konim, ( , ) in alamati k akharesh mizarim b in mani ast k chon faghat y done gozine neveshtim bayad akharesh ( , ) bezarim ta tapel bodanesh moshakhas beshe, ( tapel ) yani haman parantez k dakhelesh neveshtim   
   ordering = ('brand_title',)                 # yani moratab sazi, yani moratab sazi inha dar panel admin bae asas ch chizi bashe
   
#----------------------------------------------------------------

# in class baraye model ProductsGroup ast, dar panel admin yek ghesmat sakhte mishavad b nam ( گروه کالا )


def de_active_product_group(modeladmin, request, queryset):       # dar panel admin vaghti vared ( goroh haye kala ) mishim bala neveshte shode ( action ) k karash faghat in ast k betavanim har kalai ra k nemikhahim pak konim, vali ba in code yek morede digar ham b action ezafe mikonim k har kalai ra k khastim az ( is_active ) bardarim yani ghair fa'al konim, ama ba in code faghat mitonim kalaha ra ghair fa'al konim agar bekhahim baz hamon kala ra fa'al konim bayad yek code digar mesl in code benvisim va ( is_active ) ra True konim, bad az inke in code ra neveshtim baraye inke fa'al shavad pain minevisim ( actions = [de_active_product_group] )
   queryset.update(is_active=False)

def active_product_group(modeladmin, request, queryset):       # ba in code mitonim daron action kalahai k ghair fa'al hastand ta fa'al konim, darvaghe def bala va in def ra minevisim ta betonim kala ha ra fa'al ya ghair fa'al konim
   queryset.update(is_active=True)
# har chizi k bekhahim dar ghesmate action ezafe konim mesl code bala oun ra minevisim va bad dar class ( ProductsGroupAdmin ) oun ra minevisim ta fa'al va roye site ejra shavad


class ProductsGroupInLineAdmin(admin.TabularInline):      # in class baraye kalahaye valed hastand, vaghti dakhele panel admin darim etela'at yek kalaye valed ra minevisim b vasile in code yek seri cadr zire haman kalaye valed b vojod miyad k mitavanim etela'at kalahai k zir majmoe in kala valed hastand ra dakhle oun cadrha benvisim, masalan kalaye valed ra minevisim ( poshak ) va zir majmo'e an minevisim ( mardane, zanane, bachegane )
   model = ProductsGroup                                  # yani in class baraye model ( ProductsGroup ) ast


@admin.register(ProductsGroup)
class ProductsGroupAdmin(admin.ModelAdmin):
   list_display = ('group_title', 'is_active', 'group_parent', 'slug', 'register_date', 'update_date', 'count_sub_group', 'count_product_of_group')             # ( list_display ) haman cadrhai ast k daron panel admin sakhte mishavad va ma minevisim ch chizhai az model Brand ra mikhahim dakhele oun cadrha bebini, ( count_sub_group ) marbot b 2 def pain ast k ounja tozih dadam baraye ch kari ast
   list_filter = ('group_parent', 'is_active')              # yani yek dokme filter sakhte mishe k bar asas brand_title mitonim brand ha ra paida konim
   search_fields = ('group_title',)                           # yek dokme search sakhte mishe k bar asas brand_title mitonim brand ha ra search konim, ( , ) in alamati k akharesh mizarim b in mani ast k chon faghat y done gozine neveshtim bayad akharesh ( , ) bezarim ta tapel bodanesh moshakhas beshe, ( tapel ) yani haman parantez k dakhelesh neveshtim   
   ordering = ('group_parent', 'group_title')                 # yani moratab sazi, yani moratab sazi inha dar panel admin bae asas ch chizi bashe
   inlines = [ProductsGroupInLineAdmin]                       # onja esm class bala ra minevisim ta cadrhai k bala tozih dadam dakhele panel admin sakhte shavand
   actions = [de_active_product_group, active_product_group]   # in code mardob b def ( de_active_product_group ) ast k bala neveshtim
	
 
# in 2 def pain baraye sakhte shodane ya ezafe shodane yek cadr jeloye cadrhaye digare ( گروه کالاها )  dakhele panel admin ast
# k neshan midahad har kalaye valed chandta zir majmo'e ya zir goroh darand, baraye mesal kala ( Mod va Poshak ) 2 ta zir majmo'e darad pas jeloye in kala minevisad ( 2 )
# baraye in 2 def bayad in ketabkhane ra benvisim ( from django.db.models.aggregates import Count ) 
   def get_queryset(self, *args, **kwargs):
      qs = super(ProductsGroupAdmin, self).get_queryset(*args, **kwargs)
      qs = qs.annotate(sub_group = Count('groups'))                        # ( annotate  ) yani mikhahim moshakhas konim k tedad ( goroh haye har kala ) chandta ast, vaghti in code ra neveshtim bad miravim def marbot b in code ra pain minevisim ( count_sub_group ), ( groups ) haman esmi ast k dakhele models.py az class ( ProductsGroup ) neveshtim va az dakhele ( group_parent ) ( related_name='groups' ) neveshtim
      qs = qs.annotate(produc_of_group = Count('proucts_of_groups'))       # ( annotate  ) yani mikhahim moshakhas konim k tedad ( kalahaye har goroh ) chandta ast, vaghti in code ra neveshtim bad miravim def marbot b in code ra pain minevisim ( def count_product_of_group ), ( proucts_of_groups ) haman esmi ast k dakhele models.py az class ( Product ) neveshtim va az dakhele ( group_parent ) ( related_name='proucts_of_groups' ) neveshtim
      return qs
         
   def count_sub_group(self, obj):                # in code marbot b code bala ast ( qs = qs.annotate(sub_group = Count('groups')) ), ba in code dar dakhele panel admin dar bakhsh ( goroh kalaha ) yek satr b baghiye satrha ezafe mishe b name ( count_sub_group ) k karash in ast k har product chandta goroh dare, va dar akhar baraye inke in satr ezaf shavad bayad bala daron ( list_display ) esm in def ra benvisim ( count_sub_group ), va baraye inke dakhele panel admin esmash ra farsi konim in code ra pain minevisim ( count_sub_group.short_description = 'تعداد زیر گروهها' )
      return obj.sub_group
   
   @short_description('تعداد کالاهای گروه')       # baraye inke dakhele panel admin esmash ra farsi konim balaye def minevisim ( @short_description('تعداد کالاهای گروه') ) vaghti in code ra balaye def minevisim digar ehtiyaji nist mesl def balai in code ra benvisim ( ( count_sub_group.short_description = 'تعداد زیر گروهها' ) ) 
   @order_field('produc_of_group')                # ( order ) yani ghabeliyate moratab sazi dare, ba in code vaghti dar panel karbari roye ( تعداد کالاهای گروه' ) click mikonim mesl yek dokme ast k kalaha ra bar asas tedad kalaha moratab mikonad, ( 'produc_of_group' ) esm feilde k mikhahim rosh moratab sazi anjam bedim ra bayad benvisim
   def count_product_of_group(self, obj):         # in code marbot b code bala ast ( qs = qs.annotate(produc_of_group = Count('proucts_of_groups')) ), ba in code dar dakhele panel admin dar bakhsh ( goroh kalaha ) yek satr b baghiye satrha ezafe mishe b name ( count_product_of_group ) k karash in ast k har goroh chandta product dare, va dar akhar baraye inke in satr ezaf shavad bayad bala daron ( list_display ) esm in def ra benvisim ( count_product_of_group ), va baraye inke dakhele panel admin esmash ra farsi konim balaye def minevisim ( @short_description('تعداد کالاهای گروه') ) vaghti in code ra balaye def minevisim digar ehtiyaji nist mesl def balai in code ra benvisim ( ( count_sub_group.short_description = 'تعداد زیر گروهها' ) )
      return obj.produc_of_group


   count_sub_group.short_description = 'تعداد زیر گروهها'                   # in khat code marbot b esm oun cadr ast, bala dar ghesmate list_disply esm in cadr ra neveshtim ( 'count_sub_group' ) vali chon mikhahim esm farsi bashad ba in code dakhele admin.py mitavanim har esm engilisi ra b farsi tabdil konim k ma esm oun cadr ra neveshtim ( تعداد زیر گروهها ), ( count_sub_group ) esm title bod k b vasile ( short_description ) avaz kardim
   de_active_product_group.short_description = "غیر فعال کردن گروه‌ها"       # in esm ( de_active_product_group ) ra b farsi tabdil kardim b vasile ( short_description )
   active_product_group.short_description = "فعال کردن گروه‌ها"

 
#----------------------------------------------------------------

# in class braye model ProductFeature ast, ba in class kalaha vizhegi minevisim 

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
   list_display = ('feature_name',)             
   list_filter = ('feature_name',)                   
   search_fields = ('feature_name',)                       
   ordering = ('feature_name',)
   
#----------------------------------------------------------------

# in class marbot b model ( Product ) ast, dar panel admin yek ghesmat sakhte mishavad b nam ( kalaha )


def de_active_product(modeladmin, request, queryset):       # dar panel admin vaghti vared ( goroh haye kala ) mishim bala neveshte shode ( action ) k karash faghat in ast k betavanim har kalai ra k nemikhahim pak konim, vali ba in code yek morede digar ham b action ezafe mikonim k har kalai ra k khastim az ( is_active ) bardarim yani ghair fa'al konim, ama ba in code faghat mitonim kalaha ra ghair fa'al konim agar bekhahim baz hamon kala ra fa'al konim bayad yek code digar mesl in code benvisim va ( is_active ) ra True konim, bad az inke in code ra neveshtim baraye inke fa'al shavad pain minevisim ( actions = [de_active_product_group] )
   queryset.update(is_active=False)

def active_product(modeladmin, request, queryset):       # ba in code mitonim daron action kalahai k ghair fa'al hastand ta fa'al konim, darvaghe def bala va in def ra minevisim ta betonim kala ha ra fa'al ya ghair fa'al konim
   queryset.update(is_active=True)
# har chizi k bekhahim dar ghesmate action ezafe konim mesl code bala oun ra minevisim va bad dar class ( ProductsGroupAdmin ) oun ra minevisim ta fa'al va roye site ejra shavad


class ProductFeatureInLine(admin.TabularInline):        # in class feature ya haman vizhegi ast, har kala yek feature darad yani yek vizhegi darad mesl ( size, range, jens, vazn, cpu, ... ), in class ra minevisim ta vizhegiye kalahai k dar class pain neveshtim ra betonim moshakhas konim va bad dakhele class pain in class ra seda mizanim ba in code ( inlines = [ProductFeatureInLineAdmin] ) k dar panel admin eja shavad
   model = ProductFeature
   extra = 3                     # tedad featurha ra k dar panel admin mizadim inja minevisim k 3 ast   
   
   
class ProductGalleryInLine(admin.TabularInline):        # in class feature ya haman vizhegi ast, har kala yek feature darad yani yek vizhegi darad, vizhegi in class axsha kochak zire axs asli daron site hastand yani ba in class dakhele panel admin zire har kala alave bar vizhegiye rang o vazn ... yek cadr ya jadval digar ham sakhte mishavad k mitavanim axs apload konim k oun axsha b sorate axs kochektar zire axs asli kalamon dar site neshan dade mishavad, in class ra minevisim ta vizhegiye kalahai k dar class pain neveshtim ra betonim moshakhas konim va bad dakhele class pain in class ra seda mizanim ba in code ( inlines = [ProductGalleryInLineAdmin] ) k dar panel admin eja shavad
   model = ProductGallery
   extra = 3                              # yani ta 3 ta axs mitonim apload konim 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ('product_name', 'price', 'brand', 'is_active', 'update_date', 'slug', 'display_product_groups')             # ( list_display ) haman cadrhai ast k daron panel admin sakhte mishavad va ma minevisim ch chizhai az model Product ra mikhahim dakhele oun cadrha bebinim
   list_filter = ('brand', 'product_group')                   # yani yek dokme filter sakhte mishe k bar asas ( 'brand', 'product_group' ) mitonim Product ya kala ha ra paida konim
   search_fields = ('product_name',)                          # yek dokme search sakhte mishe k bar asas ( product_name ) mitonim Product ha ra search konim
   ordering = ('update_date', 'product_name')                 # yani moratab sazi, yani moratab sazi inha dar panel admin bar asas ch chizi bashe
   actions = [de_active_product, active_product]
   inlines = [ProductFeatureInLine, ProductGalleryInLine]      # ( inlines ) marbot b class ( ProductFeatureInLineAdmin va ProductGalleryInLine ) asr k bala minevisim, vaghti oun class ra bala minevisim va bad in code ra inja minevisim, dar panel admin dar ghesmate ( kalaha ) yek cadr b pain ezafe mishavad b name ( vizhegi ) k anja mitavanim vizhegi har kala ra benvisim
   
   de_active_product.short_description = "غیر فعال کردن کالاها"       # in esm ( de_active_product_group ) ra b farsi tabdil kardim b vasile ( short_description )
   active_product.short_description = "فعال کردن کالاها"


   def display_product_groups(self, obj):     # ba in def yek cadr b jadval ( kalaha ) ezafe mishavad b nam ( display_product_groups ) va neshan midahad har kala zir majmo'e ko2m groh kala hast, baraye mesal ( shir pastorize ) zir majmoe goroh kala ( souper market ) ast, ya ( pirahan motor savari ) zir majmoe goroh kala ( poshak mardane ) ast, va dar akhar dar bala dar ghesmat ( list_display ) esm in def ra ezafe mikonim ( 'display_product_groups' )
      return ', '.join([group.group_title for group in obj.product_group.all()])
   display_product_groups.short_description = 'گروهای کالا'         # ba in code esm in def ra avaz mikonim va dar panel admin esm in def mishavad ( grohaye kala )
      
      
   