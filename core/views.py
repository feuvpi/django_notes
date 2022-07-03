from django.shortcuts import render, redirect
from core.models import Note

# Create your views here.

def index(request):
    return redirect('/notes')

def notes_list(request):
    user = request.user
    info = Note.objects.all()
    notes = {'notes': info}
    return render(request, 'notes.html', notes)
