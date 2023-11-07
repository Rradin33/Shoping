### ( accounts ) baraye moshtariha ast k betavanand account khodeshon ro dar site ma besazand
### yani yek seri etela'at az khodeshon ro vared mikonan bad accounteshon sakhte mishe, mesl ( nam, nam khanevadegi, email, ramz obour, jensiyat va ... )
### baraye in kar aval bayad dakhele models.py modelash ra besazim ta in etela'at betavanand dar Database save shavand


from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterUserForm, VerifyRegisterForm, LoginUserForm, ChangePasswordForm, RememberPasswordForm
import utils
from .models import CustomUser, Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from apps.orders.models import Order
from django.contrib.auth.decorators import login_required
from apps.accounts.forms import UpdateProfileForm

#----------------------------------------------------------------

# in class marbot b ( class RegisterUserForm ) dar file ( forms.py ) ast,  yani moshtari vared site ma mishe dar ghesmate ( حساب کاربری ) vaghti dokme ( ورود ) ra mizanad marbot b in class ast, baraye neveshtan in class ham aval bayad daron file forms.py formesh ro benevisim bad biyaim daron views.py codhaye marbot b oun form ra benvisim  

class RegisterUserView(View):  
   template_name = "accounts_app/register.html"             # inja ham address file html ra behesh midahim
   
   def dispatch(self, request, *args, **kwargs):               # ( dispatch ) baraye in ast k shoma dakhele har safhe site k hastid vaghti hamon moghe az tarighe yek google dg varede siteton mishid shomaro vared safhe asli site kone va dige ehtiyaji nist az aval login beshid
      if request.user.is_authenticated:
         return redirect('main:index')
      return super().dispatch(request, *args, **kwargs)
   
   def get(self, request, *args, **kwargs):
      form = RegisterUserForm()                        # inja oun formi k sakhtim ra seda mizanim k b ham vast beshan, vali ghablesh bayd bala benvisim ( from .forms import RegisterUserForm )
      
      return render(request, self.template_name, {"form":form})          # dar akhar behesh migim boro dakhele folder ( accounts_app ) bad dakhele file ( register.html ) va tarahi ghesmate vorod site ra ejra kon, ( {"form":form} ) dar akhar form ra injori b sorate context akhare render minevisim
    
    
   def post(self, request, *args, **kwargs):
      form = RegisterUserForm(request.POST)        # yani in formi k avordi request bede va darkhasti k post shode ro begir
      if form.is_valid():                          # yani agar form dorost bod
         data = form.cleaned_data                  # yani bad form clean shode ro begir beriz dakhele zarfi b nam ( data )
         
         active_code = utils.create_random_code(5)        # in ra minevisim k hengam sabtenam yek code bere baraye moshtari ta check beshe va hesabesh sakhte beshe, baraye in car yek fole b name ( utils.py ) misazim va code marbot b ( active_code ) ra ounja minevisim, bad esm classi k dar file ( utils ) neveshtim ra inja behesh midahim, ( 5 ) in ham yani adadi k b sorate random mikhai besazi 5 raghami bashe, va darakhar baraye inke file utils.py ro b in views vasl konim bala bayad benvisim ( import utils )
         
         CustomUser.objects.create_user(                  # ba in code etela'ate moshtari k sabtenam mikone dar Database zakhire mishe, va baraye inke az model CustomUser estefade kardim bala minevisim ( from .models import CustomUser )
            mobile_number = ['mobile_number'],
            active_code = active_code,
            password = data['password1']
         )
         
         utils.send_sms(data['mobile_number'], f'کد فعال سازی حساب کاربری شما {active_code} میباشد')      # in code baraye ersal sms ast, codehaye ersal sms ra dar file ( utils.py ) minevisim va adressash ra inja midahim, bad az inke code fa'al sazi ersal shod ma nabayad bargardim b safhe asli site, bayad beravim dakhele yek safhe digar k in code ro verifie kone ( check kone ) pas bayad oun safhe ro pain dar class ( VerifyRegisterCodeView ) benevisim va besazim, bad az inke karbar sabtenam kard va vasash code fa'al sazish ersal shod yek fazaye ( session ) misazim k code fa'al sazish va shomare mobilesho tu hafeze khodesh negah dare, in fazaye session ro pain sakhtim
         
         request.session['user_session'] = {                     # ( session ) yek fazaye az hafeze server ast k b ezaye har karbar yeki az ouna sakhte mishe va ma mitonim tosh etela'at zakhire konim, k lahze sabtenam in 2 mored paim ro barmidarim
            'active_code': str(active_code),
            'mobile_number': data['mobile_number'],
            'remember_password': False                           # in baraye zamani ast k moshtari passwordash ra faramosh mokonad k inja an ra False migozarim
         }
         
         messages.success(request, 'اطلاعات شما ثبت شد و کد فعال‌سازی را وارد کنید', 'success')     # in code ra minevisim ta message baraye moshtari ersal shavad va baraye oun yek payam beravad, vali ghablesh bayad ketabkhane message ra bala benvisim ( from django.contrib import messages )
         return redirect('accounts:verify')           # bad ham ba in code moshtari ra vaghti k sabtenamash tamam shod mibarim b in safe ta code fa'al sazi k barash ersal shode va oun vared karde check beshe ya verify beshe.
         
      messages.error(request, 'خطا در هنگام ثبت نام', 'danger')         # bad ham in code ra minevisim k agar dar hengame sabte nam etela'atash ra eshtebah sabt, error bedahad va in payam vasash bere

# dar akhar baraye inke in messageha bar roye safhe site namayesh dade beshe bayad beravim darom folder ( partials ) yek file besazim b name ( messages.html ) va dakhele oun codhaye marbot b sakhtan message ra benvisim va bad address in file ra bayad daron ( main_template.html ) benvisim, chon ( main_template.html ) in safhe safheye asli site hast va vaghti mikhahim yek seri chizha hamishe roye tamame safhehaye site bashanad bayad addreseshan ra ounja benvisim
         
#----------------------------------------------------------------     
   
# in class marbot b verify ya check kardan kode fa'al sazi ast, yani vaghti codee fa'al sazi baraye moshtari ersal mishavad bad moshtari vared in safhe mishavad ta code fa'al sazish check shavad, in safhe verify chon yek safhe joda ast bayad yek form dashte bashad pas miravim dakhele file forms.py va form oun ra minevisim
    
class VerifyRegisterCodeView(View):                               
   template_name = "accounts_app/verify_register_code.html"             # inja ham address file html ra behesh midahim 
   
   def dispatch(self, request, *args, **kwargs):               # ( dispatch ) baraye in ast k shoma dakhele har safhe site k hastid vaghti hamon moghe az tarighe yek google dg varede siteton mishid shomaro vared safhe asli site kone va dige ehtiyaji nist az aval login beshid
      if request.user.is_authenticated:
         return redirect('main:index')
      return super().dispatch(request, *args, **kwargs)
   
   def get(self, request, *args, **kwargs):
      form = VerifyRegisterForm()                     # yani in safhe formesh ( VerifyRegisterForm ) bashe
      
      return render(request, self.template_name , {'form': form})          # va dar akhar bayad safhe html in ra besazim va dressash ra inje benvisim
      
   
   
   def post(self, request, *args, **kwargs):            # in def marbot b in ast k system betavanad code fa'al sazi k baraye moshtari ersal shode va moshtari vared karde ra baresi konad, k agar code dorost bod yek kari kon agaram eshtebah bod yek kar digar kon
      form = VerifyRegisterForm(request.POST)
      if form.is_valid():
         data = form.cleaned_data                                  # yani agar code dorost bod kole etela'at clean shode yani moratab shode ra bardar
         user_session = request.session['user_session']            # moghei k karbar code fa'al sazi ra vared mikonad va code ra baraye ma barmigardone bayad oun session ro k bala neveshtim azash begirim yani ( active_code va mobile_number )
         if data['active_code'] == user_session['active_code']:    # yani agar code k dar database save shode ba code k moshtari vared karde va dar session save shode yeki bod, bad bayad berim useremon ro yani karbar ro az dakhele databse paida konim
            user = CustomUser.objects.get(mobile_number=user_session['mobile_number'])            # ba in code useremon ro yani karbar ro az dakhele databse paida konim, yani boro dakhele mohavate ( user_session ) va karbar ro az tarighe shomare mobilesh shenasai kon bad ounCustomUser ro ba tamam etela'atesh beriz dakhele yek zarf b name ( user )
            if user_session['remember_password']==False:            # ma 2 jor mitonim codehai k baraye moshtari mifrestim ra verify konim, yekbar zaman sabtenam baraye moshtari code ersal mikonim va yekbar zamani k moshtari passwordesho faramosh mikone va mikhad yek password jadid besaze, in code b ma mige ( ['remember_password']==False ) yani remember_password mosavi ba False bod moshtari az tarighe sabtenam vared shode va code verify baraye oun ersal mishe pas karhaye zir ra anjam bede
               user.is_active = True                                  # yani user ya moshtari k dakhele database paida kardim is_acvite beshe yani fa'al beshe
               user.active_code = utils.create_random_code(5)         # vaghti baraye moshtari code fa'al sazi ersal mishe code dakhele goshish save mishe, ma in code ra yek bar digar inja ham minevisim k vaghti code baraye moshtari ersal shod badesh oun code taghir konad va moshtari digar natavanad az yek code 2bar estefade konad
               user.save()                                            # va bad ham save beshe
               messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')      # va bad ham in payam vasash bere   
               return redirect('main:index')                          # va dar akhar baresh migardonim b safhe asli
            else:
               return redirect('accounts:change_password')            # yani agar moshtari passwordash ra faramosh kard va roye dokme ( faramoshi ramz obor ) click kard bad az inke shomare mobilesh ro vared kard va code baraye oun ersal shod va code ro vared kard bad bebaresh dakhele safhe ( change_password ) ta betone password jadid besaze, ( change_password ) address in safhe ra az dakhele URL change_password inja minevisim ta in safhe ra baraye moshtari baz konad
               
         else:
            messages.error(request, 'کد فعال سازی شما اشتباه میباشد', 'danger')                  # agar ham code fa'al sazish ro eshtebah vared kard in code ra minevisim ta in payam vasash beravad
            return render(request, self.template_name, {'form': form})       # bad ham toye hamon safhe verify negahesh midarim
         
# bad az in codha miravim dakhele folder ( partials ) va file ( header ) va oun ghesmat az code k marbor b safhe sabtenam ast ra y kam taghir midahim ta vaghti dakhele site roye dokme sabtenam mizanim safhe avaz shavad va safhe sabtenam baz shavad, code injori miishavad ( <li><a href="{% url 'accounts:register' %}">ثبت نام</a></li> )      

#----------------------------------------------------------------

# in class baraye rah andakhtan ghesmate vorod(login) site ast k vaghti moshtari k ghablan sabtenam karde harmoghe bekhad login shavad bere dakhele in safhe shomare mobile va password ra vared shavad va varede site shavad, ghabl az inke in class ra benvisim, formesh ro dakhele Forms.py neveshtim 

class LoginUserView(View):         
   template_name = "accounts_app/login.html"
   
   def dispatch(self, request, *args, **kwargs):               # ( dispatch ) baraye in ast k shoma dakhele har safhe site k hastid vaghti hamon moghe az tarighe yek google dg varede siteton mishid shomaro vared safhe asli site kone va dige ehtiyaji nist az aval login beshid
      if request.user.is_authenticated:
         return redirect('main:index')
      return super().dispatch(request, *args, **kwargs)  
   
   def get(self, request, *args, **kwargs):
      form = LoginUserForm()           
      
      return render(request, self.template_name , {'form': form})   
   
   
   def post(self, request, *args, **kwargs):
      form = LoginUserForm(request.POST)
      if form.is_valid():
         data = form.cleaned_data
         user = authenticate(username=data['mobile_number'], password=data['password'])       # yani b vasile ( authenticate ) y mojavez baraye moshtari k dare vare site mishe dorost kon, ( username=data['mobile_number'] ) bad mige y username mikham k behesh migim boro az dakhele data ( mobile_number ) ro bardar, () password=data['password'] ) bad mige password ham mikham k migim boro az data ( password ) ro bardar, bad az inke inharo paida kard yek ( user ) dorost mishe k ma user ra avale code minevisim
         if user is not None:                                                             # yani in user ro agar paida kardi y raftar kon agar paida nakardi y raftar dg kon
            db_user = CustomUser.objects.get(mobile_number=data['mobile_number'])         # ( db_user ) useri ast k daron Database save shode ast, in code ra minevisim k moshakhas beshe moshtari is_active hast ya na 
            messages.success(request, 'ورود با موفقیت انجام شد')
            login(request, user)                                # ba in code sader mikonim k karbar betavanad varede site shavad, vali bayad bala ketabkhane ( login ) ra benvisim ( from django.contrib.auth import authenticate,login,logout )
            next_url = request.GET.get('next')                  # ( next ) adress safhei hast k azash oumadim vared login shodim, inja adress oun safhe ra migirim va zakhire mikonim va mirizim dakhele zarfi b name ( next_url ), baraye in ast k masalan moshtari rafte aval mahsolat ra search karde bad az safhe yeki az mahsolha varede login mishe bad ma b komake ( next ) adress safhe oun mahsol ra save mikonim k vaghti moshtari loginesho anjam dad bargarde b hamon safhe mahsoli k dasht negah mikard 
            if next_url is not None:                            # yani agar ( next_url ) khali nabod(ba yek adress por shode bod) b mani in ast k moshtari az yek sahe digar varede login shode
               return redirect(next_url)                        # pas moshtari ra barmigardanim b safhei k azash oumade
            else:
               return redirect('main:index')                    # dar ghair in sorat bareshgardon b safhe asli site
         else:
            messages.error(request,'اطلاعات وارد شده صحیح نمیباشد', 'danger')                   # agar ham karbar kolan etela'atash ra eshtebah vared kard in payam ra midahim
            return render(request, self.template_name, {'form': form})                   # va bad ham b hamon safhei login ka azash oumade baresh migardonim
      else:
         messages.error(request,'اطلاعات وارد شده نامعتبر است', 'danger')           # agar ham karbar is_valide bod in payam ra besh neshan midahim
         return render(request, self.template_name, {'form': form})          # va dar akhar b hamon safhei login ka azash oumade baresh migardonim

#----------------------------------------------------------------

# in class marbot b ( logout ) kardan ast, yani vaghti mikhaim az site biyaim biron va dokme khoroj ra mizanim
# class logout b file html ehtiyaji nadarad

class LogoutUserView(View):
   
   def dispatch(self, request, *args, **kwargs):               # ( dispatch ) baraye in ast k shoma dakhele har safhe site k hastid vaghti hamon moghe az tarighe yek google dg varede siteton mishid shomaro vared safhe asli site kone k va dige ehtiyaji nist az aval login beshid
      if not request.user.is_authenticated:
         return redirect('main:index')
      return super().dispatch(request, *args, **kwargs)
   
   def get(self, request, *args, **kwargs):
      session_data = request.session.get('shop_cart')           # in code baraye zamani ast k moshtari tedadi kala dakhele sabade kharid darad vali alan nemikhad bekhare va az site va hesabe karbari mikhad biyad biron va logout kone, in code yani ghabl az inke hesabe karbari moshtari logout beshe, request bede b session va hame etela'ate dakhele ( shop cart ) yani sabade kharid ro berize dakhele zarf ( session_data ) k vaghti logout mikone sabade kharidesh pak nashe 
      logout(request)
      request.session['shop_cart'] = session_data               # in code yani bad az inke logout kardi dobare hame etela'at dakhele sabade kharid ro az zarfe ( session_data ) bardar va bargardon sare jashon 
      return redirect('main:index')
   
#----------------------------------------------------------------

# in class marbot b form ( ChangePasswordForm ) ast, in class b celass pain vasl ast yani zamani k moshtari passwordash ra faramosh mikonad

class ChangePasswordView(View):
   template_name = "accounts_app/change_password.html"
   def get(self, request, *args, **kwargs):
      form = ChangePasswordForm()
      return render(request, self.template_name, {"form":form})    
       
   def post(self, request, *args, **kwargs):
      form = ChangePasswordForm(request.POST)
      if form.is_valid():
         data = form.cleaned_data
         user_session = request.session['user_session']                                   # in code yani etela'ate moshtari ra az session begir, etela'at session haman etela'ati hastand k dar ( request.session ) k dar class pain neveshtim yani ( active_code , mobile_number , remember_password ), vali ma az bein in 3ta faghat mikhahim mobilr_number ra azash begirim k dar code pain minevisim
         user = CustomUser.objects.get(mobile_number=user_session['mobile_number'])       # baraye etela'ate moshtari ra az ddakhele Database paida konim aval moshtari shomare khodash vared mikonad va bad in code shoro b kar mikonad, in code yani boro dakhete Database az bein Customuser(moshtariha) begard bebin ouni k shomare mobailesh ba ba shomare k dakhele user_session zakhire shode paida kon, va bad esmesh oun moshtaro ro mizarim ( user ) k avalesh neveshtim
         user.set_password(data['password1'])                    # yani moshtari k passwordesho vared kard baraye taghir password, passwordash ra save kon va bad hash kon va bad beriz dakhele etela'ate khode user dakhele Database
         user.active_code = utils.create_random_code(5)          # va bad yek code active jadid vasash besaz
         user.save()                                             # va bad user ra save mikonim
         messages.success(request, 'رمز عبور شما با موفقیت تغییر کرد', 'success')        # va bad in payam vasash mire
         return redirect('accounts:login')                       # va dar akhar moshtari ro barmigardonim b safhe login
      else:
         messages.error(request, 'اطلاعات وارد شده معتبر نمیباشد', 'denger')        # agar ham etela'ate vared shode dorost nabod in payad ra vasash ersal mikonim
         return render(request, self.template_name, {"form":form})                   # va bad ham baz bareshmigardonim b safhe khodesh 
         
#----------------------------------------------------------------

# in view marbot b form ( RememberPasswordForm ) ast

class RememberPasswordView(View):
   template_name = "accounts_app/remember_password.html"
   
   def get(self, request, *args, **kwargs):
      form = RememberPasswordForm()
      return render(request, self.template_name, {"form":form})
   
   def post(self, request, *args, **kwargs):
      form = RememberPasswordForm(request.POST)                            # yani in formi k avordi request bede va darkhasti k post shode ro begir
      if form.is_valid():                                                  # yani agar form dorost bod
         try:                              # yani say kon karhaye pain ra vasam anam bedi
            data = form.cleaned_data                                          # yani bad form clean shode ro begir beriz dakhele zarfi b nam ( data )
            user = CustomUser.objects.get(mobile_number = data['mobile_number'])     # va bad migim doro dakhele Database az baine moshtariha paida kon ouni k shomare mobailesh barabar ba hamon shomare mobaili ast k dar site vared shode va behesh migim ( user ), ( chon moshtari baraye passwordash ra faramosh karde va shomare mobilesho daron site vared karde ta vasash yek code bere va bad az inke code ro vared kard yek safhe baz mishe va mitone password jadid besaze )
            active_code = utils.create_random_code(5)                         # bad y code 5 raghami baraye moshtari tolid mikonim k baraye moshtari befrestim
            user.active_code = active_code                                    # va bad code tolid shode ra mirizim dakhele oun user k paida karde ( yani dakhele database ) 
            user.save()                                                       # va bad user ra save mikonim
            
            utils.send_sms(data['mobile_number'], f'کد فعال سازی حساب کاربری شما {active_code} میباشد')      # in code baraye ersal sms ast, codehaye ersal sms ra dar file ( utils.py ) minevisim va adressash ra inja midahim, bad az inke code fa'al sazi ersal shod ma nabayad bargardim b safhe asli site, bayad beravim dakhele yek safhe digar k in code ro verifie kone ( check kone ) pas bayad oun safhe ro pain dar class ( VerifyRegisterCodeView ) benevisim va besazim,
            request.session['user_session'] = {                                                                 # ( session ) yek fazaye az hafeze server ast k b ezaye har karbar yeki az ouna sakhte mishe va ma mitonim tosh etela'at zakhire konim, k lahze sabtenam in 2 mored paim ro barmidarim
               'active_code': str(active_code),
               'mobile_number': data['mobile_number'],
               'remember_password': True                                     # in baraye zamani ast k moshtari passwordash ra faramosh mikonad k inja an ra True migozarim     
            }
      
            messages.success(request, 'جهت تغییر رمز عبور خود کد دریافتی را ارسال کنید', 'success')        # in code ra minevisim ta message baraye moshtari ersal shavad va baraye oun yek payam beravad, vali ghablesh bayad ketabkhane message ra bala benvisim ( from django.contrib import messages )
            return redirect('accounts:verify')                               # bad ham ba in code moshtari ra vaghti k sabtenamash tamam shod mibarim b in safe ta code fa'al sazi k barash ersal shode va oun vared karde check beshe ya verify beshe
         except:                          # yani agar natonesti karhaye bala ra anjam bedi
            messages.error(request, 'شماره موبایل وارد شده موجود نمیباشد', 'danger')        # behesh error bede va in matn ra vasash benvis                           
            return render(request, self.template_name, {"form":form})                # va dar akhar bareshgardon b safhe khodesh           


# ma mikhahim yek kari konim k zamani k dar safhe ( login ) dokme ( faramoshi ramz obor ) ra mizanim safhe faramoshi ramz obor baz shavad,
# baraye in kar bayad esm safhe URL faramoshi ramz obor ra dakhele safhe HTML login benvisim yani esm safhe url faramoshi ramz obor ( remember_password ) ast
# pas ma miravim dakhele file ( login_html ) address url safhe faramoshi ramz obor ra minevisim ( <a href="{% url 'accounts:remember_password' %}"> ) k vaghti dar safhe login dokme faramoshi ramz obor ra click mikonim safhe baz shavad

#----------------------------------------------------------------

# in class baraye ( panel karbari ) ast k balaye site baraye moshtari sakhte mishavad, vaghti moshtari vared panel karbari khodesh mishavad mitavanad kharidasho bebine, sefareshatesho bebine, profilesho bebine va...

class UserPanelView(LoginRequiredMixin, View):                # ( LoginRequiredMixin ) in baes mishavad vaghti moshtari vared site mishavad va ghabl az inke login shavad mikhahad vared panel karbari khodesh shavad vaghti dokme panel karbari ra mizanad safhe login vasash baz mishavad k aval login shavad yani aval vared hesabe karbari khodesh beshe bad vared panel karbari beshe, bayad ketabkhanasho bala benvisim ( from django.contrib.auth.mixins import LoginRequiredMixin )
   def get(self, request):
      user = request.user        # aval oun useri k login shode ast ra vasash request mifrestim yani sedash mizanim, vaghti request midim mire az dakhele Database etela'ate oun useri k login shode ro vasamon miyare
      try:   
         customer = Customer.objects.get(user=request.user)   # bad ba in code migim bebin customeri paida mikoni k ba in user yeki bashe ? customer yani kasi k az site ma hadeaghal yek bar kharid karde bashe, dar kol in code yani bebin agar oun user customer ham bod etela'ate customerisho beriz dakhele zarf ( customer )
         user_info = {              # va bad inja yek dictionery misazim k agar oun user customer bod in etela'at daron site por mishe 
            "name": user.name,
            "family": user.family,
            "email": user.email,                      # ( user.family ) yani etela'ate family ro az daron Database az ghesmate user migirim
            "phone_number": customer.phone_number,    # ( customer.phone_number ) yani etela'ate telephonesh ro az daron Database az ghesmate Customer migirim
            "address": customer.address,
            "image": customer.image
         }
      except ObjectDoesNotExist:
         user_info = {            # vali agar customer nabod faghat etela'ate userisho migirim
            "name": user.name,
            "family": user.family,
            "email": user.email,
         }
      
      return render(request, "accounts_app/userpanel.html",{"user_info": user_info})
   




# in def baes mishe k akharin sefareshat moshtari daron panel karbarish zaher shavad, yani mitone akharin kharidasho bebine
@login_required          # in yani moshtari bayad login bashad ta betavanad joziyate safhe karbarisho bebine, bayad ketabkhanash ro benvisim ( from django.contrib.auth.decorators import login_required )
def show_last_orders(request): 
   orders = Order.objects.filter(customer_id = request.user.id).order_by('-reqister_date')[:4]   # yani boro tu Database ghesmate Order filter kon yani begard donbale ouni k customer_id ish ba user.id ish yeki bashe, ( .order_by('-reqister_date') ) in yani sefareshatesho moratab kon bar asas tarikh va ( [:4] ) in yani faghat 4tasho biyar, 4ta sefareshe akharesho daron panel karbarish neshon beshe
   return render(request, "accounts_app/partials/show_last_orders.html", {"orders": orders})

#----------------------------------------------------------------

# in class baraye sakhtane yek safhe dg baraye update kardane etela'ate profil moshtari ast
# yani daron in safhe etela'ate moshtari ra behehsh midahim mesl ( name, familt, email, phone_number va ... ) va mitavanad anha ra taghir dahad va avaz konad va in ghesmate marbot mishavad b panel karbari yani vared panel karbari mishavim va yek dokme ast b nam ( virayesh profil ) roye in dokme k click konim yek safhe dg baz mishe baraye virayesh etela'at
# baraye in class az 2def Get va Post estefade mikonim, Get etela'at moshtari ra az dakhele Database vasamon miyare va Post haman etela'ati k get behemon dade ro post mikone roye safhe site yani behemon neshon mide

class UpdateProfileView(LoginRequiredMixin, View):
   def get(self, request):      # def get aval mikhaim etela'ate moshtari ra az Database begirim
     
      user = request.user       # aval oun useri k login shode ast ra vasash request mifrestim yani sedash mizanim, vaghti request midim mire az dakhele Database etela'ate oun useri k login shode ro vasamon miyare
      try:
         customer = Customer.objects.get(user=request.user)       # bad ba in code migim bebin customeri paida mikoni k ba in user yeki bashe ? customer yani kasi k az site ma hadeaghal yek bar kharid karde bashe, dar kol in code yani bebin agar oun user customer ham bod etela'ate customerisho beriz dakhele zarf ( customer )
         initial_dict = {                          # inja yek dictioneri misazim b esm ( initial_dict    har esmi k bekhaim mitonim vasash entekhab konim ) va tamame etela'ati k moshtari dar hengame sabtenam por karde ast ra in dictionery neshan midahad
            "mobile_number": user.mobile_number,
            "name": user.name,
            "family": user.family,
            "email": user.email,
            "phone_number": customer.phone_number,
            "address": customer.address
         }
      except ObjectDoesNotExist: 
         initial_dict = {                           # vali agar customer nabod faghat etela'ate userisho migirim
             "mobile_number": user.mobile_number,
            "name": user.name,
            "family": user.family,
            "email": user.email,
         }
         
         
      # ma in form ra daron safhe forms.py sakhtim va inja sedash mizanim ta daron safhe site in form sakhte shavad 
      form = UpdateProfileForm(initial=initial_dict)         # agar bekhahim yek form khali daron safhe site besazim bayad parantez jelo UpdateProfileForm ra khali begozarim vali agar bekhahim yek form besazim baraye virayeshe etela'at va bekhahim form ma ba etela'ate moshtari por shavad bayad dakhele parantez ra por konim ( initial=initial_dict )
      return render(request, "accounts_app/update_profile.html", {"form": form, "image_url":customer.image_name})     # ( "image_url":customer.image_name ) in yani agar moshtari axs gozasht axs ro ham ba khodet bebar b safhe site, baraye sakhtane form va baraye inke safhe form daron site sakhte beshe hatman bayad safhe HTML oun ro benvisim
   
         
   def post(self, request):         # def post mikhaim etela'ate moshtari ra post konim yani save konim
      form = UpdateProfileForm(request.POST, request.FILES)       # aval bayad etela'at update shode ra k moshtari taghir dade ro begirim ( request.POST   yani etela'at moshtari), va ham etela'ate file yani ( request.FILES ) mesl axsha, etela'at ra migirim va mirizim dakhele zarf form
      
      if form.is_valid():           # bad k etela'at ra gereftim check mikonim bebinim valid hast ya na 
         cd = form.cleaned_data     
         user = request.user 
         user.name = cd['name']
         user.family = cd['family']
         user.email = cd['email']
         user.save()               # va bad az oun etela'ate moshtari 3 tasho k marbot b user bod ro b sorate clean shode bardashtam va dar user save kardam 
         
         try:
            customer = Customer.objects.get(user=request.user)    # va bad baghiye etela'at ro mesl ( phone_number, address, image_name ) bayad berizim dakhele Customer vali aval bayad bebinim k aya in karbar ghablan moshtrari ma bode ast ya na yai az ghabl esmash dakhele customer ast ya na, baraye hamin in code ra minevisim k check kone
            customer.phone_number = cd['phone_number']            # va inja migim agar moshtari ma bod in 3 gozinaro vasash update ya virayesh kon 
            customer.address = cd['address']
            customer.image_name = cd['image_name']
            customer.save()                            # va bad etela'at customer ro save kon
         except ObjectDoesNotExist:                    # vali agar moshtari nabod bayad yek Customer jadid besaze va in etela'at ra vasash save kone
            Customer.objects.create(                   # ba in code Customer sakhte mishavad
                     user=request.user,                # va bad user k hamin customer hast ra seda mizanim va clesn shode etela'ate pain ra vasash vared mikonim 
                     phone_number = cd['phone_number'],
                     address = cd['address'],
                     image = cd['image']
                     )
         
         messages.success(request, 'ویرایش با موفقیت انجام شد', 'success')    # va dar akhar in payam baraye moshtari mire
         return redirect('accounts:userpanel')      # va moshtari ra barmigardone b safhe ( userpanel ) yani haman safhe asli panel moshtari
      

