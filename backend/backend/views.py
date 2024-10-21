from rest_framework.views import APIView
from django.http import JsonResponse

class LoadMenu(APIView):
    def get(self, request, format=None):
        return JsonResponse({'BACKEND': 'http://localhost:9010/ventas/backend/'
                            ,'API': 'http://localhost:9010/api/xx/'
                            ,'Administrador':'http://localhost:9010/admin'
                            ,'Load':'http://localhost:9010/ventas/load/'})
    
