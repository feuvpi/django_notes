"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', views.notes_list),
    path('', RedirectView.as_view(url='/notes')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.login_user),
    path('notes/note/', views.note),
    path('notes/note/submit', views.add_note),
    path('notes/note/delete/<int:id_note>/', views.delete_note)
    ##path('', views.index) ## another way to redirect
]
