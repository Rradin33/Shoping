# file ( discounts.py ) b mani takhfif ast,
# baraye in ast k daron sabade kharid moshtari dakhele site yek cadr sakhte shavad ta moshtari agar code takhfif dasht code ra vared konad va az ghaimate kharid kam shavad
# alan mikhaim modelesh ro besazim

#----------------------------------------------------------------

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator      # in 2ketabkhane baraye ghesmate discount hast k pain neveshtim va hade'aghal va hade'aksar gheimate takhfif ra mitavanim ba in ketabkhane moshakhas konim
from apps.products.models import Product

#----------------------------------------------------------------

# in model marbot b code takhfif ast

class Coupon(models.Model):
   coupon_code = models.CharField(max_length=10, unique=True, verbose_name='کد کوپن')       # ( unique=True ) yani agar shomare coupon ta takhfif ra b yek nafar dadim dg in shomare baraye kasi tolid nashe 
   start_date = models.DateTimeField(verbose_name='تاریخ شروع')     # ( start_coupon ) yani in code az ch tarikhi etebar dare
   end_date = models.DateTimeField(verbose_name='تاریخ پایان')
   discount = models.IntegerField(verbose_name='درصد تخفیف', validators=[MinValueValidator(0),MaxValueValidator(100)])      # yani in coupon chand darsad takhfif dare, ( [MinValueValidator(0),MaxValueValidator(100)] ) ketabkhane in ra bala neveshtam, # in 2ketabkhane baraye ghesmate discount hast k pain neveshtim va hade'aghal va hade'aksar gheimate takhfif ra mitavanim ba in ketabkhane moshakhas konim
   is_active = models.BooleanField(default=False ,verbose_name='وضعیت')       # is active ham minevisism k agar khastim gheire fa'alesh konim, ( default=False ) in ra minevisim k avale kar har bar k yek coupon dorost shod b kasi rabtesh nade
   
   class Meta:
      verbose_name = 'کوپن تخفیف'
      verbose_name_plural = 'کوپنها'
   
   def __str__(self):
      return self.coupon_code
   
#----------------------------------------------------------------

# in model marbot b sabade takhfif hast, yani yek sabad dorost mikonam k masalan takhfif shabe yalda ya eid fetr az in tarikh ta in tarikh va in darsad ta in darsad fa'al bashe

class DiscountBasket(models.Model):
   discount_title = models.CharField(max_length=100, verbose_name='عنوان سبد تخفیف')
   start_date = models.DateTimeField(verbose_name='تاریخ شروع')     # ( start_coupon ) yani in code az ch tarikhi etebar dare
   end_date = models.DateTimeField(verbose_name='تاریخ پایان')
   discount = models.IntegerField(verbose_name='درصد تخفیف', validators=[MinValueValidator(0),MaxValueValidator(100)])      # yani in coupon chand darsad takhfif dare, ( [MinValueValidator(0),MaxValueValidator(100)] ) ketabkhane in ra bala neveshtam, # in 2ketabkhane baraye ghesmate discount hast k pain neveshtim va hade'aghal va hade'aksar gheimate takhfif ra mitavanim ba in ketabkhane moshakhas konim
   is_active = models.BooleanField(default=False ,verbose_name='وضعیت')       # is active ham minevisism k agar khastim gheire fa'alesh konim, ( default=False ) in ra minevisim k avale kar har bar k yek coupon dorost shod b kasi rabtesh nade
   
   class Meta:
      verbose_name = 'سبد تخفیف'
      verbose_name_plural = 'سبد های تخفیف'
   
   def __str__(self):
      return self.discount_title
   
#----------------------------------------------------------------

# vaghti yek sabade takhfif dorost mikonim bayad ( detail ) ya haman joziyate sabade takhfif ham moshakhas konim k chandta kala daron sabad gharar begirad
# baraye Detail yek class dg ham minevisim
   
class DiscountBasketDetails(models.Model):
   discount_basket = models.ForeignKey(DiscountBasket, on_delete=models.CASCADE, verbose_name='سبد تخفیف', related_name='discount_basket_details1')     # ( DiscountBasket ) in ra minevisim k begim ( discount_basket ) zir majmoe class bala yani ( DiscountBasket ) ast k b ham vasl shavand, ( on_delete=models.CASCADE ) yani harchizi har kalai pak shod zir majmoe haye an hamashon pak beshan
   product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='کالا', related_name='discount_basket_details2')                        # ( Product ) in ra minevisim k begim ( product ) zir majmoe class ( Product ) ast k dakhele model folder product neveshtim ast, in code ra minevisim ta betonim az dakhele Product kalaha ra paida konim ta b sabade takhfif vared shavand, aval bala ketabkhane Product ra minevisim ( from apps.products.models import Product )
   
   class Meta:
      verbose_name = 'جزییات سبد تخفیف'
# ba in code moshakhas mishavad k dakhele ch sabadi ch kalahai vojod dare




# bad mirim ghesmate admin.py codhaye makhsos panel admin ra minevisim ta modir betone codhaye takhfif va sabade takhfifesh ro moshakhas kone

   
   