from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from utils import FileUpload          # ( FileUpload ) esm classi ast k daron file ( utils ) neveshtim va baraye uplode kardan axsha estefade mishe

#----------------------------------------------------------------

### in class modiriyate user ha ra anjam midahad, yani karash sakhtan fazai ast k karbar betavanad anja dar site ma sabtenam konad va etela'ati k azash mikhaim ra vared konad, va sakhtan karbar superuser ast

class CustomUserManager(BaseUserManager):               # ( BaseUserManager ) modiriyate user ha ra anjam midahad, yani karash sakhtan fazai ast k karbar betavanad anja dar site ma sabtenam konad va etela'ati k azash mikhaim ra vared konad, va sakhtan karbar superuser ast
   def create_user(self, mobile_number, email="", name="", family="", active_code=None, gender=None, password=None):       # mikhahim yek ( create_user ) anjam dahim yeni yek safhe user besazim k moshtari betavanad dar site ma sabtenam konad va etela'at dakhele parantez ra az karbar mikhahim, ( active_code ) yani yek code baraye moshtari ersal mishavad ta hesabe oun fa'al shavad, (gender=Non, password=Non) vaghti Non hastan yeni ejbari nistand k hatman por shavad
      if not mobile_number:                                          # in if ra minevisim k agar shomare mobail vared nakard in matn behesh neshan dade shavad 
         raise ValueError("شماره مبایل باید وارد شود")

      user = self.model(                                     # alan mikhahim ba in code user moshtari ra save konim
         mobile_number = mobile_number,                        # yani agar shomare mobailesho dad begir azash
         email = self.normalize_email(email),                # email ra b in sorat minevisim, ( normalize_emai ) karash in ast k vaghti moshtari emailash ra varesh kard email oun ra tashih konad bad save konad, yani shayad moshtari havasesh nabashad yeki az horof emailash ra bozorg vared konad ya akhare emailash yek fasele begozarad, normalize inha ra tashih mikonad bad save mikonad
         name = name,
         family = family,
         gender = gender,                                    # yani agar jensiyatesh ro dad begir azash
         active_code = active_code,
      )                                    
      user.set_password(password)                            # password ra injori va inja minevisim, ba in kar vaghti moshtari passwordash ra vared mikonad password oun neshan dade nemishavad
      user.save(using = self._db)                                            # ba in code dar akhar tamam etela'at moshtari save mishavad
      return user



   def create_superuser(self, mobile_number, email, name, family, password=None, active_code=None, gender=None):        # in baraye zamani ast k vaghti khastim page admin ya ( superuser ) besazim az ma ya harkasi k khast b page admin vared shavad etela4at pain ra bekhahad
      user = self.create_user(                             # def create_user ra k bala neveshtim inja seda mizanim k in 2 def b ham vasl beshavand va dakhele an etela'at dakhele parantez ra minevisim k vaghti anha ra vared kardim save shavand
         mobile_number = mobile_number,
         email = email,
         name = name,
         family = family,
         active_code = active_code,
         gender = gender,
         password = password,
      )
      user.is_active = True                                # chon is_active pain dar ghesmat modelha False bod in minevisim va True mikonim
      user.is_admin = True                                 # chon is_admin pain dar ghesmat modelha False bod in minevisim va True mikonim
      user.is_superuser = True                             # ba in code vaghti in code ra minevisim ( py manage.py createsuperuser ) oun fard b sorate automat superuser mishavad yani admin asli mishavad va b tamame ghesmathaye panel admin dastresi khahad dasht, agar bekhahim kasi admin asli nashavad in code ra nabayad inja benvisim
      user.save(using = self._db)                          # ba in code dar akhar superuser k sakhtim save mishavad 
      return user

#----------------------------------------------------------------

### in model baraye in ast k yek karbar k hanoz moshtari nist betavanad dar site ma sabtenam konad va baraye sabtenam bayad etela'at pain ra por konad

class CustomUser(AbstractBaseUser, PermissionsMixin):                 # ( AbstractBaseUser ) yek user pish sakhte khode django ast k khaili az etela'at az ghabl dakhelesh zakhire shode k kare maro rahat mikone mesl ( username, is_active, firstname, lastname, email, va ... ), darvaghe alan in model man farzand class AbstractBaseUser ast, ( PermissionsMixin ) classi ast baraye ta'in sath dastresi karbaran b ghesmathaye mokhtalefe site, yani ba ( PermissionsMixin ) mitavanim moshakhas konim k moshtariha b bazi jahaye site dastresi nadashte bashand
   mobile_number = models.CharField(max_length=15, unique=True, verbose_name='شماره موبایل')        # ( unique=True ) yani hagh nadari shomare mobail tekrari vared koni
   email = models.EmailField(max_length=200, blank=True)              # ( blank=True ) yani dar hengame sabtenam ejbari nist moshtari emailesho vared kone, agar vared nakone accountesh sakhte mishe
   name = models.CharField(max_length=50, blank=True)
   family = models.CharField(max_length=50, blank=True)
   
   GENDER_CHOICES = (('True','مرد'),('False','زن'))
   gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='True', null=True, blank=True)       # ( gender ) yani jensiyat , ( choices=GENDER_CHOICES ) ba in code yek cadr dar site sakhte mishavad k mitavanim ba click kardan jensiyat ra entekhab konim, bayad ba in code cadrhaye sakhte shode ra por konim ( GENDER_CHOICES = (('True','مرد'),('False','زن')) )  
   
   register_date = models.DateField(default=timezone.now)               # ( register_date ) baraye tarikh sabtenam ast k bayad az ( timezone.now ) estefade konim k bayad in ketabkhane ra bala ezafe konim ( from django.utils import timezone ), ba in kar har moshtari k sabtenam mikonad ba sa'at va tarikh system save mishavad
   is_active = models.BooleanField(default=False)                       # ( is_active ) yani active bodan hesab karbari k ma ba in code False mikonim ( default=False ), k hichkas az haman aval True nabashad
   active_code = models.CharField(max_length=100, null=True, blank=True)           # ( active_code ) code fa'al sazi ast k az tarighe shomare mobail ya email baraye karbar mifrestim
   is_admin = models.BooleanField(default=False)                        # baraye vaziyat admin site ast
     
   
   USERNAME_FIELD = 'mobile_number'                  # ba in code darim b system migim oun username asli k to dari brabar ba mobail_number hast, yani name va family username asli nist, shomare mobail username asli bashe 
   REQUIRED_FIELDS = ['email','name','family']                     # ( required_fields ) baraye in ast k vaghti mikhahim ( superuser ) ra besazim in so'al ha ra azamon beporse, ( superuser, yani sakhtan account admin k khodema
   
   objects = CustomUserManager()                    # ba in code ( class CustomUserManager ) ra k bala neveshtim b in model vasl mikonim      
   
   
   def __str__(self):                               # dar marhale akhar baraye tamame modelha bayad str hatman benvisim
      return self.name+" "+self.family
   
   
   @property
   def is_staff(self):       # ba in def moshakhas mikonim kodam karbarha b panel admin dastresi dashte bashand ( masalan modir foroshgah, karmandan va ... )
      return  self.is_admin
    
#----------------------------------------------------------------

# in model baraye moshtarihaye siteman ast k az ghabl dar site sabtenam kardand va moshtari hastand 

class Customer(models.Model):
   user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)         # ( user ) yani moshtari, ( OneToOneField ) yani in user yek rabete yek b yek ba model ( CustomerUser ) dare, ( on_delete=models.CASCADE ) yani agar yek mahsol az in brand ra pak kardim baghiye zir majmoe in brand ham pak shavand
   phone_number = models.CharField(max_length=11, null=True, blank=True)            # ( null ) zamani k True bashad Database feilde hai ra k vasashon chizi neveshte nashode ra b sorate pishfarz null gharar mide ,( blank=True ) yani dar hengame sabtenam ejbari nist moshtari shomarasho vared kone, agar vared nakone accountesh sakhte mishe
   address = models.TextField(null=True, blank=True)
   
   # in 2 code pain marbot b upload kardan axs dar site hastand, baraye in kar aval miravim code asli ra dakhele file ( utils ) minevisim va bad address oun classi k daron file utils neveshtim ra inja minevisim, vali ghablesh bayad bala benvisim ( from utils import FileUpload )
   file_upload = FileUpload('images' , 'customer')         # axsha dar folder images va dar file customer zakhire mishavand k bayad berim dar folder images yek file customer besazim 
   image_name = models.ImageField(upload_to=file_upload.upload_to, verbose_name='تصویر  پروفایل', null=True, blank=True)


   def __str__(self):
      return f"{self.user}"



### bad az in k in code ha ra benvisim miravim dakhele setting pain minevisim ( AUTH_USER_MODEL = 'accounts.CustomUser' ) dakhele setting tozih dadam k chera bayad in code ra benvisim
### va bad bayad beravim dakhele file ( forms.py ) form haye marbot b in model ra benvisim 
