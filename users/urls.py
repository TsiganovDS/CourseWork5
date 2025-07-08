from django.urls import path

from users.views import UserListView
from .views import RegisterView, CustomLogoutView, CustomLoginView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', UserListView.as_view(), name='user_list')
]