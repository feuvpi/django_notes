from django.shortcuts import render, redirect
from core.models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

#def index(request):
   # return redirect('/notes')

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            redirect('/')
    else:
        redirect('/')

@login_required(login_url='/login/')
def notes_list(request):
    user = request.user
    info = Note.objects.all()
    notes = {'notes': info}
    return render(request, 'notes.html', notes)
