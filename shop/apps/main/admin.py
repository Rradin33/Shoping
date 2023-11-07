from django.contrib import admin
from .models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
   list_display = ('image_slide', 'slider_title1', 'link', 'is_active', 'register_date',)
   list_filter = ('slider_title1',)
   search_fields = ('slider_title1',)
   ordering = ('update_date',)             # ( ordering ) yani moratab sazi, yani moratab sazi inha dar panel admin bar asas ch chizi bashe
   readonly_fields = ('image_slide',)      # ma daron file models.py yek def neveshtim b nam ( image_slide ) k shamele codhaye HTML ast va oun def marbot b panel admin ast, baraye hamin oun def ra inja b vasile ( readonly_fields ) seda mizanim ta dar panel admin ejra shavand
   
   
   
   
   
