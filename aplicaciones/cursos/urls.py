from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

# from django.views.static.
urlpatterns = [
    url(r'^$', Curso.as_view(), name='p_inicio'),
    url(r'^detalle/(?P<slug>[^/]+)$', login_required(DetalleCurso.as_view()), name='p_ver_detalle_curso'),
]
