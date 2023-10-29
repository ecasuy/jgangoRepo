
from django.http import JsonResponse
from django.views import View
from .models import empleado
# Create your views here.
class empleadoview(View):
    
    def get(self, request):
        empleados =list(empleado.objects.values())
        if len(empleados)>0:
            datos={'message': "Success ", 'empleados':empleados}
        else:
            datos={'message': "empleados not found"}
        return JsonResponse(datos)
        
        
    def post(self,request): 
        pass
    def put(self,request): 
        pass
    def delete(self,request): 
        pass 