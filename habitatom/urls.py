from django.urls import include, path
from rest_framework.routers import DefaultRouter

from habitatom.views import (HabitCreateView, HabitDeleteView, HabitDetailView,
                             HabitListView, HabitUpdateView, HabitViewSet)

router = DefaultRouter()
router.register(r"habits", HabitViewSet, basename="habit")

urlpatterns = [
    path("api/", include(router.urls)),
    path("", HabitListView.as_view(), name="habit_list"),
    path("<int:pk>/", HabitDetailView.as_view(), name="habit_detail"),
    path("new/", HabitCreateView.as_view(), name="habit_create"),
    path("<int:pk>/edit/", HabitUpdateView.as_view(), name="habit_edit"),
    path("<int:pk>/delete/", HabitDeleteView.as_view(), name="habit_confirm_delete"),
]
