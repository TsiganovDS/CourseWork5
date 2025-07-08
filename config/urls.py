from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

def home(request):
    return render(request, 'habitatom/home.html')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/habits/', include('habitatom.urls')),
]
