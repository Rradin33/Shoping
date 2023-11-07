# ( signals ) baraye in ast k vaghti bekhahim kalai az dakhele panel admin pak konim axs oun kala ham az dakhele system va kolan az compioter pak shavad
# agar signal ra nanvisim vaghti kalai ra pak mikonim axsash pak nemishe va dakhele system compioter save mimone
# ma inja signal ra dakhele app product neveshtim chon mikhastim kalai ra pak konim vali agar khastim signal ra daron apps haye digar estefade konim aval bayad daron oun apps yek file b nam ( signals.py ) besazim va hamin codaye pain ra ounja benvisim

#----------------------------------------------------------------

from django.dispatch import receiver
from django.db.models.signals import post_delete     # baraye estefade az signals bayad ketabkhane signals ra ezafe konim ta mazhol ( post delete ) ra dashte bashim
from .models import Product
from django.conf import settings
import os

#----------------------------------------------------------------

@receiver(post_delete, sender=Product)            # in code yani bad az inke producti delete shod def pain seda zade beshe 
def Delete_product_image(sender, **kwargs):       # bad az inke in def seda zade shod oun 3 khat code pain baes mishan k file axs pak shavand
   path = settings.MEDIA_ROOT+str(kwargs['instance'].image_name)     
   if os.path.isfile(path):
      os.remove(path)
      

# bad az inke in codha ra inja neveshtim baraye in ke system in def ra beshnasad va ejra konad mirim dakhele file ( apps.py ) va code marbot b in def ra minevisim, man neveshtam b nam ( def ready )



