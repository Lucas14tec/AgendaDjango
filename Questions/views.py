from django.shortcuts import render

from Questions.models import Event


def home(request):
    eventos = Event.objects.all()
    return render(request, 'Layout.html', {'eventos':eventos})
    
def evento(request , post_id):
    evento = evento.objects.get(pk= evento_id)
    return render(request, 'Layout.html', {'eventos':evento})