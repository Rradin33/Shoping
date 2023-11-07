# in folder baraye zamani ast k ma ehtiyaj darim dakhele folderhaye models.py request dashte bashim mesl ( request.user )
# baraye hamin in poshe ra inja b esm ( middlewares ) misazim va code marbot b oun ra minevisim va bad dakhele har modeli khastim estefade konim esm kelass pain ra dakhele oun model minevisim
# va bad bayad middlewares ro dakhele setting ezafe konim, mirim dakhele setting zire ( MIDDLEWARE ) in code ra minevisim va esm class pain ra ezafe mikonim ( 'middlewares.middlewares.RequestMiddlewar' ) , middlewares aval esm folder ast, middlewares dovom esm file daron folder ast, RequestMiddlewar esm class ast
# ma az class pain daron models.py folder product estefade kardim zire kelas Product dakhele ( def get_user_scor )

#----------------------------------------------------------------

import threading


class RequestMiddleware:
   def __init__(self, get_response, thread_local=threading.local()):
      self.get_response = get_response
      self.thread_local = thread_local
      
      
   def __call__(self, request):
      self.thread_local.current_request = request
      response = self.get_response(request) 
      return response 
   
