from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductsGroup
from django.db.models import Q, Count
from django .views import View
from .compare import CompareProduct
from django.http import HttpResponse

#----------------------------------------------------------------

# in def marbot b ghesmate arzantarin mahsolat daron site ast k mikhahim arzantarin mahsolat ra az Database begirim va bebarim dakhele site

def get_cheapest_products(request, *args, **kwargs):        # ( get_cheapest_products ) yanibarkeshi arzantarin mahsolat, yani arzantarin mahsolat ra begirim va biyavarim
   products = Product.objects.filter(is_active = True).order_by('price')[:3]           # in baraye model ( Product ) ast, ba in code migim k vasl sho b Database bad vasl sho b Product bad objects(kala) ha ra paida kon va bad filter kon ounai k ( is_active = True ) ro baraye man biyar va bad ( order_by('price)[3] ) yani moratabeshon kon bar asas ghaimat va az bein hamashon faghat ( [3] ) tasho vasam biyar va bad ounaro beriz dakhele y zarfi b nam ( products )
   product_groups = ProductsGroup.objects.filter(Q(is_active = True) & Q(group_parent = None))        # in baraye model ( ProductGroup ) ast va chon az 2ta shart estefade kardim bayad ghableshon ( Q ) bezarim va ketabkhane Q ra bala ezafe mikonim ( from django.db.models import Q )
   context = {                      
		"products": products,
  		"product_groups": product_groups
	}                                          # va bad oun 2ta zarf ro mirizim dakhele ( context )
   return render(request, "product_app/partials/cheapest_products.html", context)     # va bad inja ham address safhe html ( cheapest_products ) ra minevisim ta bere ( products va product_groups ) ro behemon neshon bede
# va bad mirim URL in def ra minevisim ( cheapest_products )
# va bad baraye inke in safhe ha dar site zaher shavand bayad beravim dakhele ( index.html ) k safhe asli site ra neshan midahad dakhelash benvisim ( {% load render_partial %} ) va bad minevisim ( {% render_partial 'products:cheapest_products' %} ), ( products ) haman esm URL ast va ( cheapest_products ) esm hamin def dakhele views.py ast

#----------------------------------------------------------------

# in def marbot b ghesmate jadidtarin mahsolat daron site ast k mikhahim jadidtarin mahsolat ra az Database begirim va bebarim dakhele site

def get_last_products(request, *args, **kwargs):
   products = Product.objects.filter(is_active = True).order_by('-published_date')[:5]           # in baraye model ( Product ) ast, ba in code migim k vasl sho b Database bad vasl sho b Product bad objects(kala) ha ra paida kon va bad filter kon ounai k ( is_active = True ) ro baraye man biyar va bad ( order_by('-published_date')[:5] )  order_by yani moratabeshon kon bar asas ( published_date ) tarikh va az bein hamashon faghat ( [:5] ) tasho vasam biyar, ( - ) in alamati k gozashtim posht published_date b in mani ast k tarikh ha ra az akhar b aval moratab mikone, va bad ounaro beriz dakhele y zarfi b nam ( products )
   product_groups = ProductsGroup.objects.filter(Q(is_active = True) & Q(group_parent = None))        # in baraye model ( ProductGroup ) ast va chon az 2ta shart estefade kardim bayad ghableshon ( Q ) bezarim va ketabkhane Q ra bala ezafe mikonim ( from django.db.models import Q )
   context = {                      
		"products": products,
  		"product_groups": product_groups
	}                                          # va bad oun 2ta zarf ro mirizim dakhele ( context )
   return render(request, "product_app/partials/last_products.html", context)
# va bad mirim URL in def ra minevisim ( last_products )
# va bad baraye inke in safhe ha dar site zaher shavand bayad beravim dakhele ( index.html ) k safhe asli site ra neshan midahad dakhelash benvisim ( {% load render_partial %} ) va bad minevisim ( {% render_partial 'products:last_products' %} ), ( products ) haman esm URL ast va ( last_products ) esm hamin def dakhele views.py ast

#----------------------------------------------------------------

# in def marbot b ghesmate dastehaye mahbob daron siteast k mikhahim mahbobtarin mahsolat ra az Database begirim va bebarim dakhele site

def get_popular_product_groups(request, *args, **kwargs):
   product_groups = ProductsGroup.objects.filter(Q(is_active = True)).annotate(count=Count('products_of_groups')).order_by('-count')[:4]       # in baraye model ( ProductGroup ) ast, ba in code migim k vasl sho b Database bad vasl sho b ProductGroup bad objects(kala) ha ra paida kon va bad filter kon ounai k ( is_active = True ) ro baraye man biyar va bad ( annotate ) kon (annotate baraye ezafe kardan soton ast) pas migim ezafe kon ( Count ) ro b sotonha (count baraye shomordan chizi ast yani sum, min, max, avg anjam midahad) va bad ( products_of_groups ) ra baraye ma beshmar yani beshmar bebin chandta mahsol darim, ( products_of_groups ) haman esmi ast k dar models.py dar class Product jeloye product_group neveshtim ( related_name='proucts_of_groups' ), va bad ( order_by('-count') ) moratabesh mikonim az ziyad b kam, vaghti ( - ) mizarim az ziyad b kam moratab mishe, va dar akhar ( [:4] ) migim 4 tasho biyar
   context = {                      
  		"product_groups": product_groups
	}
   return render(request, "product_app/partials/popular_product_groups.html", context)
# va bad mirim URL in def ra minevisim ( popular_product_groups )
# va bad baraye inke in safhe ha dar site zaher shavand bayad beravim dakhele ( index.html ) k safhe asli site ra neshan midahad dakhelash benvisim ( {% load render_partial %} ) va bad minevisim ( {% render_partial 'products:popular_product_groups' %} ), ( products ) haman esm URL ast va ( popular_product_groups ) esm hamin def dakhele views.py ast

#----------------------------------------------------------------

# in class marbot b safhe joziyat kalaha dakheele site ast, yani masalan dar ghesmate arzantarin kalaha roye yek kala click mikonim va bad safhe marbot b oun kala baz mishavad va ma joziyat oun kala ra mibinim, masal rang, vazn, size va ...
# harmoghe mikhahim yek safhe kamel daron site besazim bayad az class estefade konim

class ProductDetailView(View):          # bala ketabkhane View ra bayad benvisim ( from django .views import View )
   def get(self, request, slug):
      product = get_object_or_404(Product, slug=slug)           # ( get_object_or_404 ) in tabe mitavanad baraye ma jostojo konad, ketabkhanash ro bayad bala benvisim ( get_object_or_404 ), va bad besh migim boro dakhele model ( Product ) va ouni k slug=slug hast ro baraye ma paida kon va bad berizesh dakhele yek zarfi b nam ( product )
      if product.is_active:                             # yani agar oun producti k paida kardi active bod bebaresh dakhele address pain
         return render(request, "product_app/product_detail.html", {'product':product})        # ( {'product':product} ) in hamon producti ast k paida karde v mikhad ba khodesh bebare b safhe html
   
   
#----------------------------------------------------------------

# in def marbot b ghesmate mahsolat mortabet ast, vaghti yek kala ra baz mikonim ta axshaye bishtari va tozihat an ra bebinim pain safhe oun kala yek ghesmat ast b nam mahsolat mortabet va karash in ast k kalahaye marbot b oun kalai k baz kardim ra b ma neshan bedahad, masalan ma dar site yek kala mobail ro baz mikonim ta axsasho bebinim pain hamon safhe mahsolat marbot b hamon kala ham baraye ma miyad masalan modelaye dg hamon mobile ya lavazem janebish

def get_related_products(request, *args, **kwargs):
   current_product = get_object_or_404(Product, slug=kwargs['slug'])      # ba in code ( get_object_or_404(Product, slug=kwargs['slug']) ) kalai k dakhele safhash hastim ro paida mikonim va mirizimesh dakhele zarfi b nam ( current_product ), safhe kala ro bayad az tarighe ( slug ) paida konim, ( Product, slug=kwargs['slug'] ) in code yani boro dakhele Product va slug ro paida kon
   related_products=[]                                                  # inja bayad yek list khali dorost konim k kalahai k paida mikone ro berize dakhele list
   for group in current_product.product_group.all():                    # yani dakhele har gorohi ( product_group ) ro paida kon va vasam biyar, ( product_group )haman kalahai hastand k dakhele yek goroh hastand masalan man ( kafsh motor savari va pirahan motor savari ) ra dakhele yek goroh gozashtam
      related_products.extend(Product.objects.filter(Q(is_active=True) & Q(product_group=group) & ~Q(id=current_product.id)))    # ( extend ) yani ezafe kardan, in code yani az Product kalaha ro paida kon filter kon ounai k product_group heshon ba group yeki hast, ( product_group ) yani kalahai k tu yek goroh hastand, ( group ) yani haman gorohai k kalaha dakhelesh hastand, ( Q(is_active=True) ) in code yani kalai k paida mikonim hatman bayad active bashe, ( ~Q(id=current_product.id) ) in code yani khode kalaye asli k safhash ro baz kardim dg oun pain bein mahslat mortabet neshon nade 
   return render(request, "product_app/partials/related_products.html", {'related_products':related_products})
      
# va bad mirim URL in def ra minevisim ( related_products )
# va bad baraye inke in safhe ha dar site zaher shavand bayad beravim dakhele ( product_detail.html ) k code marbot b ( mahsolat mortabet ) ounja neveshte shode ast ra benvisim ( {% render_partial 'products:related_products' slug=product.slug %} )

#----------------------------------------------------------------

# mikhahim yek safhebesazim k tamame goroh haye mahsolat ra dar an safhe neshan dahad
# harmoghe mikhahim yek safhe kamel daron site besazim bayad az class estefade konim

class ProductGroupsView(View):
   def get(self, request):
      product_groups = ProductsGroup.objects.filter(Q(is_active = True))\
                                            .annotate(count=Count('products_of_groups'))\
                                            .order_by('-count')
      return render(request, "product_app/partials/product_groups.html", {'product_groups':product_groups})
   
# bad miravim URL ra minevisim va bad codhaye safhe html ( product_groups.html ) ra inevisim va bad dar file ( popular_product_groups.html ) dar ghesmate دسته های محبوب in code ra minevisim ( <a href="{% url 'products:product_groups' %}">همه</a> ) bad yek dokme pain ghesmate dastehaye mahbob sakhte mishe b name hame k vaghti roye oun dokme bezanim yek safhe baz mishavad k hame goroh haye kalaha dakhelesh hast

#----------------------------------------------------------------

# alan yek code minevisim k vaghti dar ghesmate dastehaye mahbob roye ( moshak mardane ) click mikonim yek safhe baz shavad va kalahai k zir majmoe poshak mardane hastand ra baraye ma baz konad k baraye in kar bayad slug kalaha ra seda bezanim
# harmoghe mikhahim yek safhe kamel daron site besazim bayad az class estefade konim

class ProductByGroupView(View):
   def get_products_group(self, request, *args, **kwargs):
      current_group = get_object_or_404(ProductsGroup, slug=kwargs['slug'])                     # ba in code ( get_object_or_404(ProductGroup, slug=kwargs['slug']) ) kalai k dakhele safhash hastim ro paida mikonim va mirizimesh dakhele zarfi b nam ( current_group ), safhe kala ro bayad az tarighe ( slug ) paida konim, ( ProductGroup, slug=kwargs['slug'] ) in code yani boro dakhele ProductGroup va slug ro paida kon
      products = Product.objects.filter(Q(is_active=True) & Q(product_group=current_group))     # bad az inke slug ro paida kard y zarf dorost mikonim b name ( products ) va bad behesh migim boro dakhele Product va bad filter mikonim va 2ta shart behesh midim, yekish ( is_active=True ) kala hatman active bashe va yekish ( product_group=current_group ) product ba current_group yeki bashe yani kala va slug yeki bashand 
      return render(request, "product_app/products.html", {'products':products})
      
# badesh Url ra minevisim va bad codhaye safhe html ( products.html ) ra minevisim va bad dar file ( popular_product_groups.html ) dar ghesmate دسته های محبوب in code ra minevisim ( <a href="{% url 'products:products_of_group' slug=group.slug %}"> ) bad roye har kodam az kalaha k clock konim safhe oun kala baz mishe va kalahaye zir majmoz oun kala ham neshan dade mishe

#----------------------------------------------------------------

# code pain marbot b moghayese kalaha ba yekdigar ast va ma mikhahim yek safhe daron saite besazim k vaghti moshtari yek kala ra search mikonad tamame kalahaye shabihe oun kala daron safhe moghayese zaher shavand
# harmoghe mikhahim yek safhe kamel daron site besazim bayad az class estefade konim

class ShowCompareListView(View):              # yani har bar k ShowCompareListView ra seda zadam
   def get(self, request, *args, **kwargs):
      compare_list = CompareProduct(request)     # boro yek nemone az class CompareProduct besaz va esmesho bezar compare_list, Class CompareProduct ro dakhele file compare.py neveshtim va baraye inke b view vaslesh konim bayad bala ketabkhanash ro benvisim ( from .compare import CompareProduct )
      context = {                                # context marbot mishe b safhe HTML yani ma comper_list ro ba khodemon mibarim b safhe HTML
         'compare_list': compare_list
      }

      return render(request, 'product_app/compare_list.html', context)





# ba in def mikhahim dar hamon safhe moghayese k ba class bala sakhtim alan dar hamon safhe yek jadval dorost konim k mahsolat moshabeh ro ba ham moghayese konad
   def compare_table(request):                         # yani harmoghe compare_table ra seda zadim 
      compareList = CompareProduct(request)            # yek nemone az class CompareProduct besaz va esmesho bezar compareList, Class CompareProduct ro dakhele file compare.py neveshtim va baraye inke b view vaslesh konim bayad bala ketabkhanash ro benvisim ( from .compare import CompareProduct )
      
      products = []                                    # inja aval yek list khali mosazim k producthai k mikhan moghayese beshan ro mirizim dakhelesh
      for productId in compareList.compare_product:    # yani baraye har productId yani code kala daron compareList yani list moghayese, yani in codhaye dakhele list [ 3, 24, 65, 9 ]
         product = Product.objects.get(id=productId)   # bad har id=productId yani har code kalai k paida kardi product oun code kala ra paida kon
         products.append(product)                      # va oun producti k paida kardi ezafe kon b list products k bala listesho sakhtim
         
      features = []                                    # inja aval yek list khali baraye vizhegihaye oun kalahaye daron list products misazim
      for product in products:                         # yani baraye har kalai daron list products
         for item in product.product_feature.all():    # bad boro tamame ( product_feature ) yani tamame vizhegi oun kalaha ro biyar, ( product_feature ) ra daron folder products daron models.py zir class PriductFeature jelo prodyct neveshtim ( related_name='product_features' ) vaghti in ra minevisim yani tamame productha shamel feature ya vizhegi mishavand va beas mishe k befahmim har kala ch vizhegihai darand
            if item.feature not in features:           # yani ghabl az inke bekhai vizhegihaye kalaha ra ezafe koni b list features aval check kon bebin oun vizhegi ro ghablan ezafe kardi ya na agar kardi dg ezafe nakon
               features.append(item.feature)           # va dar akhar tamame vizhegihaye kalaha ra k paida kardi b list features ezafe kon 
               
      context = {
         'products': products,
         'features': features
      }         

      return render(request, 'product_app/partials/compare_table.html', context)
   
   
   
   
   
# in code baraye mohasebe tedad kalahaye mojod daron list moghayese ast
   def status_of_compare_list(request):
      compareList = CompareProduct(request)
      return HttpResponse(compareList.count)
   
   
   
   
# in code baraye ezafe kardan kala b list moghayese ast
   def add_to_compare_list(request):                 # vaghti baraye in def request ersal mishavad yani vaghti oun ra seda mizanim
      productId = request.GET.get('productId')       # bad id product ro migire mirize dakhele sabade productId
      compareList = CompareProduct(request)          # va bad class CompareProduct ro behesh requesr midim yani sedash mizanim, dar kol yani ba in code yek nemone az class CompareProduct misazim
      compareList.add_to_compare_product(productId)  # va bad az class CompareProduct def add_to_compare_product ro seda mizanim va id kala ra vasash va az oun def faghat productId ra migirim, chon in def ra injori neveshtim ( def add_to_compare_product(self,productId) )
      return HttpResponse('kala b list moghayese ezafe shod')
   
   
   
   
# in code baraye pak kardan kala az list moghayese ast 
   def delete_from_compare_list(request):            # vaghti baraye in def request ersal mishavad yani vaghti oun ra seda mizanim
      productId = request.GET.get('productId')       # bad id product ro migire mirize dakhele sabade productId
      compareList = CompareProduct(request)          # va bad class CompareProduct ro behesh requesr midim yani sedash mizanim, dar kol yani ba in code yek nemone az class CompareProduct misazim
      compareList.delete_from_compare_product(productId)  # va bad az class CompareProduct def delete_from_compare_product ro seda mizanim va id kala ra vasash va az oun def faghat productId ra migirim, chon in def ra injori neveshtim ( def delete_from_compare_product(self,productId) )
      return redirect("products:compare_table")
      


def delete_from_compare_list(request):            # vaghti baraye in def request ersal mishavad yani vaghti oun ra seda mizanim
      productId = request.GET.get('productId')       # bad id product ro migire mirize dakhele sabade productId
      compareList = CompareProduct(request)          # va bad class CompareProduct ro behesh requesr midim yani sedash mizanim, dar kol yani ba in code yek nemone az class CompareProduct misazim
      compareList.delete_from_compare_product(productId)  # va bad az class CompareProduct def delete_from_compare_product ro seda mizanim va id kala ra vasash va az oun def faghat productId ra migirim, chon in def ra injori neveshtim ( def delete_from_compare_product(self,productId) )
      return redirect("products:compare_table")