### dar inja mikhahim formhaye marbot b panel admin ra besazim, yani b modelhai k dar file ( models.py ) neveshtim form bedahim, form dadan yani cadrhai b bayad etela'at moshtari ra vared konim sakhte mishavad masalan jelo name yek cadr mostatil shekl baz mishavad k esm moshtari ra dakhele oun cadr mitavanim benvisim
### 2 jor form mikhaim besazim, yeki form sakht ya darj moshtari hast va yeki form taghir moshtari


from django import forms 
from django.forms import ModelForm               # ba in ketabkhane az hame jor formi mitavanim estefade konim
from .models import CustomUser                    # ( CustomUser ) modeli k mikhahim behesh form bedahim ra inja minevisim
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#----------------------------------------------------------------

class UserCreationForm(forms.ModelForm):          # in class marbot b form sakht moshtari ast k marbot b dakhel panel admin ast
   
	password1 = forms.CharField(label="password", widget=forms.PasswordInput)      # password ra pain daron ( fields ) neminevisim, inja b in sorat minevisim ta system betavanad password va Repassword k moshtari vared mikonad ra ba ham moghayese konad va yek label joda baraye password misazad, va bad baraye inke system 2 ta password ra ba ham moghayese bayad pain yek def ( def clean_password2 ) benvisim
	password2 = forms.CharField(label="Repassword", widget=forms.PasswordInput)
   
	class Meta:                                    # harmoghe az ketabkhane ( ModelForm ) estefade mikonim inja bayad az ( class Meta ) estefade konim
		model = CustomUser                          # inja behesh migim k mikhahim b model ( CustomUser ) k dar file models.py neveshtim form bedahim
		fields = ['mobile_number', 'email', 'name', 'family', 'gender']          # ( feilds ) yani etela'ati k mikhahim az moshtari begirim ra inja minevisim, inha hamamn etela'ati hastand k dar model (CustomUser) neveshtim, harkodam ra k bekhahim mitavanim b delkhah inja benvisim

	
	def clean_password2(self):                          # ba in def system mitavanad tashkhis dahad k aya pass2 yani Repassword ba pass1 yeki hastand ya na, in def baraye control dashtan roye passwordha ast
		pass1 = self.cleaned_data['password1']
		pass2 = self.cleaned_data['password2']
		if pass1 and pass2 and pass1 != pass2:           # in code yani, agar pass1 vojod dasht pass2 ham vojod dashht va pass1 namosavi ba pass2 bod partesh kon biron, Error bede
			raise ValidationError('رمز عبور و تکرار ان با هم مغایرت دارند')           # yani agar passwordha yeki nabod error bede va in matn ra benvis, ghablesh bayad bala in ketabkhane ra ezafe konim ( from django.core.exceptions import ValidationError )
		return pass2                                                                # dar akhar agar dorost bod anha ra ghabol mikonad


	def save(self, commit=True):                         # def save ra minevisim k tamam etela'at save shavand, ( commit=True ) commit zamani etefagh miyofte k ma motman mishim k zakhire mikhad etefagh biyofte
		user = super().save(commit=False)                 # ba in code behesh migim etela'at moshtari k vared karde ast ra az hamon ebteda save nakon
		user.set_password(self.cleaned_data['password1'])         # yani aval password aval ra ( hash ) kon bad save kon, ( hash ) yani password ro gheib kon yani b sorate dayerei dar biyar
		if commit:                                                # yani bad az inke password ( hash ) kardi agar commit shod yani passwordha ba ham barabar bodand tamame etela'ate moshtari ra save kon 
			user.save()
		return user

#----------------------------------------------------------------

class UserChangeForm(forms.ModelForm):             # in class marbot b form taghir etela'at moshtari ast baraye zamani k bekhahim etela'at pain ra edit konim va marbot b panel admin ast 
   
   pessword = ReadOnlyPasswordHashField           # password ro bayad inja ham benvisim ta betavanad ( hash ) shavad yani namayesh dade nashavad, in code baes mishe k password dakhele safhe ( ChangForm ) b sorate ( ReadOnly ) bashe va agar moshtari bekhad ino edit kone bayad roye dokmei click kone, baraye in code bayad ketabkhane in ra bala benvisim ( from django.contrib.auth.forms import ReadOnlyPasswordHashField )
   class Meta:
      model = CustomUser
      fields = ['mobile_number', 'password', 'email', 'name', 'family', 'gender', 'is_active', 'is_admin']            # yani vaghti mikham etela4at moshtari ra Edit konam betavanam in Etela'at ra edit konam, yani in etela'at moshtari ra betavanim b dast khodeman control konim

   
### bad az inke in formha ra neveshtim hanoz in formha dar panel admin ezafe nashodand va panel admin khali ast
### baraye inke formha dar panel admin vared shavand va sakhte shavand bad az inke inja codhaye form ra neveshtim bayad beravim dakhele file ( admin.py ) va modelha va formhai k neveshtim ra anja ezafe konim va codhashon ro benvisim

#----------------------------------------------------------------

# in class pain marbot b vorod karbar dar site ma ast, yani moshtari vared site ma mishe dar ghesmate ( حساب کاربری ) vaghti dokme ( ورود ) ra bezanad etela'at pain ra azash mikhahim, ma in form ra ba haman class ( CustomUser ) anjam midahim

class RegisterUserForm(ModelForm):
	password1 = forms.CharField(label="رمزعبور", widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'رمزعبور را وارد کنید'},))       # password ra pain daron ( fields ) neminevisim, inja b in sorat minevisim ta system betavanad password va Repassword k moshtari vared mikonad ra ba ham moghayese konad va yek label joda baraye password misazad, va bad baraye inke system 2 ta password ra ba ham moghayese bayad pain yek def ( def clean_password2 ) benvisim, ( widget ) ba widget mitavanim oun tike codi k dar file ( register.html ) ra neveshtim biyavarim inja ta zahere site hamantor k khastim taghir konad
	password2 = forms.CharField(label="تکرار رمزعبور", widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'تکرار رمزعبور را وارد کنید'},))
	class Meta:
		model = CustomUser
		fields = ['mobile_number']
		Widget = {                                       # ( widget ) ba widget mitavanim oun tike codi k dar file ( register.html ) ra neveshtim biyavarim inja ta zahere site hamantor k khastim taghir konad
			'mobile_number': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'موبایل را وارد کنید'},)        # in codi k dar ( regoster.html ) marbot b ( mobile ) ast ra inja b sorate ( widget ) minevisim k marbot b safhe register site ast k karbar mitavanad dar an safhe sabtenam konad ( <input type="text" class="form-control" placeholder="موبایل را وارد کنید"> ) , class va placeholder ra bayad inja baraye widget benvisim ta zahere in safhe site taghir konad
		}
    
	def clean_password2(self):                          # ba in def system mitavanad tashkhis dahad k aya pass2 yani Repassword ba pass1 yeki hastand ya na, in def baraye control dashtan roye passwordha ast
		pass1 = self.cleaned_data['password1']
		pass2 = self.cleaned_data['password2']
		if pass1 and pass2 and pass1 != pass2:           # in code yani, agar pass1 vojod dasht pass2 ham vojod dashht va pass1 namosavi ba pass2 bod partesh kon biron, Error bede
			raise ValidationError('رمز عبور و تکرار ان با هم مغایرت دارند')           # yani agar passwordha yeki nabod error bede va in matn ra benvis, ghablesh bayad bala in ketabkhane ra ezafe konim ( from django.core.exceptions import ValidationError )
		return pass2

# bad az inke form ghesmate vorod site ra neveshtim, bad bayad beravim dakhele file ( views.py ) va code marbot b in form ra benvisim ta ghesmate ( vorod ) site sakhte shavad, agar code marbot b in form ra dar views.py nanvisim vaghti dar site dokme vorod ra mizanim error midahad 

#------------------------------------------------------------------

class VerifyRegisterForm(forms.Form):                         # in form marbot b safhe verify ya check kardan code fa'al sazi ast k address in form ra bayad dakhele class ( VerifyRegisterCodeView) benvisim
   active_code = forms.CharField(label="",
                                 error_messages={"required":"این فیلد نمیتواند خالی باشد"},
                                 widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'کد دریافتی را وارد کنید'},) 
                                 )
   
   
#----------------------------------------------------------------

# in form marbot b safhe vorod site ast yani( Login ), bad az inke moshtari dar site sabtenam mikonad harmoghe mikhahad vared site shavad bayad biyad ghesmate login va shomare mobile o password ra bezanad ta betavanad vared site shavad, ma alan mikhahim form safhe login ra benvisim va zaherash ra besazim

class LoginUserForm(forms.Form):
   mobile_number = forms.CharField(label="شماره موبایل",
                                 error_messages={"required":"این فیلد نمیتواند خالی باشد"},
                                 widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'موبایل را وارد کنید'},) 
                                 )
   
   
   password = forms.CharField(label="رمز عبور",
                                 error_messages={"required":"این فیلد نمیتواند خالی باشد"},
                                 widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'رمزعبور را وارد کنید'},) 
                                 )

# bad az inke form ra sakhtim miravim dakhele ( views.py ) va get va post in ra minevisim va bad ham URL ra minevisim

#----------------------------------------------------------------

# in class marbot b zamani ast k moshtari passwordash ra faramosh mikonad, ma inja yek form misazim k vaghti moshtari dokme faramoshi ramz obor ra zad bad betavanad yek password jadid baraye khodash besazad
# b vasite codhaye pain 2 cadr password ba tekrar password dar site sakhte mishavad va moshtari mitavanad password jadid besazad
class ChangePasswordForm(forms.Form):
   password1 = forms.CharField(label="رمز عبور",
                                 error_messages={"required":"این فیلد نمیتواند خالی باشد"},
                                 widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'رمزعبور را وارد کنید'},) 
                                 )
   password2 = forms.CharField(label="رمز عبور",
                                 error_messages={"required":"این فیلد نمیتواند خالی باشد"},
                                 widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'تکرار رمزعبور را وارد کنید '},) 
                                 )

   
   def clean_password2(self):                          # ba in def system mitavanad tashkhis dahad k aya pass2 yani Repassword ba pass1 yeki hastand ya na, in def baraye control dashtan roye passwordha ast
      pass1 = self.cleaned_data['password1']
      pass2 = self.cleaned_data['password2']
      if pass1 and pass2 and pass1 != pass2:           # in code yani, agar pass1 vojod dasht pass2 ham vojod dashht va pass1 namosavi ba pass2 bod partesh kon biron, Error bede
         raise ValidationError('رمز عبور و تکرار ان با هم مغایرت دارند')           # yani agar passwordha yeki nabod error bede va in matn ra benvis, ghablesh bayad bala in ketabkhane ra ezafe konim ( from django.core.exceptions import ValidationError )
      return pass2
   
# bad az inke form ra neveshtim miravim view in form ra ham minevisim

#----------------------------------------------------------------

# in form baraye dokme ( faramoshi ramz obor ) ast
# alan mikhahim yek form besazim k vaghti karbar passwordash ra faramosh kard vaghti roye dokme ( faramoshi ramz obor ) zad in safhe vasash baz beshe ta betone shomare mobailesho vared kone ta yek code baraye oun ersal beshe

class RememberPasswordForm(forms.Form):
   mobile_number = forms.CharField(label="شماره موبایل",
                                 error_messages={"required":"این فیلد نمیتواند خالی باشد"},
                                 widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'موبایل را وارد کنید'},), 
                                 )
   

#----------------------------------------------------------------

# in form marbot b safhe ( virayeshe profile ) tavasote moshtari ast k ma baraye oun yek form misazim ta betavanad etela'atash ra daron site taghir dahad mesl  ( name, familt, email, phone_number va ... ) 

class UpdateProfileForm(forms.Form):
   mobile_number = forms.CharField(label="",
                                   widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره موبایل را وارد کنید', 'readonly':'readonly'})      # ( readonly ) baes mishavad k moshtari natavanad shomare mobilash ra taghir bedahad va faghat betone oun ro bekhone, pas harmoghe khastim k karbar natavanad chizi ra taghir dahad dakhele form jelo oun mozo readonly ro minevisim
                                   )
   
   name = forms.CharField(label="",
                                   error_messages = {'required':'این فیلد نمیتواند خالی باشد'},
                                   widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':' نام خود را وارد کنید'})
                                   )
   
   family = forms.CharField(label="",
                                   error_messages = {'required':'این فیلد نمیتواند خالی باشد'},
                                   widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':' نام خانوادگی خود را وارد کنید'})
                                   )
   
   email = forms.EmailField(label="",
                                   error_messages = {'required':'این فیلد نمیتواند خالی باشد'},
                                   widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':' ایمیل خود را وارد کنید'})
                                   )
   
   phone_number = forms.CharField(label="",
                                   error_messages = {'required':'این فیلد نمیتواند خالی باشد'},
                                   widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':' تلفن را وارد کنید'})
                                   )
   
   address = forms.CharField(label="",
                                   error_messages = {'required':'این فیلد نمیتواند خالی باشد'},
                                   widget = forms.Textarea(attrs={'class':'form-control', 'placeholder':' ادرس خود را وارد کنید'})
                                   )
   
   image = forms.ImageField(required=False)    # vaghti migim ( required=False ) yani in filde ejbari nist, inja yani ejbari nist k hatman axs bezare
   
# bad in form ra daron safhe views.py zir class UpdateProfileView seda mizanim ta in form royz safhe site sakhte shavad


