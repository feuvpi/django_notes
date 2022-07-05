from django.shortcuts import render, redirect
from core.models import Note
from django.contrib.auth.decorators import login_required

# Create your views here.

#def index(request):
   # return redirect('/notes')

def login_user(request):
    return render(request, 'login.html')

@login_required(login_url='/login/')
def notes_list(request):
    user = request.user
    info = Note.objects.all()
    notes = {'notes': info}
    return render(request, 'notes.html', notes)
