from django.contrib import admin
from .models import Order, OrderDetails, OrderState       # in 2ta model marbot b modelhaye dakhele models.py ast

#----------------------------------------------------------------

class OrderDetailsInLine(admin.TabularInline):          # in marbot b model ( OrderDetails ) ast yani vizhegihaye sefaresh, vaghti in class ra minevisim daron panel admin yek jadval zire ghesmate sefareshat moshtari sakhte mishavad va in 4 gozine ra darad k ( کالا, تعداد, قیمت کالا در فاکتور' ) in 3 mored hamon vizhegihai hastand k ma daron models.py zire model OrderDetails neveshtim
   model = OrderDetails
   extra = 3                 # 3 yani 3ta cadr jadval az oun vizhegiha sakhte shavad

#----------------------------------------------------------------

@admin.register(Order)
class OrderDetailsAdmin(admin.ModelAdmin):
   list_display = ['customer', 'order_state', 'register_date', 'is_finaly', 'discount']        # az model order k dakhele file models.py neveshtim in 4ta gozinaro inja seda zadim k dakhele panel admin jadvalhash sakhte beshan
   inlines = [OrderDetailsInLine]           # bad az inke class ( OrderDetailsInLine ) ra bala neveshtim bayad inja sedash bezanim ta jadvalha dakhele panel admin sakhte shavand
   
#----------------------------------------------------------------

@admin.register(OrderState)
class OrderStateAdmin(admin.ModelAdmin):
   list_display = ['id', 'order_state_title']
   
