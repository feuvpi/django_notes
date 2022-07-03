from django.shortcuts import render
from core.models import Note

# Create your views here.

def notes_list(request):
    user = request.user
    info = Note.objects.all()
    notes = {'notes': info}
    return render(request, 'notes.html', notes)
