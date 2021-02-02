from django.conf.urls import url
from .views import *

# from django.views.static.
urlpatterns = [
    url(r'^agregar_carrito_compra/(?P<slug>[^/]+)/$', agregar_curso_carrito, name='p_agregar_compra'),
    url(r'^ver_carrito/(?P<usuario>[^/]+)$', ver_carrito, name='p_ver_carrito'),
]
