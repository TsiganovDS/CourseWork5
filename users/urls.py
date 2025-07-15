from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import UserListView, UserViewSet

from .views import CustomLoginView, CustomLogoutView, RegisterView

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("", UserListView.as_view(), name="user_list"),
]

urlpatterns += router.urls
