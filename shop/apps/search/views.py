# ( Search ) in app ra misazim ra moshtariha betavannd dar site ma search konand

#----------------------------------------------------------------

from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q 
from apps.products.models import Product

#----------------------------------------------------------------

class SearchResultsView(View):
   def get(self, request, *args, **kwargs):
      
      query = self.request.GET.get('q')          # ba in code ma yek ( q ) migirim, ( q ) baraye in kar ast k vaghti moshtari khast daron site ma chizi search konad bayad ghablesh az ( q ) estefade konad va oun ra benvisad injori ( http://127.0.0.1:8000/search/?q=Shir Pastorize ) 
      products = Product.objects.filter(         # in yani harmoghe kalame ( q ) va bad oun mahsoli k search shode ( http://127.0.0.1:8000/search/?q=Shir%20Pastorize ) dakhele URL neveshte shod boro dakhele productha filter kon yani search kon va oun ro paida kon
			Q(product_name__incontains = query) |   # va bebin oun kalamei k search shode havi oun kalame kilidi hast ya na ( manzor hamon Shir Pastorize hast ), ( product_name__incontains ) incontains yani hatman nabayad kalai k mikhahim search konim ra esm kamelash ra benevisim masalan shir pastorize vavghti faghat ( sh ) ra minevisim shir pastorize ra neshan midahad, vaghti ( product_name ) neveshtim dakhele onvanda va esm asli kalaha search mikonad
			Q(description__incontains = query)      # vaghti ( description ) minevisim dakhete kalamate ghesmate tozihat ham search mikonad
  )                                              # vaghti az ( Q ) estefade mikonim darim shart mizarim va ( | ) alamat yani ( یا ), pas dar kode bala nehesh migim ya dakhele onvanhaye asli kalaha search kon ya tozihateshon, ( product_name va description ) esmhaye darom model Product hastand
      
      context = {
			"products": products       # in code yani vaghti product search shode ra paida kardi baraye man bargardon
		}
      return render(request, "search_app/search_results.html", context)
   
   