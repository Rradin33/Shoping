from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [
   path('shop_cart/', views.ShopCartView.as_view(), name="shop_cart"),
   path('show_shop_cart/', views.show_shop_cart, name="show_shop_cart"),
   path('add_to_shop_cart/', views.add_to_shop_cart, name="add_to_shop_cart"),                    # in url marbot b ajax add kardan kala hast k neveshtim, daron folder static file js file ( myscript.js ), view in ajax ro ham neveshtim
   path('delete_from_shop_cart/', views.delete_from_shop_cart, name="delete_from_shop_cart"),     # in url marbot b ajax delet kardan kala hast k neveshtim, daron folder static file js file ( myscript.js ), view in ajax ro ham neveshtim
   path('update_shop_cart/', views.update_shop_cart, name="update_shop_cart"),                    # in url marbot b ajax update kardan kala hast k neveshtim, daron folder static file js file ( myscript.js ), view in ajax ro ham neveshtim
   path('status_of_shop_cart/', views.status_of_shop_cart, name="status_of_shop_cart"),           # in url marbot b ajax status kardan kala hast k neveshtim, daron folder static file js file ( myscript.js ), view in ajax ro ham neveshtim
   path('Create_order/', views.CreateOrderView.as_view(), name="Create_order"),       # vaghti url ro neveshtim baraye inke dokme edame kharid kar kone mirim dakhele ( template, orders_app, partial, shox_shop_cart.html ) va bad code marbot b edame kharid ro paida mikonim va vasash ( href ) minevisim va adress in url ro ounja behesh midim, ( href="{% url 'orders:create_order' %}" )
   path('checkout_order/<int:order_id>/', views.CheckOutOrderView.as_view(), name="checkout_order"),      # ( <int:order_id>/ ) in ra minevisim chon dar class ( CheckOutOrderView ) jelo get order_id ra neveshte bodim ( def get(self, request, order_id) )
   path('applay_coupon/<int:order_id>/', views.ApplayCoupon.as_view(), name="applay_coupon"),
]

 