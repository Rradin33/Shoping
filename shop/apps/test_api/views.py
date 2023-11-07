from apps.products.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import ProductSerializer
from CustomPermission import CustomPermissionsForProducts


class AllProductsApi(APIView):
   permission_classes = [CustomPermissionsForProducts]
   def get(self, request):
      products = Product.objects.filter(is_active=True).order_by('-published_date')     # yani boro hameye product ha ro biyar k active hastand va ( -published_date ) in yani bar asas tarikheshon moratabeshon kon bad biyar
      self.check_object_permissions(request, products)                 # in code marbot b code bala yani ( permission_classes = [CustomPermissionsForProducts] ) in ast k yani aval boro check kon bebin kasi ( yani hamon moshtari ) k mikhad az in permission estefade kone aval bayad user bashe va bad authenticates shode bashe ( code inha ra daron file CustomPermission.py neveshtam ), bad codehaye pain ro check kon   
      ser_data = ProductSerializer(instance=products, many=True)      # va bad az dakhele Database ( instance=products ) mahsolati k baraye namone avord ( instance yani nemone ) ro ersal mikone baraye classi b nam ( ProductSerializer ) k b seriyalizer tabdil beshan yani b halate jason dar biyan, ( many=True ) yani chon chandta kala hast hatman bayad many ro True bezarim agar faghat yek kala bod False mizashtim ya aslan many ro neminveshtim
      return Response(data = ser_data.data)  
      
      
      