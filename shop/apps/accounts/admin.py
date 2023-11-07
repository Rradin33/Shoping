### ( admin.py ) dar in file codhai k dar file ( models.py ) va ( forms.py ) neveshtim ra inja seda mizanim ta panel admin ma sakhte shavad va form an ya haman tarahi an ham sakhte shavad

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser, Customer

#----------------------------------------------------------------

class CustomUserAdmin(UserAdmin):             # ( UserAdmin ) b vasile UserAdmin panel admin ma sakhte mishavad, darvaghe UserAdmin, user asli panel admin ma ast 
	
	form = UserChangeForm                      # in code yani mikhai formet chi bashe? ma ( UserChangeForm ) entekhab mikonim 
	add_form = UserCreationForm                # in code yani mikhai add_form chi bashe? ma ( UserCreationForm ) entekhab mikonim, ghablesh bayad ketabkhane in 2ta ra benevisim ( from .forms import UserChangeForm, UserCreationForm )
   
	list_display = ('mobile_number', 'email', 'name', 'family', 'gender', 'is_active', 'is_admin')          # ( list_display ) yani vaghti safhe userharo neshon mide mikhai list sar sotonhamon chi bashe?
	list_filter = ('is_active', 'is_admin', 'family')                          # ( list_filter ) yani mitavanim ba filter kardan moshtariha ra paida konim, yani masalan man filter mikonam roye ( is_active ) va bad tamam moshtarihai k dar site man fa'al hastand ra neshan midahad

	fieldsets = (                                                   # ( fieldsets ) marbot mishe b ( form = UserChangeForm ) k bala neveshtim, yani vaghti raftim dakhele panel yek moshtari k etela'atash ra bebinim bayad tanzimatesh injori bashe k daron ( fieldsets ) neveshtim va mitavanim anha ra taghir dahim va etela'at ghabele Change ast
		(None, {'fields':('mobile_number', 'password')}),            # ( None ) yani barchasb nadashte bashe
		('personal info',{'fields':('email', 'name', 'family', 'gender', 'active_code')}),
		('Permissions',{'fields':('is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}),             # ( is_superuser ) vaghti in ra minevisim dar panel admin dar ghesmate permissions yek gozine dorost mishavad b nam ( superuser status ) k vaghti admin asli bere va baraye yek nafar dg tike in gozinaro bezanad oun nafar ham admin goroh mishavad va b kole panel admin dastresi paida mikonad, ba'es mishavad k vaghti khode admin asli k super user ast vaghti vared panel admin mishavad betavand yek nafar digar ham superuser ya admin asli konad, ( 'groups', 'user_permissions' ) baraye in hastand k shayad admin gouroh nakhast kase digari ra admin konad vali bekhad yek seri ekhtiyarat b yek nafar bedahad mesl add kardan kasi, ya change kardan etela'at ya delete kardan, bad oun fard admin nist vali mitavanad vared panel admin shavad va in karha ra anjam dahad, baraye in mored pain ham bayad benvisim ( filter_horizontal = ('groups', 'user_permissions') )
	)
	
	add_fieldsets = (                                               # ( add_fildesets ) marbot mishe b ( add_form = UserCreationForm ) k bala neveshtim, yani vaghti raftim dar ghesmat add k yek moshtari ra add konim va etela'atash ra vared konim, tanzimatesh injori bashe k daron ( add_fieldsets ) neveshtim, yani zamani k mikhahim add konim in etela'at ra az ma bekhahad
			(None, {'fields':('mobile_number', 'email', 'name', 'family', 'gender', 'password1', 'password2')}),
		)
 
	search_fields = ('mobile_number',)            # ( search_fields ) ba in code yek cadr sakhte mishavad k ma mitavanim ba vared kardan shomare mobile moshtari oun ra search konim
	ordering = ('mobile_number',)                 # ( ordering ) yani moratab sazi, yani moshtariha bar asas shomare mobaileshon dar jadval moratab shavand
	filter_horizontal = ('groups', 'user_permissions')        # groups va user_permissions ra aval bala dakhele ( permissions ) minevisim bad inja, inha baes mishavand k vaghti varede panel admin mishavim vaghti miravim dakhele etela'at yek custom user mishavim dar ghesmate permissions 2ta cadr jadval bozorg sakhte mishavand k mitavanim yek seri etela,ar az cadr user permissions b anha vared konim va dar ghesmate gourops ba filter kardan mitavanim goroh besazim va har goroh ch vizhegi dashte bashand mesl add kardan, delete kardan, change kardan va ...
 

admin.site.register(CustomUser,CustomUserAdmin)               # in code ra bayad dar akhar benvisim k tamam etela'ati k neveshti register shavand va panel admin sakhte shavad, in code yani model CustomUser mano b vasile user CustomUserAdmin register kon

#----------------------------------------------------------------

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
   list_display = ['user', 'phone_number']
   
   