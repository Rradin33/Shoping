from django.db import models
from apps.products.models import Product
from apps.accounts.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

#----------------------------------------------------------------

# in modele baraye in ast k karbar betavanad dar site ma comment bedahad

class Comment(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment_product', verbose_name='کالا')       # in ra minevisim ta moshakhas shavad karbar dare baraye ch producti comment mizare, vaghti inja baraye yek model foreignkey minevisim va bad vasash related_name minevisim b in mani ast k bayad esmi k jelo related_name yani ( 'comment_product' ) neveshtim ra b modele folder Products ezafe shavad
   commenting_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments_user1', verbose_name='نظر دهنده')     # in ra minevisim ta moshakhas shavad kodam moshtari dare comment mide
   approving_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments_user2', verbose_name='مدیر تایید کننده نظر')     # approving_user baraye in ast k vaghti yek moshtari zire yek kala comment mide bad yek modir bayad bere va oun comment ra taeed kone ta oun oun comment namayesh dade beshe, dar halate adi vaghti yek moshtari comment migozarad sabt nemishavad yani neshan dade nemishavad ta yeki az modiran site beravand va oun comment ra tike bezanand ta taeed shavad
   comment_text = models.TextField(verbose_name='متن نظر')      # in ra minevisim baraye matn comment k moshtariha mitavanand bebinand
   registerdate = models.DateField(auto_now_add=True, verbose_name='تاریخ درج')   # tarikh va zaman comment ra neshan midahad
   is_active = models.BooleanField(default=False, verbose_name='وضیت نظر')      # oun commenti  k dade shode ( default = False ) ast yani comment neshan dade nemishe va active nist ta zamani k yeki az modiran site bere dakhele panel modiriyat va tike ouncomment ro bezane ta active beshe comment baraye moshtariha neshan dade beshe
   comment_parent = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='comments_child', verbose_name='والد نظر')    # ( comment_parent ) haman model commenthai hastand k masalan yek nafar mire zire comment yeki dg comment mizare bad oun nafare avali k zire commentesh baghiye javabesho dadan mishe comment_parent, baraye in kar bayad yek foreignkey benvisim khode hamin class Comment va chon foreignkey b khodesh zadim bayad injori neveshte beshe ( 'Comment' )
   
   
   def __str__(self):
      return f"{self.product} - {self.commenting_user}"
   
   
   class Meta:
      verbose_name = 'نظر'
      verbose_name_plural = 'نظرات'
   
# bad az in code mirim ghesmate admin.py va code marbot b in class ro ounja ham minevisim ta in class ro daro, panel karbari hamdashte bashim
# va bad bayad yek form dakhele forms.py marbot b in model benvisim ta karbar betone comment bezare, vaghti form minevisim yek kadr mostatil shekl zire kala dar ghesmate commenha b vojod miyad k karbar mitone tosh comment bezare 
# va bad bayad dar ghesmate views.py view marbot b Comment ra benvisim 
#----------------------------------------------------------------

# in modele baraye in ast k karbar betavanad dar site ma b kalai k kharide emtiyaz bedahad masalan 5 ta setare

class Scoring(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scoring_product', verbose_name='کالا')    # yani b ch kalai emtiyaz mide, ( related_name='scoring_product' ) ba neveshtan related_name in esm yani scoring_product b model product vasl mishavad
   scoring_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='scoring_user1', verbose_name='امتیاز دهنده')      # yani kodam user ya kodam moshtari dare emtiyaz mide
   registerdate = models.DateField(auto_now_add=True, verbose_name='تاریخ درج')      # tarikh va zaman emtiyaz dadan ra neshan midahad
   score = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='امتیاز')       # ( score ) in baraye adad emtiyaz ast k bein 0 ta 5 ast 


   def __str__(self):
      return f"{self.product} - {self.scoring_user}"
   
   
   class Meta:
      verbose_name = 'امتیاز'
      verbose_name_plural = 'امتیازات'
      
# bad mirim dakhele folder Product dakhele models.py 2 def marbot b in class ra zire class Product minevisim ( get_average_score   in baraye miyangin emtiyazat ) - ( get_user_scor   in neshan midahad kodam moshtari ch emtiyazi dade ast )
# va bad daron view.py code marbot ra minevisim ( def add_score )

#----------------------------------------------------------------

# in class baraye in ast k moshtari dar site az kalahai k khoshesh miyad ounaro tike mizane va ouna dar yek safhe dg save mishan
# masalan kenare kalaha yek tike b shekl ghalb hast k agar az oun kala khoshemon biyad oun ghalb ro mizanim va bad oun kala b list alaghemandihaye ma ezafe mishavad
# alan yek model minevisim ta befahmim ch kalai tavasote ch karbari dar ch tarikhi dar b list alaghemandiha ezafe shode ast

class Favorite(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorite_product', verbose_name='کالا')    # yani b ch kalai alaghe darim mide, ( related_name='favorite_product' ) ba neveshtan related_name in esm yani favorite_product b model product vasl mishavad
   favorite_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorite_user1', verbose_name='کاربر علاقه مند')      # yani kodam user ya kodam moshtari b oun kala alaghe dare mide   
   register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درج')   # baraye in ast k befahmim moshtari dar ch tarikhi kalai k behesh alaghemand hast ro b list alaghemandihash ezafe karde
   
   
   def __str__(self):
      return f"{self.product} - {self.favorite_user}"



   class Meta:
      verbose_name = 'علاقه'
      verbose_name_plural = 'علایق'


# bad mirim dakhele folder Product dakhele models.py def marbot b in class ra zire class Product minevisim ( get_user_favorite )
# bad view va url oun ro minevisim


