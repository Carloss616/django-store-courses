from django.conf.urls import url
# para poder importar las imagenes
from django.views.static import serve
from .views import *
# from views import Usuarios
from django.conf import settings

# from django.views.static.
urlpatterns = [
    # url(r'^usuarios', Usuarios.as_view(), name='inicio'),
    url(r'^$', UsuarioVer.as_view(), name='p_inicio'),
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
