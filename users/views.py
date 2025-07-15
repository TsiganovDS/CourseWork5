from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework import viewsets

from users.forms import CustomUserCreationForm
from users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "users"


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/registration/register.html"
    success_url = reverse_lazy("login")


class CustomLoginView(LoginView):
    template_name = "users/registration/login.html"


class CustomLogoutView(LogoutView):
    template_name = "users/registration/logged_out.html"
