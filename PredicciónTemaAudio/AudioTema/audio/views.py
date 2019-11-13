from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Audio
from .forms import AudioForm
from django.http import HttpResponseRedirect
from .volverTexto import volverTexto
from .predictorBackEnd import analizar
# Create your views here.

class SubirAudio(CreateView):
    model = Audio
    form_class = AudioForm
    template_name = "pedirAudio.html"
    success_url = reverse_lazy("exitoso")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        return context

    def get_success_url(self):
        return reverse('verAudio', kwargs={'pk' : self.idAudio})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print(type(form.cleaned_data['audio']))
            objectAudio = form.save(commit = False)
            objectAudio.save()
            print(objectAudio.audio.url)

            #Volver texto
            texto = volverTexto(objectAudio.audio.url)
            objectAudio.textoAudio = texto

            #Predecir el tema
            tema = analizar(texto)
            objectAudio.tema = tema

            objectAudio.save()
            self.idAudio = objectAudio.id
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form))




class VerAudio(DetailView):
    model = Audio
    template_name = "analisisAudio.html"





