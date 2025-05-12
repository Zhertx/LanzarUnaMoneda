from django.contrib import admin
from django.urls import path
from lanzamiento.views import tirar_moneda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tirar_moneda, name='tirar_moneda'),
]
