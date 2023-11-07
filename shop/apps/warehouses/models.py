# app ( warehouses ) baraye anbardari ast, yani anbare sitemon ast k ch ajnasi vared anbar mishe va ch ajnasi kharej mishe ya bebinim az yek kala chandta darim
# baraye anbar site ma b 2 model ehtiyaj darim, yeki ( WarehouseType ) yani noe anbar masalan ( kharid, forosh, marjoee kala, amanat dadan, amanat gereftan, kharab bodan kala )
# yek modele digar darim b nam ( Warehouse ) k modele aslimon ast yani anbar

#----------------------------------------------------------------

from django.db import models
from apps.products.models import Product
from apps.accounts.models import CustomUser

#----------------------------------------------------------------

# modele ( WarehouseType ) yani noe anbar masalan ( kharid, forosh, marjoee kala, amanat dadan, amanat gereftan, kharab bodan kala )

class WarehouseType(models.Model):
   warehouse_type_title = models.CharField(max_length=50, verbose_name='نوع انبار')
   
   def __str__(self):
      return self.warehouse_type_title
   
   class Meta:
      verbose_name = 'نوع انبار'
      verbose_name_plural = 'انواع روش انبار'
      
#----------------------------------------------------------------

#( Warehouse ) modele aslimon ast yani anbar k mire migarde kalaha va Va CustomeUser yani id moshtariharo paida mikone az dakhele Database 

class Warehouse(models.Model):
   warehouse_type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE, related_name='Warehouses', verbose_name='انبار')     # in ra b sorate ( ForeignKey ) neveshtim yani in ra b class bala ( WarehouseType ) vasl kardim k bebinim ayan kharide? aya foroshe? va ...
   user_registered = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='warehouseuser_registered', verbose_name='کد مشتری')      # in code ra minevisim k yani in amaliyate anbar tavasote ch useri dare anjam mishe? ch useri dare kalaro b anbar azafe mikone? ch useri dare kalaro az anbar kharej mikone? user_registered ya modir site ast ya moshtari ast chon modirha dakhele panel admin kala ra b anbar azafe mikonand moshtariha az anbar kharej mikonand 
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='warehouse_products', verbose_name='کالا')                # in yani ch kalai dare b anbar ezafe mishe ya kharej mishe, vaghti inja baraye yek model foreignkey minevisim va bad vasash related_name minevisim b in mani ast k bayad esmi k jelo related_name yani ( 'warehouse_products' ) neveshtim ra b modele folder Products ezafe shavad
   qty = models.IntegerField(verbose_name='تعداد')        # in baraye tedad kala ast, masalan pirahan 8 ta kharej shod
   price = models.IntegerField(verbose_name='قیمت واحد', null=True, blank=True)        # in baraye ghaimate kala ast
   register_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سبت')      # in baraye tarikhe sabte kala daron anbar ast
   
   def __str__(self):
      return f"{self.warehouse_type} - {self.product}"
   
   
   class Meta:
      verbose_name = 'نوع انبار'
      verbose_name_plural = 'انبارها'
   
   