from django.db import models
from utils import FileUpload
from django.utils import timezone
from django.utils.html import mark_safe         # ( mark_safe ) yak tage HTML ro migire va oun ro ejra mikone

#----------------------------------------------------------------

# class ( slider ) baraye cover safhe asli site ast
# dar safhe asli yek cover balaye safhe vojod darad k 3ta axs darad va axshaye oun ra ba click kardan mitanavim taghir bedahim 

class Slider( models.Model ):
   slider_title1 = models.CharField(max_length=500, null=True, blank=True, verbose_name='متن اول')         # in 3 code pain ra minevisim k agar lazem shod roye slideremon ya hamon cover matn benvisim, ma 3 ta code neveshtim baraye neveshtane 3khat matn roye cover site, albate agar khastim, ( null=True, blank=True ) yani ( blank ) harmoghe True bashad yani ejbari nist dar in ghesmat chizi neveshte shavad, ( null ) zamani k True bashad Database feilde hai ra k vasashon chizi neveshte nashode ra b sorate pishfarz null gharar mide
   slider_title2 = models.CharField(max_length=500, null=True, blank=True, verbose_name='متن دوم')         
   slider_title3 = models.CharField(max_length=500, null=True, blank=True, verbose_name='متن سوم')
   
   file_upload = FileUpload('images', 'slides')            # in 2 code marbot b upload kardan axs dar site hastand, baraye in kar aval miravim code asli ra dakhele file ( utils ) minevisim va bad address oun classi k daron file utils neveshtim ra inja minevisim, vali ghablesh bayad bala benvisim ( from utils import FileUpload )
   image_name = models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر اسلاید')
   
   slider_link = models.URLField(max_length=200, null=True, blank=True, verbose_name='لینک')        # in code ra minevisim ta siler ya cover ma ghabele click kardan bashe yani cover ma 3 ta axs darad k vaghti roye yeki az oun axsha click mikonim yek safhe jadid marbot b etela'ate oun cover baz mishavad, inja ham baz ( null=True, blank=True, ) har 2 ra True migozarim k agar nakhastim link bedim poresh nakonim
   is_active = models.BooleanField(default=True, blank=True, verbose_name='وضعیت فعال / غیر فعال')
   register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درج')
   published_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')      # baraye timezon bayad bala benvisim ( from django.utils import timezone )
   update_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ اخرین به روز رسانی')
   
   
   def __str__(self):
      return f"{self.slider_title1}"      # yani title1 mishe onvane asli ma
   
   
   class Meta:
      verbose_name = 'اسلاید'
      verbose_name_plural = 'اسلایدها'
      
      
# code pain baes mishavad k har axsi k ma baraye slide ya coveremon entekhab kaedim dar size kochak 80 dar 80 daron panel admin neshan dade beshe ta betavanim bebinim k baraye har slide ch axsi entekhab kardim
   def image_slide(self):
      return mark_safe(f'<img src="/media/{self.image_name}" style="width:80px;height:80px"/>')     # ( mark_safe ) yak tage HTML ro migire va oun ro ejra mikone, vali aval bayad ketabkhone oun ro bala benvisim ( from django.utils.html import mark_safe )
   image_slide.short_description = 'تصویر اسلاید'      # ( image_slide.short_description ) short_description yani daron panel admin balaye har axs cover neveshte beshe ( 'تصویر اسلاید' ), darvaghe esm sar soton ast 
# baraye inke in codha daron panel admin neshan dade beshan va ghabele ejra bashan bayad in def ra daron admin.py seda bezanim b vasile readonly_fields, injori ( readonly_fields = ('image_slide',) )
   
   
   def link(self):      # in def ra minevisim ta sliderha ya coverhaye site ghabele click kardan bashand
      return mark_safe(f'<a href="{self.slider_link}" target="_blank">link</a>')    # ( mark_safe ) yak tage HTML ro migire va oun ro ejra mikone, vali aval bayad ketabkhone oun ro bala benvisim ( from django.utils.html import mark_safe )
      
      

# bad az in codha mirirm dakhele safhe ( admin.py ) va codhaye marbot b safhe panel admin ra minevisim ta slider ra betavanim az daron panel admin modiriyat konim
# va bad bayad berim dakhele ( view.py ) yek class b nam ( class SliderView ) benvisim ta axshai k entekhab kardim roye cover site neshan dade beshan
# va bad ham URL va codhaye safhe HTML ra bayad benvisim ( man codhaye safhe HTML ro nanveshtam baraye hamon axsha roye cover site neshan dade nemishe )
