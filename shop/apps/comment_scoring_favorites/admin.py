from django.contrib import admin
from .models import Comment

#----------------------------------------------------------------

# in code marbot b class Comment dakhele models.py ast

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
   list_display = ['product', 'commenting_user', 'comment_text', 'is_active']
   list_editable = ['is_active']    # ( list_editable ) baraye in ast k betavanim list dakhele panel karbari ra edit konim va ma oun ro bar asas is_active gharar dadim, in kar baes shode k yek cadr moraba jelo har nazar dorost beshe k modir goroh betone oun nzar ro jelosh tik bezane ya tikesho bardare k active ya ghaire active beshe
   
   
# va bad bayad yek form dakhele forms.py marbot b in model benvisim ta karbar betone comment bezare, vaghti form minevisim yek kadr mostatil shekl zire kala dar ghesmate commenha b vojod miyad k karbar mitone tosh comment bezare 
# va bad bayad dar ghesmate views.py view marbot b Comment ra benvisim 

#----------------------------------------------------------------


   
   
   