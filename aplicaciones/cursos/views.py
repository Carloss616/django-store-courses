from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from aplicaciones.cursos.models import Curso as CursoModel

# Create your views here.

class Curso(TemplateView):
    template_name = 'cursos/cursos.html'

    def get_context_data(self, **kwargs):
        context = super(Curso, self).get_context_data(**kwargs)
        context['cursos'] = CursoModel.objects.filter(estado=True)
        return context

class DetalleCurso(DetailView):
    model = CursoModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['curso'] = get_object_or_404(CursoModel, slug=self.kwargs['slug'])
            return context
        except Exception as e:
            raise e

class Index_principal(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index_principal, self).get_context_data(**kwargs)
        context['cursos'] = CursoModel.objects.filter(estado=True)[0:2]
        return context