from rest_framework.permissions import BasePermission

class CustomPermissionsForProducts(BasePermission):
   def has_permission(self, request, obj):
      return request.user and request.user.is_authenticated     # yani kasi k mikhad az in permission estefade kone ( manzor mashtari ast ) aval bayad user bashe va bad authenticates shode bashe
   
   