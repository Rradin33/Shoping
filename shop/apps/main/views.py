# ( main ) app asli proje ast k ghaleb asli site safhe asli site ra misazad

#----------------------------------------------------------------

from django.shortcuts import render
from django.conf import settings
from django.views import View
from .models import Slider
from django.db.models import Q 

#----------------------------------------------------------------

def media_admin(request):                                  # in code ra bayad inja benvisim k tamame axshaye site neshan dade shavand, va bad miravim dakhele setting zire ghesmate (TEMPLATES) minevisim ('apps.main.views.media_admin') 
   return {"media_url": settings.MEDIA_URL,}            



def index(request):
   return render(request, 'main_app/index.html')

#----------------------------------------------------------------

# in class marbot b ( class Slider ) dakhele models.py ast va marbot mishe b axshaye cover site k masalan chandta axs darim va click kardan in axsha avaz mishavand

class SliderView(View):
   def get(self, request):
      sliders = Slider.objects.filter(Q(is_active=True))       # yani boro dakhele Database soraghe Slider va ouni k active hast ro baraye man biyar
      return render(request, "main_app/sliders.html", {"sliders": sliders})        # va amadash kon befresr b safhe ( slider.html )
   

#----------------------------------------------------------------

# in class baraye sakhtan safhe error 404 hast, yani agar moshtari dar ghesmate URL site sahei ra eshtebah type konad safhe error 404 baraye oun baz mishavad
# baraye in def nabayad daron urls.py folder main URL benvisim chon safhe error 404 dar sharayet khas azash estefade mishe vaghti k moshtari khatai anjam mide, vali yek URL darad k bayad ouno daron folder shop va daron urls.py benvisim k tamame application ha oun ra bebinand, url ra injori minevisim ( handler404 = 'app.main.views.handler404' )
def handler404(request, exception=None):
   return render(request, 'main_app/404.html')

# dar akhar dakhele settings balaye INSTALLED8APPS bayad code pain ra benvisim ta safhe error dakhele site neshan dade beshe

#DEBUG = False
#ALLOWED_HOSTS = ['*']       # setare yani roye har safhei yani tamame safheha error neshan dade beshe
   

