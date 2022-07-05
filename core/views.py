from django.shortcuts import render, redirect
from core.models import Note
from django.contrib.auth.decorators import login_required

# Create your views here.

#def index(request):
   # return redirect('/notes')

@login_required()
def notes_list(request):
    user = request.user
    info = Note.objects.all()
    notes = {'notes': info}
    return render(request, 'notes.html', notes)
