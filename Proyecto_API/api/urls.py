from django.urls import path
from .views import empleadoview

urlpatterns=[
    path('empleado/',empleadoview.as_view(),name='empleados_list')
]