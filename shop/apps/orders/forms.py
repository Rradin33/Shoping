from django import forms
from .models import PaymentType

#----------------------------------------------------------------

# inja mikhahim yek form besazim baraye factor kharid moshtari k in etela'at ra dashte bashad
# ( nam, nam khanevadegi, email, telephone, address, tozihat, noe model pardakht(yani moshtari online pardakhr mikone ya b sorate naghdi vaghti kala ra gereft) )

class OrderForm(forms.Form):               #( OrderForm ) yani form sefaresh 
   name = forms.CharField(label="",
                        	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
   								error_messages = {'required':'این فیلد نمیتواند خالی باشد'}),
   
   family = forms.ChoiceField(label="",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
   								error_messages = {'required':'این فیلد نمیتواند خالی باشد'}),
   
   email = forms.ChoiceField(label="",
                           widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل '}),
   								required=False)    # ( required=False ) yani telephone ejbari nist k hatman roye factor bashe
   
   phone_number = forms.ChoiceField(label="",
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'تلفن'}),
									required=False)    # ( required=False ) yani telephone ejbari nist k hatman roye factor bashe
   
   address = forms.ChoiceField(label="",
                           widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ادرس', 'rows':'2'}),    # ( 'rows':'2' ) ba in code jadval address dakhele site kochektar mishavad, masalan agar bedim 4 bozorgtar mishavad
   								error_messages = {'required':'این فیلد نمیتواند خالی باشد'}),
   
   description = forms.ChoiceField(label="",
                           widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات', 'rows':'4'}), 
   								required=False)    # ( required=False ) yani telephone ejbari nist k hatman roye factor bashe
   
   payment_type = forms.ChoiceField(label="",
                           choices=[(item.pk, item) for item in PaymentType.objects.all()],       # baraye inke betonim form PaymentType ro benvisim bayad in ro az models.py seda bezanim, baraye in kar bayad ketabkhane in class ra bala benvisim ( from .models import PaymentType )
                           widget=forms.RadioSelect())
   

