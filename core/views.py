from django.core.mail.backends import console
from django.shortcuts import render, redirect
from core.models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

#def index(request):
   # return redirect('/notes')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid user or password.")
        return redirect('/')

@login_required(login_url='/login/')
def note(request):
    id_note = request.GET.get('id')
    dados = {}
    if id_note:
        dados['note'] = Note.objects.get(id=id_note)
    return render(request, 'note.html', dados)

@login_required(login_url='/login/')
def add_note(request):
    if request.POST:
        note = request.POST.get('note')
        user = request.user
        id_note = request.POST.get('id')
        if id_note:
            print("just got id note")
            Note.objects.filter(id=id_note).update(note=note)
            return redirect('/')

        else:
            print("didnt got note.id")
            Note.objects.create(note=note, user=user)
            return redirect('/')


@login_required(login_url='/login/')
def delete_note(request, id_note):
    user = request.user
    note = Note.object.get(id=id_note)
    if user == note.user:
        note.delete()
        return redirect('/')
    else:
        console.log('Access denied.')


    Note.objects.filter(id=id_note).delete()
    return redirect('/')


@login_required(login_url='/login/')
def notes_list(request):
    user = request.user
    info = Note.objects.filter(user=user)
    notes = {'notes': info}
    return render(request, 'notes.html', notes)
