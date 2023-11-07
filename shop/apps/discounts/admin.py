# inja codhaye makhsos panel admin ra minevisim ta modir betone codhaye takhfif va sabade takhfifesh ro moshakhas kone

#----------------------------------------------------------------

from django.contrib import admin
from .models import Coupon, DiscountBasket, DiscountBasketDetails

#----------------------------------------------------------------

# in code marbot b model ( Coupon ) ast

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
   list_display = ('coupon_code', 'start_date', 'end_date', 'discount', 'is_active') 
   ordering = ('is_active',)            # yani faghat kasi k active hast mitone az code takhfif estefade kone va sefaresh bede
   
#----------------------------------------------------------------

# in code marbot b model ( DiscountBastekDetails ) ast k b sorate Inline minevisim ta daron panel admin zir majmoe ( DiscountBasket ) beshe
class DiscountBasketDetailsInline(admin.TabularInline):
   model = DiscountBasketDetails
   extra = 3                          # yani 3ta cadr ya jadval azash sakhte beshe 


# in code marbot b model ( DiscountBasket ) ast
@admin.register(DiscountBasket)
class DiscountBasket(admin.ModelAdmin):
   list_display = ('discount_title', 'start_date', 'end_date', 'discount', 'is_active')
   ordering = ('is_active',)            # yani faghat kasi k active hast mitone az code takhfif estefade kone va sefaresh bede
   inlines = (DiscountBasketDetailsInline,) 
   
#----------------------------------------------------------------

