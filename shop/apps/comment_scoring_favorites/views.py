# in app ra misazim baraye
# comment (yani karbar betavanad zire mahsolati k kharide comment begozarad va zire nazarate gigaran ham betavanad comment begozarad)
# scoring (yani karbar betavanad b mahsoli k kharide emtiyaz bedahad masalan 4 setare)
# favorites (yani az har mahsoli k khoshesh oumad tike ghalbesho bezane va oun mahsol dar ghesmate alaghemandiha save baeshe)

#----------------------------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Comment, Scoring, Favorite
from apps.products.models import Product
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from django.db.models import Q 

#----------------------------------------------------------------

# in view marbot b class Comment dakhele models.py ast k inja b 2 raveshe GET va POST minevisim,
# raveshe GET etela'at ra az Database migirad
# raveshe POST etela'ati k az Database gerefte shode ast ra post mikonad va neshan midahad 

class CommentView(View):
   def get (self, request, *args, **kwargs):
      productId = request.GET.get('productId')  # in code yani productId ro az Database begir, yani vasamon biyar k baraye ch producti comment gozashte shode
      commentId = request.GET.get('commentId')  # in code yani commentId ro az Database begir, yani vasamon biyar k commenti k gozashte shode chi hast, agaram commenti gozashte nashode null ast va neshan nemide yani shayad null bashe shayadam nabashe
      slug = kwargs['slug']      # slug haman URL ast k az system gerefte mishavad, va bad slug ra ham bayad dar ghesmate URL benvisim ham dar HTML 
      
      initial_dict = {                 # initial marbot b form ast, yek dictionery ast k dar ghesmate view minevisim va behesh migim product_id va comment_id k dron file forms.py zire class CommentForm neveshtim ra biyar inja ba in kar khodesh tashkhis mide k commenti k gozashte shode baraye ch producti ya zire ch commenti gozashte shode ast
			"product_id" : productId,     # yani productId k bala neveshtim barabar hast ba product_id dakhele Database
			"comment_id" : commentId,     # yani commentId k bala neveshtim barabar hast ba comment_id dakhele Database
   	}
      form = CommentForm(initial = initial_dict)     # inja ham oun formi k vasash dakhele forms.py neveshtim ra sedash mizanim k yani get kon va oun form ro ham vasamon biyar va bad ( initial_dict ) ra behesh midahim yani productId va commentId ra k az Databas gereftim darim midahim b form 
      
      return render(request, "csf_app/partials/create_comment.html", {"form": form, "slug": slug})

   
   
   def post(self, request, *args, **kwargs):
      slug = kwargs.get('slug')   # dar halate post aval slug ra b dast miyarim baraye inke url neshan dade shavad
      product = get_object_or_404(Product, slug=slug)      # az roye slug bala mifahmim k mahsolemon chi hast
      
      form = CommentForm(request.POST)   # bad migim harchi etela'at az class CommentForm dari ro post kon va beriz dakhele zarfi b nam form
      if form.is_valid():                # agar form is_valid hast
         cd = form.cleaned_data          # data haye clean shode ya tamiz shode ra beriz dakhele zarfi b nam cd
         
         parent = None                  # inja mikhaim befahmim aya commenti k ersal shode zire kala dade shode ya zire comment yek nafar digar k b in mored k zire comment yek nafar dg comment bezaran behesh migan parent, in code yani aval parent ro bezar None, yani az aal farz mikonim k zire comment yeki dg comment dade nashe va parent None hast 
         if(cd['comment_id']):          # bad migim agar comment_id ro paida kardi pas parent hast 
            parentId = cd['comment_id']    # pas parentId mishe in comment_id, yani pas b vasile id ha moshakhas mishe k kodam ( comment_id yani moshtari ) zire kodam ( parentId yani comment yek nafar dg) comment gozashte ast
            parent = Comment.objects.get(id=parentId)     # va dar akhar ba in code commenti k marbot b parent yani valed hast ro paida mikone
            
         Comment.objects.create(        # in code baraye in ast bad az inke moshtari comment dad va dokme ersal ra zad bad comment darj mishe
            product = Product,          # baraye in product
            commenting_user = request.user,    # tavasote in user
            comment_text = cd['comment_text'],   # matnesh ham clean shode sabt mishe 
            comment_parent = parent              # parent ham k None hast, chon bala neveshtim ( parent = None ) va dakhele Database ghesmate comment_parent minevise None, vali agar zire comment yeki dg comment bed code bala fa'al mishe va comment ro ghesmate parent por mikone va dakhele Database b jaue None minevide masalan 4 yani zire 4romin Comment, comment dade
         )
         
         messages.success(request, 'ثبت شد')
         return redirect("products:product_details", product.slug)    # in yani moshtari ro barmigardone b hamon safhei k dakhelesh bod
      messages.error(request, "خطا در ارسال", 'danger')
      return redirect("products:product_details", product.slug)
# bad in in URL va ajax marbot b in class ra ham minevisim

#----------------------------------------------------------------

# in def baraye imtiyaz dadan b kala tavasote moshtari ast, masalan chandta setare emtiyaz midan

def add_score(request): 
   productId = request.Get.get('productId')    # productId ro az Database migirim ta befahmim moshtari b ch kalai emtiyaz dade
   score = request.GET.get('score')            # score ro az Database migirim ta befahmim moshtari ch emtiyazi b kala dade
   product = Product.objects.get(id=productId)    # bad product ro paida mikonim az roye id=productId 
   Scoring.objects.create(            # va bad in chizha ro dakhele Database dakhele jadvale Scoring ezafe mikonim 
      product = product,              # product ro ezafe mikonim
      scoring_user = request.user,    # oun useri k roye oun kala click karde ro ezafe mikonim 
      score = score,                  # emtiyazesh ham ezafe mikonim
      )
      
   return HttpResponse('امتیاز ثبت شد')
# bad in in URL va ajax marbot b in class ra ham minevisim

#----------------------------------------------------------------

# in def marbot b class Favorite dakhele folder ( comment_scoring_favorite ) va dakhele models.py ast
# in def baraye in ast k masalan moshtari mikhad yek kala ro b ghesmate alaghemandihaye khodash dar site ezafe konad, ba in code system motevajeh mishe k aya oun user va product ghablan dakhele ghesmate Favorite Database add shodan ya na agar add shode bashand k payam mide ('این کالا قبلا به لیست علایق شمااضافه شد') agar nabashand ounaro add mikone va mige ('این کالا به لیست علایق شما اضافه شد')
# ma ghablan HTML va Ajax favorite ra neveshtim va chon in 2 ta nemitonan b Database vasl beshan ma dakhele view.py in code ra minevisim k ouna b vasile in code b Data base vasl beshan va etela'ati k az az Database mikhan o beheshon bede

def add_to_favorite(request):
   productId = request.GET.get('productId')     # inja aval id product ro migire
   product = Product.objects.get(id=productId)     # inja prodact morede nazar ro paida mikone
   
   flag = Favorite.objects.filter(              # ba in 3 khat code check mikone bebine product morede nazar vojod dare ya nadare, ( Favorite.objects.filter ) in code yani boro dakhele Database ghesmate Favorite bad objects yani dakhele kalaha filter kon yani searche kon bebin ( edame pain )
      Q(favorite_user_id = request.user.id) &        # searche kon bebin k aya in useri k login hast
      Q(product_id = productId)).exist()             # va in kalai k mikhad bere joze favoriteha ghablan dakhele Favorithaye Database nist? agar nist b vasile code pain ham kala ham user ro add kon va b ghesmate Favorite Database ezafe kon
   
   if (not flag):                 # agar user va product ro dar ghesmate Favorite Database paida nakard ba in codehaye pain ounaro add mikonim 
      Favorite.objects.create(
         product = Product,
         favorite_user = request.user
      )
   
      return HttpResponse('این کالا به لیست علایق شما اضافه شد')
   return HttpResponse('این کالا قبلا به لیست علایق شمااضافه شد')

# bad miravim URL in def ra minevisim

#----------------------------------------------------------------

# inja yek safhe daron site misazim marbot b Favorite k vaghti oun ra seda bezanim yek safhe jadid baz mishavad va tamam kalahai k moshtari tike ghalbesho zade va b safhe alaghemandihash ezafe karde ro neshon mide 

class UserFavoriteView(View):
   def get(self, request, *args, **kwargs):
      user_favorite_products = Favorite.objects.filter(Q(Favorite_user_id = request.user.id))
      return render(request, 'csf_app/user_favorite.html', {'user_favorite_products': user_favorite_products})
   