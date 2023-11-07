# inja yek model misazim k marbot b sabade kharid ast
# baraye zamani ast k moshtari chand kala ra gozashte dakhele sabade kharid va mikhad ounaro bekhare

#----------------------------------------------------------------	

from django.db import models
from apps.accounts.models import Customer
from apps.products.models import Product
from django.utils import timezone
import uuid

#----------------------------------------------------------------

# yek model minevisim baraye noe parkhat poshtari, yani moshtari vaghti mikhahad az site kharid konad online pardakhr mikone ya b sorate naghdi vaghti kala ra gereft

class PaymentType(models.Model):
   payment_title = models.CharField(max_length=50, verbose_name='نوع پرداخت')
   
   def __str__(self):
      return self.payment_title
   
   class Meta:
      verbose_name = 'نوع پرداخت'
      verbose_name_plural = 'انواع روش پرداخت'

#----------------------------------------------------------------

# in class baraye vaziyate kala dar hengam ersal ast yani kala ersal shode ast baraye moshtari bad moshtari mitavanad bebinad k kala alan koja ast va kay miresad

class OrderState(models.Model):
   order_state_title = models.CharField(max_length=50, verbose_name='عنوان وضعیت سفارش')
   
   
   def __str__(self):
      return self.order_state_title
   
   
   class Meta:
      verbose_name = 'وضعیت سفارش'
      verbose_name_plural = 'انواع وضعیتهای سفارش'
# bad az inke code balara neveshtim bayad beram va code marbot b panel modiriyate(admin.py) ra ham benvisim ta admin site betavanad har lahze etela'ate vaziyate ersal kala ra taghir dahad k kala alan koja hast 

#----------------------------------------------------------------

# inja yek model b nam ( Order yani sefaresh ) misazim va dakhelesh moshakhas mikonim k in kharid marbot b kodam moshtari ast

class Order(models.Model):
   customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders", verbose_name='مشتری')          # ma ghablan yek model Customer dakhele folder accounts sakhte bodim k moshakhasat moshtarihamon ro k mikhaim azashon begirim va dakhele Database save beshe neveshte bodim, alan inja oun model Customer ro injori ba in code seda mizanim k beshe az ghabeliyathaye oun model Customer estefade konim mesl ( user, phone_number, address, image_name ),  ( on_delete=models.CASCADE ) yani agar yek mahsol az in brand ra pak kardim baghiye zir majmoe in brand ham pak shavand
   register_date = models.DateField(default=timezone.now, verbose_name="تاریخ درج سفارش")                # ( register_date ) baraye in ast k in sefaresh dar ch tarikhi sabt shode ast, baraye neveshtan register bayad bala in ketabkhane ro ezafe konim ( from django.utils import timezone )
   update_date = models.DateField(auto_now=True, verbose_name="تاریخ ویرایش سفارش")
   is_finaly = models.BooleanField(default=False, verbose_name="نهایی شده سفارش")           # ( is_finaly ) yani aya in moshtari finaly shode ya na? k ma mizani ( default=False ) yani az moshtari az ebteda finaly nashe, finaly shodan zamani etefagh miyfte k pardakht anjam shode bashe 
   order_code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, verbose_name="کد تولیدی برای سفارش")             # ( order_code ) yek code ast k b in fuctor moshtari midim va in code baraye har fuctor motefavet ast, ( unique=True ) yani hichvaght code tekrari nadaran va unique ast, ( default=uuid.uuid4 ) inja az uuid 4 estefade mikonim k bayad bala ketabkhone oun ro benvisim ( import uuid ), ( editable=False ) yano ejaze nemidim k oun code ghabele taghir bashe
   discount = models.IntegerField(blank=True, null=True, default=0, verbose_name="تخفیف روی فاکتور")                  # ( discount ) darsad takhfif roye fuctor hast, ( null ) zamani k True bashad Database feilde hai ra k vasashon chizi neveshte nashode ra b sorate pishfarz null gharar mide ,( blank=True ) yani dar hengame sabtenam ejbari nist moshtari code takhfifesho k yek adad chand raghami ast ra vared kone, agar vared nakone accountesh sakhte mishe, ( default=0 ) yani darsad takhfif az aval 0 bashad
   description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
   payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, null=True, blank=True, related_name='payment_types', verbose_name='نوع پرداخت')           # in model marbot b class bala ast baraye nahveye pardakht moshtari, ( PaymentType, on_delete=models.CASCADE, null=True, blank=True ) inja aval ( PaymentType ) class bala ra seda mizanim va bad chizhaye feilde haye dg behesh ezafe mikonim  
   order_state = models.ForeignKey(OrderState, on_delete=models.CASCADE, verbose_name='وضعیت سفارش', related_name='orders_states', null=True, blank=True)
   
   
   
   # in def ra minevisim ta dar factor Database ghaimate kole kalaye kharid shode hesab beshe, masalan yek moshtari az yek kala 5 ta kharide bad gheimate oun kala zarbedar 5 beshe va neshan dade beshe 
   def get_order_total_price(self):
      sum = 0                       # yek zarf darim b nam ( sum ) k oun ra 0 mikonim
      for item in self.orders_details1.all():      # yani baraye har item dakhele orders_details1 ( all ) yani boro hamari biyar, dar kol yani boro dakhele Database ghesmate order tamam onvanhai k dakhele orders_details1 neveshte shode ro bardar biyar mesl ( id, qty, price, order_id, product_id ), ( orders_details1 ) ro dakhele class pain jelo order neveshtim va sakhtimesh
         sum+=item.product.get_price_by_discount()*item.qty      # yani ( item.product.get_price_by_discount() ) az har kodom az item ha(item hamon jadvalhaye dakhele Database hastand) boro dakhele jadval productesh va get kon yani biyar ( price_by_discount ) yani gheimate takhfif khorde kala ro biyar, yani agar yek kala roye safhe site gheimate vagheish 20 toman bod vali ba takhfif shode bod 10 toman ba in code ghaimate takhfif khorde yani oun 10 toman ro hesab mikone va bad ( sum+ ) yani ezafe mikonim b sum k bala neveshtim
      
      delivery = 25000     # inja baraye haml o nagh monevisim, migim hazine post mishe 25000 toman
      if sum > 50000:      # agar gheimate kharid moshtari bishtar az 50000 toman bod 
         delivery = 0      # hamlonaghlesho 0 bezar yani majani beshe
         
      tax = sum*0.09       # inja baraye maliyat minevisim, yani 
      return sum+delivery+tax  # va dar akhar natije majmo factor ro vasamon barmigardone
      
         
   
   def __str__(self):
      return f"{self.customer}\t{self.id}\t{self.is_finaly}"
   
   
   class Meta:
      verbose_name = 'سفارش'
      verbose_name_plural = 'سفارشات'        # dar vaghe in baraye panel admin ast k dar ghesmate title b sorate jam neveshte mishavad, baraye sitehaye engilisi zaban ehtiyaji nist benvisim chon khode panel ye ( s ) b akharesh ezafe mikone vali baraye sitehaye farsi minevisim
   
#-----------------------------------------------------

# va bad yek model dg misazim b nam ( OrderDetail ) k yani dakhele in sefaresh ch mahsolati vojod darad k in kharidha dakhele Database save beshe ta faktore kharid moshtari rahat amade she

class OrderDetails(models.Model):
   order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders_details1', verbose_name='سفارش')
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders_details2', verbose_name='کالا')        # in code ra minevisim k kalahai k dar factor hastand ra moshakhas konim k bayad bala ketabkhane Product ra benvisim ta inja sedash bezanim ( from apps.products.models import Product ) 
   qty = models.PositiveIntegerField(default=1, verbose_name='تعداد')       # ba in code moshakhas mishe k az har kala chandta vojod darad dakhele factor
   price = models.IntegerField(verbose_name='قیمت کالا در فاکتور')       # in code baraye ghaimat kala daron fuctor ast
   
   
   def __str__(self):
      return f"{self.order}\t{self.product}\t{self.qty}\t{self.price}"





# bad amaliyate migrate rp anjam midim va dakhele Database tamame jadvalhaye in 2model sakhte mishavand
# bad mirim dakhele file ( admin.py ) in 2ta model ro ( Order, OrderDetails ) ounja ham seda mizanim codhashon ro minevisim ta jadvalhashon dakhele panel admin ham sakhte shavand


