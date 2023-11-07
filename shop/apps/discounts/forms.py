from django import forms

# --------------------------------------------

# in form baraye dokme code takhfif ast dakhele safhe sabade kharid ast k moshtari agar code takhfif darad vared konad ta az gheimate kharid kam shavad 
# in form ra minevisim ta form ya jadval code takhfif dakhele sate sakhte shavad
# baraye mesal code takhfif ma ( abcd ) ast in code baes mishavad ta bere dakhele Database bebine codi b nam ( abcd ) fa'al hast ya na va agar fa'al bod emal kone

class CouponForm(forms.Form):
   coupon_code = forms.CharField(label="",       # ( coupon_code ) baraye in minevisim chon ma b yek code takhfif ehtiyaj darim va mikhahim yek code takhfif az karbar begirim
											error_messages = {'required':'این فیلد نمیتواند خالی باشد'},
											widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'کد تخفیف'})
											)


# bad az in k in code ro neveshtim bayad berim codesh ro dakhele forlder orders va bad file views.py minevisim ta in form dakhele sitemon ejra beshe
# dakhele orders va bad file views.py minevisim chon code view marbot b safhe sabade kharid ra ounja neveshtim b esm ( class CheckOutOrderView ) va zire hamin class in form ra seda mizanim

