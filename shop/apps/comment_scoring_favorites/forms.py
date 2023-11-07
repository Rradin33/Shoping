from django import forms 

#----------------------------------------------------------------

# in form marbot b class Comment dakhele models.py ast

class CommentForm(forms.Form):
   product_id = forms.CharField(widget=forms.HiddenInput(), required=False)    # in code baes mishe commenti k gozashte shode moshakhas beshe baraye ch kalai hast
   comment_id = forms.CharField(widget=forms.HiddenInput(), required=False)    # in code baes mishe commenti k gozashte shode moshakhas beshe baraye ch commenti hast
   comment_text = forms.CharField(
		label="",
		error_messages = {'required':'این فیلد نمیتواند خالی باشد'},
		widget = forms.Textarea(attrs={'class':'form-control', 'placeholder':'متن نظر', 'rows':'4'})    # ( Textarea ) baes mishe k yek cadr mostatil bozorg dakhele site besaze baraye comment gozashtan, ( 'rows':'4' ) yani tedad satrhaye dakhele oun mostatil 4 bashe yani oun mostatil b andaze 4ta khat pahn bashe, ( 'placeholder':'متن نظر' ) in baes mishavad dakhele mostatil khaili kamrang benvise ( متن نظر )
	)
   
   
# va bad bayad dar ghesmate views.py view marbot b Comment ra benvisim 

